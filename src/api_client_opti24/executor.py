from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Any, Protocol, TypeVar

from .config import TimeoutPolicy
from .endpoints import EndpointSpec, RouteVariant
from .errors import NotAuthenticatedError
from .logger import LoggerLike
from .registry import MethodRegistry
from .response import DecodedPayload
from .runtime import Clock
from .service_base import (
    APIKeyProvider,
    JSONPayload,
    PathParams,
    SessionContext,
    SessionGate,
    SessionRecovery,
)
from .utils import sanitize_for_logging

ResultT = TypeVar("ResultT")


class Transport(Protocol):
    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        **kwargs: Any,
    ) -> DecodedPayload: ...

    async def request_stream(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        headers: Mapping[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes: ...

    async def aclose(self) -> None: ...


@dataclass(frozen=True, slots=True)
class _ResolvedOperation:
    spec: EndpointSpec
    route: RouteVariant
    endpoint: str


class OperationExecutor:
    def __init__(
        self,
        *,
        api_key_provider: APIKeyProvider,
        transport: Transport,
        session_context: SessionContext,
        registry: MethodRegistry,
        timeouts: TimeoutPolicy,
        logger: LoggerLike,
        clock: Clock,
    ) -> None:
        self.__api_key_provider = api_key_provider
        self.__transport = transport
        self.__session_context = session_context
        self.__registry = registry
        self.__timeouts = timeouts
        self.__logger = logger
        self.__clock = clock

    def headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]:
        api_key = self.__api_key_provider.get_api_key()
        if not api_key:
            raise ValueError("API key provider returned an empty value")
        headers = {
            "api_key": api_key,
            "date_time": self.__clock.now().strftime("%Y-%m-%d %H:%M:%S"),
            "User-Agent": "apiclientopti24",
            "Content-Type": (
                "application/json" if content_type_json else "application/x-www-form-urlencoded"
            ),
        }
        if include_session and self.__session_context.session_id:
            headers["session_id"] = self.__session_context.session_id
            if self.__session_context.contract_id:
                headers["contract_id"] = self.__session_context.contract_id
        self.__logger.debug("Prepared headers: %s", sanitize_for_logging(headers))
        return headers

    def resolve(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
    ) -> _ResolvedOperation:
        spec = self.__registry.get(operation)
        route = spec.resolve_route(api_version=api_version, route_name=route_name)
        return _ResolvedOperation(spec=spec, route=route, endpoint=route.render(path_params))

    def _request_headers(
        self,
        spec: EndpointSpec,
        kwargs: dict[str, Any],
    ) -> dict[str, str]:
        custom_headers = kwargs.pop("headers", None)
        if custom_headers is not None and not isinstance(custom_headers, Mapping):
            raise TypeError("headers must be a mapping of strings")
        headers = dict(custom_headers or {})
        headers.update(
            self.headers(
                include_session=spec.requires_session,
                content_type_json="json" in kwargs,
            )
        )
        return headers

    async def execute_resolved(
        self,
        resolved: _ResolvedOperation,
        **kwargs: Any,
    ) -> JSONPayload:
        request_kwargs = dict(kwargs)
        result = await self.__transport.request(
            resolved.route.http_method,
            resolved.endpoint,
            api_version=resolved.route.api_version,
            headers=self._request_headers(resolved.spec, request_kwargs),
            timeout=self.__timeouts.resolve(resolved.spec.timeout_class),
            method_name=resolved.spec.name,
            retry_class=resolved.spec.retry_class,
            idempotent=resolved.spec.idempotent,
            **request_kwargs,
        )
        if not isinstance(result, dict):
            self.__logger.error(
                "Unexpected API response operation=%s response_type=%s",
                resolved.spec.name,
                type(result).__name__,
            )
            raise TypeError("Expected API response to be a JSON object")
        self.__logger.debug("Received response type: %s", type(result).__name__)
        return result

    async def execute(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> JSONPayload:
        resolved = self.resolve(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
        )
        self.__logger.debug(
            "Preparing API request operation=%s version=%s route=%s",
            resolved.spec.name,
            resolved.route.api_version,
            resolved.route.name,
        )
        return await self.execute_resolved(resolved, **kwargs)

    async def execute_stream_resolved(
        self,
        resolved: _ResolvedOperation,
        **kwargs: Any,
    ) -> bytes:
        request_kwargs = dict(kwargs)
        return await self.__transport.request_stream(
            resolved.route.http_method,
            resolved.endpoint,
            api_version=resolved.route.api_version,
            headers=self._request_headers(resolved.spec, request_kwargs),
            timeout=self.__timeouts.resolve(resolved.spec.timeout_class),
            method_name=resolved.spec.name,
            retry_class=resolved.spec.retry_class,
            idempotent=resolved.spec.idempotent,
            **request_kwargs,
        )

    async def execute_stream(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> bytes:
        resolved = self.resolve(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
        )
        return await self.execute_stream_resolved(resolved, **kwargs)


class DefaultRequestExecutor:
    def __init__(
        self,
        *,
        operation_executor: OperationExecutor,
        session_gate: SessionGate,
        session_recovery: SessionRecovery,
        logger: LoggerLike,
    ) -> None:
        self.__operation_executor = operation_executor
        self.__session_gate = session_gate
        self.__session_recovery = session_recovery
        self.__logger = logger

    def headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]:
        return self.__operation_executor.headers(
            include_session=include_session,
            content_type_json=content_type_json,
        )

    def _audit(
        self,
        event: str,
        resolved: _ResolvedOperation,
        *,
        recovered: bool = False,
    ) -> None:
        self.__logger.info(
            "API request audit",
            extra={
                "request_audit": True,
                "event": event,
                "operation": resolved.spec.name,
                "api_version": resolved.route.api_version,
                "route_name": resolved.route.name,
                "http_method": resolved.route.http_method,
                "recovered": recovered,
            },
        )

    async def _run_with_recovery(
        self,
        resolved: _ResolvedOperation,
        request: Callable[[], Awaitable[ResultT]],
    ) -> ResultT:
        self._audit("started", resolved)
        try:
            result = await request()
        except NotAuthenticatedError:
            if not resolved.spec.requires_session:
                self._audit("failed", resolved)
                raise
            self._audit("session_recovery", resolved)
            await self.__session_recovery.recover()
            try:
                result = await request()
            except Exception:
                self._audit("failed", resolved, recovered=True)
                raise
            self._audit("completed", resolved, recovered=True)
            return result
        except Exception:
            self._audit("failed", resolved)
            raise
        self._audit("completed", resolved)
        return result

    async def execute(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> JSONPayload:
        resolved = self.__operation_executor.resolve(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
        )
        if resolved.spec.requires_session:
            await self.__session_gate.ensure_authenticated()
        return await self._run_with_recovery(
            resolved,
            lambda: self.__operation_executor.execute_resolved(resolved, **kwargs),
        )

    async def execute_stream(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> bytes:
        resolved = self.__operation_executor.resolve(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
        )
        if resolved.spec.requires_session:
            await self.__session_gate.ensure_authenticated()
        return await self._run_with_recovery(
            resolved,
            lambda: self.__operation_executor.execute_stream_resolved(resolved, **kwargs),
        )

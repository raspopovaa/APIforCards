from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
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

    def _resolve_operation(
        self,
        operation: str,
        *,
        api_version: str | None,
        route_name: str,
        path_params: PathParams | None,
    ) -> tuple[EndpointSpec, RouteVariant, str]:
        spec = self.__registry.get(operation)
        route = spec.resolve_route(api_version=api_version, route_name=route_name)
        return spec, route, route.render(path_params)

    def _request_headers(
        self,
        spec: EndpointSpec,
        kwargs: dict[str, Any],
    ) -> dict[str, str]:
        custom_headers = kwargs.pop("headers", None)
        if custom_headers is not None and not isinstance(custom_headers, Mapping):
            raise TypeError("headers must be a mapping of strings")
        headers = self.headers(
            include_session=spec.requires_session,
            content_type_json="json" in kwargs,
        )
        for name, value in dict(custom_headers or {}).items():
            normalized_name = name.lower().replace("-", "_")
            if normalized_name in {"api_key", "session_id", "date_time"}:
                raise ValueError(f"Header override is not allowed: {name}")
            headers[name] = value
        return headers

    async def _request_json(
        self,
        spec: EndpointSpec,
        route: RouteVariant,
        endpoint: str,
        kwargs: dict[str, Any],
    ) -> JSONPayload:
        result = await self.__transport.request(
            route.http_method,
            endpoint,
            api_version=route.api_version,
            headers=self._request_headers(spec, kwargs),
            timeout=self.__timeouts.resolve(spec.timeout_class),
            method_name=spec.name,
            retry_class=spec.retry_class,
            idempotent=spec.idempotent,
            **kwargs,
        )
        if not isinstance(result, dict):
            self.__logger.error(
                "Unexpected API response operation=%s response_type=%s",
                spec.name,
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
        spec, route, endpoint = self._resolve_operation(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
        )
        self.__logger.debug(
            "Preparing API request operation=%s version=%s route=%s",
            spec.name,
            route.api_version,
            route.name,
        )
        return await self._request_json(spec, route, endpoint, dict(kwargs))

    async def _request_bytes(
        self,
        spec: EndpointSpec,
        route: RouteVariant,
        endpoint: str,
        kwargs: dict[str, Any],
    ) -> bytes:
        return await self.__transport.request_stream(
            route.http_method,
            endpoint,
            api_version=route.api_version,
            headers=self._request_headers(spec, kwargs),
            timeout=self.__timeouts.resolve(spec.timeout_class),
            method_name=spec.name,
            **kwargs,
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
        spec, route, endpoint = self._resolve_operation(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
        )
        return await self._request_bytes(spec, route, endpoint, dict(kwargs))


class DefaultRequestExecutor:
    def __init__(
        self,
        *,
        operation_executor: OperationExecutor,
        session_gate: SessionGate,
        session_recovery: SessionRecovery,
        registry: MethodRegistry,
        logger: LoggerLike,
    ) -> None:
        self.__operation_executor = operation_executor
        self.__session_gate = session_gate
        self.__session_recovery = session_recovery
        self.__registry = registry
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
        spec: EndpointSpec,
        route: RouteVariant,
        *,
        recovered: bool = False,
    ) -> None:
        self.__logger.info(
            "API request audit",
            extra={
                "request_audit": True,
                "event": event,
                "operation": spec.name,
                "api_version": route.api_version,
                "route_name": route.name,
                "http_method": route.http_method,
                "recovered": recovered,
            },
        )

    async def _run_with_recovery(
        self,
        spec: EndpointSpec,
        route: RouteVariant,
        request: Callable[[], Awaitable[ResultT]],
    ) -> ResultT:
        self._audit("started", spec, route)
        try:
            result = await request()
        except NotAuthenticatedError:
            if not spec.requires_session:
                self._audit("failed", spec, route)
                raise
            self._audit("session_recovery", spec, route)
            await self.__session_recovery.recover()
            try:
                result = await request()
            except Exception:
                self._audit("failed", spec, route, recovered=True)
                raise
            self._audit("completed", spec, route, recovered=True)
            return result
        except Exception:
            self._audit("failed", spec, route)
            raise
        self._audit("completed", spec, route)
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
        spec = self.__registry.get(operation)
        route = spec.resolve_route(api_version=api_version, route_name=route_name)
        if spec.requires_session:
            await self.__session_gate.ensure_authenticated()
        return await self._run_with_recovery(
            spec,
            route,
            lambda: self.__operation_executor.execute(
                operation,
                api_version=api_version,
                route_name=route_name,
                path_params=path_params,
                **kwargs,
            ),
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
        spec = self.__registry.get(operation)
        route = spec.resolve_route(api_version=api_version, route_name=route_name)
        if spec.requires_session:
            await self.__session_gate.ensure_authenticated()
        return await self._run_with_recovery(
            spec,
            route,
            lambda: self.__operation_executor.execute_stream(
                operation,
                api_version=api_version,
                route_name=route_name,
                path_params=path_params,
                **kwargs,
            ),
        )

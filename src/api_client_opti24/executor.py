from __future__ import annotations

from typing import Any, Protocol

from .config import TimeoutPolicy
from .decorators import get_current_api_method_name
from .logger import LoggerLike
from .registry import MethodRegistry, MethodSpec
from .response import DecodedPayload
from .runtime import Clock
from .service_base import JSONPayload, SessionContext
from .transport import AuthRecovery
from .utils import sanitize_for_logging


class Transport(Protocol):
    def set_auth_recovery(self, auth_recovery: AuthRecovery) -> None: ...

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
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes: ...

    async def aclose(self) -> None: ...


class DefaultRequestExecutor:
    def __init__(
        self,
        *,
        api_key: str,
        transport: Transport,
        session_context: SessionContext,
        registry: MethodRegistry,
        timeouts: TimeoutPolicy,
        logger: LoggerLike,
        clock: Clock,
    ) -> None:
        self.__api_key = api_key
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
        headers = {
            "api_key": self.__api_key,
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

    def _resolve_method_spec(
        self,
        endpoint: str,
        api_version: str,
        http_method: str | None = None,
    ) -> MethodSpec | None:
        return self.__registry.find_by_endpoint(
            endpoint,
            api_version,
            http_method=http_method,
        )

    def _current_method_spec(
        self,
        endpoint: str,
        api_version: str,
        http_method: str,
    ) -> MethodSpec | None:
        method_name = get_current_api_method_name()
        if method_name is not None:
            try:
                return self.__registry.get(method_name)
            except KeyError:
                pass
        return self._resolve_method_spec(endpoint, api_version, http_method=http_method)

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        **kwargs: Any,
    ) -> JSONPayload:
        spec = self._current_method_spec(endpoint, api_version, method)

        timeout_class = spec.timeout_class if spec is not None else "default"
        self.__logger.debug(
            "Preparing API request operation=%s version=%s",
            spec.name if spec is not None else "unregistered",
            api_version,
        )
        result = await self.__transport.request(
            method,
            endpoint,
            api_version=api_version,
            timeout=self.__timeouts.resolve(timeout_class),
            method_name=spec.name if spec is not None else None,
            retry_class=spec.retry_class if spec is not None else None,
            idempotent=spec.idempotent if spec is not None else None,
            **kwargs,
        )
        if not isinstance(result, dict):
            self.__logger.error(
                "Unexpected API response operation=%s response_type=%s",
                spec.name if spec is not None else "unregistered",
                type(result).__name__,
            )
            raise TypeError("Expected API response to be a JSON object")
        self.__logger.debug("Received response type: %s", type(result).__name__)
        return result

    async def request_stream(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes:
        spec = self._current_method_spec(endpoint, api_version, method)
        timeout_class = spec.timeout_class if spec is not None else "default"
        return await self.__transport.request_stream(
            method,
            endpoint,
            api_version=api_version,
            headers=headers,
            timeout=self.__timeouts.resolve(timeout_class),
            method_name=spec.name if spec is not None else None,
            **kwargs,
        )

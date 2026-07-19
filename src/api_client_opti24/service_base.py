from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, Protocol, TypeAlias

from .logger import LoggerLike

JSONPayload: TypeAlias = dict[str, Any]
AuthenticateCallback: TypeAlias = Callable[[], Awaitable[object]]


class RequestExecutor(Protocol):
    def headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]: ...

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        **kwargs: Any,
    ) -> JSONPayload: ...

    async def request_stream(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes: ...


class SessionContext(Protocol):
    @property
    def session_id(self) -> str | None: ...

    @property
    def contract_id(self) -> str | None: ...


class SessionGate(Protocol):
    async def ensure_authenticated(self) -> str: ...


class SessionMutator(SessionContext, Protocol):

    def mark_authenticated(
        self,
        session_id: str,
        contract_id: str | None = None,
    ) -> None: ...

    def set_contract(self, contract_id: str | None) -> None: ...

    def invalidate(self) -> None: ...

    def reset(self) -> None: ...


class CredentialsProvider(Protocol):
    def get_credentials(self) -> tuple[str, str]: ...


class AuthenticationSession(SessionMutator, Protocol):
    async def ensure_authenticated(self, authenticate: AuthenticateCallback) -> str: ...


class ServiceMethodContext(Protocol):
    @property
    def logger(self) -> LoggerLike: ...

    @property
    def session_gate(self) -> SessionGate: ...


class _BaseService:
    def __init__(
        self,
        request_executor: RequestExecutor,
        session_context: SessionContext,
        session_gate: SessionGate,
        logger: LoggerLike,
    ) -> None:
        self.__request_executor = request_executor
        self.__session_context = session_context
        self.__session_gate = session_gate
        self.__logger = logger

    @property
    def logger(self) -> LoggerLike:
        return self.__logger

    @property
    def session_gate(self) -> SessionGate:
        return self.__session_gate

    @property
    def contract_id(self) -> str | None:
        return self.__session_context.contract_id

    def _headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]:
        return self.__request_executor.headers(include_session, content_type_json)

    async def _request(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        **kwargs: Any,
    ) -> JSONPayload:
        return await self.__request_executor.request(
            method,
            endpoint,
            api_version=api_version,
            **kwargs,
        )

    async def _request_stream(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes:
        return await self.__request_executor.request_stream(
            method,
            endpoint,
            api_version=api_version,
            headers=headers,
            **kwargs,
        )

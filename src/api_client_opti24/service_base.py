from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Protocol, TypeAlias

from .logger import LoggerLike

JSONPayload: TypeAlias = dict[str, Any]
PathParams: TypeAlias = Mapping[str, str | int]


class RequestExecutor(Protocol):
    async def execute(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> JSONPayload: ...

    async def execute_stream(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> bytes: ...


class SessionContext(Protocol):
    @property
    def session_id(self) -> str | None: ...

    @property
    def contract_id(self) -> str | None: ...


class SessionGate(Protocol):
    async def ensure_authenticated(self) -> str: ...


class SessionRecovery(Protocol):
    async def recover(self) -> str: ...


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


class APIKeyProvider(Protocol):
    def get_api_key(self) -> str: ...


class ServiceMethodContext(Protocol):
    @property
    def logger(self) -> LoggerLike: ...


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
    def contract_id(self) -> str | None:
        return self.__session_context.contract_id

    async def _resolve_contract_id(self, contract_id: str | None) -> str:
        if contract_id:
            return contract_id
        await self.__session_gate.ensure_authenticated()
        if self.__session_context.contract_id is None:
            raise ValueError("contract_id is required when no default contract is selected")
        return self.__session_context.contract_id

    async def _request(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> JSONPayload:
        return await self.__request_executor.execute(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
            **kwargs,
        )

    async def _request_stream(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: PathParams | None = None,
        **kwargs: Any,
    ) -> bytes:
        return await self.__request_executor.execute_stream(
            operation,
            api_version=api_version,
            route_name=route_name,
            path_params=path_params,
            **kwargs,
        )

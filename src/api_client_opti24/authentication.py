from __future__ import annotations

import asyncio
from typing import Protocol

from .logger import LoggerLike
from .modeling import decode_model
from .models.auth import AuthUserResponse
from .service_base import CredentialsProvider, RequestExecutor, SessionMutator
from .session import SessionManager
from .utils import hash_password


class Authenticator(Protocol):
    async def authenticate(
        self,
        *,
        api_version: str | None = None,
        contract_id: str | None = None,
        contract_number: str | None = None,
    ) -> AuthUserResponse: ...


class DefaultAuthenticator:
    def __init__(
        self,
        request_executor: RequestExecutor,
        session_mutator: SessionMutator,
        credentials_provider: CredentialsProvider,
        logger: LoggerLike,
    ) -> None:
        self.__request_executor = request_executor
        self.__session_mutator = session_mutator
        self.__credentials_provider = credentials_provider
        self.__logger = logger

    async def authenticate(
        self,
        *,
        api_version: str | None = None,
        contract_id: str | None = None,
        contract_number: str | None = None,
    ) -> AuthUserResponse:
        login, password = self.__credentials_provider.get_credentials()
        data = await self.__request_executor.execute(
            "auth_user",
            api_version=api_version,
            data={"login": login, "password": hash_password(password)},
        )
        auth_response = decode_model(AuthUserResponse, data)
        contracts = auth_response.data.contracts
        selected = None
        if contract_id:
            selected = next((item for item in contracts if item.id == contract_id), None)
        elif contract_number:
            selected = next((item for item in contracts if item.number == contract_number), None)
        elif contracts:
            selected = contracts[0]

        self.__session_mutator.mark_authenticated(
            session_id=auth_response.data.session_id,
            contract_id=selected.id if selected else None,
        )
        if selected:
            self.__logger.info("Contract selected")
        else:
            self.__logger.warning("Контракт не найден — contract_id не установлен")
        return auth_response


class AuthenticationCoordinator:
    def __init__(
        self,
        session: SessionManager,
        authenticator: Authenticator,
    ) -> None:
        self.__session = session
        self.__authenticator = authenticator
        self.__recovery_lock = asyncio.Lock()

    async def authenticate(self) -> AuthUserResponse:
        return await self.__authenticator.authenticate()

    async def ensure_authenticated(self) -> str:
        return await self.__session.ensure_authenticated(self.authenticate)

    async def recover(self) -> str:
        failed_session_id = self.__session.session_id
        selected_contract_id = self.__session.contract_id
        async with self.__recovery_lock:
            current_session_id = self.__session.session_id
            if current_session_id is not None and current_session_id != failed_session_id:
                return current_session_id
            self.__session.invalidate()
            return await self.__session.ensure_authenticated(
                lambda: self.__authenticator.authenticate(contract_id=selected_contract_id)
            )

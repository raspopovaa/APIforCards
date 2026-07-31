from __future__ import annotations

from typing import Protocol

from .errors import ContractSelectionError
from .logger import LoggerLike
from .models.auth import AuthUserResponse, ContractInfo
from .service_base import CredentialsProvider, RequestExecutor, SessionMutator
from .session import SessionManager
from .utils import hash_password


def _contract_choices(contracts: list[ContractInfo]) -> tuple[tuple[str, str], ...]:
    return tuple((item.id, item.number) for item in contracts)


def _select_contract(
    contracts: list[ContractInfo],
    *,
    contract_id: str | None,
    contract_number: str | None,
) -> ContractInfo | None:
    if contract_id is not None and contract_number is not None:
        raise ContractSelectionError(
            "Pass either contract_id or contract_number, not both"
        )

    if contract_id is not None:
        matches = [item for item in contracts if item.id == contract_id]
        if len(matches) != 1:
            raise ContractSelectionError(
                "Requested contract_id is unavailable or ambiguous",
                available_contracts=_contract_choices(contracts),
            )
        return matches[0]

    if contract_number is not None:
        matches = [item for item in contracts if item.number == contract_number]
        if len(matches) != 1:
            raise ContractSelectionError(
                "Requested contract_number is unavailable or ambiguous",
                available_contracts=_contract_choices(contracts),
            )
        return matches[0]

    if not contracts:
        return None
    if len(contracts) == 1:
        return contracts[0]
    raise ContractSelectionError(
        "Multiple contracts are available; pass contract_id or contract_number explicitly",
        available_contracts=_contract_choices(contracts),
    )


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
        if contract_id is not None and contract_number is not None:
            raise ContractSelectionError(
                "Pass either contract_id or contract_number, not both"
            )

        login, password = self.__credentials_provider.get_credentials()
        data = await self.__request_executor.execute(
            "auth_user",
            api_version=api_version,
            data={"login": login, "password": hash_password(password)},
        )
        auth_response = AuthUserResponse(**data)
        try:
            selected = _select_contract(
                auth_response.data.contracts,
                contract_id=contract_id,
                contract_number=contract_number,
            )
        except ContractSelectionError:
            self.__session_mutator.invalidate()
            raise

        self.__session_mutator.mark_authenticated(
            session_id=auth_response.data.session_id,
            contract_id=selected.id if selected else None,
        )
        if selected:
            self.__logger.info("Contract selected")
        else:
            self.__logger.info("Authentication completed without an available contract")
        return auth_response


class AuthenticationCoordinator:
    def __init__(
        self,
        session: SessionManager,
        authenticator: Authenticator,
    ) -> None:
        self.__session = session
        self.__authenticator = authenticator

    async def authenticate(self) -> AuthUserResponse:
        return await self.__authenticator.authenticate(
            contract_id=self.__session.contract_id,
        )

    async def ensure_authenticated(self) -> str:
        return await self.__session.ensure_authenticated(self.authenticate)

    async def recover(self) -> str:
        selected_contract_id = self.__session.contract_id
        self.__session.invalidate()
        self.__session.set_contract(selected_contract_id)
        return await self.ensure_authenticated()

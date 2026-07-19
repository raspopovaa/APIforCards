from ..decorators import api_method
from ..logger import LoggerLike
from ..models.auth import AuthUserResponse, GetInfoResponse
from ..runtime import Clock
from ..service_base import (
    CredentialsProvider,
    RequestExecutor,
    SessionContext,
    SessionGate,
    SessionMutator,
    _BaseService,
)
from ..utils import hash_password


class AuthService(_BaseService):
    def __init__(
        self,
        request_executor: RequestExecutor,
        session_context: SessionContext,
        session_gate: SessionGate,
        session_mutator: SessionMutator,
        credentials_provider: CredentialsProvider,
        clock: Clock,
        logger: LoggerLike,
    ) -> None:
        super().__init__(request_executor, session_context, session_gate, logger)
        self.__session_mutator = session_mutator
        self.__credentials_provider = credentials_provider
        self.__clock = clock

    @api_method
    async def logoff(self, api_version: str | None = None) -> dict[str, object]:
        response = await self._request("logoff", api_version=api_version)
        self.__session_mutator.reset()
        return response

    @api_method
    async def get_info(
        self,
        api_version: str | None = None,
        period: str | None = None,
    ) -> GetInfoResponse:
        """Получение статистических данных по вызовам всех методов."""
        if period is None:
            now = self.__clock.now()
            period = now.strftime("%Y-%m-%d %H:%M:%S")
        data = await self._request(
            "get_info",
            api_version=api_version,
            params={"period": period},
        )

        return GetInfoResponse(**data)

    @api_method
    async def auth_user(
        self,
        *,
        api_version: str | None = None,
        contract_id: str | None = None,
        contract_number: str | None = None,
    ) -> AuthUserResponse:
        login, password = self.__credentials_provider.get_credentials()
        payload = {"login": login, "password": hash_password(password)}

        data = await self._request(
            "auth_user",
            api_version=api_version,
            data=payload,
        )

        auth_response = AuthUserResponse(**data)
        contracts = [
            {"id": item.id, "number": item.number} for item in auth_response.data.contracts
        ]

        selected = None
        if contract_id:
            selected = next((c for c in contracts if c["id"] == contract_id), None)
        elif contract_number:
            selected = next((c for c in contracts if c["number"] == contract_number), None)
        elif contracts:
            selected = contracts[0]

        selected_contract_id = selected["id"] if selected else None
        self.__session_mutator.mark_authenticated(
            session_id=auth_response.data.session_id,
            contract_id=selected_contract_id,
        )

        if selected:
            self.logger.info("Contract selected")
        else:
            self.logger.warning("Контракт не найден — contract_id не установлен")

        return auth_response

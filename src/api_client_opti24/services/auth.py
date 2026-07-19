from ..authentication import Authenticator
from ..decorators import api_method
from ..logger import LoggerLike
from ..models.auth import AuthUserResponse, GetInfoResponse
from ..runtime import Clock
from ..service_base import (
    RequestExecutor,
    SessionContext,
    SessionGate,
    SessionMutator,
    _BaseService,
)


class AuthService(_BaseService):
    def __init__(
        self,
        request_executor: RequestExecutor,
        session_context: SessionContext,
        session_gate: SessionGate,
        session_mutator: SessionMutator,
        authenticator: Authenticator,
        clock: Clock,
        logger: LoggerLike,
    ) -> None:
        super().__init__(request_executor, session_context, session_gate, logger)
        self.__session_mutator = session_mutator
        self.__authenticator = authenticator
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
        return await self.__authenticator.authenticate(
            api_version=api_version,
            contract_id=contract_id,
            contract_number=contract_number,
        )

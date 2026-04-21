from datetime import datetime

from ..decorators import api_method
from ..logger import logger
from ..models.auth import AuthUserResponse, GetInfoResponse
from ..utils import hash_password


class AuthMixin:
    @api_method(require_session=True, default_version="v1")
    async def logoff(self, api_version: str = "v1") -> dict:
        response = await self._request(
            "get",
            "logoff",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        self.session_manager.reset()
        return response

    @api_method(require_session=True, default_version="v1")
    async def get_info(
        self,
        api_version: str = "v1",
        period: str | None = None,
    ) -> dict:
        """Получение статистических данных по вызовам всех методов."""
        if period is None:
            period = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = await self._request(
            "get",
            "info",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={
                "period": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },  # можно указать день "2018-10-20"
        )

        return GetInfoResponse(**data)

    @api_method(require_session=False, default_version="v1")
    async def auth_user(
        self,
        *,
        api_version: str = "v1",
        contract_id: str | None = None,
        contract_number: str | None = None,
    ) -> AuthUserResponse:
        payload = {"login": self.login, "password": hash_password(self.password)}

        data = await self._request(
            "post",
            "authUser",
            api_version=api_version,
            headers=self._headers(),
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
        self.session_manager.mark_authenticated(
            session_id=auth_response.data.session_id,
            contract_id=selected_contract_id,
        )

        if selected:
            logger.info(f"Выбран контракт: id={selected['id']}, number={selected['number']}")
        else:
            logger.warning("Контракт не найден — contract_id не установлен")

        return auth_response

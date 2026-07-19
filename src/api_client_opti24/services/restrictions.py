from typing import Any, Optional

from ..decorators import api_method
from ..models.restrictions import (
    RestrictionGetResponse,
    RestrictionRemoveResponse,
    RestrictionSetResponse,
)
from ..service_base import _BaseService
from ..utils import to_json_param


class RestrictionsService(_BaseService):
    """
    Методы для работы с товарными ограничителями (v1).
    """

    # ---------------- Запрос ----------------
    @api_method(require_session=True, default_version="v1")
    async def get_restrictions(
        self,
        *,
        contract_id: str,
        card_id: Optional[str] = None,
        group_id: Optional[str] = None,
        api_version: str = "v1",
    ) -> RestrictionGetResponse:
        """
        Получение списка товарных ограничителей по договору, карте или группе карт.
        """
        params = {"contract_id": contract_id}
        if card_id:
            params["card_id"] = card_id
        if group_id:
            params["group_id"] = group_id

        raw = await self._request(
            "get",
            "restriction",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        self.logger.debug("Restriction list received")
        return RestrictionGetResponse(**raw)

    # ---------------- Установка ----------------
    @api_method(require_session=True, default_version="v1")
    async def set_restriction(
        self,
        *,
        restrictions: list[dict[str, Any]],
        api_version: str = "v1",
    ) -> RestrictionSetResponse:
        """
        Установка или изменение товарного ограничителя по карте или группе карт.
        Для изменения ограничителя необходимо передавать его ID.
        """
        if not restrictions:
            raise ValueError("Список restrictions не может быть пустым")

        body = {"restriction": to_json_param(restrictions)}

        raw = await self._request(
            "post",
            "setRestriction",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        self.logger.debug("Restriction updated")
        return RestrictionSetResponse(**raw)

    # ---------------- Удаление ----------------
    @api_method(require_session=True, default_version="v1")
    async def remove_restriction(
        self,
        *,
        contract_id: str,
        restriction_id: str,
        group_id: Optional[str] = None,
        api_version: str = "v1",
    ) -> RestrictionRemoveResponse:
        """
        Удаление товарного ограничителя по карте или группе карт.
        """
        body = {
            "restriction_id": restriction_id,
            "contract_id": contract_id,
        }
        if group_id:
            body["group_id"] = group_id

        raw = await self._request(
            "post",
            "removeRestriction",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        self.logger.debug("Restriction removed")
        return RestrictionRemoveResponse(**raw)

from typing import Any

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
    @api_method
    async def get_restrictions(
        self,
        *,
        contract_id: str,
        card_id: str | None = None,
        group_id: str | None = None,
        api_version: str | None = None,
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
            "get_restrictions",
            api_version=api_version,
            params=params,
        )

        self.logger.debug("Restriction list received")
        return RestrictionGetResponse(**raw)

    # ---------------- Установка ----------------
    @api_method
    async def set_restriction(
        self,
        *,
        restrictions: list[dict[str, Any]],
        api_version: str | None = None,
    ) -> RestrictionSetResponse:
        """
        Установка или изменение товарного ограничителя по карте или группе карт.
        Для изменения ограничителя необходимо передавать его ID.

        Типовой сценарий:
            Разрешить карте покупки только выбранного типа продукта. Для
            изменения существующего ограничителя добавьте его ``id``.

        Пример вызова:
        ```python
        result = await client.restrictions.set_restriction(
            restrictions=[{
                "contract_id": "contract-id",
                "card_id": "card-id",
                "productType": "product-type-id",
                "restriction_type": 1,
            }]
        )
        ```

        Пример логического payload до сериализации поля ``restriction``:
        ```json
        {
          "contract_id": "contract-id",
          "card_id": "card-id",
          "productType": "product-type-id",
          "restriction_type": 1
        }
        ```
        """
        if not restrictions:
            raise ValueError("Список restrictions не может быть пустым")

        body = {"restriction": to_json_param(restrictions)}

        raw = await self._request(
            "set_restriction",
            api_version=api_version,
            data=body,
        )

        self.logger.debug("Restriction updated")
        return RestrictionSetResponse(**raw)

    # ---------------- Удаление ----------------
    @api_method
    async def remove_restriction(
        self,
        *,
        contract_id: str,
        restriction_id: str,
        group_id: str | None = None,
        api_version: str | None = None,
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
            "remove_restriction",
            api_version=api_version,
            data=body,
        )

        self.logger.debug("Restriction removed")
        return RestrictionRemoveResponse(**raw)

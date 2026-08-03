from collections.abc import Mapping
from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.restrictions import (
    RestrictionGetResponse,
    RestrictionRemoveResponse,
    RestrictionRequestItem,
    RestrictionSetResponse,
)
from ..service_base import _BaseService
from ..utils import to_json_param
from ..validation import require_identifier, validate_card_or_group_target


class RestrictionsService(_BaseService):
    """
    Методы для работы с товарными ограничителями (v1).
    """

    async def _validated_contract_id(self, contract_id: str | None) -> str:
        resolved = await self._resolve_contract_id(contract_id)
        return require_identifier(resolved, "contract_id")

    # ---------------- Запрос ----------------
    @api_method
    async def get_restrictions(
        self,
        *,
        contract_id: str | None = None,
        card_id: str | None = None,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RestrictionGetResponse:
        """
        Получение списка товарных ограничителей по договору, карте или группе карт.
        """
        cid = await self._validated_contract_id(contract_id)
        card_id, group_id = validate_card_or_group_target(
            card_id=card_id,
            group_id=group_id,
        )
        params = {"contract_id": cid}
        if card_id is not None:
            params["card_id"] = card_id
        if group_id is not None:
            params["group_id"] = group_id

        raw = await self._request(
            "get_restrictions",
            api_version=api_version,
            params=params,
        )

        return decode_model(RestrictionGetResponse, raw)

    # ---------------- Установка ----------------
    @api_method
    async def set_restriction(
        self,
        *,
        restrictions: list[RestrictionRequestItem | Mapping[str, Any]],
        contract_id: str | None = None,
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
            raise ValueError("restrictions must contain at least one item")
        parsed_restrictions = [RestrictionRequestItem.model_validate(item) for item in restrictions]
        for item in parsed_restrictions:
            validate_card_or_group_target(
                card_id=item.card_id,
                group_id=item.group_id,
                required=True,
            )

        fallback_contract_id: str | None = None
        if contract_id is not None or any(item.contract_id is None for item in parsed_restrictions):
            fallback_contract_id = await self._validated_contract_id(contract_id)

        serialized_restrictions: list[dict[str, Any]] = []
        for item in parsed_restrictions:
            serialized = item.model_dump(by_alias=True, exclude_none=True)
            serialized["contract_id"] = (
                require_identifier(item.contract_id, "contract_id")
                if item.contract_id is not None
                else fallback_contract_id
            )
            serialized_restrictions.append(serialized)

        body = {"restriction": to_json_param(serialized_restrictions)}

        raw = await self._request(
            "set_restriction",
            api_version=api_version,
            data=body,
        )

        return decode_model(RestrictionSetResponse, raw)

    # ---------------- Удаление ----------------
    @api_method
    async def remove_restriction(
        self,
        *,
        contract_id: str | None = None,
        restriction_id: str,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RestrictionRemoveResponse:
        """
        Удаление товарного ограничителя по карте или группе карт.
        """
        cid = await self._validated_contract_id(contract_id)
        body = {
            "restriction_id": require_identifier(restriction_id, "restriction_id"),
            "contract_id": cid,
        }
        if group_id is not None:
            body["group_id"] = require_identifier(group_id, "group_id")

        raw = await self._request(
            "remove_restriction",
            api_version=api_version,
            data=body,
        )

        return decode_model(RestrictionRemoveResponse, raw)

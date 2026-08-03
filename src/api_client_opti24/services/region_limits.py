from collections.abc import Mapping
from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.region_limits import (
    RegionLimitRequestItem,
    RegionLimitResponse,
    RegionLimitSetResponse,
    RemoveRegionLimit,
)
from ..service_base import _BaseService
from ..utils import to_json_param
from ..validation import require_identifier, validate_card_or_group_target


class RegionLimitsService(_BaseService):
    """
    Методы для работы с региональными лимитами (v1).
    """

    @api_method
    async def get_region_limits(
        self,
        *,
        contract_id: str | None = None,
        card_id: str | None = None,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RegionLimitResponse:
        """
        Получение списка региональных лимитов по договору, карте или группе карт.
        """
        cid = await self._resolve_contract_id(contract_id)
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
            "get_region_limits",
            api_version=api_version,
            params=params,
        )
        return decode_model(RegionLimitResponse, raw)

    @api_method
    async def set_region_limit(
        self,
        *,
        region_limits: list[RegionLimitRequestItem | Mapping[str, Any]],
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> RegionLimitSetResponse:
        """
        Установка/изменение регионального лимита по карте или группе карт.
        Для изменения лимита необходимо передавать его ID.

        Типовой сценарий:
            Разрешить обслуживание карты только в выбранной стране или регионе.

        Пример вызова:
        ```python
        result = await client.region_limits.set_region_limit(
            region_limits=[{
                "contract_id": "contract-id",
                "card_id": "card-id",
                "country": "RUS",
                "region": "54",
                "limit_type": 1,
            }]
        )
        ```

        Пример логического payload до сериализации поля ``region_limit``:
        ```json
        {
          "contract_id": "contract-id",
          "card_id": "card-id",
          "country": "RUS",
          "region": "54",
          "limit_type": 1
        }
        ```
        """
        if not region_limits:
            raise ValueError("region_limits must contain at least one item")
        parsed_limits = [RegionLimitRequestItem.model_validate(item) for item in region_limits]
        for item in parsed_limits:
            validate_card_or_group_target(
                card_id=item.card_id,
                group_id=item.group_id,
                required=True,
            )

        fallback_contract_id: str | None = None
        if contract_id is not None or any(item.contract_id is None for item in parsed_limits):
            fallback_contract_id = await self._resolve_contract_id(contract_id)

        serialized_limits: list[dict[str, Any]] = []
        for item in parsed_limits:
            serialized = item.model_dump(by_alias=True, exclude_none=True)
            serialized["contract_id"] = (
                require_identifier(item.contract_id, "contract_id")
                if item.contract_id is not None
                else fallback_contract_id
            )
            serialized_limits.append(serialized)

        body = {"region_limit": to_json_param(serialized_limits)}

        raw = await self._request(
            "set_region_limit",
            api_version=api_version,
            data=body,
        )
        return decode_model(RegionLimitSetResponse, raw)

    @api_method
    async def remove_region_limit(
        self,
        *,
        contract_id: str | None = None,
        regionlimit_id: str,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RemoveRegionLimit:
        """
        Удаление регионального лимита по карте или группе карт.
        """
        cid = await self._resolve_contract_id(contract_id)
        body = {
            "regionlimit_id": require_identifier(regionlimit_id, "regionlimit_id"),
            "contract_id": cid,
        }
        if group_id is not None:
            body["group_id"] = require_identifier(group_id, "group_id")

        raw = await self._request(
            "remove_region_limit",
            api_version=api_version,
            data=body,
        )
        return decode_model(RemoveRegionLimit, raw)

from typing import Any

from ..decorators import api_method
from ..models.region_limits import (
    RegionLimitResponse,
    RemoveRegionLimit,
)
from ..service_base import _BaseService
from ..utils import to_json_param


class RegionLimitsService(_BaseService):
    """
    Методы для работы с региональными лимитами (v1).
    """

    @api_method
    async def get_region_limits(
        self,
        *,
        contract_id: str,
        card_id: str | None = None,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RegionLimitResponse:
        """
        Получение списка региональных лимитов по договору, карте или группе карт.
        """
        params = {"contract_id": contract_id}
        if card_id:
            params["card_id"] = card_id
        if group_id:
            params["group_id"] = group_id

        raw = await self._request(
            "get_region_limits",
            api_version=api_version,
            params=params,
        )
        return RegionLimitResponse(**raw)

    @api_method
    async def set_region_limit(
        self,
        *,
        region_limits: list[dict[str, Any]],
        api_version: str | None = None,
    ) -> dict[str, Any]:
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
        body = {"region_limit": to_json_param(region_limits)}

        return await self._request(
            "set_region_limit",
            api_version=api_version,
            data=body,
        )

    @api_method
    async def remove_region_limit(
        self,
        *,
        contract_id: str,
        regionlimit_id: str,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RemoveRegionLimit:
        """
        Удаление регионального лимита по карте или группе карт.
        """
        body = {"regionlimit_id": regionlimit_id, "contract_id": contract_id}
        if group_id:
            body["group_id"] = group_id

        raw = await self._request(
            "remove_region_limit",
            api_version=api_version,
            data=body,
        )
        return RemoveRegionLimit(**raw)

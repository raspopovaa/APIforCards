import json
from collections.abc import Mapping
from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.limits import (
    LimitRequestItem,
    LimitsResponse,
    RemoveLimitResponse,
    SetLimitResponse,
)
from ..service_base import _BaseService
from ..validation import (
    require_identifier,
    validate_card_or_group_target,
)


class LimitsService(_BaseService):
    """
    Методы для работы с продуктовыми лимитами (v1).

    Поддерживаются:
      • Получение списка лимитов (по договору, карте или группе)
      • Установка / изменение лимита
      • Удаление лимита
    """

    async def _validated_contract_id(self, contract_id: str | None) -> str:
        resolved = await self._resolve_contract_id(contract_id)
        return require_identifier(resolved, "contract_id")

    # ------------------- GET /limit -------------------

    @api_method
    async def get_limits(
        self,
        *,
        contract_id: str | None = None,
        card_id: str | None = None,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> LimitsResponse:
        """
        Получить список продуктовых лимитов по договору, карте или группе карт.

        :param contract_id: ID договора
        :param card_id: ID карты (опционально)
        :param group_id: ID группы карт (опционально)
        :param api_version: версия API (по умолчанию v1)
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
            "get_limits",
            api_version=api_version,
            params=params,
        )

        return decode_model(LimitsResponse, raw)

    # ------------------- POST /setLimit -------------------

    @api_method
    async def set_limit(
        self,
        *,
        limits: list[LimitRequestItem | Mapping[str, Any]],
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> SetLimitResponse:
        """
        Для изменения уже ранее созданного лимита, требуется передавать в запросе его ID.
        Для договора нельзя выставить продуктовый лимит, можно для карты или группы карт.
        :param limits: список лимитов в виде словарей (см. документацию API)

        Типовой сценарий:
            Ограничить дневной расход конкретной карты. Для изменения ранее
            созданного лимита добавьте его ``id`` в тот же словарь.

        Пример вызова:
        ```python
        result = await client.limits.set_limit(
            limits=[{
                "contract_id": "contract-id",
                "card_id": "card-id",
                "sum": {"currency": "810", "value": 5000.0},
                "time": {"number": 1, "type": 5},
            }]
        )
        ```

        Пример логического payload до сериализации поля ``limit``:
        ```json
        {
          "contract_id": "contract-id",
          "card_id": "card-id",
          "sum": {"currency": "810", "value": 5000.0},
          "time": {"number": 1, "type": 5}
        }
        ```
        """
        if not limits:
            raise ValueError("limits must contain at least one item")
        parsed_limits = [LimitRequestItem.model_validate(item) for item in limits]
        for item in parsed_limits:
            validate_card_or_group_target(
                card_id=item.card_id,
                group_id=item.group_id,
                required=True,
            )
            if item.amount is None and item.sum is None:
                raise ValueError("each limit must contain amount or sum")

        fallback_contract_id: str | None = None
        if contract_id is not None or any(item.contract_id is None for item in parsed_limits):
            fallback_contract_id = await self._validated_contract_id(contract_id)

        serialized_limits: list[dict[str, Any]] = []
        for item in parsed_limits:
            serialized = item.model_dump(by_alias=True, exclude_none=True)
            serialized["contract_id"] = (
                require_identifier(item.contract_id, "contract_id")
                if item.contract_id is not None
                else fallback_contract_id
            )
            serialized_limits.append(serialized)

        body = {
            "limit": json.dumps(
                serialized_limits,
                ensure_ascii=False,
                separators=(",", ":"),
            )
        }

        raw = await self._request(
            "set_limit",
            api_version=api_version,
            data=body,
        )

        return decode_model(SetLimitResponse, raw)

    # ------------------- POST /removeLimit -------------------

    @api_method
    async def remove_limit(
        self,
        *,
        contract_id: str | None = None,
        limit_id: str,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RemoveLimitResponse:
        """
        Удалить продуктовый лимит по карте или группе карт.
        Если ID группы карты не передано, то будет удален лимит по карте.
         Если передан ID группы карт, то будет удален лимит по группе карт
        :param contract_id: ID договора
        :param limit_id: ID лимита
        :param group_id: ID группы карт (опционально)
        """
        cid = await self._validated_contract_id(contract_id)
        body = {
            "limit_id": require_identifier(limit_id, "limit_id"),
            "contract_id": cid,
        }
        if group_id is not None:
            body["group_id"] = require_identifier(group_id, "group_id")

        raw = await self._request(
            "remove_limit",
            api_version=api_version,
            data=body,
        )

        return decode_model(RemoveLimitResponse, raw)

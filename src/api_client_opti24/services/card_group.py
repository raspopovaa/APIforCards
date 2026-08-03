import json
from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models import (
    CardGroupListResponse,
    RemoveCardGroupResponse,
    SetCardGroupResponse,
    SetCardsToGroupResponse,
)
from ..service_base import _BaseService


class CardGroupsService(_BaseService):
    """
    Методы для работы с группами карт (v1).
    """

    # -------------------------------
    # Получение списка групп карт
    # -------------------------------
    @api_method
    async def get_card_groups(
        self,
        *,
        contract_id: str,
        api_version: str | None = None,
    ) -> CardGroupListResponse:
        """
        Получить список групп карт по договору.
        """
        params = {"contract_id": contract_id}

        raw = await self._request(
            "get_card_groups",
            api_version=api_version,
            params=params,
        )
        return decode_model(CardGroupListResponse, raw)

    # -------------------------------
    # Создание или изменение группы
    # -------------------------------
    @api_method
    async def set_card_group(
        self,
        *,
        contract_id: str,
        name: str,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> SetCardGroupResponse:
        """
        Создать новую или изменить существующую группу карт.

        Args:
            contract_id: Идентификатор договора.
            name: Название группы карт.
            group_id: (опционально) ID группы для изменения.

        Типовой сценарий:
            Создать группу для отдельного подразделения, затем добавить карты
            через ``set_cards_to_group``.

        Пример вызова:
        ```python
        group = await client.card_groups.set_card_group(
            contract_id="contract-id",
            name="Служебные автомобили",
        )
        ```

        Пример payload:
        ```json
        {"contract_id": "contract-id", "name": "Служебные автомобили"}
        ```
        """
        body = {"contract_id": contract_id, "name": name}
        if group_id:
            body["id"] = group_id

        raw = await self._request(
            "set_card_group",
            api_version=api_version,
            data=body,
        )
        return decode_model(SetCardGroupResponse, raw)

    # -------------------------------
    # Добавление карт в группу
    # -------------------------------
    @api_method
    async def set_cards_to_group(
        self,
        *,
        contract_id: str,
        group_id: str,
        cards_list: list[dict[str, Any]],
        api_version: str | None = None,
    ) -> SetCardsToGroupResponse:
        """
        Добавление карт в группу.

        Args:
            contract_id: Идентификатор договора.
            group_id: Идентификатор группы карт.
            cards_list: Список карт и действий, например:
                [{"id": "2728111", "type": "Attach"}, {"id": "2728112", "type": "Attach"}]
        """
        body = {
            "contract_id": contract_id,
            "group_id": group_id,
            "cards_list": json.dumps(cards_list),
        }

        raw = await self._request(
            "set_cards_to_group",
            api_version=api_version,
            data=body,
        )
        return decode_model(SetCardsToGroupResponse, raw)

    # -------------------------------
    # Удаление группы карт
    # -------------------------------
    @api_method
    async def remove_card_group(
        self,
        *,
        contract_id: str,
        group_id: str,
        api_version: str | None = None,
    ) -> RemoveCardGroupResponse:
        """
        Удалить группу карт по ID.

        Args:
            contract_id: Идентификатор договора.
            group_id: Идентификатор группы карт.
        """
        body = {"contract_id": contract_id, "group_id": group_id}

        raw = await self._request(
            "remove_card_group",
            api_version=api_version,
            data=body,
        )
        return decode_model(RemoveCardGroupResponse, raw)

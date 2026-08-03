import json
from collections.abc import Mapping

from ..models import (
    CardGroupAssignmentRequest,
    CardGroupListResponse,
    RemoveCardGroupResponse,
    SetCardGroupResponse,
    SetCardsToGroupResponse,
)
from ..operations import operation
from ..service_base import _BaseService

GET_CARD_GROUPS = operation("get_card_groups", CardGroupListResponse)
SET_CARD_GROUP = operation("set_card_group", SetCardGroupResponse)
SET_CARDS_TO_GROUP = operation("set_cards_to_group", SetCardsToGroupResponse)
REMOVE_CARD_GROUP = operation("remove_card_group", RemoveCardGroupResponse)


class CardGroupsService(_BaseService):
    """
    Методы для работы с группами карт (v1).
    """

    # -------------------------------
    # Получение списка групп карт
    # -------------------------------
    async def get_card_groups(
        self,
        *,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> CardGroupListResponse:
        """
        Получить список групп карт по договору.
        """
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        params = {"contract_id": resolved_contract_id}

        return await self._request(
            GET_CARD_GROUPS,
            api_version=api_version,
            params=params,
            request_contract_id=resolved_contract_id,
        )

    # -------------------------------
    # Создание или изменение группы
    # -------------------------------
    async def set_card_group(
        self,
        *,
        name: str,
        contract_id: str | None = None,
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
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        body = {"contract_id": resolved_contract_id, "name": name}
        if group_id:
            body["id"] = group_id

        return await self._request(
            SET_CARD_GROUP,
            api_version=api_version,
            data=body,
            request_contract_id=resolved_contract_id,
        )

    # -------------------------------
    # Добавление карт в группу
    # -------------------------------
    async def set_cards_to_group(
        self,
        *,
        group_id: str,
        cards_list: list[CardGroupAssignmentRequest | Mapping[str, object]],
        contract_id: str | None = None,
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
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        assignments = [
            CardGroupAssignmentRequest.model_validate(card).model_dump() for card in cards_list
        ]
        body = {
            "contract_id": resolved_contract_id,
            "group_id": group_id,
            "cards_list": json.dumps(assignments),
        }

        return await self._request(
            SET_CARDS_TO_GROUP,
            api_version=api_version,
            data=body,
            request_contract_id=resolved_contract_id,
        )

    # -------------------------------
    # Удаление группы карт
    # -------------------------------
    async def remove_card_group(
        self,
        *,
        group_id: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> RemoveCardGroupResponse:
        """
        Удалить группу карт по ID.

        Args:
            contract_id: Идентификатор договора.
            group_id: Идентификатор группы карт.
        """
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        body = {"contract_id": resolved_contract_id, "group_id": group_id}

        return await self._request(
            REMOVE_CARD_GROUP,
            api_version=api_version,
            data=body,
            request_contract_id=resolved_contract_id,
        )

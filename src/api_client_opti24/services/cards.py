from collections.abc import AsyncIterator

from ..models.cards import (
    BoolResponse,
    CardDetailResponse,
    CardDriversResponse,
    CardGroupResponse,
    CardsListResponse,
    CardsV2Response,
    CardV2Item,
    IDListResponse,
)
from ..operations import operation
from ..service_base import _BaseService

GET_CARDS_V1 = operation("get_cards_v1", CardsListResponse)
GET_CARDS_V2 = operation("get_cards_v2", CardsV2Response)
GET_CARDS_BY_GROUP = operation("get_cards_by_group", CardGroupResponse)
GET_CARD_DRIVERS = operation("get_card_drivers", CardDriversResponse)
GET_CARD_DETAIL = operation("get_card_detail", CardDetailResponse)
BLOCK_CARD = operation("block_card", IDListResponse)
SET_CARD_COMMENT = operation("set_card_comment", BoolResponse)
VERIFY_PIN = operation("verify_pin", BoolResponse)
RESET_PIN = operation("reset_pin", BoolResponse)


class CardsService(_BaseService):
    """Методы работы с топливными картами."""

    # --- Список карт (v1) ---
    async def get_cards_v1(
        self,
        *,
        contract_id: str | None = None,
        cache: bool = True,
        api_version: str | None = None,
    ) -> CardsListResponse:
        """Список топливных карт (Процессинг).
        :param contract_id: Идентификатор договора
        :param cache: Кеш карт. false или не задан - данные берутся по прямому запросу из процессинга.
        :return: Объект CardsListResponse с данными о картах

        """
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        params = {"contract_id": resolved_contract_id, "cache": str(cache).lower()}
        self.logger.info("Requesting cards version=v1")
        return await self._request(
            GET_CARDS_V1,
            api_version=api_version,
            params=params,
            request_contract_id=resolved_contract_id,
        )

    async def get_cards_v2(
        self,
        *,
        contract_id: str | None = None,
        sort: str = "-id",
        q: str | None = None,
        status: str | None = None,
        carrier: str | None = None,
        platon: bool | None = None,
        avtodor: bool | None = None,
        users: bool | None = None,
        group_id: str | None = None,
        page: int | None = None,
        onpage: int | None = None,
        api_version: str | None = None,
    ) -> CardsV2Response:
        """
        Получение списка карт договора (v2).
        :param contract_id: Идентификатор договора
        :param sort: Поле сортировки (по умолчанию '-id')
        :param q: Поисковый запрос (например, часть номера карты)
        :param status: Фильтр по статусу карты (Active, Locked и т.д.)
        :param carrier: Тип носителя карты ('Plastic', 'Virtual Card')
        :param platon: Фильтр по поддержке Платон
        :param avtodor: Фильтр по поддержке Автодор
        :param users: Фильтр по наличию пользователей
        :param group_id: Идентификатор группы карт (опционально)
        :param page: Номер страницы (по умолчанию 1)
        :param onpage: Количество элементов на странице (по умолчанию 10)
        :return: Объект CardsV2Response с данными о картах
        """
        resolved_contract_id = await self._resolve_contract_id(contract_id)

        params = {
            "contract_id": resolved_contract_id,
            "sort": sort,
            "q": q,
            "status": status,
            "carrier": carrier,
            "platon": platon,
            "avtodor": avtodor,
            "users": users,
            "group_id": group_id,
            "page": page,
            "onpage": onpage,
        }

        # Исключаем None, чтобы не отправлять пустые параметры
        filtered_params = {k: v for k, v in params.items() if v is not None}

        return await self._request(
            GET_CARDS_V2,
            api_version=api_version,
            params=filtered_params,
            request_contract_id=resolved_contract_id,
        )

    async def iter_cards_v2(
        self,
        *,
        contract_id: str | None = None,
        sort: str = "-id",
        q: str | None = None,
        status: str | None = None,
        carrier: str | None = None,
        group_id: str | None = None,
        onpage: int = 100,
        max_pages: int = 100,
        api_version: str | None = None,
    ) -> AsyncIterator[CardV2Item]:
        """Последовательно получить карты, ограничив число страниц."""
        if onpage < 1 or max_pages < 1:
            raise ValueError("onpage and max_pages must be greater than zero")
        yielded = 0
        for page in range(1, max_pages + 1):
            response = await self.get_cards_v2(
                contract_id=contract_id,
                sort=sort,
                q=q,
                status=status,
                carrier=carrier,
                group_id=group_id,
                page=page,
                onpage=onpage,
                api_version=api_version,
            )
            for item in response.result:
                yield item
                yielded += 1
            if not response.result or yielded >= response.total_count:
                return

    # --- Список карт по группе ---
    async def get_cards_by_group(
        self,
        *,
        group_id: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> CardGroupResponse:
        """Получение списка топливных карт по группе карт."""
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        params = {"contract_id": resolved_contract_id, "group_id": group_id}
        self.logger.info("Requesting cards by group")
        return await self._request(
            GET_CARDS_BY_GROUP,
            api_version=api_version,
            params=params,
            request_contract_id=resolved_contract_id,
        )

    # --- Водители по карте ---
    async def get_card_drivers(
        self,
        *,
        card_id: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> CardDriversResponse:
        """Получение списка водителей по карте."""
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        self.logger.info("Requesting card drivers")
        return await self._request(
            GET_CARD_DRIVERS,
            api_version=api_version,
            path_params={"card_id": card_id},
            params={"contract_id": resolved_contract_id},
            request_contract_id=resolved_contract_id,
        )

    # --- Детальная информация по карте ---
    async def get_card_detail(
        self,
        *,
        card_id: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> CardDetailResponse:
        """Получение детальной информации по карте."""
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        params = {"contract_id": resolved_contract_id, "card_id": card_id}
        self.logger.info("Requesting card details")
        return await self._request(
            GET_CARD_DETAIL,
            api_version=api_version,
            params=params,
            request_contract_id=resolved_contract_id,
        )

    # --- Блокировка / разблокировка карты ---
    async def block_card(
        self,
        *,
        card_ids: list[str],
        contract_id: str | None = None,
        block: bool = True,
        api_version: str | None = None,
    ) -> IDListResponse:
        """Блокировка или разблокировка топливных карт.

        Типовой сценарий:
            Немедленно заблокировать одну или несколько утраченных карт. Для
            обратной операции передайте ``block=False``.

        Пример вызова:
        ```python
        result = await client.cards.block_card(
            contract_id="contract-id",
            card_ids=["card-id-1", "card-id-2"],
            block=True,
        )
        ```

        Пример payload:
        ```json
        {
          "contract_id": "contract-id",
          "card_id": ["card-id-1", "card-id-2"],
          "block": "true"
        }
        ```
        """

        resolved_contract_id = await self._resolve_contract_id(contract_id)
        payload = {
            "contract_id": resolved_contract_id,
            "card_id": card_ids,
            "block": str(block).lower(),
        }
        if block:
            self.logger.info("Blocking cards")
        else:
            self.logger.info("Unblocking cards")

        return await self._request(
            BLOCK_CARD,
            api_version=api_version,
            data=payload,
            request_contract_id=resolved_contract_id,
        )

    # --- Установка комментария ---
    async def set_card_comment(
        self,
        *,
        card_id: str,
        comment: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> BoolResponse:
        """Установить комментарий на топливную карту."""
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        payload = {
            "card_id": card_id,
            "contract_id": resolved_contract_id,
            "comment": comment,
        }
        self.logger.info("Updating card comment")
        return await self._request(
            SET_CARD_COMMENT,
            api_version=api_version,
            data=payload,
            request_contract_id=resolved_contract_id,
        )

    # --- Запрос одноразового кода для сброса PIN ---
    async def verify_pin(
        self,
        *,
        card_id: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> BoolResponse:
        """Запрос одноразового кода для сброса PIN карты.
        Данный метод позволяет инициировать запрос на сброс попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
        Вам будет отправлено письмо с кодом подтверждения на почту, которая привязана к вашей учетной записи.
        Данный код нужно ввести в метод resetPIN для завершения операции сброса попыток.
        """
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        self.logger.info("Requesting PIN reset verification")
        return await self._request(
            VERIFY_PIN,
            api_version=api_version,
            path_params={"card_id": card_id},
            params={"contract_id": resolved_contract_id},
            request_contract_id=resolved_contract_id,
        )

    # --- Подтверждение сброса PIN ---
    async def reset_pin(
        self,
        *,
        card_id: str,
        code: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> BoolResponse:
        """Подтверждение сброса PIN карты.
        Данный метод позволяет завершить операцию со сбросом попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
        Код подтверждения будет отправлен на почту, которая привязана к вашей учетной записи.
        """
        resolved_contract_id = await self._resolve_contract_id(contract_id)
        payload = {"contract_id": resolved_contract_id, "code": code}
        self.logger.info("Resetting card PIN")
        return await self._request(
            RESET_PIN,
            api_version=api_version,
            path_params={"card_id": card_id},
            data=payload,
            request_contract_id=resolved_contract_id,
        )

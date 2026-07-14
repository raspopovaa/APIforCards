from ..decorators import api_method
from ..logger import logger
from ..modeling import decode_model
from ..models.cards import (
    BoolResponse,
    CardDetailResponse,
    CardDriversResponse,
    CardGroupResponse,
    CardsListResponse,
    CardsV2Response,
    IDListResponse,
)


class CardsMixin:
    """Методы работы с топливными картами."""

    # --- Список карт (v1) ---
    @api_method(require_session=True, default_version="v1")
    async def get_cards_v1(
        self, contract_id: str, cache: bool = True, api_version: str = "v1"
    ) -> CardsListResponse:
        """Список топливных карт (Процессинг).
        :param contract_id: Идентификатор договора
        :param cache: Кеш карт. false или не задан - данные берутся по прямому запросу из процессинга.
        :return: Объект CardsListResponse с данными о картах

        """
        params = {"contract_id": contract_id, "cache": str(cache).lower()}
        logger.info("Requesting cards version=v1")
        data = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        return decode_model(CardsListResponse, data)

    @api_method(require_session=True, default_version="v2")
    async def get_cards_v2(
        self,
        contract_id: str | None = None,
        sort: str = "-id",
        q: str | None = None,
        status: str | None = None,
        carrier: str | None = None,
        platon: bool | None = None,
        avtodor: bool | None = None,
        users: bool | None = None,
        group_id: str | None = None,
        page: int = None,
        onpage: int = None,
        api_version: str = "v2",
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
        resolved_contract_id = contract_id or getattr(self, "contract_id", None)
        if resolved_contract_id is None:
            raise ValueError("contract_id is required when no default contract is selected")

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

        response = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=filtered_params,
        )

        # Возвращаем полный типизированный ответ API
        return decode_model(CardsV2Response, response)

    # --- Список карт по группе ---
    @api_method(require_session=True, default_version="v1")
    async def get_cards_by_group(
        self, contract_id: str, group_id: str, api_version: str = "v1"
    ) -> CardGroupResponse:
        """Получение списка топливных карт по группе карт."""
        params = {"contract_id": contract_id, "group_id": group_id}
        logger.info("Requesting cards by group")
        data = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return decode_model(CardGroupResponse, data)

    # --- Водители по карте ---
    @api_method(require_session=True, default_version="v2")
    async def get_card_drivers(
        self, card_id: str, contract_id: str, api_version: str = "v2"
    ) -> CardDriversResponse:
        """Получение списка водителей по карте."""
        logger.info("Requesting card drivers")
        data = await self._request(
            "get",
            f"cards/{card_id}/drivers",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": contract_id},
        )
        return decode_model(CardDriversResponse, data)

    # --- Детальная информация по карте ---
    @api_method(require_session=True, default_version="v1")
    async def get_card_detail(
        self, contract_id: str, card_id: str, api_version: str = "v1"
    ) -> CardDetailResponse:
        """Получение детальной информации по карте."""
        params = {"contract_id": contract_id, "card_id": card_id}
        logger.info("Requesting card details")
        data = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return decode_model(CardDetailResponse, data)

    # --- Блокировка / разблокировка карты ---
    @api_method(require_session=True, default_version="v1")
    async def block_card(
        self,
        contract_id: str,
        card_ids: list[str],
        block: bool = True,
        api_version: str = "v1",
    ) -> IDListResponse:
        """Блокировка или разблокировка топливных карт.
        :param contract_id: Идентификатор договора
        :param card_ids: Список идентификаторов карт
        :param block: True для блокировки, False для разблокировки
        return: Объект IDListResponse с результатом операции"""

        payload = {
            "contract_id": contract_id,
            "card_id": card_ids,
            "block": str(block).lower(),
        }
        if block:
            logger.info("Blocking cards")
        else:
            logger.info("Unblocking cards")

        data = await self._request(
            "post",
            "blockCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return decode_model(IDListResponse, data)

    # --- Установка комментария ---
    @api_method(require_session=True, default_version="v1")
    async def set_card_comment(
        self, card_id: str, contract_id: str, comment: str, api_version: str = "v1"
    ) -> BoolResponse:
        """Установить комментарий на топливную карту."""
        payload = {"card_id": card_id, "contract_id": contract_id, "comment": comment}
        logger.info("Updating card comment")
        data = await self._request(
            "post",
            "setCardComment",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return decode_model(BoolResponse, data)

    # --- Запрос одноразового кода для сброса PIN ---
    @api_method(require_session=True, default_version="v2")
    async def verify_pin(
        self, card_id: str, contract_id: str, api_version: str = "v2"
    ) -> BoolResponse:
        """Запрос одноразового кода для сброса PIN карты.
        Данный метод позволяет инициировать запрос на сброс попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
        Вам будет отправлено письмо с кодом подтверждения на почту, которая привязана к вашей учетной записи.
        Данный код нужно ввести в метод resetPIN для завершения операции сброса попыток.
        """
        logger.info("Requesting PIN reset verification")
        data = await self._request(
            "post",
            f"cards/{card_id}/verifyPIN",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": contract_id},
        )
        return decode_model(BoolResponse, data)

    # --- Подтверждение сброса PIN ---
    @api_method(require_session=True, default_version="v2")
    async def reset_pin(
        self, card_id: str, contract_id: str, code: str, api_version: str = "v2"
    ) -> BoolResponse:
        """Подтверждение сброса PIN карты.
        Данный метод позволяет завершить операцию со сбросом попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
        Код подтверждения будет отправлен на почту, которая привязана к вашей учетной записи.
        """
        payload = {"contract_id": contract_id, "code": code}
        logger.info("Resetting card PIN")
        data = await self._request(
            "post",
            f"cards/{card_id}/resetPIN",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return decode_model(BoolResponse, data)

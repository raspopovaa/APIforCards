from typing import Optional

from ..decorators import api_method
from ..logger import logger
from ..models.dictionaries import (
    AzsFiltersResponse,
    AzsListV1Response,
    AzsListV2Response,
    DictionaryResponse,
)


class DictionariesMixin:
    """Методы для работы со справочниками и торговыми точками"""

    # ==========================================================
    # 🔹 Получение списка торговых точек (v1)
    # ==========================================================
    @api_method(require_session=True, default_version="v1")
    async def get_azs_list_v1(
        self,
        page: int = 1,
        onpage: int = 10,
        filter: Optional[dict] = None,
        id: Optional[str] = None,
        api_version: str = "v1",
    ) -> AzsListV1Response:
        """
        Получение списка торговых точек (АЗС, версия 1)

        Позволяет получить список АЗС с фильтрацией и пагинацией.
        """
        logger.info("Получение списка торговых точек (v1), страница %s", page)

        params = {"page": page, "onpage": onpage}
        if filter:
            params["filter"] = filter
        if id:
            params["id"] = id

        data = await self._request(
            "get",
            "AZS",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        return AzsListV1Response(**data)

    # ==========================================================
    # 🔹 Получение списка торговых точек (v2)
    # ==========================================================
    @api_method(require_session=True, default_version="v2")
    async def get_azs_list_v2(
        self,
        filter: Optional[dict] = None,
        q: Optional[str] = None,
        api_version: str = "v2",
    ) -> AzsListV2Response:
        """
        Получение списка торговых точек (АЗС, версия 2)

        Новая версия метода с расширенной фильтрацией и улучшенной структурой ответа.
        """
        logger.info("Получение списка торговых точек (v2) с фильтрацией: %s", filter)

        params = {}
        if filter:
            params["filter"] = filter
        if q:
            params["q"] = q

        data = await self._request(
            "get",
            "azs",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return AzsListV2Response(**data)

    # ==========================================================
    # 🔹 Получение списка фильтров торговых точек
    # ==========================================================
    @api_method(require_session=True, default_version="v2")
    async def get_azs_filters(
        self,
        *,
        api_version: str = "v2",
    ) -> AzsFiltersResponse:
        """
        Получить список доступных фильтров для поиска торговых точек (АЗС)
        """
        logger.info("Получение списка фильтров торговых точек")

        data = await self._request(
            "get",
            "azs/filters",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )

        # У метода data — это словарь с результатом фильтров
        logger.info("Получен список фильтров: %s", data)
        return AzsFiltersResponse(**data)

    # ==========================================================
    # 🔹 Получение общего справочника
    # ==========================================================
    @api_method(require_session=True, default_version="v1")
    async def get_dictionary(
        self,
        *,
        name: str,
        api_version: str = "v1",
    ) -> DictionaryResponse:
        """
        Получить общий справочник по имени.

        Примеры доступных справочников:
        - CardStatus – статусы карт
        - ContractStatus – статусы договоров
        - Country – список стран
        - Currency – список валют
        - Goods – виды топлива
        - PaymentScheme – схемы оплаты
        - PaymentTerm – условия оплаты
        - ProductGroup – группы продуктов
        - ProductType – типы продуктов
        - POIType – типы торговых точек
        - Region – регионы
        - Services – услуги на АЗС
        - Unit – единицы измерения
        - Office – офисы продаж
        - POIPartner – партнёры
        - DiscountScheme – схемы расчёта скидок
        """
        logger.info("Получение справочника: %s", name)

        params = {"name": name}

        data = await self._request(
            "get",
            "getDictionary",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        return DictionaryResponse(**data)

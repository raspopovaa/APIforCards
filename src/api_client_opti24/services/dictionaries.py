from typing import Any, Optional

from ..decorators import api_method
from ..models.dictionaries import (
    AzsFiltersResponse,
    AzsListV1Response,
    AzsListV2Response,
    DictionaryResponse,
)
from ..service_base import _BaseService


class DictionariesService(_BaseService):
    """Методы для работы со справочниками и торговыми точками"""

    # ==========================================================
    # 🔹 Получение списка торговых точек (v1)
    # ==========================================================
    @api_method(require_session=True, default_version="v1")
    async def get_azs_list_v1(
        self,
        page: int = 1,
        onpage: int = 10,
        filter: Optional[dict[str, Any]] = None,
        id: Optional[str] = None,
        api_version: str = "v1",
    ) -> AzsListV1Response:
        """
        Получение списка торговых точек (АЗС, версия 1)

        Позволяет получить список АЗС с фильтрацией и пагинацией.
        """
        self.logger.info("Получение списка торговых точек (v1), страница %s", page)

        params: dict[str, Any] = {"page": page, "onpage": onpage}
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
        filter: Optional[dict[str, Any]] = None,
        q: Optional[str] = None,
        api_version: str = "v2",
    ) -> AzsListV2Response:
        """
        Получение списка торговых точек (АЗС, версия 2)

        Новая версия метода с расширенной фильтрацией и улучшенной структурой ответа.
        """
        self.logger.info("Получение списка торговых точек (v2) с фильтрацией: %s", filter)

        params: dict[str, Any] = {}
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
        self.logger.info("Получение списка фильтров торговых точек")

        data = await self._request(
            "get",
            "azs/filters",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )

        # У метода data — это словарь с результатом фильтров
        self.logger.info("Dictionary filters received")
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
        self.logger.info("Получение справочника: %s", name)

        params = {"name": name}

        data = await self._request(
            "get",
            "getDictionary",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        return DictionaryResponse(**data)

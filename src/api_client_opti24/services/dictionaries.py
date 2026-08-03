from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
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
    @api_method
    async def get_azs_list_v1(
        self,
        *,
        page: int = 1,
        onpage: int = 10,
        filter: dict[str, Any] | None = None,
        id: str | None = None,
        api_version: str | None = None,
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
            "get_azs_list_v1",
            api_version=api_version,
            params=params,
        )

        return decode_model(AzsListV1Response, data)

    # ==========================================================
    # 🔹 Получение списка торговых точек (v2)
    # ==========================================================
    @api_method
    async def get_azs_list_v2(
        self,
        *,
        filter: dict[str, Any] | None = None,
        q: str | None = None,
        api_version: str | None = None,
    ) -> AzsListV2Response:
        """
        Получение списка торговых точек (АЗС, версия 2)

        Новая версия метода с расширенной фильтрацией и улучшенной структурой ответа.

        Типовой сценарий:
            Получить доступные торговые точки перед расчётом финальных цен или
            построением маршрута.

        Пример вызова:
        ```python
        stations = await client.dictionaries.get_azs_list_v2(
            filter={"services": ["fuel"]},
            q="Новосибирск",
        )
        ```

        Пример query-параметров:
        ```json
        {"filter": {"services": ["fuel"]}, "q": "Новосибирск"}
        ```
        """
        self.logger.info("Получение списка торговых точек (v2) с фильтрацией: %s", filter)

        params: dict[str, Any] = {}
        if filter:
            params["filter"] = filter
        if q:
            params["q"] = q

        data = await self._request(
            "get_azs_list_v2",
            api_version=api_version,
            params=params,
        )
        return decode_model(AzsListV2Response, data)

    # ==========================================================
    # 🔹 Получение списка фильтров торговых точек
    # ==========================================================
    @api_method
    async def get_azs_filters(
        self,
        *,
        api_version: str | None = None,
    ) -> AzsFiltersResponse:
        """
        Получить список доступных фильтров для поиска торговых точек (АЗС)
        """
        self.logger.info("Получение списка фильтров торговых точек")

        data = await self._request(
            "get_azs_filters",
            api_version=api_version,
        )

        # У метода data — это словарь с результатом фильтров
        self.logger.info("Dictionary filters received")
        return decode_model(AzsFiltersResponse, data)

    # ==========================================================
    # 🔹 Получение общего справочника
    # ==========================================================
    @api_method
    async def get_dictionary(
        self,
        *,
        name: str,
        api_version: str | None = None,
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
            "get_dictionary",
            api_version=api_version,
            params=params,
        )

        return decode_model(DictionaryResponse, data)

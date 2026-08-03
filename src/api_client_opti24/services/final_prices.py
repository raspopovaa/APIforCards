from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.final_prices import CheckPurchaseResponse, FinalPricesResponse
from ..service_base import _BaseService


class FinalPricesService(_BaseService):
    """
    Методы для получения финальных цен и проверки покупок по карте.
    """

    @api_method
    async def get_final_prices(
        self,
        *,
        card_id: str,
        poi_id: str,
        goods: list[str],
        api_version: str | None = None,
    ) -> FinalPricesResponse:
        """
        Получение финальных цен на АЗС по карте (POST /vip/v2/cards/{card_id}/calculatePrices)

        Типовой сценарий:
            Перед оплатой получить персональные цены для выбранной карты,
            торговой точки и перечня товаров.

        Пример вызова:
        ```python
        prices = await client.final_prices.get_final_prices(
            card_id="card-id",
            poi_id="poi-id",
            goods=["fuel-code-1", "fuel-code-2"],
        )
        ```

        Пример payload:
        ```json
        {"poi_id": "poi-id", "goods": ["fuel-code-1", "fuel-code-2"]}
        ```
        """
        payload = {"poi_id": poi_id, "goods": goods}
        self.logger.info("Requesting final prices")

        data = await self._request(
            "get_final_prices",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=payload,
        )

        return decode_model(FinalPricesResponse, data)

    @api_method
    async def check_purchase(
        self,
        *,
        card_id: str,
        poi_id: str,
        goods: list[dict[str, Any]],
        api_version: str | None = None,
    ) -> CheckPurchaseResponse:
        """
        Проверка возможности проведения транзакции по карте
        (POST /vip/v2/cards/{card_id}/checkPurchase)
        """
        payload = {"poi_id": poi_id, "goods": goods}
        self.logger.info("Checking purchase availability")

        data = await self._request(
            "check_purchase",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=payload,
        )

        return decode_model(CheckPurchaseResponse, data)

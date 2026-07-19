from typing import Any

from ..decorators import api_method
from ..models.final_prices import CheckPurchaseResponse, FinalPricesResponse
from ..service_base import _BaseService


class FinalPricesService(_BaseService):
    """
    Методы для получения финальных цен и проверки покупок по карте.
    """

    @api_method(require_session=True, default_version="v2")
    async def get_final_prices(
        self,
        *,
        card_id: str,
        poi_id: str,
        goods: list[str],
        api_version: str = "v2",
    ) -> FinalPricesResponse:
        """
        Получение финальных цен на АЗС по карте (POST /vip/v2/cards/{card_id}/calculatePrices)
        """
        payload = {"poi_id": poi_id, "goods": goods}
        self.logger.info("Requesting final prices")

        data = await self._request(
            "post",
            f"cards/{card_id}/calculatePrices",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )

        return FinalPricesResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def check_purchase(
        self,
        *,
        card_id: str,
        poi_id: str,
        goods: list[dict[str, Any]],
        api_version: str = "v2",
    ) -> CheckPurchaseResponse:
        """
        Проверка возможности проведения транзакции по карте
        (POST /vip/v2/cards/{card_id}/checkPurchase)
        """
        payload = {"poi_id": poi_id, "goods": goods}
        self.logger.info("Checking purchase availability")

        data = await self._request(
            "post",
            f"cards/{card_id}/checkPurchase",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )

        return CheckPurchaseResponse(**data)

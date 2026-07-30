from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.final_prices import (
    CheckPurchaseRequest,
    CheckPurchaseResponse,
    FinalPricesResponse,
)
from ..service_base import _BaseService


class FinalPricesService(_BaseService):
    """Методы для получения финальных цен и проверки покупок по карте."""

    @api_method
    async def get_final_prices(
        self,
        *,
        card_id: str,
        poi_id: str,
        goods: list[str],
        api_version: str | None = None,
    ) -> FinalPricesResponse:
        """Получить финальные цены на АЗС по карте."""
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
        """Проверить возможность проведения транзакции по карте."""
        request = CheckPurchaseRequest.model_validate({"poi_id": poi_id, "goods": goods})
        payload = request.model_dump(by_alias=True, exclude_none=True)
        self.logger.info("Checking purchase availability")

        data = await self._request(
            "check_purchase",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=payload,
        )

        return decode_model(CheckPurchaseResponse, data)

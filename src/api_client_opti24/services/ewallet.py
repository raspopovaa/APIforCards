from decimal import Decimal
from typing import Literal

from ..decorators import api_method
from ..modeling import decode_model
from ..models.ewallet import (
    MoveToCardResponse,
    MoveToContractResponse,
    SetCardProductResponse,
)
from ..service_base import _BaseService
from ..utils import to_json_param
from ..validation import decimal_to_wire, require_identifier

CardProduct = Literal["wallet", "limit"]


class EwalletService(_BaseService):
    """
    Методы для работы с электронными кошельками (Ewallet).

    Электронный кошелёк — это тип карты, обслуживание которой производится не из средств договора,
    а из отдельного кошелькового счёта. Пользователь может:
      • менять тип карты (лимитная ↔ электронный кошелёк);
      • переводить средства со счёта договора на кошелёк;
      • переводить средства обратно с кошелька на договор.
    """

    # ============================================================
    # Изменить тип продукта карты
    # ============================================================

    @api_method
    async def set_card_product(
        self,
        *,
        contract_id: str | None = None,
        card_ids: list[str],
        product: CardProduct,
        api_version: str | None = None,
    ) -> SetCardProductResponse:
        """
        Изменить тип карты (лимитная ↔ электронный кошелёк).

        Args:
            contract_id: Идентификатор договора (если не указан — берётся из сессии).
            card_ids: Список ID карт для изменения.
            product: Тип продукта ("limit" или "wallet").
            api_version: Версия API (по умолчанию v1).

        Returns:
            SetCardProductResponse: Результат изменения продукта карт.
        """
        cid = await self._resolve_contract_id(contract_id)
        if not card_ids:
            raise ValueError("card_ids must contain at least one card ID")
        normalized_card_ids = [require_identifier(card_id, "card_id") for card_id in card_ids]
        if product not in {"wallet", "limit"}:
            raise ValueError("product must be either 'wallet' or 'limit'")

        body = {
            "contract_id": cid,
            "card_id": to_json_param(normalized_card_ids),
            "product": product,
        }

        data = await self._request(
            "set_card_product",
            api_version=api_version,
            data=body,
        )

        return decode_model(SetCardProductResponse, data)

    # ============================================================
    # Перевести деньги с договора на кошелёк
    # ============================================================

    @api_method
    async def move_to_card(
        self,
        *,
        contract_id: str | None = None,
        card_id: str,
        amount: Decimal,
        api_version: str | None = None,
    ) -> MoveToCardResponse:
        """
        Перевести деньги со счёта договора на электронный кошелёк карты.

        Args:
            contract_id: Идентификатор договора.
            card_id: Идентификатор карты-кошелька.
            amount: Сумма перевода.
            api_version: Версия API (по умолчанию v1).

        Returns:
            MoveToCardResponse: Результат перевода.

        Типовой сценарий:
            Пополнить электронный кошелёк конкретной карты перед поездкой.
            Операция изменяет баланс и не должна повторяться вслепую после
            неопределённого сетевого результата.

        Пример вызова:
        ```python
        transfer = await client.ewallet.move_to_card(
            contract_id="contract-id",
            card_id="card-id",
            amount=Decimal("2500.00"),
        )
        ```

        Пример payload:
        ```json
        {"contract_id": "contract-id", "card_id": "card-id", "amount": "2500.00"}
        ```
        """
        cid = await self._resolve_contract_id(contract_id)

        body = {
            "contract_id": cid,
            "card_id": require_identifier(card_id, "card_id"),
            "amount": decimal_to_wire(amount),
        }

        data = await self._request(
            "move_to_card",
            api_version=api_version,
            data=body,
        )

        return decode_model(MoveToCardResponse, data)

    # ============================================================
    # Перевести деньги с кошелька на договор
    # ============================================================

    @api_method
    async def move_to_contract(
        self,
        *,
        contract_id: str | None = None,
        card_id: str,
        amount: Decimal,
        api_version: str | None = None,
    ) -> MoveToContractResponse:
        """
        Перевести деньги с электронного кошелька карты обратно на договор.

        Args:
            contract_id: Идентификатор договора.
            card_id: Идентификатор карты.
            amount: Сумма перевода.
            api_version: Версия API (по умолчанию v1).

        Returns:
            MoveToContractResponse: Результат перевода.
        """
        cid = await self._resolve_contract_id(contract_id)

        body = {
            "contract_id": cid,
            "card_id": require_identifier(card_id, "card_id"),
            "amount": decimal_to_wire(amount),
        }

        data = await self._request(
            "move_to_contract",
            api_version=api_version,
            data=body,
        )

        return decode_model(MoveToContractResponse, data)

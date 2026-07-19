from ..decorators import api_method
from ..models.contracts import (
    ContractResponse,
    DocumentsOrderResponse,
    DocumentsResponse,
    InvoiceOrderResponse,
    InvoicesResponse,
    OrderCardsResponse,
    PaymentsResponse,
)
from ..service_base import _BaseService


class ContractsService(_BaseService):
    @api_method
    async def get_contract_data(
        self, contract_id: str, api_version: str | None = None
    ) -> ContractResponse:
        """Получение информации о контракте."""
        params = {"contract_id": contract_id}
        data = await self._request(
            "get_contract_data",
            api_version=api_version,
            params=params,
        )
        return ContractResponse(**data["data"])

    @api_method
    async def get_payments(
        self, contract_id: str, api_version: str | None = None
    ) -> PaymentsResponse:
        """Получение данных о платежах по контракту."""
        params = {"contract_id": contract_id}
        data = await self._request(
            "get_payments",
            api_version=api_version,
            params=params,
        )
        return PaymentsResponse(**data)

    @api_method
    async def get_documents(
        self,
        date_start: str,
        date_end: str,
        api_version: str | None = None,
        page: int = 1,
        on_page: int = 10,
    ) -> DocumentsResponse:
        """Получение списка первичных документов (номер документа, дата, сумма, НДС, номер договора и пр.)."""
        params = {
            "date_start": date_start,
            "date_end": date_end,
            "page": page,
            "on_page": on_page,
        }
        data = await self._request(
            "get_documents",
            api_version=api_version,
            params=params,
        )
        return DocumentsResponse(**data)

    @api_method
    async def order_documents_email(
        self, ids: list[str], fmt: str, emails: list[str], api_version: str | None = None
    ) -> DocumentsOrderResponse:
        """Заказ первичных документов по ID документа на указанные email – адреса (до 5 адресов)."""
        payload = {"id": ids, "format": fmt, "emails": emails}
        self.logger.debug("Ordering documents")
        data = await self._request(
            "order_documents_email",
            api_version=api_version,
            json=payload,
        )
        return DocumentsOrderResponse(**data)

    @api_method
    async def order_cards(
        self, count: int, office_id: str, api_version: str | None = None
    ) -> OrderCardsResponse:
        """Заказ необходимого количества топливных карт в определенном офисе продаж."""
        payload = {"count": count, "office_id": office_id}
        self.logger.debug("Ordering cards")
        data = await self._request(
            "order_cards",
            api_version=api_version,
            json=payload,
        )
        return OrderCardsResponse(**data)

    @api_method
    async def order_invoice(
        self, amount: float, email: str, api_version: str | None = None
    ) -> InvoiceOrderResponse:
        """Заказать счёт на оплату и отправить его на email.

        Типовой сценарий:
            Сформировать счёт на заданную сумму после проверки адреса
            получателя. Повтор запроса выполняйте только после проверки статуса
            предыдущей операции.

        Пример вызова:
        ```python
        invoice = await client.contracts.order_invoice(
            amount=15000.0,
            email="billing@example.org",
        )
        ```

        Пример payload:
        ```json
        {"sum": 15000.0, "email": "billing@example.org"}
        ```
        """
        payload = {"sum": amount, "email": email}
        self.logger.debug("Ordering invoice")
        data = await self._request(
            "order_invoice",
            api_version=api_version,
            json=payload,
        )
        return InvoiceOrderResponse(**data)

    @api_method
    async def get_invoices(self, api_version: str | None = None) -> InvoicesResponse:
        """Получение списка счетов на оплату."""
        data = await self._request(
            "get_invoices",
            api_version=api_version,
        )
        return InvoicesResponse(**data)

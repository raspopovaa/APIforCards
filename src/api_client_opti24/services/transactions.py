from collections.abc import Callable
from typing import Any

from .. import utils
from ..decorators import api_method
from ..modeling import decode_model
from ..models.transactions import (
    TransactionDetailResponse,
    TransactionItemV2,
    TransactionsV1Response,
    TransactionsV2Response,
    TransactionV1,
)
from ..service_base import _BaseService


class TransactionsService(_BaseService):
    """
    Методы для работы с транзакциями (v1 и v2).
    """

    # ---------------- Вспомогательный метод ---------------- #

    def _filter_and_sort(
        self,
        items: list[Any],
        *,
        filter_fn: Callable[..., Any] | None = None,
        sort_by: str | None = None,
        reverse: bool = False,
    ) -> list[Any]:
        """
        Фильтрует и сортирует список транзакций.
        """
        result = items

        if filter_fn:
            result = list(filter(filter_fn, result))

        if sort_by:
            try:

                def sort_value(item: Any) -> Any:
                    return getattr(item, sort_by, None)

                result.sort(key=sort_value, reverse=reverse)
            except Exception:
                self.logger.warning("Transaction sorting failed")

        return result

    # ---------------- v1: Транзакции ---------------- #

    @api_method
    async def get_transactions_v1(
        self,
        *,
        contract_id: str,
        card_id: str | None = None,
        count: int = 20,
        api_version: str | None = None,
        filter_fn: Callable[[TransactionV1], bool] | None = None,
        sort_by: str | None = None,
        reverse: bool = False,
    ) -> TransactionsV1Response:
        """
        Получение списка последних транзакций по договору или карте (v1).

        :param contract_id: Идентификатор договора
        :param card_id: Идентификатор карты (опционально)
        :param count: Количество транзакций (по умолчанию 20)
        :param filter_fn: Функция для фильтрации списка
        :param sort_by: Поле для сортировки
        :param reverse: Обратный порядок сортировки
        """
        params = {"contract_id": contract_id, "count": count}
        if card_id:
            params["card_id"] = card_id

        raw = await self._request(
            "get_transactions_v1",
            api_version=api_version,
            params=params,
        )

        tx_response = decode_model(TransactionsV1Response, raw)
        tx_response.data.result = self._filter_and_sort(
            tx_response.data.result,
            filter_fn=filter_fn,
            sort_by=sort_by,
            reverse=reverse,
        )

        return tx_response

    # ---------------- v2: Транзакции по договору ---------------- #

    @api_method
    async def get_transactions_v2(
        self,
        *,
        contract_id: str,
        date_from: str,
        date_to: str,
        page_limit: int = 100,
        page_offset: int = 0,
        api_version: str | None = None,
        filter_fn: Callable[[TransactionItemV2], bool] | None = None,
        sort_by: str | None = None,
        reverse: bool = False,
    ) -> TransactionsV2Response:
        """
        Получение списка транзакций по договору (v2).

        :param contract_id: Идентификатор договора
        :param date_from: Начало периода (YYYY-MM-DD)
        :param date_to: Конец периода (YYYY-MM-DD)
        :param page_limit: Количество записей на странице
        :param page_offset: Смещение страницы

        Типовой сценарий:
            Загрузить страницу транзакций за период не более одного месяца,
            затем при необходимости применить локальную фильтрацию и сортировку.

        Пример вызова:
        ```python
        transactions = await client.transactions.get_transactions_v2(
            contract_id="contract-id",
            date_from="2026-01-01",
            date_to="2026-01-31",
            page_limit=100,
            page_offset=0,
            sort_by="date",
            reverse=True,
        )
        ```

        Пример query-параметров:
        ```json
        {
          "contract_id": "contract-id",
          "date_from": "2026-01-01",
          "date_to": "2026-01-31",
          "page_limit": 100,
          "page_offset": 0
        }
        ```
        """
        utils.validate_month_span(date_from, date_to)

        params = {
            "contract_id": contract_id,
            "date_from": date_from,
            "date_to": date_to,
            "page_limit": page_limit,
            "page_offset": page_offset,
        }

        raw = await self._request(
            "get_transactions_v2",
            api_version=api_version,
            params=params,
        )

        tx_response = decode_model(TransactionsV2Response, raw)
        tx_response.data.result = self._filter_and_sort(
            tx_response.data.result,
            filter_fn=filter_fn,
            sort_by=sort_by,
            reverse=reverse,
        )

        return tx_response

    # ---------------- v2: Транзакции по карте ---------------- #

    @api_method
    async def get_card_transactions_v2(
        self,
        *,
        card_id: str,
        contract_id: str | None = None,
        date_from: str,
        date_to: str,
        page_limit: int = 100,
        page_offset: int = 0,
        api_version: str | None = None,
        filter_fn: Callable[[TransactionItemV2], bool] | None = None,
        sort_by: str | None = None,
        reverse: bool = False,
    ) -> TransactionsV2Response:
        """
        Получение списка транзакций по карте (v2).

        :param card_id: Идентификатор карты
        :param contract_id: Идентификатор договора (если не указан, берётся из сессии)
        :param date_from: Начало периода (YYYY-MM-DD)
        :param date_to: Конец периода (YYYY-MM-DD)
        """
        utils.validate_month_span(date_from, date_to)

        cid = await self._resolve_contract_id(contract_id)

        params = {
            "contract_id": cid,
            "date_from": date_from,
            "date_to": date_to,
            "page_limit": page_limit,
            "page_offset": page_offset,
        }

        raw = await self._request(
            "get_card_transactions_v2",
            api_version=api_version,
            path_params={"card_id": card_id},
            params=params,
        )

        tx_response = decode_model(TransactionsV2Response, raw)
        tx_response.data.result = self._filter_and_sort(
            tx_response.data.result,
            filter_fn=filter_fn,
            sort_by=sort_by,
            reverse=reverse,
        )

        return tx_response

    # ---------------- v2: Детали транзакции ---------------- #

    @api_method
    async def get_transaction_detail(
        self,
        *,
        transaction_id: str,
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> TransactionDetailResponse:
        """
        Получение детальной информации по транзакции (v2).

        :param transaction_id: ID транзакции
        :param contract_id: Идентификатор договора
        """
        cid = await self._resolve_contract_id(contract_id)

        raw = await self._request(
            "get_transaction_detail",
            api_version=api_version,
            path_params={"transaction_id": transaction_id},
            params={"contract_id": cid},
        )

        return decode_model(TransactionDetailResponse, raw)

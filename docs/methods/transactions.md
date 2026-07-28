# `client.transactions`

Получение списка транзакций и детальной информации по отдельной операции.

## `client.transactions.get_card_transactions_v2()`

Получение списка транзакций по карте (v2).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `cards/{card_id}/transactions` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор карты |
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора (если не указан, берётся из сессии) |
| `date_from` | `str` | Да | — | Начало периода (YYYY-MM-DD) |
| `date_to` | `str` | Да | — | Конец периода (YYYY-MM-DD) |
| `page_limit` | `int` | Нет | `100` | Параметр публичного метода SDK. |
| `page_offset` | `int` | Нет | `0` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `filter_fn` | `Callable[[<class 'api_client_opti24.models.transactions.TransactionItemV2'>], bool] | None` | Нет | `None` | Параметр публичного метода SDK. |
| `sort_by` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `reverse` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TransactionsV2Response`

### Пример

```python
result = await client.transactions.get_card_transactions_v2(
    card_id="card-id",
    date_from="date-from",
    date_to="date-to",
    page_limit=100,
    page_offset=0,
    reverse=False,
)
print(result)
```

## `client.transactions.get_transaction_detail()`

Получить детальную информацию об одной транзакции.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `transactions/{transaction_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `transaction_id` | `str` | Да | — | ID транзакции |
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TransactionDetailResponse`

### Пример

```python
result = await client.transactions.get_transaction_detail(
    transaction_id="transaction-id",
)
print(result)
```

## `client.transactions.get_transactions_v1()`

Получение списка последних транзакций по договору или карте (v1).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `transactions` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора |
| `card_id` | `str | None` | Нет | `None` | Идентификатор карты (опционально) |
| `count` | `int` | Нет | `20` | Количество транзакций (по умолчанию 20) |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `filter_fn` | `Callable[[<class 'api_client_opti24.models.transactions.TransactionV1'>], bool] | None` | Нет | `None` | Функция для фильтрации списка |
| `sort_by` | `str | None` | Нет | `None` | Поле для сортировки |
| `reverse` | `bool` | Нет | `False` | Обратный порядок сортировки |

### Возвращаемое значение

`TransactionsV1Response`

### Пример

```python
result = await client.transactions.get_transactions_v1(
    contract_id="contract-id",
    count=20,
    reverse=False,
)
print(result)
```

## `client.transactions.get_transactions_v2()`

Получить транзакции договора за заданный период.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `transactions` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора |
| `date_from` | `str` | Да | — | Начало периода (YYYY-MM-DD) |
| `date_to` | `str` | Да | — | Конец периода (YYYY-MM-DD) |
| `page_limit` | `int` | Нет | `100` | Количество записей на странице |
| `page_offset` | `int` | Нет | `0` | Смещение страницы Типовой сценарий: Загрузить страницу транзакций за период не более одного месяца, затем при необходимости применить локальную фильтрацию и сортировку. Пример вызова: ```python transactions = await client.transactions.get_transactions_v2( contract_id="contract-id", date_from="2026-01-01", date_to="2026-01-31", page_limit=100, page_offset=0, sort_by="date", reverse=True, ) ``` Пример query-параметров: ```json { "contract_id": "contract-id", "date_from": "2026-01-01", "date_to": "2026-01-31", "page_limit": 100, "page_offset": 0 } ``` |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `filter_fn` | `Callable[[<class 'api_client_opti24.models.transactions.TransactionItemV2'>], bool] | None` | Нет | `None` | Параметр публичного метода SDK. |
| `sort_by` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `reverse` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TransactionsV2Response`

### Пример

```python
result = await client.transactions.get_transactions_v2(
    contract_id="contract-id",
    date_from="date-from",
    date_to="date-to",
    page_limit=100,
    page_offset=0,
    reverse=False,
)
print(result)
```

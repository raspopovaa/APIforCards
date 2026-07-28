# `client.contracts`

Данные договора, платежи, счета, документы и заказ топливных карт.

## `client.contracts.get_contract_data()`

Получение информации о контракте.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `getPartContractData` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`ContractResponse`

### Пример

```python
result = await client.contracts.get_contract_data(
    contract_id="contract-id",
)
print(result)
```

## `client.contracts.get_documents()`

Получение списка первичных документов (номер документа, дата, сумма, НДС, номер договора и пр.).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `documents` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `date_start` | `str` | Да | — | Параметр публичного метода SDK. |
| `date_end` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `page` | `int` | Нет | `1` | Номер страницы результата. |
| `on_page` | `int` | Нет | `10` | Параметр публичного метода SDK. |

### Возвращаемое значение

`DocumentsResponse`

### Пример

```python
result = await client.contracts.get_documents(
    date_start="date-start",
    date_end="date-end",
    page=1,
    on_page=10,
)
print(result)
```

## `client.contracts.get_invoices()`

Получение списка счетов на оплату.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `invoices` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`InvoicesResponse`

### Пример

```python
result = await client.contracts.get_invoices(
)
print(result)
```

## `client.contracts.get_payments()`

Получение данных о платежах по контракту.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `getPayments` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`PaymentsResponse`

### Пример

```python
result = await client.contracts.get_payments(
    contract_id="contract-id",
)
print(result)
```

## `client.contracts.order_cards()`

Заказ необходимого количества топливных карт в определенном офисе продаж.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `orderCards` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `count` | `int` | Да | — | Параметр публичного метода SDK. |
| `office_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`OrderCardsResponse`

### Пример

```python
result = await client.contracts.order_cards(
    count=1,
    office_id="office-id",
)
print(result)
```

## `client.contracts.order_documents_email()`

Заказ первичных документов по ID документа на указанные email – адреса (до 5 адресов).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `documents` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `ids` | `list[str]` | Да | — | Параметр публичного метода SDK. |
| `fmt` | `str` | Да | — | Параметр публичного метода SDK. |
| `emails` | `list[str]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`DocumentsOrderResponse`

### Пример

```python
result = await client.contracts.order_documents_email(
    ids=["item-id"],
    fmt="fmt",
    emails=["item-id"],
)
print(result)
```

## `client.contracts.order_invoice()`

Заказать счёт на оплату и отправить его на email.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `invoice` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `amount` | `float` | Да | — | Параметр публичного метода SDK. |
| `email` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`InvoiceOrderResponse`

### Пример

```python
result = await client.contracts.order_invoice(
    amount=1.0,
    email="email",
)
print(result)
```

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

**Тип после валидации:** `ContractResponse`

**Pydantic-модель:** [`ContractResponse`](../data-types/contracts/ContractResponse.md)

Ответ передаётся в `ContractResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `mpc` | `bool` | `boolean` | Да | Нет | Разрешен ли выпуск виртуальных карт |
| `template_id` | `str` | `string` | Да | Нет | ID шаблона виртуальных карт |
| `status` | `str` | `string` | Да | Нет | Статус Way4 |
| `status_crm` | `str` | `string` | Да | Нет | Статус CRM |
| `payment_term_id` | `str \| None` | `string \| null` | Нет | Да | ID справочника условия оплаты |
| `payment_scheme_id` | `str \| None` | `string \| null` | Нет | Да | ID справочника схема оплаты |
| `is_dealer` | `bool` | `boolean` | Да | Нет | Признак дилерский |
| `balanceData` | `BalanceData` | `object (BalanceData)` | Да | Нет | Данные по расходу и балансу договора |
| `contractData` | `ContractData` | `object (ContractData)` | Да | Нет | Данные договора |
| `managerData` | `ManagerData \| None` | `object (ManagerData) \| null` | Нет | Да | Данные по менеджеру договора |
| `cardsData` | `CardsData` | `object (CardsData)` | Да | Нет | Данные по количеству карт и групп карт на договоре |

**Вложенные модели:**
- [`BalanceData`](../data-types/contracts/BalanceData.md)
- [`ContractData`](../data-types/contracts/ContractData.md)
- [`ManagerData`](../data-types/contracts/ManagerData.md)
- [`CardsData`](../data-types/contracts/CardsData.md)

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
| `date_start` | `str` | Да | — | Дата начала периода в формате `YYYY-MM-DD`. |
| `date_end` | `str` | Да | — | Дата окончания периода в формате `YYYY-MM-DD`. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `page` | `int` | Нет | `1` | Номер страницы результата. |
| `on_page` | `int` | Нет | `10` | Количество элементов на странице. |

### Возвращаемое значение

**Тип после валидации:** `DocumentsResponse`

**Pydantic-модель:** [`DocumentsResponse`](../data-types/contracts/DocumentsResponse.md)

Ответ передаётся в `DocumentsResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект статуса, например {'code': 200} |
| `data` | `DocumentsData` | `object (DocumentsData)` | Да | Нет | Основные данные — список документов |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (Unix timestamp) |

**Вложенные модели:**
- [`DocumentsData`](../data-types/contracts/DocumentsData.md)

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

**Тип после валидации:** `InvoicesResponse`

**Pydantic-модель:** [`InvoicesResponse`](../data-types/contracts/InvoicesResponse.md)

Ответ передаётся в `InvoicesResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект статуса, например {'code': 200} |
| `data` | `InvoicesData` | `object (InvoicesData)` | Да | Нет | Основные данные — список счетов |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (Unix timestamp) |

**Вложенные модели:**
- [`InvoicesData`](../data-types/contracts/InvoicesData.md)

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

**Тип после валидации:** `PaymentsResponse`

**Pydantic-модель:** [`PaymentsResponse`](../data-types/contracts/PaymentsResponse.md)

Ответ передаётся в `PaymentsResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект с кодом статуса ответа сервера, например {'code': 200} |
| `data` | `PaymentsData` | `object (PaymentsData)` | Да | Нет | Основная часть ответа с данными о платежах |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа сервера в формате Unix timestamp |

**Вложенные модели:**
- [`PaymentsData`](../data-types/contracts/PaymentsData.md)

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
| `count` | `int` | Да | — | Количество заказываемых карт. |
| `office_id` | `str` | Да | — | ID офиса продаж из справочника `Office`. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `OrderCardsResponse`

**Pydantic-модель:** [`OrderCardsResponse`](../data-types/contracts/OrderCardsResponse.md)

Ответ передаётся в `OrderCardsResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект статуса, например {'code': 200} |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции: true — заказ выполнен успешно |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (Unix timestamp) |

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
| `ids` | `list[str]` | Да | — | Список ID документов. В API параметр называется `id`. |
| `fmt` | `str` | Да | — | Формат документа: `pdf` или `xlsx`. В API параметр называется `format`. |
| `emails` | `list[str]` | Да | — | Список email-адресов для отправки документов, не более пяти. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `DocumentsOrderResponse`

**Pydantic-модель:** [`DocumentsOrderResponse`](../data-types/contracts/DocumentsOrderResponse.md)

Ответ передаётся в `DocumentsOrderResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект статуса, например {'code': 200} |
| `data` | `bool` | `boolean` | Да | Нет | Признак успешной отправки (true — заказ выполнен) |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (Unix timestamp) |

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
| `amount` | `float` | Да | — | Сумма счёта в рублях. В API параметр называется `sum`. |
| `email` | `str` | Да | — | Email-адрес для отправки счёта. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `InvoiceOrderResponse`

**Pydantic-модель:** [`InvoiceOrderResponse`](../data-types/contracts/InvoiceOrderResponse.md)

Ответ передаётся в `InvoiceOrderResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект статуса, например {'code': 200} |
| `data` | `bool` | `boolean` | Да | Нет | Признак успешного создания счёта |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (Unix timestamp) |

### Пример

```python
result = await client.contracts.order_invoice(
    amount=1.0,
    email="email",
)
print(result)
```

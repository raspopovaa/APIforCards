# `client.cards`

Получение карт и их реквизитов, блокировка, комментарии, водители и операции с PIN.

## `client.cards.block_card()`

Заблокировать или разблокировать одну или несколько топливных карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `blockCard` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_ids` | `list[str]` | Да | — | Список идентификаторов топливных карт. |
| `block` | `bool` | Нет | `True` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `IDListResponse`

**Pydantic-модель:** [`IDListResponse`](../data-types/cards/IDListResponse.md)

Ответ передаётся в `IDListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус запроса |
| `data` | `list[str]` | `array[string]` | Да | Нет | ID карт, которые были заблокированы/разблокированы |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

### Пример

```python
result = await client.cards.block_card(
    contract_id="contract-id",
    card_ids=["item-id"],
    block=True,
)
print(result)
```

## `client.cards.get_card_detail()`

Получить детальную информацию о топливной карте.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `cards` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `CardDetailResponse`

**Pydantic-модель:** [`CardDetailResponse`](../data-types/cards/CardDetailResponse.md)

Ответ передаётся в `CardDetailResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус ответа |
| `data` | `CardDetailData` | `object (CardDetailData)` | Да | Нет | Основные данные |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

**Вложенные модели:**
- [`CardDetailData`](../data-types/cards/CardDetailData.md)

### Пример

```python
result = await client.cards.get_card_detail(
    contract_id="contract-id",
    card_id="card-id",
)
print(result)
```

## `client.cards.get_card_drivers()`

Получение списка водителей по карте.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `cards/{card_id}/drivers` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `CardDriversResponse`

**Pydantic-модель:** [`CardDriversResponse`](../data-types/cards/CardDriversResponse.md)

Ответ передаётся в `CardDriversResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус запроса |
| `data` | `CardDriversData` | `object (CardDriversData)` | Да | Нет | Основные данные |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

**Вложенные модели:**
- [`CardDriversData`](../data-types/cards/CardDriversData.md)

### Пример

```python
result = await client.cards.get_card_drivers(
    card_id="card-id",
    contract_id="contract-id",
)
print(result)
```

## `client.cards.get_cards_by_group()`

Получение списка топливных карт по группе карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `cards` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `group_id` | `str` | Да | — | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `CardGroupResponse`

**Pydantic-модель:** [`CardGroupResponse`](../data-types/cards/CardGroupResponse.md)

Ответ передаётся в `CardGroupResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус ответа |
| `data` | `CardGroupData` | `object (CardGroupData)` | Да | Нет | Основные данные |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

**Вложенные модели:**
- [`CardGroupData`](../data-types/cards/CardGroupData.md)

### Пример

```python
result = await client.cards.get_cards_by_group(
    contract_id="contract-id",
    group_id="group-id",
)
print(result)
```

## `client.cards.get_cards_v1()`

Получить список топливных карт через API v1.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `cards` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора |
| `cache` | `bool` | Нет | `True` | Кеш карт. false или не задан - данные берутся по прямому запросу из процессинга. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `CardsListResponse`

**Pydantic-модель:** [`CardsListResponse`](../data-types/cards/CardsListResponse.md)

Ответ передаётся в `CardsListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект со статусом ответа (например, {'code': 200}) |
| `data` | `CardsListData` | `object (CardsListData)` | Да | Нет | Основные данные ответа |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка сервера (UNIX-timestamp) |

**Вложенные модели:**
- [`CardsListData`](../data-types/cards/CardsListData.md)

### Пример

```python
result = await client.cards.get_cards_v1(
    contract_id="contract-id",
    cache=True,
)
print(result)
```

## `client.cards.get_cards_v2()`

Получить постраничный список топливных карт договора через API v2.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `cards` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора |
| `sort` | `str` | Нет | `'-id'` | Поле сортировки (по умолчанию '-id') |
| `q` | `str | None` | Нет | `None` | Поисковый запрос (например, часть номера карты) |
| `status` | `str | None` | Нет | `None` | Фильтр по статусу карты (Active, Locked и т.д.) |
| `carrier` | `str | None` | Нет | `None` | Тип носителя карты ('Plastic', 'Virtual Card') |
| `platon` | `bool | None` | Нет | `None` | Фильтр по поддержке Платон |
| `avtodor` | `bool | None` | Нет | `None` | Фильтр по поддержке Автодор |
| `users` | `bool | None` | Нет | `None` | Фильтр по наличию пользователей |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы карт (опционально) |
| `page` | `int | None` | Нет | `None` | Номер страницы (по умолчанию 1) |
| `onpage` | `int | None` | Нет | `None` | Количество элементов на странице (по умолчанию 10) |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `CardsV2Response`

**Pydantic-модель:** [`CardsV2Response`](../data-types/cards/CardsV2Response.md)

Ответ передаётся в `CardsV2Response.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Объект статуса (например {'code': 200}) |
| `data` | `CardsV2Data` | `object (CardsV2Data)` | Да | Нет | Основные данные (список карт) |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (Unix timestamp) |

**Вложенные модели:**
- [`CardsV2Data`](../data-types/cards/CardsV2Data.md)

### Пример

```python
result = await client.cards.get_cards_v2(
    sort='-id',
)
print(result)
```

## `client.cards.reset_pin()`

Подтверждение сброса PIN карты.
Данный метод позволяет завершить операцию со сбросом попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
Код подтверждения будет отправлен на почту, которая привязана к вашей учетной записи.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `cards/{card_id}/resetPIN` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `code` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `BoolResponse`

**Pydantic-модель:** [`BoolResponse`](../data-types/cards/BoolResponse.md)

Ответ передаётся в `BoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус запроса |
| `data` | `bool` | `boolean` | Да | Нет | Флаг результата операции (True — успех) |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

### Пример

```python
result = await client.cards.reset_pin(
    card_id="card-id",
    contract_id="contract-id",
    code="code",
)
print(result)
```

## `client.cards.set_card_comment()`

Установить комментарий на топливную карту.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setCardComment` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `comment` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `BoolResponse`

**Pydantic-модель:** [`BoolResponse`](../data-types/cards/BoolResponse.md)

Ответ передаётся в `BoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус запроса |
| `data` | `bool` | `boolean` | Да | Нет | Флаг результата операции (True — успех) |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

### Пример

```python
result = await client.cards.set_card_comment(
    card_id="card-id",
    contract_id="contract-id",
    comment="comment",
)
print(result)
```

## `client.cards.verify_pin()`

Запрос одноразового кода для сброса PIN карты.
Данный метод позволяет инициировать запрос на сброс попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
Вам будет отправлено письмо с кодом подтверждения на почту, которая привязана к вашей учетной записи.
Данный код нужно ввести в метод resetPIN для завершения операции сброса попыток.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `cards/{card_id}/verifyPIN` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `BoolResponse`

**Pydantic-модель:** [`BoolResponse`](../data-types/cards/BoolResponse.md)

Ответ передаётся в `BoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус запроса |
| `data` | `bool` | `boolean` | Да | Нет | Флаг результата операции (True — успех) |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

### Пример

```python
result = await client.cards.verify_pin(
    card_id="card-id",
    contract_id="contract-id",
)
print(result)
```

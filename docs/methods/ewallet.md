# `client.ewallet`

Переводы между договором и картой, а также выбор продуктовой схемы карты.

## `client.ewallet.move_to_card()`

Перевести деньги со счёта договора на электронный кошелёк карты.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `moveToCard` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `amount` | `float` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `MoveToCardResponse`

**Pydantic-модель:** [`MoveToCardResponse`](../data-types/ewallet/MoveToCardResponse.md)

Ответ передаётся в `MoveToCardResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `Status` | `object (Status)` | Да | Нет | Статус выполнения операции. |
| `data` | `bool` | `boolean` | Да | Нет | Результат выполнения операции (true — успешно). |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (UNIX timestamp). |

**Вложенные модели:**
- [`Status`](../data-types/ewallet/Status.md)

### Пример

```python
result = await client.ewallet.move_to_card(
    card_id="card-id",
    amount=1.0,
)
print(result)
```

## `client.ewallet.move_to_contract()`

Перевести деньги с электронного кошелька карты обратно на договор.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `moveToContract` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `amount` | `float` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `MoveToContractResponse`

**Pydantic-модель:** [`MoveToContractResponse`](../data-types/ewallet/MoveToContractResponse.md)

Ответ передаётся в `MoveToContractResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `Status` | `object (Status)` | Да | Нет | Статус выполнения операции. |
| `data` | `bool` | `boolean` | Да | Нет | Результат выполнения операции (true — успешно). |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (UNIX timestamp). |

**Вложенные модели:**
- [`Status`](../data-types/ewallet/Status.md)

### Пример

```python
result = await client.ewallet.move_to_contract(
    card_id="card-id",
    amount=1.0,
)
print(result)
```

## `client.ewallet.set_card_product()`

Изменить тип карты (лимитная ↔ электронный кошелёк).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setCardProduct` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_ids` | `list[str]` | Да | — | Список идентификаторов топливных карт. |
| `product` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `SetCardProductResponse`

**Pydantic-модель:** [`SetCardProductResponse`](../data-types/ewallet/SetCardProductResponse.md)

Ответ передаётся в `SetCardProductResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `Status` | `object (Status)` | Да | Нет | Статус выполнения операции. |
| `data` | `list[str]` | `array[string]` | Да | Нет | Список идентификаторов карт, у которых изменён продукт. |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени ответа (UNIX timestamp). |

**Вложенные модели:**
- [`Status`](../data-types/ewallet/Status.md)

### Пример

```python
result = await client.ewallet.set_card_product(
    card_ids=["item-id"],
    product="product",
)
print(result)
```

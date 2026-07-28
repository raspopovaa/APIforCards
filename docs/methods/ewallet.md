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

`MoveToCardResponse`

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

`MoveToContractResponse`

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

`SetCardProductResponse`

### Пример

```python
result = await client.ewallet.set_card_product(
    card_ids=["item-id"],
    product="product",
)
print(result)
```

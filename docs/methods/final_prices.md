# `client.final_prices`

Проверка возможности покупки и расчет итоговых цен по карте.

## `client.final_prices.check_purchase()`

Проверка возможности проведения транзакции по карте
(POST /vip/v2/cards/{card_id}/checkPurchase)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `cards/{card_id}/checkPurchase` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `poi_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `goods` | `list[dict[str, Any]]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`CheckPurchaseResponse`

### Пример

```python
result = await client.final_prices.check_purchase(
    card_id="card-id",
    poi_id="poi-id",
    goods={},
)
print(result)
```

## `client.final_prices.get_final_prices()`

Получение финальных цен на АЗС по карте (POST /vip/v2/cards/{card_id}/calculatePrices)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `cards/{card_id}/calculatePrices` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `poi_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `goods` | `list[str]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`FinalPricesResponse`

### Пример

```python
result = await client.final_prices.get_final_prices(
    card_id="card-id",
    poi_id="poi-id",
    goods=["item-id"],
)
print(result)
```

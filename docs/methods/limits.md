# `client.limits`

Получение, установка и удаление продуктовых лимитов топливной карты.

## `client.limits.get_limits()`

Получить список продуктовых лимитов по договору, карте или группе карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `limit` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | ID договора |
| `card_id` | `str | None` | Нет | `None` | ID карты (опционально) |
| `group_id` | `str | None` | Нет | `None` | ID группы карт (опционально) |
| `api_version` | `str | None` | Нет | `None` | версия API (по умолчанию v1) |

### Возвращаемое значение

`LimitsResponse`

### Пример

```python
result = await client.limits.get_limits(
    contract_id="contract-id",
)
print(result)
```

## `client.limits.remove_limit()`

Удалить продуктовый лимит карты.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `removeLimit` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | ID договора |
| `limit_id` | `str` | Да | — | ID лимита |
| `group_id` | `str | None` | Нет | `None` | ID группы карт (опционально) |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`RemoveLimitResponse`

### Пример

```python
result = await client.limits.remove_limit(
    contract_id="contract-id",
    limit_id="limit-id",
)
print(result)
```

## `client.limits.set_limit()`

Установить или изменить продуктовый лимит карты.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setLimit` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `limits` | `list[dict[str, Any]]` | Да | — | список лимитов в виде словарей (см. документацию API) Типовой сценарий: Ограничить дневной расход конкретной карты. Для изменения ранее созданного лимита добавьте его ``id`` в тот же словарь. Пример вызова: ```python result = await client.limits.set_limit( limits=[{ "contract_id": "contract-id", "card_id": "card-id", "sum": {"currency": "810", "value": 5000.0}, "time": {"number": 1, "type": 1}, }] ) ``` Пример логического payload до сериализации поля ``limit``: ```json { "contract_id": "contract-id", "card_id": "card-id", "sum": {"currency": "810", "value": 5000.0}, "time": {"number": 1, "type": 1} } ``` |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`SetLimitResponse`

### Пример

```python
result = await client.limits.set_limit(
    limits={},
)
print(result)
```

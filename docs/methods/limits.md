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
| `contract_id` | `str | None` | Нет | `None` | ID договора |
| `card_id` | `str | None` | Нет | `None` | ID карты (опционально) |
| `group_id` | `str | None` | Нет | `None` | ID группы карт (опционально) |
| `api_version` | `str | None` | Нет | `None` | версия API (по умолчанию v1) |

### Возвращаемое значение

**Тип после валидации:** `LimitsResponse`

**Pydantic-модель:** [`LimitsResponse`](../data-types/limits/LimitsResponse.md)

Ответ передаётся в `LimitsResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `ResponseStatus` | `object (ResponseStatus)` | Да | Нет | Статус ответа API |
| `data` | `LimitsData` | `object (LimitsData)` | Да | Нет | Типизированные данные ответа API |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа API |

**Вложенные модели:**
- [`ResponseStatus`](../data-types/modeling/ResponseStatus.md)
- [`LimitsData`](../data-types/limits/LimitsData.md)

### Пример

```python
result = await client.limits.get_limits(
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
| `contract_id` | `str | None` | Нет | `None` | ID договора |
| `limit_id` | `str` | Да | — | ID лимита |
| `group_id` | `str | None` | Нет | `None` | ID группы карт (опционально) |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `RemoveLimitResponse`

**Pydantic-модель:** [`RemoveLimitResponse`](../data-types/limits/RemoveLimitResponse.md)

Ответ передаётся в `RemoveLimitResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `ResponseStatus` | `object (ResponseStatus)` | Да | Нет | Статус ответа API |
| `data` | `bool` | `boolean` | Да | Нет | Типизированные данные ответа API |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа API |

**Вложенные модели:**
- [`ResponseStatus`](../data-types/modeling/ResponseStatus.md)

### Пример

```python
result = await client.limits.remove_limit(
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
| `limits` | `list[LimitRequestItem | Mapping[str, Any]]` | Да | — | список лимитов в виде словарей (см. документацию API) Типовой сценарий: Ограничить дневной расход конкретной карты. Для изменения ранее созданного лимита добавьте его ``id`` в тот же словарь. Пример вызова: ```python result = await client.limits.set_limit( limits=[{ "contract_id": "contract-id", "card_id": "card-id", "sum": {"currency": "810", "value": 5000.0}, "time": {"number": 1, "type": 5}, }] ) ``` Пример логического payload до сериализации поля ``limit``: ```json { "contract_id": "contract-id", "card_id": "card-id", "sum": {"currency": "810", "value": 5000.0}, "time": {"number": 1, "type": 5} } ``` |
| `contract_id` | `str | None` | Нет | `None` | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `SetLimitResponse`

**Pydantic-модель:** [`SetLimitResponse`](../data-types/limits/SetLimitResponse.md)

Ответ передаётся в `SetLimitResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `ResponseStatus` | `object (ResponseStatus)` | Да | Нет | Статус ответа API |
| `data` | `list[str]` | `array[string]` | Да | Нет | Типизированные данные ответа API |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа API |

**Вложенные модели:**
- [`ResponseStatus`](../data-types/modeling/ResponseStatus.md)

### Пример

```python
result = await client.limits.set_limit(
    limits="limits",
)
print(result)
```

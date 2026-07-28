# `client.restrictions`

Управление временными, количественными и иными ограничителями топливных карт.

## `client.restrictions.get_restrictions()`

Получение списка товарных ограничителей по договору, карте или группе карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `restriction` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_id` | `str | None` | Нет | `None` | Идентификатор топливной карты. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `RestrictionGetResponse`

**Pydantic-модель:** [`RestrictionGetResponse`](../data-types/restrictions/RestrictionGetResponse.md)

Ответ передаётся в `RestrictionGetResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `data` | `RestrictionList` | `object (RestrictionList)` | Да | Нет | Данные с ограничителями |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа (Unix time) |

**Вложенные модели:**
- [`RestrictionList`](../data-types/restrictions/RestrictionList.md)

### Пример

```python
result = await client.restrictions.get_restrictions(
    contract_id="contract-id",
)
print(result)
```

## `client.restrictions.remove_restriction()`

Удаление товарного ограничителя по карте или группе карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `removeRestriction` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `restriction_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `RestrictionRemoveResponse`

**Pydantic-модель:** [`RestrictionRemoveResponse`](../data-types/restrictions/RestrictionRemoveResponse.md)

Ответ передаётся в `RestrictionRemoveResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения (например, {'code': 200}) |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (True — успешно) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Временная метка ответа (Unix time) |

### Пример

```python
result = await client.restrictions.remove_restriction(
    contract_id="contract-id",
    restriction_id="restriction-id",
)
print(result)
```

## `client.restrictions.set_restriction()`

Установка или изменение товарного ограничителя по карте или группе карт.
Для изменения ограничителя необходимо передавать его ID.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setRestriction` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `restrictions` | `list[dict[str, Any]]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `RestrictionSetResponse`

**Pydantic-модель:** [`RestrictionSetResponse`](../data-types/restrictions/RestrictionSetResponse.md)

Ответ передаётся в `RestrictionSetResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `data` | `list[str]` | `array[string]` | Да | Нет | Список ID созданных или изменённых ограничителей |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа (Unix time) |

### Пример

```python
result = await client.restrictions.set_restriction(
    restrictions={},
)
print(result)
```

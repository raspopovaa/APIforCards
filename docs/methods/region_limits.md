# `client.region_limits`

Получение, установка и удаление ограничений по регионам обслуживания.

## `client.region_limits.get_region_limits()`

Получение списка региональных лимитов по договору, карте или группе карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `regionLimit` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `card_id` | `str | None` | Нет | `None` | Идентификатор топливной карты. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `RegionLimitResponse`

**Pydantic-модель:** [`RegionLimitResponse`](../data-types/region_limits/RegionLimitResponse.md)

Ответ передаётся в `RegionLimitResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус ответа |
| `data` | `RegionLimitList` | `object (RegionLimitList)` | Да | Нет | Данные с лимитами |
| `timestamp` | `int` | `integer` | Да | Нет | Метка времени сервера |

**Вложенные модели:**
- [`RegionLimitList`](../data-types/region_limits/RegionLimitList.md)

### Пример

```python
result = await client.region_limits.get_region_limits(
    contract_id="contract-id",
)
print(result)
```

## `client.region_limits.remove_region_limit()`

Удаление регионального лимита по карте или группе карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `removeRegionLimit` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `regionlimit_id` | `str` | Да | — | ID регионального лимита. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `RemoveRegionLimit`

**Pydantic-модель:** [`RemoveRegionLimit`](../data-types/region_limits/RemoveRegionLimit.md)

Ответ передаётся в `RemoveRegionLimit.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (True — успешно) |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа |

### Пример

```python
result = await client.region_limits.remove_region_limit(
    contract_id="contract-id",
    regionlimit_id="regionlimit-id",
)
print(result)
```

## `client.region_limits.set_region_limit()`

Установка/изменение регионального лимита по карте или группе карт.
Для изменения лимита необходимо передавать его ID.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setRegionLimit` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `region_limits` | `list[dict[str, Any]]` | Да | — | Массив параметров регионального лимита: ID лимита, карты, группы и договора, страна, регион, АЗС, партнёр и `limit_type` (`1` — разрешающий, `2` — запрещающий). |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `dict[str, Any]`

**Pydantic-модель:** нет.

SDK возвращает значение указанного Python-типа; отдельная модель ответа не применяется.

### Пример

```python
result = await client.region_limits.set_region_limit(
    region_limits={},
)
print(result)
```

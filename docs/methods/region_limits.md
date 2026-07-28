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

`RegionLimitResponse`

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
| `regionlimit_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`RemoveRegionLimit`

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
| `region_limits` | `list[dict[str, Any]]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`dict[str, Any]`

### Пример

```python
result = await client.region_limits.set_region_limit(
    region_limits={},
)
print(result)
```

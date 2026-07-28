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

`RestrictionGetResponse`

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

`RestrictionRemoveResponse`

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

`RestrictionSetResponse`

### Пример

```python
result = await client.restrictions.set_restriction(
    restrictions={},
)
print(result)
```

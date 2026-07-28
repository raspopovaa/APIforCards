# `client.card_groups`

Создание, изменение и удаление групп карт, а также управление составом группы.

## `client.card_groups.get_card_groups()`

Получить список групп карт по договору.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `cardGroups` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`CardGroupListResponse`

### Пример

```python
result = await client.card_groups.get_card_groups(
    contract_id="contract-id",
)
print(result)
```

## `client.card_groups.remove_card_group()`

Удалить группу карт по ID.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `removeCardGroup` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `group_id` | `str` | Да | — | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`RemoveCardGroupResponse`

### Пример

```python
result = await client.card_groups.remove_card_group(
    contract_id="contract-id",
    group_id="group-id",
)
print(result)
```

## `client.card_groups.set_card_group()`

Создать новую или изменить существующую группу карт.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setCardGroup` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `name` | `str` | Да | — | Параметр публичного метода SDK. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`SetCardGroupResponse`

### Пример

```python
result = await client.card_groups.set_card_group(
    contract_id="contract-id",
    name="name",
)
print(result)
```

## `client.card_groups.set_cards_to_group()`

Добавление карт в группу.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `setCardsToGroup` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `group_id` | `str` | Да | — | Идентификатор группы топливных карт. |
| `cards_list` | `list[dict[str, Any]]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`SetCardsToGroupResponse`

### Пример

```python
result = await client.card_groups.set_cards_to_group(
    contract_id="contract-id",
    group_id="group-id",
    cards_list={},
)
print(result)
```

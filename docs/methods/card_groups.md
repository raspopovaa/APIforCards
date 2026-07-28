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

**Тип после валидации:** `CardGroupListResponse`

**Pydantic-модель:** [`CardGroupListResponse`](../data-types/card_group/CardGroupListResponse.md)

Ответ передаётся в `CardGroupListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Информация о статусе запроса (код и описание) |
| `data` | `CardGroupListData` | `object (CardGroupListData)` | Да | Нет | Основные данные ответа |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа (UNIX timestamp) |

**Вложенные модели:**
- [`CardGroupListData`](../data-types/card_group/CardGroupListData.md)

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

**Тип после валидации:** `RemoveCardGroupResponse`

**Pydantic-модель:** [`RemoveCardGroupResponse`](../data-types/card_group/RemoveCardGroupResponse.md)

Ответ передаётся в `RemoveCardGroupResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Информация о статусе запроса (код и описание) |
| `data` | `bool` | `boolean` | Да | Нет | Флаг успешного выполнения операции |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа (UNIX timestamp) |

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
| `name` | `str` | Да | — | Имя группы карт. |
| `group_id` | `str | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `SetCardGroupResponse`

**Pydantic-модель:** [`SetCardGroupResponse`](../data-types/card_group/SetCardGroupResponse.md)

Ответ передаётся в `SetCardGroupResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Информация о статусе запроса (код и описание) |
| `data` | `SetCardGroupData` | `object (SetCardGroupData)` | Да | Нет | Информация о созданной/обновлённой группе |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа (UNIX timestamp) |

**Вложенные модели:**
- [`SetCardGroupData`](../data-types/card_group/SetCardGroupData.md)

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
| `cards_list` | `list[dict[str, Any]]` | Да | — | Список карт договора, добавляемых в группу или удаляемых из неё. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `SetCardsToGroupResponse`

**Pydantic-модель:** [`SetCardsToGroupResponse`](../data-types/card_group/SetCardsToGroupResponse.md)

Ответ передаётся в `SetCardsToGroupResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Информация о статусе запроса (код и описание) |
| `data` | `bool` | `boolean` | Да | Нет | Флаг успешного выполнения операции |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка ответа (UNIX timestamp) |

### Пример

```python
result = await client.card_groups.set_cards_to_group(
    contract_id="contract-id",
    group_id="group-id",
    cards_list={},
)
print(result)
```

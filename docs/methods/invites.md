# `client.invites`

Создание, просмотр, повторная отправка, продление и удаление приглашений.

## `client.invites.create_invite()`

Создать приглашение.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `invites` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `data` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `with_send` | `bool` | Нет | `True` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `InviteResponse`

**Pydantic-модель:** [`InviteResponse`](../data-types/invites/InviteResponse.md)

Ответ передаётся в `InviteResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `data` | `InviteActionResult` | `object (InviteActionResult)` | Да | Нет | — |

**Вложенные модели:**
- [`InviteActionResult`](../data-types/invites/InviteActionResult.md)

### Пример

```python
result = await client.invites.create_invite(
    data={},
    with_send=True,
)
print(result)
```

## `client.invites.delete_invite()`

Удалить приглашение (v2).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| DELETE | v2 | `invites/{invite_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `invite_id` | `str` | Да | — | Идентификатор приглашения. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `InviteBoolResponse`

**Pydantic-модель:** [`InviteBoolResponse`](../data-types/invites/InviteBoolResponse.md)

Ответ передаётся в `InviteBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `data` | `bool` | `boolean` | Да | Нет | — |

### Пример

```python
result = await client.invites.delete_invite(
    invite_id="invite-id",
    use_post=False,
)
print(result)
```

## `client.invites.get_invites()`

Получить список приглашений (v2).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `invites` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `role` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `user_id` | `str | None` | Нет | `None` | Идентификатор пользователя. |
| `sort` | `str | None` | Нет | `None` | Выражение сортировки. Префикс «-» задает сортировку по убыванию. |
| `status` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `q` | `str | None` | Нет | `None` | Строка полнотекстового поиска. |
| `page` | `int | None` | Нет | `None` | Номер страницы результата. |
| `on_page` | `int | None` | Нет | `None` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `InviteList`

**Pydantic-модель:** [`InviteList`](../data-types/invites/InviteList.md)

Ответ передаётся в `InviteList.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `total_count` | `int` | `integer` | Да | Нет | Общее количество приглашений |
| `result` | `list[InviteItem]` | `array[object (InviteItem)]` | Да | Нет | Список приглашений |

**Вложенные модели:**
- [`InviteItem`](../data-types/invites/InviteItem.md)

### Пример

```python
result = await client.invites.get_invites(
)
print(result)
```

## `client.invites.prolong_invite()`

Продлить приглашение.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `invites/{invite_id}/prolong` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `invite_id` | `str` | Да | — | Идентификатор приглашения. |
| `with_send` | `bool` | Нет | `True` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `InviteBoolResponse`

**Pydantic-модель:** [`InviteBoolResponse`](../data-types/invites/InviteBoolResponse.md)

Ответ передаётся в `InviteBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `data` | `bool` | `boolean` | Да | Нет | — |

### Пример

```python
result = await client.invites.prolong_invite(
    invite_id="invite-id",
    with_send=True,
)
print(result)
```

## `client.invites.resend_invite()`

Повторно отправить приглашение (v2).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `invites/{invite_id}/send` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `invite_id` | `str` | Да | — | Идентификатор приглашения. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `InviteResponse`

**Pydantic-модель:** [`InviteResponse`](../data-types/invites/InviteResponse.md)

Ответ передаётся в `InviteResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `data` | `InviteActionResult` | `object (InviteActionResult)` | Да | Нет | — |

**Вложенные модели:**
- [`InviteActionResult`](../data-types/invites/InviteActionResult.md)

### Пример

```python
result = await client.invites.resend_invite(
    invite_id="invite-id",
)
print(result)
```

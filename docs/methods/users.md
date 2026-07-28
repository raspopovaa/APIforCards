# `client.users`

Управление пользователями договора и привязками пользователей к картам.

## `client.users.attach_card()`

Прикрепление карты к пользователю.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `users/{user_id}/attachCard` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `user_id` | `str` | Да | — | Идентификатор пользователя. |
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserBoolResponse`

**Pydantic-модель:** [`UserBoolResponse`](../data-types/users/UserBoolResponse.md)

Ответ передаётся в `UserBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (true/false) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени |

### Пример

```python
result = await client.users.attach_card(
    user_id="user-id",
    card_id="card-id",
)
print(result)
```

## `client.users.attach_contracts()`

Прикрепление договоров к пользователю.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `users/{user_id}/attachContracts` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `user_id` | `str` | Да | — | Идентификатор пользователя. |
| `contracts` | `list[dict[str, Any]]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserBoolResponse`

**Pydantic-модель:** [`UserBoolResponse`](../data-types/users/UserBoolResponse.md)

Ответ передаётся в `UserBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (true/false) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени |

### Пример

```python
result = await client.users.attach_contracts(
    user_id="user-id",
    contracts={},
)
print(result)
```

## `client.users.create_user()`

Создание водителя без персональных данных.
Данный метод позволяет создать себе технических водителей без ФИО (персональных данных),
чтобы использовать их для дальнейших интеграций. Реальных водителей стоит создавать через сервис “Инвайты”.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `users` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `uuid` | `str` | Да | — | Параметр публичного метода SDK. |
| `mobile` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserCreateResponse`

**Pydantic-модель:** [`UserCreateResponse`](../data-types/users/UserCreateResponse.md)

Ответ передаётся в `UserCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `str` | `string` | Да | Нет | ID созданного пользователя |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени |

### Пример

```python
result = await client.users.create_user(
    uuid="uuid",
    mobile="mobile",
)
print(result)
```

## `client.users.delete_user()`

Удаление пользователя.
Если ваша система не умеет отправлять DELETE запросы, то можно отправить POST, но в BODY указать _method=DELETE:
Пример:
await client.users.delete_user(user_id="1-FK485FK")

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| DELETE | v2 | `users/{user_id}` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `user_id` | `str` | Да | — | Идентификатор пользователя. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserBoolResponse`

**Pydantic-модель:** [`UserBoolResponse`](../data-types/users/UserBoolResponse.md)

Ответ передаётся в `UserBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (true/false) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени |

### Пример

```python
result = await client.users.delete_user(
    user_id="user-id",
    use_post=False,
)
print(result)
```

## `client.users.detach_card()`

Открепление карты от пользователя.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `users/{user_id}/detachCard` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `user_id` | `str` | Да | — | Идентификатор пользователя. |
| `card_id` | `str` | Да | — | Идентификатор топливной карты. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserBoolResponse`

**Pydantic-модель:** [`UserBoolResponse`](../data-types/users/UserBoolResponse.md)

Ответ передаётся в `UserBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (true/false) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени |

### Пример

```python
result = await client.users.detach_card(
    user_id="user-id",
    card_id="card-id",
)
print(result)
```

## `client.users.detach_contracts()`

Открепление договоров от пользователя.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `users/{user_id}/detachContracts` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `user_id` | `str` | Да | — | Идентификатор пользователя. |
| `contracts` | `list[str]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserBoolResponse`

**Pydantic-модель:** [`UserBoolResponse`](../data-types/users/UserBoolResponse.md)

Ответ передаётся в `UserBoolResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (true/false) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени |

### Пример

```python
result = await client.users.detach_contracts(
    user_id="user-id",
    contracts=["item-id"],
)
print(result)
```

## `client.users.get_users()`

Получить список пользователей.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `users` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `sort` | `str | None` | Нет | `None` | Выражение сортировки. Префикс «-» задает сортировку по убыванию. |
| `page` | `int | None` | Нет | `None` | Номер страницы результата. |
| `on_page` | `int | None` | Нет | `None` | Параметр публичного метода SDK. |
| `q` | `str | None` | Нет | `None` | Строка полнотекстового поиска. |
| `filter` | `dict[str, Any] | None` | Нет | `None` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `UserListResponse`

**Pydantic-модель:** [`UserListResponse`](../data-types/users/UserListResponse.md)

Ответ передаётся в `UserListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any]` | `object` | Да | Нет | Статус выполнения запроса (например {'code': 200}) |
| `data` | `UserList \| None` | `object (UserList) \| null` | Нет | Да | Основные данные ответа |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Временная метка ответа |

**Вложенные модели:**
- [`UserList`](../data-types/users/UserList.md)

### Пример

```python
result = await client.users.get_users(
)
print(result)
```

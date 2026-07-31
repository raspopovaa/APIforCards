# `client.auth`

Методы авторизации пользователя, завершения сессии и получения сведений об учетной записи.

## `client.auth.auth_user()`

Авторизовать пользователя, открыть сессию SDK и выбрать договор.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v1 | `authUser` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `contract_id` | `str | None` | Нет | `None` | Точный идентификатор договора, который должен стать активным. |
| `contract_number` | `str | None` | Нет | `None` | Точный номер договора, который должен стать активным. |

`contract_id` и `contract_number` нельзя передавать одновременно.

Правила выбора договора:

1. отсутствие договоров допускает сессию без `contract_id`;
2. единственный договор выбирается автоматически;
3. при нескольких договорах требуется `contract_id` или `contract_number`;
4. отсутствующее или неоднозначное совпадение вызывает `ContractSelectionError`;
5. SDK не выбирает первый договор по порядку ответа.

### Возвращаемое значение

**Тип после валидации:** `AuthUserResponse`

**Pydantic-модель:** [`AuthUserResponse`](../data-types/auth/AuthUserResponse.md)

Ответ передаётся в `AuthUserResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `StatusResponse` | `object (StatusResponse)` | Да | Нет | Статус ответа API |
| `data` | `AuthUserData` | `object (AuthUserData)` | Да | Нет | Данные авторизованного пользователя |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени (unix timestamp) |

**Вложенные модели:**
- [`StatusResponse`](../data-types/auth/StatusResponse.md)
- [`AuthUserData`](../data-types/auth/AuthUserData.md)

Возвращает типизированные данные авторизации, включая идентификатор сессии и доступные договоры. Активный договор доступен через `client.contract_id`.

### Пример

```python
result = await client.auth.auth_user(
    contract_number="TEST-001",
)
print(client.contract_id)
print(result.data.user_id)
```

Предпочтительный договор также можно установить до первого защищённого вызова:

```python
client.contract_id = "contract-id"
cards = await client.cards.get_cards_v2()
```

Lazy authentication и re-auth используют и повторно проверяют этот ID.

## `client.auth.get_info()`

Получение статистических данных по вызовам всех методов.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `info` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `period` | `str | None` | Нет | `None` | Период: месяц в формате `YYYY-MM` или конкретный день в формате `YYYY-MM-DD`. |

### Возвращаемое значение

**Тип после валидации:** `GetInfoResponse`

**Pydantic-модель:** [`GetInfoResponse`](../data-types/auth/GetInfoResponse.md)

Ответ передаётся в `GetInfoResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `StatusResponse` | `object (StatusResponse)` | Да | Нет | Статус ответа API |
| `data` | `InfoData` | `object (InfoData)` | Да | Нет | Детализированные данные о статистике |
| `timestamp` | `int` | `integer` | Да | Нет | Временная метка (UNIX timestamp) |

**Вложенные модели:**
- [`StatusResponse`](../data-types/auth/StatusResponse.md)
- [`InfoData`](../data-types/auth/InfoData.md)

### Пример

```python
result = await client.auth.get_info()
print(result)
```

## `client.auth.logoff()`

Завершить серверную сессию и очистить локальное состояние клиента.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `logoff` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `dict[str, object]`

**Pydantic-модель:** нет.

SDK возвращает значение указанного Python-типа; отдельная модель ответа не применяется.

### Пример

```python
result = await client.auth.logoff()
print(result)

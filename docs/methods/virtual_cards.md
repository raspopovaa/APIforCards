# `client.virtual_cards`

Выпуск и управление виртуальными топливными картами.

## `client.virtual_cards.create_virtual_card()`

Выпуск виртуальной карты (старый метод POST /vip/v2/cards)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `cards` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `user_id` | `str` | Да | — | Идентификатор пользователя. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `VirtualCardResponse`

**Pydantic-модель:** [`VirtualCardResponse`](../data-types/virtual_cards/VirtualCardResponse.md)

Ответ передаётся в `VirtualCardResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `StatusModel` | `object (StatusModel)` | Да | Нет | Статус ответа от сервера |
| `data` | `VirtualCardData` | `object (VirtualCardData)` | Да | Нет | Информация о выпущенной виртуальной карте |
| `timestamp` | `int` | `integer` | Да | Нет | Время ответа сервера в формате Unix Timestamp |

**Вложенные модели:**
- [`StatusModel`](../data-types/virtual_cards/StatusModel.md)
- [`VirtualCardData`](../data-types/virtual_cards/VirtualCardData.md)

### Пример

```python
result = await client.virtual_cards.create_virtual_card(
    user_id="user-id",
)
print(result)
```

## `client.virtual_cards.release_virtual_card()`

Выпуск виртуальной карты (новый метод /vip/v2/cards/release)
Можно указать:
- type (например, "wallet")
- template_id (ID шаблона ВК)
- user_id (ID пользователя)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `cards/release` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `type_` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `template_id` | `str | None` | Нет | `None` | Идентификатор шаблона. |
| `user_id` | `str | None` | Нет | `None` | Идентификатор пользователя. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `VirtualCardResponse`

**Pydantic-модель:** [`VirtualCardResponse`](../data-types/virtual_cards/VirtualCardResponse.md)

Ответ передаётся в `VirtualCardResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `StatusModel` | `object (StatusModel)` | Да | Нет | Статус ответа от сервера |
| `data` | `VirtualCardData` | `object (VirtualCardData)` | Да | Нет | Информация о выпущенной виртуальной карте |
| `timestamp` | `int` | `integer` | Да | Нет | Время ответа сервера в формате Unix Timestamp |

**Вложенные модели:**
- [`StatusModel`](../data-types/virtual_cards/StatusModel.md)
- [`VirtualCardData`](../data-types/virtual_cards/VirtualCardData.md)

### Пример

```python
result = await client.virtual_cards.release_virtual_card(
)
print(result)
```

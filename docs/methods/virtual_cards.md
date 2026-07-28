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

`VirtualCardResponse`

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

`VirtualCardResponse`

### Пример

```python
result = await client.virtual_cards.release_virtual_card(
)
print(result)
```

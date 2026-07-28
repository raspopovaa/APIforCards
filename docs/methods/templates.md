# `client.templates`

Управление шаблонами, лимитами, ограничителями и географическими ограничениями.

## `client.templates.create_template()`

Создать новый шаблон виртуальной карты.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `type_` | `str` | Да | — | Тип карты: `Limit` — лимитная схема, `Wallet` — электронный кошелёк. |
| `name` | `str` | Да | — | Имя шаблона ВК, уникальное в рамках договора. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateCreateResponse`

**Pydantic-модель:** [`TemplateCreateResponse`](../data-types/templates/TemplateCreateResponse.md)

Ответ передаётся в `TemplateCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.create_template(
    contract_id="contract-id",
    type_="type-",
    name="name",
)
print(result)
```

## `client.templates.create_template_georestriction()`

Создать геоограничитель для шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}/georestrictions` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `payload` | `dict[str, Any]` | Да | — | Параметры геоограничителя: `contract_id`, `country`, `region`, `partner`, `service_center`, `restriction_type` (`1` — разрешающий, `2` — запрещающий). |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateGeoRestrictionCreateResponse`

**Pydantic-модель:** [`TemplateGeoRestrictionCreateResponse`](../data-types/templates/TemplateGeoRestrictionCreateResponse.md)

Ответ передаётся в `TemplateGeoRestrictionCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного геоограничителя шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.create_template_georestriction(
    template_id="template-id",
    payload={},
)
print(result)
```

## `client.templates.create_template_limit()`

Создать лимит для шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}/limits` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `payload` | `dict[str, Any]` | Да | — | Параметры лимита шаблона ВК: `contract_id`, ограничение `amount` или `sum`, параметры `time`/`term`, `product_type`, `product_group`, а также `create_restriction`. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateLimitCreateResponse`

**Pydantic-модель:** [`TemplateLimitCreateResponse`](../data-types/templates/TemplateLimitCreateResponse.md)

Ответ передаётся в `TemplateLimitCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного лимита шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.create_template_limit(
    template_id="template-id",
    payload={},
)
print(result)
```

## `client.templates.create_template_restriction()`

Создать ограничитель для шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}/restrictions` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `payload` | `dict[str, Any]` | Да | — | Параметры ограничителя: `contract_id`, `product_type`, `product_group`, `restriction_type` (`1` — разрешающий, `2` — запрещающий). |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateRestrictionCreateResponse`

**Pydantic-модель:** [`TemplateRestrictionCreateResponse`](../data-types/templates/TemplateRestrictionCreateResponse.md)

Ответ передаётся в `TemplateRestrictionCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного ограничителя шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.create_template_restriction(
    template_id="template-id",
    payload={},
)
print(result)
```

## `client.templates.delete_template()`

Удалить шаблон ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| DELETE | v2 | `vc/templates/{template_id}` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

**Тип после валидации:** `TemplateDeleteResponse`

**Pydantic-модель:** [`TemplateDeleteResponse`](../data-types/templates/TemplateDeleteResponse.md)

Ответ передаётся в `TemplateDeleteResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `bool` | `boolean` | Да | Нет | Результат операции (true — успешно, false — ошибка) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.delete_template(
    template_id="template-id",
    use_post=False,
)
print(result)
```

## `client.templates.delete_template_georestriction()`

Удалить геоограничитель шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| DELETE | v2 | `vc/templates/{template_id}/georestrictions/{georestriction_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `georestriction_id` | `str` | Да | — | ID геоограничителя шаблона ВК. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

**Тип после валидации:** `TemplateGeoRestrictionDeleteResponse`

**Pydantic-модель:** [`TemplateGeoRestrictionDeleteResponse`](../data-types/templates/TemplateGeoRestrictionDeleteResponse.md)

Ответ передаётся в `TemplateGeoRestrictionDeleteResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `bool` | `boolean` | Да | Нет | Результат удаления геоограничителя (true — успешно) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.delete_template_georestriction(
    template_id="template-id",
    georestriction_id="georestriction-id",
    use_post=False,
)
print(result)
```

## `client.templates.delete_template_limit()`

Удалить лимит шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| DELETE | v2 | `vc/templates/{template_id}/limits/{limit_id}` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `limit_id` | `str` | Да | — | ID лимита шаблона ВК. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

**Тип после валидации:** `TemplateLimitDeleteResponse`

**Pydantic-модель:** [`TemplateLimitDeleteResponse`](../data-types/templates/TemplateLimitDeleteResponse.md)

Ответ передаётся в `TemplateLimitDeleteResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `bool` | `boolean` | Да | Нет | Результат удаления лимита (true — успешно) |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.delete_template_limit(
    template_id="template-id",
    limit_id="limit-id",
    use_post=False,
)
print(result)
```

## `client.templates.delete_template_restriction()`

Удалить ограничитель шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| DELETE | v2 | `vc/templates/{template_id}/restrictions/{restriction_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `restriction_id` | `str` | Да | — | ID ограничителя шаблона ВК. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

**Тип после валидации:** `TemplateRestrictionDeleteResponse`

**Pydantic-модель:** [`TemplateRestrictionDeleteResponse`](../data-types/templates/TemplateRestrictionDeleteResponse.md)

Ответ передаётся в `TemplateRestrictionDeleteResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `bool` | `boolean` | Да | Нет | Результат удаления ограничителя |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.delete_template_restriction(
    template_id="template-id",
    restriction_id="restriction-id",
    use_post=False,
)
print(result)
```

## `client.templates.get_template_georestrictions()`

Получить список геоограничителей шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `vc/templates/{template_id}/georestrictions` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateGeoRestrictionListResponse`

**Pydantic-модель:** [`TemplateGeoRestrictionListResponse`](../data-types/templates/TemplateGeoRestrictionListResponse.md)

Ответ передаётся в `TemplateGeoRestrictionListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `TemplateGeoRestrictionListData` | `object (TemplateGeoRestrictionListData)` | Да | Нет | Основные данные списка геоограничителей |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

**Вложенные модели:**
- [`TemplateGeoRestrictionListData`](../data-types/templates/TemplateGeoRestrictionListData.md)

### Пример

```python
result = await client.templates.get_template_georestrictions(
    template_id="template-id",
)
print(result)
```

## `client.templates.get_template_limits()`

Получить список лимитов шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `vc/templates/{template_id}/limits` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateLimitListResponse`

**Pydantic-модель:** [`TemplateLimitListResponse`](../data-types/templates/TemplateLimitListResponse.md)

Ответ передаётся в `TemplateLimitListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `TemplateLimitListData` | `object (TemplateLimitListData)` | Да | Нет | Основные данные списка лимитов |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

**Вложенные модели:**
- [`TemplateLimitListData`](../data-types/templates/TemplateLimitListData.md)

### Пример

```python
result = await client.templates.get_template_limits(
    template_id="template-id",
)
print(result)
```

## `client.templates.get_template_restrictions()`

Получить список ограничителей шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `vc/templates/{template_id}/restrictions` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateRestrictionListResponse`

**Pydantic-модель:** [`TemplateRestrictionListResponse`](../data-types/templates/TemplateRestrictionListResponse.md)

Ответ передаётся в `TemplateRestrictionListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `TemplateRestrictionListData` | `object (TemplateRestrictionListData)` | Да | Нет | Основные данные списка ограничителей |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

**Вложенные модели:**
- [`TemplateRestrictionListData`](../data-types/templates/TemplateRestrictionListData.md)

### Пример

```python
result = await client.templates.get_template_restrictions(
    template_id="template-id",
)
print(result)
```

## `client.templates.get_templates()`

Получить список шаблонов ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `vc/templates` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplatesListResponse`

**Pydantic-модель:** [`TemplatesListResponse`](../data-types/templates/TemplatesListResponse.md)

Ответ передаётся в `TemplatesListResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа (код, сообщение и т.д.) |
| `data` | `TemplatesListData` | `object (TemplatesListData)` | Да | Нет | Основные данные списка шаблонов |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

**Вложенные модели:**
- [`TemplatesListData`](../data-types/templates/TemplatesListData.md)

### Пример

```python
result = await client.templates.get_templates(
    contract_id="contract-id",
)
print(result)
```

## `client.templates.update_template()`

Изменить существующий шаблон ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `type_` | `str` | Да | — | Тип карты: `Limit` — лимитная схема, `Wallet` — электронный кошелёк. |
| `name` | `str` | Да | — | Имя шаблона ВК, уникальное в рамках договора. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateCreateResponse`

**Pydantic-модель:** [`TemplateCreateResponse`](../data-types/templates/TemplateCreateResponse.md)

Ответ передаётся в `TemplateCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.update_template(
    template_id="template-id",
    contract_id="contract-id",
    type_="type-",
    name="name",
)
print(result)
```

## `client.templates.update_template_georestriction()`

Изменить геоограничитель шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}/georestrictions/{georestriction_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `georestriction_id` | `str` | Да | — | ID геоограничителя шаблона ВК. |
| `payload` | `dict[str, Any]` | Да | — | Изменяемые параметры геоограничителя: `country`, `region`, `partner`, `service_center`, `restriction_type`; `contract_id` изменить нельзя. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `True` | Параметр публичного метода SDK. |

### Возвращаемое значение

**Тип после валидации:** `TemplateGeoRestrictionCreateResponse`

**Pydantic-модель:** [`TemplateGeoRestrictionCreateResponse`](../data-types/templates/TemplateGeoRestrictionCreateResponse.md)

Ответ передаётся в `TemplateGeoRestrictionCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного геоограничителя шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.update_template_georestriction(
    template_id="template-id",
    georestriction_id="georestriction-id",
    payload={},
    use_post=True,
)
print(result)
```

## `client.templates.update_template_limit()`

Обновить лимит шаблона ВК.
Новые параметры описывается в виде словаря, содержащего параметры amount, sum, time, term и т.д.
Если система не поддерживает PUT — передай `use_post=True`,
тогда запрос будет отправлен методом POST с добавленным `_method="PUT"`.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}/limits/{limit_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `limit_id` | `str` | Да | — | ID лимита шаблона ВК. |
| `limits` | `list[dict[str, Any]]` | Да | — | Параметры изменения лимита: ограничение `amount` или `sum`, `time`/`term`, `product_type`, `product_group`; `contract_id` изменить нельзя. |
| `use_post` | `bool` | Нет | `True` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `TemplateLimitCreateResponse`

**Pydantic-модель:** [`TemplateLimitCreateResponse`](../data-types/templates/TemplateLimitCreateResponse.md)

Ответ передаётся в `TemplateLimitCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного лимита шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.update_template_limit(
    template_id="template-id",
    limit_id="limit-id",
    limits={},
    use_post=True,
)
print(result)
```

## `client.templates.update_template_restriction()`

Изменить ограничитель шаблона ВК

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `vc/templates/{template_id}/restrictions/{restriction_id}` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `template_id` | `str` | Да | — | Идентификатор шаблона. |
| `restriction_id` | `str` | Да | — | ID ограничителя шаблона ВК. |
| `payload` | `dict[str, Any]` | Да | — | Изменяемые параметры ограничителя: `product_type`, `product_group`, `restriction_type`; `contract_id` изменить нельзя. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `True` | Параметр публичного метода SDK. |

### Возвращаемое значение

**Тип после валидации:** `TemplateRestrictionCreateResponse`

**Pydantic-модель:** [`TemplateRestrictionCreateResponse`](../data-types/templates/TemplateRestrictionCreateResponse.md)

Ответ передаётся в `TemplateRestrictionCreateResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `status` | `dict[str, Any] \| None` | `object \| null` | Нет | Да | Статус ответа |
| `data` | `str` | `string` | Да | Нет | ID созданного ограничителя шаблона |
| `timestamp` | `int \| None` | `integer \| null` | Нет | Да | Метка времени ответа (Unix) |

### Пример

```python
result = await client.templates.update_template_restriction(
    template_id="template-id",
    restriction_id="restriction-id",
    payload={},
    use_post=True,
)
print(result)
```

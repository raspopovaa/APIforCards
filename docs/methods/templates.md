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
| `type_` | `str` | Да | — | Параметр публичного метода SDK. |
| `name` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TemplateCreateResponse`

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
| `payload` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TemplateGeoRestrictionCreateResponse`

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
| `payload` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TemplateLimitCreateResponse`

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
| `payload` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TemplateRestrictionCreateResponse`

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

`TemplateDeleteResponse`

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
| `georestriction_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TemplateGeoRestrictionDeleteResponse`

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
| `limit_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TemplateLimitDeleteResponse`

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
| `restriction_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `False` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TemplateRestrictionDeleteResponse`

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

`TemplateGeoRestrictionListResponse`

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

`TemplateLimitListResponse`

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

`TemplateRestrictionListResponse`

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

`TemplatesListResponse`

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
| `type_` | `str` | Да | — | Параметр публичного метода SDK. |
| `name` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TemplateCreateResponse`

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
| `georestriction_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `payload` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `True` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TemplateGeoRestrictionCreateResponse`

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
| `limit_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `limits` | `list[dict[str, Any]]` | Да | — | Параметр публичного метода SDK. |
| `use_post` | `bool` | Нет | `True` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`TemplateLimitCreateResponse`

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
| `restriction_id` | `str` | Да | — | Параметр публичного метода SDK. |
| `payload` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |
| `use_post` | `bool` | Нет | `True` | Параметр публичного метода SDK. |

### Возвращаемое значение

`TemplateRestrictionCreateResponse`

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

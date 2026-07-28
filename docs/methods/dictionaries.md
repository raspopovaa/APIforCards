# `client.dictionaries`

Справочные значения, список АЗС и фильтры торговых точек.

## `client.dictionaries.get_azs_filters()`

Получить список доступных фильтров для поиска торговых точек (АЗС)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `azs/filters` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`AzsFiltersResponse`

### Пример

```python
result = await client.dictionaries.get_azs_filters(
)
print(result)
```

## `client.dictionaries.get_azs_list_v1()`

Получение списка торговых точек (АЗС, версия 1)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `AZS` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `page` | `int` | Нет | `1` | Номер страницы результата. |
| `onpage` | `int` | Нет | `10` | Количество элементов на странице. |
| `filter` | `dict[str, Any] | None` | Нет | `None` | Параметр публичного метода SDK. |
| `id` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`AzsListV1Response`

### Пример

```python
result = await client.dictionaries.get_azs_list_v1(
    page=1,
    onpage=10,
)
print(result)
```

## `client.dictionaries.get_azs_list_v2()`

Получение списка торговых точек (АЗС, версия 2)

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `azs` | Нет | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `filter` | `dict[str, Any] | None` | Нет | `None` | Параметр публичного метода SDK. |
| `q` | `str | None` | Нет | `None` | Строка полнотекстового поиска. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`AzsListV2Response`

### Пример

```python
result = await client.dictionaries.get_azs_list_v2(
)
print(result)
```

## `client.dictionaries.get_dictionary()`

Получить общий справочник по имени.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `getDictionary` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `name` | `str` | Да | — | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`DictionaryResponse`

### Пример

```python
result = await client.dictionaries.get_dictionary(
    name="name",
)
print(result)
```

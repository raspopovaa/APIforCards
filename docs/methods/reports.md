# `client.reports`

Заказ отчетов, просмотр заданий и скачивание сформированных файлов.

## `client.reports.download_report_file()`

Скачать файл сформированного отчета.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `reports/jobs/{job_id}` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `job_id` | `str` | Да | — | Идентификатор задания формирования отчета. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `bytes`

**Pydantic-модель:** нет.

SDK возвращает значение указанного Python-типа; отдельная модель ответа не применяется.

Возвращает бинарное содержимое файла отчета.

### Пример

```python
result = await client.reports.download_report_file(
    job_id="job-id",
)
print(result)
```

## `client.reports.download_report_file_v1()`

Скачать файл отчета (v1)
После того как вы узнали Job_ID своего заказанного отчета по ссылке, его содержимое нужно получить и сформировать файл.
Формирование файла вы занимаетесь на своей стороне,
выставить имя файла, формат файл, содержимое и размер, получив от нас данные в виде потока application/octet-stream.
Если заказывать отчет с параметром archive=true, то нужно выставить формат zip и данные прийдут в виде application/zip.
Внутри архива будет находится отчет в заказанном формате (pdf, xlsx, csv, xml и другие)..

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `getReportFile` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `job_id` | `str` | Да | — | Идентификатор задания формирования отчета. |
| `archive` | `bool` | Нет | `False` | Архивировать отчёт в ZIP. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `bytes`

**Pydantic-модель:** нет.

SDK возвращает значение указанного Python-типа; отдельная модель ответа не применяется.

### Пример

```python
result = await client.reports.download_report_file_v1(
    job_id="job-id",
    archive=False,
)
print(result)
```

## `client.reports.get_report_job_list_v1()`

Получить список заказанных отчетов (v1).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `getReportJobList` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `ReportV1JobList`

**Pydantic-модель:** [`ReportV1JobList`](../data-types/reports/ReportV1JobList.md)

Ответ передаётся в `ReportV1JobList.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `jobs` | `list[ReportV1JobItem]` | `array[object (ReportV1JobItem)]` | Да | Нет | Массив заказанных отчетов |

**Вложенные модели:**
- [`ReportV1JobItem`](../data-types/reports/ReportV1JobItem.md)

### Пример

```python
result = await client.reports.get_report_job_list_v1(
)
print(result)
```

## `client.reports.get_report_jobs()`

Получить список заказанных отчетов (v2).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `reports/jobs` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `ReportJobList`

**Pydantic-модель:** [`ReportJobList`](../data-types/reports/ReportJobList.md)

Ответ передаётся в `ReportJobList.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `total_count` | `int \| None` | `integer \| null` | Нет | Да | Количество найденных отчетов |
| `result` | `list[ReportJobItem]` | `array[object (ReportJobItem)]` | Да | Нет | Список заказанных отчетов |

**Вложенные модели:**
- [`ReportJobItem`](../data-types/reports/ReportJobItem.md)

### Пример

```python
result = await client.reports.get_report_jobs(
)
print(result)
```

## `client.reports.get_reports()`

Получить список доступных отчетов (v2).

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v2 | `reports` | Да | Нет |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `ReportList`

**Pydantic-модель:** [`ReportList`](../data-types/reports/ReportList.md)

Ответ передаётся в `ReportList.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `total_count` | `int` | `integer` | Да | Нет | Количество доступных отчетов |
| `result` | `list[ReportItem]` | `array[object (ReportItem)]` | Да | Нет | Массив отчетов |

**Вложенные модели:**
- [`ReportItem`](../data-types/reports/ReportItem.md)

### Пример

```python
result = await client.reports.get_reports(
)
print(result)
```

## `client.reports.order_report()`

Создать задание на формирование отчета.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| POST | v2 | `reports` | Да | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `report_id` | `str` | Да | — | Идентификатор отчета. |
| `format` | `str` | Да | — | Формат отчёта; допустимые форматы приведены в поле `formats` метода получения списка доступных отчётов. |
| `params` | `dict[str, Any]` | Да | — | Параметры отчёта; набор параметров приведён в поле `parameters` метода получения списка доступных отчётов. |
| `emails` | `str | None` | Нет | `None` | Список email-адресов получателей отчёта. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `ReportOrderResponse`

**Pydantic-модель:** [`ReportOrderResponse`](../data-types/reports/ReportOrderResponse.md)

Ответ передаётся в `ReportOrderResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `job_id` | `list[str]` | `array[string]` | Да | Нет | Идентификаторы созданных заданий на генерацию отчета |

### Пример

```python
result = await client.reports.order_report(
    report_id="report-id",
    format="format",
    params={},
)
print(result)
```

## `client.reports.order_report_v1()`

Заказ отчета (v1) – email или файл.

### Маршрут

| HTTP | API | Route | DEMO | Тарифицируется |
|---:|---:|---|:---:|:---:|
| GET | v1 | `reports` | Нет | Да |

### Параметры

| Параметр | Python-тип | Обязательный | Значение по умолчанию | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | — | Идентификатор договора. Для части методов может быть получен из активного контекста SDK. |
| `start` | `str` | Да | — | Дата начала отчётного периода. |
| `end` | `str` | Да | — | Дата окончания отчётного периода. |
| `report_format` | `str` | Да | — | Формат отчёта: `xlsx`, `xml`, `pdf` или `csv`. |
| `email` | `str | None` | Нет | `None` | Email-адреса для отправки отчёта. |
| `cards_list` | `list[str] | None` | Нет | `None` | Список 16-значных номеров карт для формирования отчёта. Если список не передан, отчёт формируется по указанной группе карт либо по всем картам договора. |
| `group_id` | `list[str] | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `archive` | `bool` | Нет | `False` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

**Тип после валидации:** `ReportV1OrderResponse`

**Pydantic-модель:** [`ReportV1OrderResponse`](../data-types/reports/ReportV1OrderResponse.md)

Ответ передаётся в `ReportV1OrderResponse.model_validate(payload)`. Pydantic проверяет обязательные поля, преобразует значения по аннотациям и рекурсивно валидирует вложенные модели.

#### Поля возвращаемой модели

| Поле | Тип после валидации | JSON-тип | Обязательное | `None` | Описание |
|---|---|---|:---:|:---:|---|
| `report_ids` | `list[str]` | `array[string]` | Да | Нет | ID заказанных отчетов |

### Пример

```python
result = await client.reports.order_report_v1(
    contract_id="contract-id",
    start="start",
    end="end",
    report_format="report-format",
    archive=False,
)
print(result)
```

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

`bytes`

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
| `archive` | `bool` | Нет | `False` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`bytes`

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

`ReportV1JobList`

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

`ReportJobList`

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

`ReportList`

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
| `format` | `str` | Да | — | Параметр публичного метода SDK. |
| `params` | `dict[str, Any]` | Да | — | Параметр публичного метода SDK. |
| `emails` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`ReportOrderResponse`

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
| `start` | `str` | Да | — | Параметр публичного метода SDK. |
| `end` | `str` | Да | — | Параметр публичного метода SDK. |
| `report_format` | `str` | Да | — | Параметр публичного метода SDK. |
| `email` | `str | None` | Нет | `None` | Параметр публичного метода SDK. |
| `cards_list` | `list[str] | None` | Нет | `None` | Параметр публичного метода SDK. |
| `group_id` | `list[str] | None` | Нет | `None` | Идентификатор группы топливных карт. |
| `archive` | `bool` | Нет | `False` | Параметр публичного метода SDK. |
| `api_version` | `str | None` | Нет | `None` | Версия API. Обычно определяется SDK автоматически. |

### Возвращаемое значение

`ReportV1OrderResponse`

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

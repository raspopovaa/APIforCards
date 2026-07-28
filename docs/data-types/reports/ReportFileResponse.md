# `ReportFileResponse`

Ответ при генерации файла отчета.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `content` | `bytes | None` | Нет | `—` | Бинарное содержимое файла (application/octet-stream) |
| `format` | `str | None` | Нет | `—` | Формат файла (pdf, xlsx, csv и т.д.) |
| `filename` | `str | None` | Нет | `—` | Имя файла отчета |
| `size` | `int | None` | Нет | `—` | Размер файла в байтах |

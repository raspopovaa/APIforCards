# `DocumentsResponse`

Ответ метода GET /v2/documents.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Объект статуса, например {'code': 200} |
| `data` | `DocumentsData` | Да | `—` | Основные данные — список документов |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (Unix timestamp) |

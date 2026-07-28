# `InvoicesResponse`

Ответ метода GET /v2/invoices.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Объект статуса, например {'code': 200} |
| `data` | `InvoicesData` | Да | `—` | Основные данные — список счетов |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (Unix timestamp) |

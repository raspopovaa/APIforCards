# `InvoiceOrderResponse`

Ответ метода POST /v2/invoice.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Объект статуса, например {'code': 200} |
| `data` | `bool` | Да | `—` | Признак успешного создания счёта |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (Unix timestamp) |

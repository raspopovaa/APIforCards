# `DocumentsOrderResponse`

Ответ метода POST /v2/documents (заказ документов).

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Объект статуса, например {'code': 200} |
| `data` | `bool` | Да | `—` | Признак успешной отправки (true — заказ выполнен) |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (Unix timestamp) |

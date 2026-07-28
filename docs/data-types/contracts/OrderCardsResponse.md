# `OrderCardsResponse`

Ответ метода POST /v2/orderCards.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Объект статуса, например {'code': 200} |
| `data` | `bool` | Да | `—` | Результат операции: true — заказ выполнен успешно |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (Unix timestamp) |

# `CardsV2Response`

Ответ API метода GET /v2/cards.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Объект статуса (например {'code': 200}) |
| `data` | `CardsV2Data` | Да | `—` | Основные данные (список карт) |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (Unix timestamp) |

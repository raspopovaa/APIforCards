# `RestrictionRemoveResponse`

Ответ на удаление ограничителя (POST /removeRestriction).

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `dict[str, Any]` | Да | `—` | Статус выполнения (например, {'code': 200}) |
| `data` | `bool` | Да | `—` | Результат операции (True — успешно) |
| `timestamp` | `int | None` | Нет | `—` | Временная метка ответа (Unix time) |

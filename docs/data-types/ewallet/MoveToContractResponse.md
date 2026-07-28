# `MoveToContractResponse`

Ответ на запрос перевода денег с кошелька на договор (moveToContract).
Пример ответа:
{
    "status": {"code": 200},
    "data": true,
    "timestamp": 1596024392
}

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `status` | `Status` | Да | `—` | Статус выполнения операции. |
| `data` | `bool` | Да | `—` | Результат выполнения операции (true — успешно). |
| `timestamp` | `int` | Да | `—` | Метка времени ответа (UNIX timestamp). |

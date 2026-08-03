# Ошибки и retry

SDK проверяет одновременно HTTP-статус и `payload.status.code`. Успешный код в
теле ответа не может скрыть HTTP-ошибку.

## Иерархия исключений API

| Код/тип | Исключение | Типичная причина |
|---|---|---|
| `400` | `ValidationError` | Некорректные параметры или payload |
| `401` | `NotAuthenticatedError` | Недействительная сессия или credentials |
| `403` | `AccessDeniedError` | Роль, API key, IP, договор или квота |
| `404` | `NotFoundError` | Объект или маршрут не найден |
| `409` | `DuplicateConflictError` | Повтор операции или конфликт |
| `429`, `509` | `RateLimitError` | Превышен лимит запросов |
| `5xx` | `ServerError` | Серверная ошибка |

Все перечисленные специализированные исключения наследуют `APIError`.

## Ошибка выбора договора

`ContractSelectionError` наследует `ValueError`, а не `APIError`: это локальная
ошибка выбора контекста сессии, а не ошибка HTTP API.

Она возникает, когда:

- одновременно переданы `contract_id` и `contract_number`;
- указанный договор не найден;
- номер договора неоднозначен;
- доступно несколько договоров, но выбор не указан.

Доступные пары `(id, number)` находятся в `exc.available_contracts`. Они не
включаются в текст исключения, поэтому обычный `str(exc)` не раскрывает список
договоров в журнале.

```python
from api_client_opti24 import ContractSelectionError

try:
    await client.auth.auth_user()
except ContractSelectionError as exc:
    for contract_id, contract_number in exc.available_contracts:
        print(contract_id, contract_number)
```

Не передавайте `available_contracts` во внешнюю telemetry без необходимости.

## Обработка ошибки API

```python
from api_client_opti24 import APIError, RateLimitError, ValidationError

try:
    cards = await client.cards.get_cards_v2(page=1, onpage=20)
except ValidationError as exc:
    print("Некорректный запрос:", exc.context.messages)
except RateLimitError as exc:
    print("Повтор возможен:", exc.context.retryable)
except APIError as exc:
    print("HTTP:", exc.context.http_status_code)
    print("API:", exc.context.api_status_code)
    print("Подсказка:", exc.context.hint)
```

!!! danger "Персональные данные"
    `APIError.context.raw_payload` может содержать договорные или персональные
    данные. Не передавайте его в общие логи и внешнюю telemetry без очистки.

## Re-auth

Для защищённой операции SDK выполняет не более одного восстановления сессии и
одного повторного запроса. `auth_user` выполняется через низкоуровневый executor
без auth-recovery, поэтому рекурсивный захват session lock исключён.

Выбранный `contract_id` сохраняется при re-auth и повторно проверяется по
актуальному списку договоров. Если доступ к договору отозван, SDK возвращает
`ContractSelectionError` и не переключается на другой договор.

## Retry policy

Автоматический retry разрешён только если одновременно выполняются условия
`EndpointSpec.retry_class` и `EndpointSpec.idempotent`.

- безопасные операции чтения могут повторяться после временной сетевой ошибки;
- операции изменения не повторяются после неопределённого сетевого результата;
- `429` и `509` повторяются только для разрешённых policy операций;
- duplicate conflict не считается основанием для автоматического retry;
- JSON и binary download используют одну и ту же execution policy.

## Практические рекомендации

1. Не добавляйте внешний retry вокруг всех вызовов без учёта idempotency.
2. Сохраняйте `method_name`, HTTP/API-коды и sanitized correlation data.
3. Не журналируйте credentials, session ID и исходный payload ошибки.
4. Для длительных сбоев используйте circuit breaker на уровне приложения.

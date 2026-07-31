# Архитектура SDK

## Request pipeline

1. Доменный метод передаёт executor имя операции, route name, версию и параметры пути.
2. `OperationExecutor.resolve()` один раз получает декларативный `EndpointSpec`,
   выбирает `RouteVariant` и безопасно формирует endpoint. Результат хранится во
   внутреннем immutable-объекте `_ResolvedOperation`.
3. `DefaultRequestExecutor` использует тот же resolved-объект для session policy,
   request audit, первой попытки и повторной попытки после re-auth. Повторного
   обращения к registry и повторного render path-параметров нет.
4. `OperationExecutor` формирует headers и передаёт timeout, `retry_class` и
   `idempotent` в transport.
5. `AsyncTransport` применяет единый retry/rate-limit pipeline как для JSON, так и
   для бинарных ответов. Различается только выполнение одной HTTP-попытки и
   декодирование результата.
6. `ResponseDecoder` требует успешные HTTP-код и `payload.status.code`.
7. Executor проверяет, что JSON-ответ является объектом, а доменный сервис
   преобразует его в типизированную модель.

## Однократное разрешение операции

Registry остаётся единственным источником HTTP-контракта. Внешний executor больше
не получает registry напрямую: он использует результат, подготовленный
`OperationExecutor.resolve()`. Это гарантирует, что audit, session recovery и
фактический HTTP-запрос относятся к одному и тому же route.

Низкоуровневые вызовы, в частности `auth_user`, сохраняют метод
`OperationExecutor.execute()`. Он является короткой обёрткой над `resolve()` и
`execute_resolved()` и не запускает автоматический re-auth.

## Декларативные endpoints

Все маршруты находятся в `endpoints.py`. Registry не использует AST, `inspect`,
динамический импорт сервисов или соглашения об именовании методов. `MethodSpec`
сохранён как alias `EndpointSpec` для обратной совместимости.

Сервисы не содержат HTTP-методов и endpoint-строк: operation-centric executor
является единственной точкой разрешения маршрута. Внешний код и признак
тарификации объявляются непосредственно в соответствующем вызове `endpoint()`
или `route()`.

Значения path-параметров кодируются, а разделители пути, query/fragment symbols и
dot-segments запрещены.

## Dependency injection и composition root

`APIClient` принимает `transport`, `session_manager`, `registry`, `logger`,
`clock`, `credentials_provider` и `api_key_provider`. Внутренний
`_resolve_inputs()` сводит legacy-параметры, settings и providers к трём готовым
объектам:

- `ConnectionSettings`;
- `CredentialsProvider`;
- `APIKeyProvider`.

Промежуточный объект не хранит строки API key, логина или пароля. После
разрешения входов конструктор создаёт только принадлежащие клиенту ресурсы и
передаёт их в `compose_client_runtime()`.

Функция `compose_client_runtime()` статически собирает authenticator, coordinator,
оба executor и сервисы; двухфазной настройки через `bind()` и DI-фреймворка нет.

Публичный `client.settings` имеет тип `ConnectionSettings` и не содержит API key,
логин или пароль. Секреты находятся в отдельных `APIKeyProvider` и
`CredentialsProvider`. `OperationExecutor` запрашивает API key непосредственно
перед каждым запросом, поэтому ротация в secret manager не требует пересоздания
клиента. `DefaultAuthenticator` — единственный компонент, который получает логин
и пароль.

Сервисы зависят только от узких протоколов `RequestExecutor`, read-only
`SessionContext`, `SessionGate` и logger. Они не могут изменять состояние сессии.
Только `DefaultAuthenticator` получает `SessionMutator` и
`CredentialsProvider`.

## Авторизация и выбор договора

`SessionManager` сериализует первоначальную авторизацию через `asyncio.Lock`,
чтобы конкурентные защищённые запросы не создавали auth stampede.

Выбор договора выполняется по строгим правилам:

1. одновременно передавать `contract_id` и `contract_number` нельзя;
2. явно переданный ID или номер должен иметь ровно одно совпадение;
3. отсутствие договоров допускает сессию без `contract_id`;
4. единственный договор выбирается автоматически;
5. несколько договоров требуют явного выбора и приводят к
   `ContractSelectionError`.

Исключение хранит доступные пары `(id, number)` в структурированном поле
`available_contracts`, но не добавляет их в текст сообщения. Поэтому обычное
логирование исключения не раскрывает список договоров.

Предварительно выбранный `client.contract_id` передаётся в lazy authentication.
При re-auth coordinator сохраняет ID выбранного договора, повторно проверяет его
по актуальному ответу `authUser` и не переключается на другой договор молча.

Auth-операция выполняется через низкоуровневый `OperationExecutor` и помечена в
registry как не требующая сессии, поэтому её `401` возвращается вызывающему коду
без рекурсивного re-auth.

## Transport и единая execution policy

`AsyncTransport` отдельно принимает HTTP client, response decoder, политики,
logger и clock. Transport не знает об `APIClient`, session manager или re-auth.

JSON и binary download используют общий private policy runner. Он отвечает за:

- client-side rate limit;
- минимальный интервал повторной авторизации;
- network retry;
- exponential backoff;
- retry ответов `429` и `509`;
- учёт `retry_class` и idempotency.

Конкретная HTTP-попытка остаётся разной: JSON использует `client.request()`, а
binary download открывает `client.stream()`, полностью читает ответ и закрывает
контекст до следующей попытки. Частичные результаты разных попыток не
объединяются.

Unsafe операции не получают автоматический retry. Повтор разрешается только
когда endpoint metadata допускает retry и операция является идемпотентной.
Потоковый endpoint обязан быть относительным, поэтому API key и session ID не
могут быть отправлены на другой origin.

## Наблюдаемость

Каждый экземпляр клиента создаёт собственный logger и владеет только своими
handlers. Закрытие одного клиента не влияет на остальные. Если инициализация
клиента завершается ошибкой после создания managed logger, SDK закрывает уже
созданные handlers.

Основной файл лога и `request_log_file` открываются в append-режиме. Request-аудит
записывается в JSONL и содержит только имя операции, версию, route name,
HTTP-метод и результат; URL, path-параметры и payload в него не попадают.
Внедрённый пользователем logger не закрывается SDK.

## Композиционные сервисы

Все доменные вызовы выполняются через композиционные сервисы:

```python
auth = await client.auth.auth_user(contract_number="TEST-001")
cards = await client.cards.get_cards_v2()
jobs = await client.reports.get_report_jobs()
users = await client.users.get_users()
```

Каждый доменный метод объявлен непосредственно в конкретном сервисе. В SDK нет
доменных mixin-классов и прямых методов вида `client.get_cards_v2()`.
`AuthService` создаётся отдельно в composition root и делегирует работу с
credentials изолированному authenticator. `ServiceContainer` собирает остальные
сервисы в одном типизированном composition root, а внутренний `_ServiceFacade`
предоставляет явные свойства без динамического `__getattr__`.

Доступные пространства имён: `auth`, `card_groups`, `cards`, `contracts`,
`dictionaries`, `ewallet`, `final_prices`, `invites`, `limits`, `region_limits`,
`reports`, `restrictions`, `templates`, `transactions`, `users` и
`virtual_cards`.

## Модели данных

SDK использует Pydantic v2. Совместимый `BaseModel` сохраняет
`model_validate()`, `model_dump()`, `Field`, validators, `describe()` и адаптер
`decode_model()`.

Response-модели сохраняют дополнительные серверные поля для forward
compatibility, а `StrictRequestModel` запрещает неизвестные поля во всех request
DTO.

## Контракт endpoints

`tests/contracts/endpoints.json` является версионируемым snapshot-контрактом для
всех операций. Contract-тест сравнивает с ним имя и домен операции, версии,
маршруты, demo-доступность, idempotency, session policy, timeout и retry class.

Snapshot дополняется независимым текстовым контрактом
`specifications/api-methods.yaml`. Скрипт `scripts/verify_external_contract.py`
выполняет строгое сопоставление `external_code → EndpointSpec/RouteVariant` и
проверяет operation, route name, HTTP-метод, версию, путь, DEMO-доступность и
тарификацию.

## Архитектурные инварианты

После изменений остаются обязательными следующие правила:

- сервис передаёт только имя операции и бизнес-параметры;
- registry является единственным источником маршрута;
- операция разрешается один раз на бизнес-вызов;
- audit и повтор после re-auth используют тот же resolved route;
- JSON и binary download используют одну retry/rate-limit policy;
- unsafe операции не повторяются автоматически;
- network locks не удерживаются во время HTTP-вызова;
- API key получается из provider перед каждым запросом;
- логин и пароль доступны только authenticator;
- `client.settings` не содержит секретов;
- при re-auth договор не меняется незаметно.

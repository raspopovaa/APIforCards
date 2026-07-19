# Архитектура SDK

## Request pipeline

1. Доменный метод явно передаёт executor имя операции и параметры пути.
2. `DefaultRequestExecutor` получает декларативный `EndpointSpec` из registry,
   выбирает route variant и безопасно кодирует path-параметры.
3. Executor обеспечивает сессию, передаёт timeout, `retry_class` и `idempotent`
   в transport и выполняет не более одного re-auth для защищённой операции.
4. Transport независимо применяет rate limit и сетевой retry.
5. `ResponseDecoder` требует успешные HTTP-код и `payload.status.code`.
6. Executor проверяет, что JSON-ответ является объектом, а доменный сервис
   преобразует его в типизированную модель.

## Декларативные endpoints

Все маршруты находятся в `endpoints.py`. Registry не использует AST,
`inspect`, динамический импорт сервисов или соглашения об именовании методов.
`MethodSpec` сохранён как alias `EndpointSpec` для обратной совместимости.
Сервисы не содержат HTTP-методов и endpoint-строк: operation-centric executor
является единственной точкой разрешения маршрута.

## Dependency injection

`APIClient` принимает `transport`, `session_manager`, `registry`, `logger` и
`clock`. `AsyncTransport` отдельно принимает HTTP client, response decoder,
политики, logger и clock. Transport не знает об `APIClient`, session manager или
re-auth.

Публичный `client.settings` имеет тип `ConnectionSettings` и не содержит API key,
логин или пароль. Секреты находятся в отдельных `APIKeyProvider` и
`CredentialsProvider`; единый `StaticCredentialsProvider` реализует оба узких
контракта, но executor получает только значение API key, а `AuthService` — только
логин и пароль. Legacy `APISettings` преобразуется в безопасные настройки в
composition root и не сохраняется клиентом.

Сервисы зависят только от узких протоколов `RequestExecutor`, read-only
`SessionContext`, `SessionGate` и logger. Они не могут изменять состояние сессии.
`SessionGate` также используется асинхронным resolver договора, если вызывающий
код не передал `contract_id` явно.
Только `AuthService` дополнительно получает `SessionMutator`, `CredentialsProvider`
и `Clock`. Ни один доменный сервис не хранит ссылку на `APIClient`, его настройки
или transport.

`AuthenticationCoordinator` связывает `AuthService` с `SessionManager` и реализует
`SessionGate` и `SessionRecovery`. Auth-операция помечена в registry как не
требующая сессии, поэтому её `401` возвращается вызывающему коду без рекурсивного
re-auth. Пароль не передаётся остальным сервисам.

Потоковые и JSON-запросы используют только маршруты registry и настроенный
`base_url`. Значения path-параметров кодируются, а разделители пути и dot-segments
запрещены. API key и session ID не могут быть отправлены на другой origin.

## Наблюдаемость

Каждый экземпляр клиента создаёт собственный logger и владеет только своими
handlers. Закрытие одного клиента не влияет на остальные. Основной файл лога и
`request_log_file` открываются в append-режиме. Request-аудит записывается в
JSONL и содержит только имя операции, версию, route name, HTTP-метод и результат;
URL, path-параметры и payload в него не попадают. Внедрённый пользователем logger
не закрывается SDK.

## Композиционные сервисы

Все доменные вызовы выполняются через композиционные сервисы:

```python
auth = await client.auth.auth_user()
cards = await client.cards.get_cards_v2()
jobs = await client.reports.get_report_jobs()
users = await client.users.get_users()
```

Каждый доменный метод объявлен непосредственно в конкретном сервисе. В SDK нет
доменных mixin-классов и прямых методов вида `client.get_cards_v2()`.
`AuthService` создаётся отдельно в composition root и является единственным сервисом,
получающим `CredentialsProvider`. `ServiceContainer` не зависит от учётных данных и
собирает остальные сервисы в одном типизированном composition root,
а внутренний `_ServiceFacade` предоставляет явные свойства без динамического
`__getattr__`.

Доступные пространства имён: `auth`, `card_groups`, `cards`, `contracts`,
`dictionaries`, `ewallet`, `final_prices`, `invites`, `limits`, `region_limits`,
`reports`, `restrictions`, `templates`, `transactions`, `users` и
`virtual_cards`.

## Модели данных

Локальный modeling framework заменён Pydantic v2. Совместимый `BaseModel`
сохраняет `model_validate()`, `model_dump()`, `Field`, validators, `describe()` и
адаптер `decode_model()`, поэтому сервисный API не изменился. Pydantic проверяет
типы элементов `dict`, длину fixed tuple и вложенные структуры. Response-модели
сохраняют дополнительные серверные поля для forward compatibility, а
`StrictRequestModel` запрещает неизвестные поля во всех request DTO.

## Контракт endpoints

`tests/contracts/endpoints.json` является версионируемым snapshot-контрактом для
всех 89 операций. Contract-тест сравнивает с ним имя и домен операции, версии,
маршруты, demo-доступность, idempotency, session policy, timeout и retry class.
Изменение registry поэтому требует явного изменения контракта, а не проходит
незаметно вместе с реализацией.

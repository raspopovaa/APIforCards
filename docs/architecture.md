# Архитектура SDK

## Request pipeline

1. Доменный метод устанавливает имя операции через `@api_method`.
2. `DefaultRequestExecutor` получает декларативный `EndpointSpec` из registry.
3. Executor передаёт timeout, `retry_class` и `idempotent` в transport.
4. Transport применяет rate limit, retry и при необходимости единственный re-auth.
5. `ResponseDecoder` одинаково проверяет HTTP-код и `payload.status.code`.
6. Executor проверяет, что JSON-ответ является объектом, а доменный сервис
   преобразует его в типизированную модель.

## Декларативные endpoints

Все маршруты находятся в `endpoints.py`. Registry не использует AST,
`inspect`, динамический импорт сервисов или соглашения об именовании методов.
`MethodSpec` сохранён как alias `EndpointSpec` для обратной совместимости.

## Dependency injection

`APIClient` принимает `transport`, `session_manager`, `registry`, `logger` и
`clock`. `AsyncTransport` отдельно принимает HTTP client, response decoder,
политики, logger и clock. Transport не знает об `APIClient`; re-auth подключается
через callback.

Сервисы зависят только от узких протоколов `RequestExecutor`, read-only
`SessionContext`, `SessionGate` и logger. Они не могут изменять состояние сессии.
Только `AuthService` дополнительно получает `SessionMutator`, `CredentialsProvider`
и `Clock`. Ни один доменный сервис не хранит ссылку на `APIClient`, его настройки
или transport.

`AuthenticationCoordinator` связывает `AuthService` с `SessionManager` и
transport re-auth callback, а также реализует `SessionGate`. Пароль не
передаётся остальным сервисам.

Потоковые и JSON-запросы используют одинаковые относительные endpoint и
настроенный `base_url`. Абсолютные stream URL запрещены, поэтому API key и
session ID не могут быть отправлены на другой origin.

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

## Миграция моделей

Существующий `BaseModel` поддерживает `model_validate()` и `model_dump()`.
`@dataclass_transform` сохраняет сигнатуры полей для статических анализаторов.
Функция `decode_model()` отделяет сервисы от конкретного modeling framework и
уже используется частью доменов. Следующие модели следует переносить по одной,
после чего внутренний framework можно заменить стандартными dataclass либо
внешним валидатором без изменения сервисного API.

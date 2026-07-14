# Архитектура SDK

## Request pipeline

1. Доменный метод устанавливает имя операции через `@api_method`.
2. `APIClient` получает декларативный `EndpointSpec` из registry.
3. Timeout, `retry_class` и `idempotent` передаются в `AsyncTransport`.
4. Transport применяет rate limit, retry и при необходимости единственный re-auth.
5. `ResponseDecoder` одинаково проверяет HTTP-код и `payload.status.code`.
6. Доменный сервис преобразует payload через `decode_model`.

## Декларативные endpoints

Все маршруты находятся в `endpoints.py`. Registry не использует AST,
`inspect`, динамический импорт сервисов или соглашения об именовании методов.
`MethodSpec` сохранён как alias `EndpointSpec` для обратной совместимости.

## Dependency injection

`APIClient` принимает `transport`, `session_manager`, `registry`, `logger` и
`clock`. `AsyncTransport` отдельно принимает HTTP client, response decoder,
политики, logger и clock. Transport не знает об `APIClient`; re-auth подключается
через callback.

## Композиционные сервисы

Новый код рекомендуется писать через:

```python
cards = await client.cards.get_cards_v2()
jobs = await client.reports.get_report_jobs()
```

Прямые методы `client.get_cards_v2()` и `client.get_report_jobs()` пока
сохранены для обратной совместимости. Остальные домены могут переноситься на
композицию тем же способом.

## Миграция моделей

Существующий `BaseModel` поддерживает `model_validate()` и `model_dump()`.
Функция `decode_model()` отделяет сервисы от конкретного modeling framework и
уже используется доменами cards/reports. Следующие домены следует переносить
по одному, после чего внутренний framework можно заменить стандартными
dataclass либо внешним валидатором без изменения сервисного API.

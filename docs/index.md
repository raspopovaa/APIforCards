# API Client SDK

Асинхронная Python-библиотека для авторизации, управления картами, договорами,
транзакциями, отчётами, пользователями и виртуальными картами.

!!! info "Текущая версия"
    Документация соответствует `api-client-opti24 3.0.0` и Python
    `>=3.11,<3.15`.

## Начните отсюда

| Раздел | Для чего нужен |
|---|---|
| [Установка и быстрый запуск](getting-started.md) | Установить пакет и выполнить первый запрос |
| [Конфигурация](configuration.md) | Настроить URL, credentials, timeout, retry и rate limit |
| [Миграция на 3.0](migration-3.0.md) | Перейти с линии 2.x на явный lifecycle и строгие модели |
| [Типовые сценарии](scenarios.md) | Собрать вызовы SDK в безопасные прикладные последовательности |
| [Методы API](methods.md) | Найти вызов SDK, маршрут, DEMO-доступность и тарификацию |
| [Ошибки и retry](errors.md) | Обработать HTTP/API-ошибки и безопасные повторы |
| [API Reference](api-reference.md) | Посмотреть сигнатуры сервисов и модели данных |

## Основной стиль использования

SDK предоставляет типизированные композиционные сервисы:

```python
auth = await client.auth.auth_user()
cards = await client.cards.get_cards_v2(page=1, onpage=20)
reports = await client.reports.get_reports()
transactions = await client.transactions.get_transactions_v2(
    contract_id="contract-id",
    date_from="2026-07-01",
    date_to="2026-07-31",
)
```

Прямых методов вида `client.get_cards_v2()` нет. Каждый метод находится в
своём доменном пространстве: `client.cards`, `client.reports`, `client.users` и
других.

## Гарантии SDK

- единый декларативный registry маршрутов;
- проверка HTTP-кода и API-кода ответа;
- re-auth без рекурсивного захвата session lock;
- общий deadline и лимит попыток для одной бизнес-операции;
- retry только в соответствии с idempotency policy;
- percent-encoding параметров пути и запрет небезопасных сегментов;
- изоляция credentials от доменных сервисов;
- типизированные response/request модели на Pydantic v2;
- автоматическая сверка 91 внешнего метода с независимым YAML-контрактом.

## Дополнительные материалы

- [Архитектура SDK](architecture.md)
- [Информационная безопасность](security.md)
- [Совместимость со спецификацией](spec-compatibility.md)
- [Версионирование документации](versioning.md)
- [Исходный код на GitHub](https://github.com/raspopovaa/APIforCards)
- [Пакет 3.0.0 на TestPyPI](https://test.pypi.org/project/api-client-opti24/3.0.0/)

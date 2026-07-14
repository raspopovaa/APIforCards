# ⛽ APIClient

APIClient SDK — асинхронная Python-библиотека для работы с корпоративным API топливных карт.

Проект упрощает интеграцию с API и предоставляет:

- единый `APIClient`
- доменные сервисы для карт, транзакций, пользователей, шаблонов, лимитов и отчетов
- типизированные модели ответов
- безопасные retry, re-auth и ограничение частоты на транспортном уровне
- demo-сценарий для DEMO-стенда

Проект является независимой разработкой. Использование API должно соответствовать официальным правилам и ограничениям провайдера.

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Возможности

| Группа | Что есть в SDK | Описание |
|--------|----------------|----------|
| 🔐 Аутентификация | `auth_user`, `logoff`, сессии | Авторизация, выбор договора, re-auth |
| 💳 Карты | `cards v1/v2`, водители, детали карты | Работа с топливными картами |
| 💰 Транзакции | список и детализация `v2` | История операций по договору и карте |
| 👥 Пользователи | список, создание, привязка | Управление пользователями |
| 📊 Отчеты | список отчетов и jobs | Работа с отчетными методами |
| 🚦 Лимиты и ограничения | лимиты, restrictions, region limits | Ограничения по продуктам и географии |
| 🧾 Шаблоны и ВК | templates, virtual cards, MPC QR | Работа с шаблонами виртуальных карт и операциями МПК/QR |
| 📚 Справочники | dictionaries, AZS, related data | Поддержка общих справочников |

## 🏗️ Архитектура

Основные слои проекта:

- [client.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/client.py)  
  Главная точка входа. Собирает зависимости и предоставляет композиционные сервисы `client.cards` и `client.reports`.

- [transport.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/transport.py)  
  Независимый HTTP-слой с внедряемыми client, decoder, logger, clock и policy.

- [endpoints.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/endpoints.py)
  Декларативный каталог `EndpointSpec` для всех маршрутов без AST и runtime-import сервисов.

- [response.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/response.py)
  Единое декодирование JSON, бинарных ответов и API-ошибок.

- [session.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/session.py)  
  Управляет `session_id` и активным `contract_id`.

- [registry.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/registry.py)  
  Хранит метаданные методов и timeout policy.

- [modeling.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/modeling.py)  
  Совместимый stdlib-only слой моделей и адаптер `decode_model` для постепенной миграции.

## 📦 Установка

Установка из TestPyPI:

```bash
python3 -m venv .venv
.venv/bin/pip install -i https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  api-client-opti24
```

Проверка импорта:

```bash
.venv/bin/python -c "from api_client_opti24 import APIClient; print(APIClient.__name__)"
```

Локальная установка для разработки:

```bash
cd path/to/api-pro-sdk
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

## ⚡ Быстрый старт

Перед запуском настройте `.env` или переменные окружения `API_BASE_URL`, `API_KEY`, `API_LOGIN`, `API_PASSWORD`.

Проверка, что клиент создается корректно:

```python
import asyncio

from api_client_opti24 import APIClient


async def smoke_check() -> None:
    async with APIClient(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
    ) as client:
        print(type(client).__name__)


asyncio.run(smoke_check())
```

Полный пример с авторизацией и запросами:

```python
import asyncio
from pathlib import Path

from api_client_opti24 import APIClient, APISettings


async def main() -> None:
    settings = APISettings.from_env(env_file=Path(__file__).with_name(".env"))

    async with APIClient(settings=settings) as client:
        auth_response = await client.auth_user()
        print("=== АВТОРИЗАЦИЯ ===")
        print(auth_response.data.contracts[0])

        info_response = await client.get_info()
        print("=== СТАТИСТИКА ===")
        print(info_response.data.client_info)

        cards_response = await client.cards.get_cards_v2()
        print("=== КАРТЫ V2 ===")
        print(cards_response.total_count)

        await client.logoff()


if __name__ == "__main__":
    asyncio.run(main())
```

Этот пример требует реального доступа к API. Создайте файл `.env` рядом со
скриптом: пример загружает его по пути `Path(__file__).with_name(".env")` и
поэтому не зависит от рабочей директории IDE.

## 📖 Конфигурация

SDK читает настройки из `.env` через встроенный загрузчик:

- [env.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/env.py)
- [config.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/config.py)

Шаблон файла:
- [`.env.example`](https://github.com/raspopovaa/APIforCards/blob/main/.env.example)

Пример:

```env
API_BASE_URL=https://api-demo.opti-24.ru/vip/
API_KEY=your_api_key_here
API_LOGIN=your_login
API_PASSWORD=your_password
API_REQUESTS_PER_SECOND=2
REQUEST_LOG_FILE=./api_requests.jsonl
LOGGER_FILE=./api.log
LOG_LEVEL=INFO
```

`API_BASE_URL` должен быть полным абсолютным адресом и начинаться с `https://`
(либо с `http://` для локального тестового сервера). Пустой адрес и значение без
протокола отклоняются при создании клиента с понятной ошибкой.

`API_REQUESTS_PER_SECOND` включает упреждающее ограничение частоты. По
предоставленной спецификации для DEMO рекомендуется `2`, для production — `5`.
Если переменная не задана, SDK не вводит клиентский лимит и полагается на сервер.

Удалённые адреса принимаются только по HTTPS. HTTP разрешён для loopback; для
изолированных тестовых стендов его можно явно включить через
`API_ALLOW_INSECURE_HTTP=true`.

## 🎯 Что важно в реализации

- **♻️ Policy-driven retry** для безопасных запросов и авторизации
- **🔐 Re-auth** при потере сессии
- **📚 Типизированные модели** на `dataclasses`
- **🧾 Описание полей** через `Field(..., description=...)`
- **🧪 Покрытие тестами** для моделей, transport, session и registry
- **⚖️ Policy “спека vs реальность”** в спорных местах
- **🗂️ Полный registry** с demo-флагами и alias-маршрутами для веток API
- **🚨 Устойчивый error handling** по HTTP-коду и `payload.status.code`

### Безопасность повторов

- `GET`, `HEAD` и `OPTIONS` повторяются после временных сетевых ошибок и `429/509`.
- Запросы изменения данных не повторяются после сетевой ошибки: результат операции
  мог сохраниться на сервере, поэтому автоматический retry создаёт риск дубля.
- Авторизация имеет отдельный интервал не менее 5 секунд между попытками.
- Политики можно заменить через `APISettings.retry_policy` и
  `APISettings.rate_limit_policy`, а transport — внедрить в `APIClient` для тестов.
- Решение о повторе учитывает одновременно `EndpointSpec.retry_class` и
  `EndpointSpec.idempotent`.

### Информационная безопасность

- SDK не пишет request/response payload, URL с идентификаторами и текст исключения в лог.
- Ключи, сессии, пароли, телефоны, email и идентификаторы очищаются logger-фильтром.
- Внешний logger получает тот же фильтр автоматически через dependency injection.
- Raw payload ошибки доступен в `APIError.context` и должен обрабатываться как
  чувствительная информация; его не следует отправлять в общие журналы.
- Секреты следует передавать через окружение или secret manager и никогда не
  сохранять в репозитории.

### POST-fallback для PUT и DELETE

Спецификация допускает вызов части операций через `POST` с полем `_method`.
Методы удаления пользователей, приглашений и элементов шаблонов принимают
`use_post=True`; методы обновления шаблонов используют этот режим по умолчанию.
SDK создаёт копию payload и не изменяет переданный вызывающим кодом объект.

## 🚨 Ошибки API

SDK теперь обрабатывает ошибки в двух слоях:

- HTTP-статус ответа
- внутренний `status.code` из payload API

Это важно для случаев, когда API возвращает `HTTP 200`, но внутри тела ответа приходит бизнес-ошибка, например `401 notAuthenticated`.

Из коробки отдельно маппятся:

- `400` → ошибки валидации
- `401` → ошибка авторизации
- `403` → ошибка доступа
- `404` → ресурс не найден
- `409` → конфликт / дублирование запроса
- `429` и `509` → rate limit
- `5xx` → серверные ошибки

У исключений сохраняются:

- HTTP-код
- API-код из payload
- список сообщений
- hint по устранению
- признак `retryable`

## 🧭 Registry и DEMO

`registry` теперь хранит не только основной маршрут метода, но и:

- demo-доступность метода на основании сводной API-таблицы
- alias-маршруты для альтернативных веток (`invites_free`, `prolong_free`)
- alias-маршруты для `PUT`-вариантов обновления шаблонов ВК

Это особенно важно для методов, где один Python-метод поддерживает несколько HTTP-маршрутов.

## 🧠 Модели и описание данных

Вместо `pydantic` используется собственный слой моделей на стандартной библиотеке:

- `BaseModel`
- `Field`
- `field_validator`
- nested parsing
- `describe()`

Пример интроспекции:

```python
from api_client_opti24.models.auth import AuthUserResponse

print(AuthUserResponse.describe())
```

Это показывает:

- поле
- тип
- обязательность
- описание

## 📚 Автоматическая документация

В проект добавлена автоматическая генерация API-документации:

- генератор: [scripts/generate_api_docs.py](https://github.com/raspopovaa/APIforCards/blob/main/scripts/generate_api_docs.py)
- индекс документации: [docs/index.md](https://github.com/raspopovaa/APIforCards/blob/main/docs/index.md)
- сгенерированный reference: [docs/api-reference.md](https://github.com/raspopovaa/APIforCards/blob/main/docs/api-reference.md)
- совместимость со спецификацией: [docs/spec-compatibility.md](https://github.com/raspopovaa/APIforCards/blob/main/docs/spec-compatibility.md)
- архитектура: [docs/architecture.md](https://github.com/raspopovaa/APIforCards/blob/main/docs/architecture.md)
- информационная безопасность: [docs/security.md](https://github.com/raspopovaa/APIforCards/blob/main/docs/security.md)

Что генерируется автоматически:

- публичные модули SDK
- публичные классы и функции
- сигнатуры
- docstring'и
- описание полей моделей через `describe()`

Локальный запуск:

```bash
.venv/bin/python scripts/generate_api_docs.py
```

В GitHub Actions есть отдельный workflow `Docs`, который:

- запускает генерацию на `push` и `pull_request`
- собирает актуальные `docs/`
- прикладывает их как artifact

Для публикации документации как сайта добавлен отдельный workflow GitHub Pages:

- [pages.yml](https://github.com/raspopovaa/APIforCards/blob/main/.github/workflows/pages.yml)

Он:

- генерирует `docs/api-reference.md`
- собирает статический HTML-сайт
- публикует его через GitHub Pages

HTML-сборка выполняется скриптом:

- [build_docs_site.py](https://github.com/raspopovaa/APIforCards/blob/main/scripts/build_docs_site.py)

## 📌 Политика по спецификации

Спецификация API и реальные ответы DEMO-стенда местами расходятся. В проекте приняты такие правила:

- если табличная спецификация противоречит примеру ответа и реальному payload, приоритет у примера и стенда
- если обязательное по спецификации поле реально иногда отсутствует, модель может быть ослаблена до optional
- если поле стабильно и в таблице, и в примере, модель делается строгой

Примеры:

- `contracts.managerData` оставлен optional из-за реального ответа стенда
- спорные числовые поля в `transactions v2` описаны по живым payload'ам
- `cards v2.contract_name` сделан обязательным

## 🧪 Тестирование

```bash
.venv/bin/pytest
```

Сейчас тесты покрывают:

- auth
- cards
- contracts
- users
- errors
- registry
- session manager
- transport
- modeling layer

## 🚀 Публикация пакета

Подготовка релиза:

```bash
cd path/to/api-pro-sdk
rm -rf dist/ build/ *.egg-info
uv build
```

Проверка артефактов:

```bash
python -m zipfile -l dist/*.whl
python -m tarfile -l dist/*.tar.gz
```

Публикация в TestPyPI:

```bash
export UV_PUBLISH_TOKEN="<testpypi-token>"
uv publish --publish-url https://test.pypi.org/legacy/
```

После этого пакет будет доступен на странице проекта в TestPyPI, а установить его можно так:

```bash
pip install -i https://test.pypi.org/simple/ api-client-opti24
```

## 🤖 GitHub Actions

В репозитории настроен базовый CI workflow:

- [ci.yml](https://github.com/raspopovaa/APIforCards/blob/main/.github/workflows/ci.yml)

Он запускается:

- на `push` в `main`
- на `pull_request`

Текущий pipeline:

- поднимает `Python 3.14`
- устанавливает зависимости через `pip install -e ".[dev]"`
- запускает `pytest`

Почему пока только тесты:

- `pytest` уже стабильно зеленый
- `ruff` и `mypy` пока требуют отдельной доработки проекта перед тем, как делать их блокирующими проверками
- такой стартовый CI лучше, чем постоянно красный workflow без практической пользы

## ▶️ Demo-скрипт

Файл:
- [examples/demo_async.py](https://github.com/raspopovaa/APIforCards/blob/main/examples/demo_async.py)

Запуск:

```bash
.venv/bin/python examples/demo_async.py
```

Если DEMO-стенд начинает ограничивать запросы:

```bash
DEMO_MIN_REQUEST_INTERVAL=0.35 .venv/bin/python examples/demo_async.py
```

## 📲 MPC и QR

SDK теперь покрывает дополнительные операции по мобильному профилю карты:

- `get_mpc_qr_list`
- `generate_payment_qr`
- `init_mpc`
- `confirm_mpc`
- `update_mpc`
- `delete_mpc`
- `reset_mpc`

## 📁 Структура проекта

```text
api-pro-sdk/
├── examples/
├── src/api_client_opti24/
│   ├── models/
│   ├── services/
│   ├── client.py
│   ├── config.py
│   ├── env.py
│   ├── errors.py
│   ├── modeling.py
│   ├── registry.py
│   ├── session.py
│   └── transport.py
├── tests/
├── pyproject.toml
└── README.md
```

## 🛠️ Разработка

```bash
.venv/bin/pytest
.venv/bin/ruff check .
.venv/bin/black .
.venv/bin/mypy src
```

Примечание:

- локально доступны `ruff`, `black` и `mypy`, но в GitHub Actions они пока не включены как обязательные проверки

## ⚠️ Ограничения

- SDK рассчитан на Python `3.14`
- transport использует `httpx`
- точность моделей зависит от качества внешней спецификации
- DEMO-стенд ограничивает интенсивность запросов

## 📄 Лицензия

Распространяется под MIT лицензией.

## 🔗 Репозиторий

Текущий репозиторий:

- [raspopovaa/APIforCards](https://github.com/raspopovaa/APIforCards)

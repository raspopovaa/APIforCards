# ⛽ APIClient

APIClient SDK — асинхронная Python-библиотека для работы с корпоративным API топливных карт.

Проект упрощает интеграцию с API и предоставляет:

- единый `APIClient`
- композиционные доменные сервисы `client.auth`, `client.cards`, `client.reports` и другие
- типизированные модели ответов
- безопасные retry, re-auth и ограничение частоты на транспортном уровне
- demo-сценарий для DEMO-стенда

Проект является независимой разработкой. Использование API должно соответствовать официальным правилам и ограничениям провайдера.

![Python Version](https://img.shields.io/badge/python-3.11--3.14-blue)
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
  Главная точка входа. Собирает инфраструктуру и типизированный `ServiceContainer`.

- [executor.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/executor.py)
  Разделяет session/recovery orchestration и низкоуровневое выполнение операции;
  динамически получает API key из provider перед каждым запросом.

- [composition.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/composition.py)
  Статически собирает authenticator, coordinator, executors и сервисы без `bind()`.

- [service_base.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/service_base.py)
  Содержит узкие протоколы `RequestExecutor`, read-only `SessionContext`,
  `SessionGate`, `SessionRecovery`, внутренний `SessionMutator` и `CredentialsProvider`.

- [authentication.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/authentication.py)
  Изолирует credentials и координирует первичную авторизацию и re-auth.

- [service_groups.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/service_groups.py)
  Явно собирает 16 сервисов и предоставляет типизированные свойства без runtime-магии.

- [transport.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/transport.py)  
  Независимый HTTP-слой без зависимости от авторизации, с внедряемыми client,
  decoder, logger, clock и policy.

- [endpoints.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/endpoints.py)
  Декларативный каталог `EndpointSpec` для всех маршрутов, безопасного рендеринга
  path-параметров и выбора POST/PUT/DELETE-вариантов; `external_code` и
  тарификация объявлены рядом с соответствующим endpoint/route.

- [response.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/response.py)
  Единое декодирование JSON, бинарных ответов и API-ошибок.

- [session.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/session.py)  
  Управляет `session_id` и активным `contract_id`.

- [registry.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/registry.py)  
  Предоставляет поиск и группировку декларативных endpoint-спецификаций.

- [modeling.py](https://github.com/raspopovaa/APIforCards/blob/main/src/api_client_opti24/modeling.py)  
  Тонкий адаптер над Pydantic v2: строгие request-модели, расширяемые response-модели
  и совместимые `decode_model()`/`describe()`.

Публичные доменные пространства имён:

| Домен | Вызов |
|-------|-------|
| Авторизация и статистика | `client.auth` |
| Карты и группы карт | `client.cards`, `client.card_groups` |
| Договоры и кошельки | `client.contracts`, `client.ewallet` |
| Лимиты и ограничения | `client.limits`, `client.restrictions`, `client.region_limits` |
| Отчёты и транзакции | `client.reports`, `client.transactions` |
| Пользователи и приглашения | `client.users`, `client.invites` |
| Шаблоны и виртуальные карты | `client.templates`, `client.virtual_cards` |
| Справочники и цены | `client.dictionaries`, `client.final_prices` |

## 📦 Установка

Пакет `api-client-opti24==2.2.2` опубликован на TestPyPI и поддерживает
`Python >=3.11,<3.15`. Зависимости лучше устанавливать из основного PyPI
отдельно: это исключает случайную подмену зависимостей пакетами из тестового
индекса.

### Вариант 1: uv

```bash
uv venv --python 3.11
uv pip install "httpx>=0.27.0,<1.0" "pydantic>=2.13.4,<3.0"
uv pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.2.2
```

### Вариант 2: pip

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install "httpx>=0.27.0,<1.0" "pydantic>=2.13.4,<3.0"
python -m pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.2.2
```

Проверка версии и публичных импортов:

```bash
.venv/bin/python -c \
  "from api_client_opti24 import APIClient, ConnectionSettings, __version__; print(__version__, APIClient.__name__, ConnectionSettings.__name__)"
```

Локальная установка репозитория для разработки:

```bash
# uv
uv sync --extra dev

# либо pip в активированном virtualenv
python -m pip install -e ".[dev]"
```

## ⚡ Быстрый старт

Перед запуском настройте `.env` или переменные окружения `API_BASE_URL`, `API_KEY`, `API_LOGIN`, `API_PASSWORD`.

```python
import asyncio
from pathlib import Path

from api_client_opti24 import (
    APIClient,
    ConnectionSettings,
    EnvironmentCredentialsProvider,
)


async def main() -> None:
    env_file = Path(__file__).with_name(".env")
    settings = ConnectionSettings.from_env(env_file=env_file)
    credentials = EnvironmentCredentialsProvider.from_env(env_file=env_file)

    async with APIClient(settings=settings, credentials_provider=credentials) as client:
        auth = await client.auth.auth_user()
        try:
            info = await client.auth.get_info()
            cards = await client.cards.get_cards_v2(page=1, onpage=5)

            print("Договоров:", len(auth.data.contracts))
            print("Запросов по тарифу:", info.data.client_info.Queries)
            print("Карт найдено:", cards.total_count)
        finally:
            await client.auth.logoff()


if __name__ == "__main__":
    asyncio.run(main())
```

Этот пример требует реального доступа к API. Сохраните его как `test.py`, а
`.env` разместите рядом: путь определяется через
`Path(__file__).with_name(".env")` и не зависит от рабочей директории IDE.

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
API_ALLOW_INSECURE_HTTP=false
REQUEST_LOG_FILE=./api_requests.jsonl
LOGGER_FILE=./api.log
LOG_LEVEL=INFO
```

`ConnectionSettings` содержит только несекретные параметры. API key, логин и
пароль загружаются отдельным `EnvironmentCredentialsProvider` либо передаются
через `StaticCredentialsProvider`. `APISettings` сохранён для совместимости со
старыми интеграциями, но `APIClient.settings` всегда содержит безопасный
`ConnectionSettings` без credentials.

После авторизации contract-bound сервисы `contracts`, `limits`,
`region_limits`, `restrictions` и `templates` используют договор активной
сессии. `contract_id` можно передать явно для безопасного override. Все параметры
этих сервисов и `ewallet` передаются только по имени; денежные операции принимают
`Decimal` и сериализуют сумму строкой согласно спецификации v1.1.59.

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
- **📚 Типизированные модели** на Pydantic v2
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
- Политики можно заменить через `ConnectionSettings.retry_policy` и
  `ConnectionSettings.rate_limit_policy`, а transport — внедрить в `APIClient` для тестов.
- Решение о повторе учитывает одновременно `EndpointSpec.retry_class` и
  `EndpointSpec.idempotent`.

### Информационная безопасность

- SDK не пишет request/response payload, URL с идентификаторами и текст исключения в лог.
- Ключи, сессии, пароли, телефоны, email и идентификаторы очищаются logger-фильтром.
- Внешний logger получает тот же фильтр автоматически через dependency injection.
- Каждый клиент владеет только своими handlers; файлы открываются в append-режиме.
- `request_log_file` содержит JSONL-аудит без URL, payload и объектных идентификаторов.
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

Успешный API-код не маскирует ошибочный HTTP-статус: оба уровня должны
свидетельствовать об успехе.

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
В текущем каталоге описано `89` уникальных `EndpointSpec`; registry не читает
исходники через AST и не импортирует сервисы динамически.
Сервисы передают executor только имя операции и параметры пути; HTTP-метод,
шаблон URL, версия по умолчанию, session policy, timeout и retry берутся из registry.

## 🧠 Модели и описание данных

Модели используют Pydantic v2 через небольшой совместимый адаптер:

- `BaseModel`
- `Field`
- `field_validator`
- проверка типов содержимого `dict`, длины tuple и вложенных моделей
- `model_validate()` и `model_dump()`
- сохранение дополнительных полей response для совместимости с расширениями API
- запрет дополнительных полей в request-моделях
- адаптер `decode_model()`
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

## 📚 Документация

Документация публикуется как сайт на MkDocs Material:

- [сайт документации](https://raspopovaa.github.io/APIforCards/)
- [установка и быстрый запуск](https://raspopovaa.github.io/APIforCards/getting-started/)
- [каталог методов, DEMO-доступность и тарификация](https://raspopovaa.github.io/APIforCards/methods/)
- [API Reference](https://raspopovaa.github.io/APIforCards/api-reference/)
- [архитектура и безопасность](https://raspopovaa.github.io/APIforCards/architecture/)
- [типовые сценарии](https://raspopovaa.github.io/APIforCards/scenarios/)

API Reference и каталог методов генерируются из кода и runtime registry. Для
локальной проверки выполните:

```bash
uv run python scripts/generate_api_docs.py
uv run python scripts/generate_method_catalog.py
uv run python scripts/build_docs_site.py
uv run mike serve
```

Строгая сборка создаётся в `site/`. Workflow `Docs` проверяет её в pull request,
а workflow `Pages` публикует текущую линию `major.minor` и сохраняет предыдущие
версии в `gh-pages`. Alias `latest` всегда указывает на актуальную линию SDK.

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
uv run pytest

# либо в активированном pip-окружении
python -m pytest
```

Сейчас набор из `125` тестов покрывает:

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
uv build --clear
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
pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.2.2
```

## 🤖 GitHub Actions

В репозитории настроен базовый CI workflow:

- [ci.yml](https://github.com/raspopovaa/APIforCards/blob/main/.github/workflows/ci.yml)

Он запускается:

- на `push` в `main`
- на `pull_request`

Текущий pipeline:

- запускает матрицу `Python 3.11` и `Python 3.14`
- устанавливает зависимости через `pip install -e ".[dev]"`
- запускает `pytest`
- запускает полную конфигурацию Ruff для `src`, `tests` и `scripts`
- проверяет Black для `src`, `tests` и `scripts`
- запускает `mypy --strict` для всех source-файлов SDK

## ▶️ Demo-скрипт

Файл:
- [examples/demo_async.py](https://github.com/raspopovaa/APIforCards/blob/main/examples/demo_async.py)

Запуск:

```bash
uv run python examples/demo_async.py
```

Если DEMO-стенд начинает ограничивать запросы:

```bash
DEMO_MIN_REQUEST_INTERVAL=0.35 uv run python examples/demo_async.py
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
│   ├── authentication.py
│   ├── config.py
│   ├── env.py
│   ├── errors.py
│   ├── executor.py
│   ├── endpoints.py
│   ├── modeling.py
│   ├── policies.py
│   ├── registry.py
│   ├── response.py
│   ├── runtime.py
│   ├── service_base.py
│   ├── service_groups.py
│   ├── session.py
│   └── transport.py
├── docs/
├── scripts/
├── tests/
├── uv.lock
├── pyproject.toml
└── README.md
```

## 🛠️ Разработка

```bash
uv run pytest
uv run ruff check .
uv run black .
uv run mypy src
```

Весь SDK проходит строгий `mypy`; преобразование и проверку runtime-данных
выполняет Pydantic v2.

## ⚠️ Ограничения

- SDK требует Python не ниже `3.11` и поддерживает диапазон `>=3.11,<3.15`
- transport использует `httpx`
- точность моделей зависит от качества внешней спецификации
- DEMO-стенд ограничивает интенсивность запросов

## ✅ Соответствие README коду

| Раздел README | Источник истины в репозитории | Проверено |
|---------------|-------------------------------|-----------|
| Возможности | `client.py`, `services/`, `service_groups.py` | Все 89 endpoint-методов доступны только через композиционные доменные сервисы |
| Архитектура | `client.py`, `executor.py`, `service_base.py`, `service_groups.py` | Сервисы не хранят `APIClient`; зависимости разделены узкими протоколами |
| Установка | `pyproject.toml`, `uv.lock`, `__init__.py` | Версия `2.2.2`, диапазон Python и публичные импорты совпадают |
| Быстрый старт | `config.py`, `auth.py`, `cards.py`, модели auth/cards | Сигнатуры и используемые поля ответа проверены |
| Конфигурация | `config.py`, `credentials.py`, `.env.example`, `env.py` | Безопасные connection settings отделены от providers секретов |
| Retry и безопасность | `policies.py`, `transport.py`, `logger.py`, `utils.py` | Retry зависит от idempotency; удалённый HTTP запрещён; логи очищаются |
| Ошибки API | `errors.py`, `response.py` | HTTP/API-коды и перечисленные классы ошибок обрабатываются |
| Registry и DEMO | `endpoints.py`, `registry.py`, `tests/contracts/endpoints.json`, `specifications/api-methods.yaml` | 91 внешний код, маршруты, DEMO-флаги и тарификация строго сверяются с независимым YAML-контрактом |
| Модели | `modeling.py`, `models/` | Pydantic проверяет контейнеры и request extras; response extras сохраняются |
| Документация | `scripts/generate_api_docs.py`, `scripts/build_docs_site.py`, `docs/` | Генераторы и статический сайт присутствуют |
| Политика спецификации | `docs/spec-compatibility.md`, модели и тесты | Зафиксированы известные расхождения и принятые решения |
| Тестирование | `tests/`, настройки pytest в `pyproject.toml` | Полный набор и внешняя contract-проверка запускаются в CI |
| Публикация | `pyproject.toml`, `uv.lock` | Сборка выполняется через `uv build`, публикация — `uv publish` |
| GitHub Actions | `.github/workflows/` | CI, Docs и Pages соответствуют описанию |
| Demo-скрипт | `examples/demo_async.py` | Асинхронный цветной сценарий существует и учитывает rate limit |
| MPC и QR | `services/virtual_cards.py` | Все перечисленные методы реализованы |
| Структура и разработка | дерево репозитория, dev dependencies | Пути и команды актуализированы |
| Ограничения, лицензия, репозиторий | `pyproject.toml` | Python range, HTTP dependency, MIT metadata и URL совпадают |

## 📄 Лицензия

Распространяется под MIT лицензией.

## 🔗 Репозиторий

Текущий репозиторий:

- [raspopovaa/APIforCards](https://github.com/raspopovaa/APIforCards)

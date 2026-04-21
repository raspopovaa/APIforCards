# ⛽ APIClient OPTI24

APIClient OPTI24 SDK — асинхронная Python-библиотека для работы с корпоративным API топливных карт Газпромнефть / Opti24.

Проект упрощает интеграцию с API и предоставляет:

- единый `APIClient`
- доменные сервисы для карт, транзакций, пользователей, шаблонов, лимитов и отчетов
- типизированные модели ответов
- retry и re-auth на транспортном уровне
- demo-сценарий для DEMO-стенда

Проект является независимой разработкой и не связан с АО «Газпром нефть». Использование API должно соответствовать официальным правилам и ограничениям провайдера.

![Python Version](https://img.shields.io/badge/python-3.14-blue)
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
| 🧾 Шаблоны и ВК | templates, virtual cards | Работа с шаблонами виртуальных карт |
| 📚 Справочники | dictionaries, AZS, related data | Поддержка общих справочников |

## 🏗️ Архитектура

Основные слои проекта:

- [client.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/client.py)  
  Главная точка входа. Собирает `settings`, `registry`, `session_manager` и `transport`.

- [transport.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/transport.py)  
  Выполняет HTTP-запросы через `httpx`, делает retry для сетевых ошибок и `429/509`, а также повторную авторизацию.

- [session.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/session.py)  
  Управляет `session_id` и активным `contract_id`.

- [registry.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/registry.py)  
  Хранит метаданные методов и timeout policy.

- [modeling.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/modeling.py)  
  Собственный stdlib-only слой моделей на `dataclasses` с ручной валидацией.

## 📦 Установка

```bash
cd "/Users/andrejraspopov/Documents/New project/api-pro-sdk"
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

## ⚡ Быстрый старт

```python
import asyncio

from api_client_opti24.client import APIClient
from api_client_opti24.config import APISettings


async def main() -> None:
    settings = APISettings.from_env()

    async with APIClient(
        base_url=settings.base_url,
        api_key=settings.api_key,
        login=settings.login,
        password=settings.password,
    ) as client:
        auth_response = await client.auth_user()
        print("=== АВТОРИЗАЦИЯ ===")
        print(auth_response.data.contracts[0])

        info_response = await client.get_info()
        print("=== СТАТИСТИКА ===")
        print(info_response.data.client_info)

        cards_response = await client.get_cards_v2()
        print("=== КАРТЫ V2 ===")
        print(cards_response.total_count)

        await client.logoff()


if __name__ == "__main__":
    asyncio.run(main())
```

## 📖 Конфигурация

SDK читает настройки из `.env` через встроенный загрузчик:

- [env.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/env.py)
- [config.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/src/api_client_opti24/config.py)

Шаблон файла:
- [`.env.example`](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/.env.example)

Пример:

```env
API_BASE_URL=https://api-demo.opti-24.ru/vip/
API_KEY=your_api_key_here
API_LOGIN=your_login
API_PASSWORD=your_password
REQUEST_LOG_FILE=./api_requests.jsonl
LOGGER_FILE=./api.log
LOG_LEVEL=INFO
```

## 🎯 Что важно в реализации

- **♻️ Retry и backoff** для сетевых ошибок и rate limiting
- **🔐 Re-auth** при потере сессии
- **📚 Типизированные модели** на `dataclasses`
- **🧾 Описание полей** через `Field(..., description=...)`
- **🧪 Покрытие тестами** для моделей, transport, session и registry
- **⚖️ Policy “спека vs реальность”** в спорных местах

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

## ▶️ Demo-скрипт

Файл:
- [examples/demo_async.py](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/examples/demo_async.py)

Запуск:

```bash
.venv/bin/python examples/demo_async.py
```

Если DEMO-стенд начинает ограничивать запросы:

```bash
DEMO_MIN_REQUEST_INTERVAL=0.35 .venv/bin/python examples/demo_async.py
```

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

## ⚠️ Ограничения

- SDK рассчитан на Python `3.14`
- transport использует `httpx`
- точность моделей зависит от качества внешней спецификации
- DEMO-стенд ограничивает интенсивность запросов

## 📄 Лицензия

Распространяется под MIT лицензией.

## 🔗 Репозиторий

Текущий репозиторий:

- [raspopovaa/raspopovaa](https://github.com/raspopovaa/raspopovaa)

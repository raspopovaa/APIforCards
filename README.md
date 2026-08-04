# API Client SDK

[![CI](https://github.com/raspopovaa/APIforCards/actions/workflows/ci.yml/badge.svg)](https://github.com/raspopovaa/APIforCards/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11--3.14-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/license/mit)

Асинхронный Python SDK для работы с корпоративным API топливных карт.

> [!IMPORTANT]
> Проект находится в разработке. Текущая версия публикуется в TestPyPI и не
> предназначена для production-интеграций без предварительного тестирования.

## Возможности

- типизированные асинхронные методы на базе `httpx` и Pydantic;
- доменные сервисы `client.auth`, `client.cards`, `client.reports` и другие;
- управление сессией, выбор договора и безопасное восстановление авторизации;
- retry только для разрешённых политикой операций;
- ограничение частоты и числа параллельных запросов;
- единая обработка HTTP- и API-ошибок;
- потоковое скачивание файлов отчётов;
- каталог методов с DEMO-доступностью и тарификацией.

## Требования

- Python `>=3.11,<3.15`;
- URL стенда, API key, логин и пароль;
- доступ к API из разрешённой сети.

## Установка

Пока пакет размещён в TestPyPI. Зависимости устанавливаются отдельно из
основного PyPI, чтобы тестовый индекс не участвовал в их разрешении.

### uv

```bash
uv venv --python 3.11
uv pip install "httpx>=0.27,<1.0" "pydantic>=2.13.4,<3.0"
uv pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.3.0
```

### pip

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install "httpx>=0.27,<1.0" "pydantic>=2.13.4,<3.0"
python -m pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.3.0
```

Проверка импорта:

```bash
.venv/bin/python -c \
  "from api_client_opti24 import APIClient, __version__; print(__version__, APIClient.__name__)"
```

## Быстрый старт

Создайте рядом со скриптом файл `.env`:

```env
API_BASE_URL=https://api.example.ru/vip/
API_KEY=your_api_key
API_LOGIN=your_login
API_PASSWORD=your_password
```

Не добавляйте `.env` в Git.

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

    async with APIClient(
        settings=settings,
        credentials_provider=credentials,
    ) as client:
        auth = await client.auth.auth_user()
        try:
            cards = await client.cards.get_cards_v2(page=1, onpage=5)
            print("Договоров:", len(auth.data.contracts))
            print("Карт найдено:", cards.total_count)
        finally:
            await client.auth.logoff()


if __name__ == "__main__":
    asyncio.run(main())
```

Пример выполняет реальные сетевые запросы. Корректные credentials не отменяют
сетевые и географические ограничения API.

## Использование

Методы сгруппированы по предметным областям:

```python
await client.auth.get_info()
await client.cards.get_cards_v2(page=1, onpage=20)
await client.transactions.get_transactions_v2()
await client.reports.get_reports()
```

Параметры публичных методов передаются по имени. JSON-операции возвращают
типизированный envelope `status/data/timestamp`.

## Документация

Полное руководство опубликовано на
[GitHub Pages](https://raspopovaa.github.io/APIforCards/).

| Раздел | Содержание |
|---|---|
| [Начало работы](https://raspopovaa.github.io/APIforCards/getting-started/) | Установка, `.env` и первый запрос |
| [Конфигурация](https://raspopovaa.github.io/APIforCards/configuration/) | Timeout, retry, rate limit и dependency injection |
| [Методы API](https://raspopovaa.github.io/APIforCards/methods/) | Сигнатуры, маршруты, DEMO-доступность и тарификация |
| [Типовые сценарии](https://raspopovaa.github.io/APIforCards/scenarios/) | Прикладные последовательности вызовов |
| [Ошибки и retry](https://raspopovaa.github.io/APIforCards/errors/) | Исключения и правила безопасных повторов |
| [Архитектура](https://raspopovaa.github.io/APIforCards/architecture/) | Слои SDK и зависимости |
| [Безопасность](https://raspopovaa.github.io/APIforCards/security/) | Credentials, журналирование и транспорт |
| [API Reference](https://raspopovaa.github.io/APIforCards/api-reference/) | Сервисы и модели данных |

## Разработка

```bash
git clone https://github.com/raspopovaa/APIforCards.git
cd APIforCards
uv sync --extra dev

uv run pytest
uv run ruff check .
uv run black --check .
uv run mypy src
```

Перед изменением API-контрактов также запустите сборку документации, описанную в
[руководстве проекта](https://raspopovaa.github.io/APIforCards/versioning/).

## Лицензия

Проект распространяется на условиях лицензии MIT.

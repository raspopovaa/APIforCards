# Установка и быстрый запуск

## Требования

- Python `>=3.11,<3.15`;
- доступ к API из разрешённой сети;
- API key, логин и пароль;
- HTTPS URL стенда с путём `/vip/`.

## Установка через uv

Зависимости устанавливаются из основного PyPI, а библиотека — из TestPyPI.
Так тестовый индекс не используется для разрешения транзитивных зависимостей.

```bash
uv venv --python 3.11
uv pip install "httpx>=0.27.0,<1.0" "pydantic>=2.13.4,<3.0"
uv pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.3.0
```

## Установка через pip

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install "httpx>=0.27.0,<1.0" "pydantic>=2.13.4,<3.0"
python -m pip install --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24==2.3.0
```

Проверка установки:

```bash
.venv/bin/python -c \
  "from api_client_opti24 import APIClient, __version__; print(__version__, APIClient.__name__)"
```

Ожидаемый результат:

```text
2.3.0 APIClient
```

## Файл `.env`

Создайте `.env` рядом с запускаемым скриптом:

```env
API_BASE_URL=https://api.example.ru/vip/
API_KEY=your_api_key
API_LOGIN=your_login
API_PASSWORD=your_password
API_REQUESTS_PER_SECOND=2
API_ALLOW_INSECURE_HTTP=false
```

Не добавляйте `.env` в Git.

## Быстрый старт

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

!!! warning "Доступ к стенду"
    Пример выполняет реальные сетевые запросы. Если API принимает запросы только
    из определённой страны, сети или списка IP, запуск из другой сети завершится
    ошибкой доступа независимо от корректности SDK.

## Следующие шаги

1. Проверьте все параметры в разделе [Конфигурация](configuration.md).
2. Найдите нужный вызов в [каталоге методов](methods.md).
3. Добавьте обработку исключений из раздела [Ошибки и retry](errors.md).

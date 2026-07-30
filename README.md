# ⛽ APIClient

Асинхронный Python SDK для работы с корпоративным API топливных карт.

SDK предоставляет единый клиент, доменные сервисы и типизированные модели, чтобы
интеграции не реализовывали вручную авторизацию, повторные запросы, обработку ошибок
и ограничение частоты вызовов.

> Проект является независимой разработкой. Для использования SDK необходим
> официальный доступ к API провайдера.

![Python Version](https://img.shields.io/badge/python-3.11--3.14-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Основные возможности

- асинхронный клиент на `httpx`;
- доменные сервисы: карты, договоры, транзакции, пользователи, отчёты и лимиты;
- типизированные модели запросов и ответов на Pydantic v2;
- автоматическая авторизация и восстановление сессии;
- безопасные retry и клиентское ограничение частоты запросов;
- единая обработка HTTP-ошибок и внутренних кодов API;
- журналирование с очисткой секретов и персональных данных.

Полный список поддерживаемых методов приведён в
[каталоге методов](https://raspopovaa.github.io/APIforCards/methods/).

## Требования

- Python `>=3.11,<3.15`;
- действующие `api_key`, логин и пароль API;
- HTTPS-доступ к production- или DEMO-стенду.

## Установка

Пакет пока публикуется в TestPyPI. Зависимости рекомендуется устанавливать из
основного PyPI отдельно, чтобы тестовый индекс не использовался для их разрешения.

```bash
python -m pip install "httpx>=0.27,<1.0" "pydantic>=2.13.4,<3.0"
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --no-deps api-client-opti24
```

Страница пакета: [TestPyPI](https://test.pypi.org/project/api-client-opti24/).

## Конфигурация

Скопируйте [`.env.example`](.env.example) в `.env` и укажите свои данные:

```env
API_BASE_URL=https://api-demo.opti-24.ru/vip/
API_KEY=your_api_key_here
API_LOGIN=your_login_here
API_PASSWORD=your_password_here
API_REQUESTS_PER_SECOND=2
```

Не сохраняйте реальные ключи, пароли и идентификаторы сессий в репозитории.

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

Пример требует реального доступа к API. Дополнительный сценарий находится в
[`examples/demo_async.py`](examples/demo_async.py).

## Важное поведение и ограничения

- **SDK асинхронный.** Методы вызываются через `await`, а клиент рекомендуется
  использовать как асинхронный контекстный менеджер.
- **DEMO-стенд ограничивает частоту запросов.** Для него рекомендуется начинать с
  `API_REQUESTS_PER_SECOND=2`.
- **Изменяющие запросы не повторяются после сетевой ошибки.** Операция могла быть
  выполнена сервером, поэтому автоматический retry создавал бы риск дублирования.
- **Успех проверяется на двух уровнях.** SDK учитывает HTTP-статус и внутренний
  `status.code` в JSON-ответе.
- **Ответы API могут расширяться.** Response-модели сохраняют неизвестные поля для
  обратной совместимости, а request-модели запрещают лишние поля.
- **Контекст ошибки может содержать чувствительные данные.** Не отправляйте
  `APIError.context` в общие журналы без дополнительной очистки.
- **Спецификация и фактические ответы иногда расходятся.** Принятые решения и
  известные исключения описаны в
  [политике совместимости](https://raspopovaa.github.io/APIforCards/spec-compatibility/).

## Документация

- [Установка и начало работы](https://raspopovaa.github.io/APIforCards/getting-started/)
- [Каталог методов](https://raspopovaa.github.io/APIforCards/methods/)
- [API Reference](https://raspopovaa.github.io/APIforCards/api-reference/)
- [Типовые сценарии](https://raspopovaa.github.io/APIforCards/scenarios/)
- [Архитектура и безопасность](https://raspopovaa.github.io/APIforCards/architecture/)

Ошибки и предложения можно создавать в
[GitHub Issues](https://github.com/raspopovaa/APIforCards/issues).

## Разработка

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run mypy src
```

## Лицензия

Проект распространяется по лицензии [MIT](LICENSE).

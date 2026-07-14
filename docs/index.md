# Документация APIClient

Этот каталог содержит документацию проекта.

Основные разделы:

- [README проекта](https://github.com/raspopovaa/APIforCards/blob/main/README.md)
- [Автоматически сгенерированный API Reference](https://github.com/raspopovaa/APIforCards/blob/main/docs/api-reference.md)
- [Совместимость со спецификацией](https://github.com/raspopovaa/APIforCards/blob/main/docs/spec-compatibility.md)
- [Архитектура SDK](https://github.com/raspopovaa/APIforCards/blob/main/docs/architecture.md)
- [Информационная безопасность](https://github.com/raspopovaa/APIforCards/blob/main/docs/security.md)

## Как обновлять документацию

Локально:

```bash
cd path/to/api-pro-sdk
.venv/bin/python scripts/generate_api_docs.py
```

После запуска будет обновлен файл:

- [api-reference.md](https://github.com/raspopovaa/APIforCards/blob/main/docs/api-reference.md)

## Что попадает в автодокументацию

- публичные модули пакета `api_client_opti24`
- публичные классы и функции
- сигнатуры
- docstring'и
- описание полей моделей через `BaseModel.describe()`

Отдельно стоит учитывать, что `registry` отражает:

- demo-доступность методов
- alias-маршруты для альтернативных веток API
- дополнительные MPC/QR-методы, покрытые SDK

## Публикация пакета

Локальная сборка:

```bash
cd path/to/api-pro-sdk
uv build
```

Публикация в TestPyPI:

```bash
export UV_PUBLISH_TOKEN="<testpypi-token>"
uv publish --publish-url https://test.pypi.org/legacy/
```

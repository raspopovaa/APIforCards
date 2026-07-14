# Документация APIClient

Этот каталог содержит документацию проекта.

Основные разделы:

- [README проекта](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/README.md)
- [Автоматически сгенерированный API Reference](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/docs/api-reference.md)

## Как обновлять документацию

Локально:

```bash
cd "/Users/andrejraspopov/Documents/New project/api-pro-sdk"
.venv/bin/python scripts/generate_api_docs.py
```

После запуска будет обновлен файл:

- [api-reference.md](/Users/andrejraspopov/Documents/New%20project/api-pro-sdk/docs/api-reference.md)

## Что попадает в автодокументацию

- публичные модули пакета `api_client_opti24`
- публичные классы и функции
- сигнатуры
- docstring'и
- описание полей моделей через `BaseModel.describe()`

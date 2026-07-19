# Конфигурация

## Переменные окружения

| Переменная | Обязательна | Назначение | Значение по умолчанию |
|---|:---:|---|---|
| `API_BASE_URL` | Да | Полный URL API с `http://` или `https://` | — |
| `API_KEY` | Да | Ключ API | — |
| `API_LOGIN` | Да | Логин пользователя | — |
| `API_PASSWORD` | Да | Пароль пользователя | — |
| `API_REQUESTS_PER_SECOND` | Нет | Упреждающий rate limit клиента | без ограничения |
| `API_ALLOW_INSECURE_HTTP` | Нет | Разрешить удалённый HTTP | `false` |
| `LOG_LEVEL` | Нет | Уровень журнала | `INFO` |
| `LOGGER_FILE` | Нет | Основной файл журнала | `./api.log` |
| `REQUEST_LOG_FILE` | Нет | JSONL-аудит операций | `./api_requests.jsonl` |

## Безопасные настройки

Рекомендуемый `ConnectionSettings` не содержит credentials:

```python
from api_client_opti24 import ConnectionSettings

settings = ConnectionSettings(
    base_url="https://api.example.ru/vip/",
    request_log_file="./api_requests.jsonl",
    logger_file="./api.log",
    log_level="INFO",
)
```

Credentials передаются отдельно:

```python
from api_client_opti24 import StaticCredentialsProvider

credentials = StaticCredentialsProvider(
    api_key="api-key",
    login="login",
    password="password",
)
```

`APISettings` сохранён для совместимости, но новые интеграции должны предпочитать
`ConnectionSettings` и отдельные providers.

## Динамическая ротация API key

`OperationExecutor` вызывает provider перед каждым запросом. Поэтому можно
подключить secret manager без пересоздания клиента:

```python
class SecretManagerAPIKeyProvider:
    def get_api_key(self) -> str:
        return read_cached_api_key_from_secret_manager()
```

Provider должен возвращать непустую строку. Сетевой запрос к secret manager лучше
не выполнять на каждый API-вызов: используйте безопасный кэш с контролируемым TTL.

## Timeout

```python
from api_client_opti24 import ConnectionSettings, TimeoutPolicy

settings = ConnectionSettings(
    base_url="https://api.example.ru/vip/",
    timeouts=TimeoutPolicy(
        default=30.0,
        auth=30.0,
        read_heavy=120.0,
    ),
)
```

Конкретный timeout выбирается из `EndpointSpec.timeout_class`.

## Rate limit

Для DEMO обычно используется значение `2`, для production — `5`, если это
соответствует условиям конкретного договора:

```env
API_REQUESTS_PER_SECOND=2
```

Клиентский limiter не отменяет серверные ограничения и тарификацию.

## HTTP и HTTPS

- удалённые API адреса должны использовать HTTPS;
- HTTP разрешён для loopback;
- небезопасный удалённый HTTP требует явного `allow_insecure_http=True`;
- path-параметры централизованно кодируются и не могут содержать `/`, `\\`, `?`,
  `#`, `.` или `..`.

## Dependency injection

Для тестирования можно внедрять `transport`, `session_manager`, `registry`,
`logger`, `clock`, `credentials_provider` и `api_key_provider` через конструктор
`APIClient`.

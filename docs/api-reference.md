# API Reference

Этот файл сгенерирован автоматически скриптом `scripts/generate_api_docs.py`.

Ниже собраны публичные модули, классы, функции и описание моделей SDK.

## `api_client_opti24`

Описание отсутствует.

_Публичные классы и функции не обнаружены._

## `api_client_opti24.client`

Описание отсутствует.

### `APIClient`

Методы работы с топливными картами.

Сигнатура: `APIClient(base_url: str, api_key: str, login: str, password: str)`

Публичные методы:

- `aclose(self) -> None`

## `api_client_opti24.config`

Описание отсутствует.

### `APISettings`

APISettings(base_url: 'str', api_key: 'str', login: 'str', password: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0))

Сигнатура: `APISettings(base_url: 'str', api_key: 'str', login: 'str', password: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0)) -> None`

Публичные методы:

- `from_env(*, load_dotenv: 'bool' = True) -> "'APISettings'"`

### `TimeoutPolicy`

TimeoutPolicy(default: 'float' = 30.0, auth: 'float' = 30.0, read_heavy: 'float' = 120.0)

Сигнатура: `TimeoutPolicy(default: 'float' = 30.0, auth: 'float' = 30.0, read_heavy: 'float' = 120.0) -> None`

Публичные методы:

- `resolve(self, timeout_class: 'str') -> 'float'`

## `api_client_opti24.decorators`

Описание отсутствует.

### `api_method`

Описание отсутствует.

Сигнатура: `api_method(require_session: bool = False, default_version: str = 'v1')`

### `get_current_api_method_name`

Описание отсутствует.

Сигнатура: `get_current_api_method_name() -> str | None`

## `api_client_opti24.env`

Описание отсутствует.

### `load_env_file`

Описание отсутствует.

Сигнатура: `load_env_file(path: 'str | Path' = '.env', *, override: 'bool' = False) -> 'None'`

## `api_client_opti24.errors`

Описание отсутствует.

### `APIError`

Common base class for all non-exit exceptions.

Сигнатура: `APIError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `AccessDeniedError`

Common base class for all non-exit exceptions.

Сигнатура: `AccessDeniedError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `DuplicateConflictError`

Common base class for all non-exit exceptions.

Сигнатура: `DuplicateConflictError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ErrorContext`

ErrorContext(http_status_code: 'int', api_status_code: 'int | None', error_type: 'str | None', messages: 'tuple[str, ...]', raw_payload: 'Any', endpoint: 'str | None', method_name: 'str | None', hint: 'str | None', retryable: 'bool')

Сигнатура: `ErrorContext(http_status_code: 'int', api_status_code: 'int | None', error_type: 'str | None', messages: 'tuple[str, ...]', raw_payload: 'Any', endpoint: 'str | None', method_name: 'str | None', hint: 'str | None', retryable: 'bool') -> None`

### `NotAuthenticatedError`

Common base class for all non-exit exceptions.

Сигнатура: `NotAuthenticatedError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `NotFoundError`

Common base class for all non-exit exceptions.

Сигнатура: `NotFoundError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `RateLimitError`

Common base class for all non-exit exceptions.

Сигнатура: `RateLimitError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ServerError`

Common base class for all non-exit exceptions.

Сигнатура: `ServerError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ValidationError`

Common base class for all non-exit exceptions.

Сигнатура: `ValidationError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `build_api_error`

Описание отсутствует.

Сигнатура: `build_api_error(*, status_code: 'int', body: 'Any', endpoint: 'str | None', method_name: 'str | None' = None, http_status_code: 'int | None' = None) -> 'APIError'`

## `api_client_opti24.modeling`

Описание отсутствует.

### `BaseModel`

Описание отсутствует.

Сигнатура: `BaseModel(**kwargs: 'Any') -> 'None'`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FieldInfo`

Описание отсутствует.

Сигнатура: `FieldInfo(default: 'Any' = <object object at 0x10294c700>, *, default_factory: 'Callable[[], Any] | Any' = <dataclasses._MISSING_TYPE object at 0x102d16270>, alias: 'str | None' = None, description: 'str | None' = None) -> 'None'`

### `ValidationError`

Inappropriate argument value (of correct type).

Сигнатура: `ValidationError()`

### `Field`

Описание отсутствует.

Сигнатура: `Field(default: 'Any' = <object object at 0x10294c700>, *, default_factory: 'Callable[[], Any] | Any' = <dataclasses._MISSING_TYPE object at 0x102d16270>, alias: 'str | None' = None, description: 'str | None' = None) -> 'FieldInfo'`

### `field_validator`

Описание отсутствует.

Сигнатура: `field_validator(*field_names: 'str', mode: 'str' = 'after', **_: 'Any') -> 'Callable[[Callable[..., Any]], Any]'`

### `validator`

Описание отсутствует.

Сигнатура: `validator(*field_names: 'str', pre: 'bool' = False) -> 'Callable[[Callable[..., Any]], Any]'`

## `api_client_opti24.models`

Описание отсутствует.

_Публичные классы и функции не обнаружены._

## `api_client_opti24.models.auth`

Описание отсутствует.

### `AccessRights`

AccessRights(**kwargs: 'Any') -> 'None'

Сигнатура: `AccessRights(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
web:
  type: bool
  required: False
  description: Доступ к веб-интерфейсу
api:
  type: bool
  required: False
  description: Доступ к API
mobile:
  type: bool
  required: False
  description: Доступ к мобильному приложению
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthError`

AuthError(**kwargs: 'Any') -> 'None'

Сигнатура: `AuthError(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
code:
  type: str
  required: True
  description: Код ошибки (например, INVALID_CREDENTIALS)
message:
  type: str
  required: True
  description: Текст ошибки
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthErrorResponse`

AuthErrorResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `AuthErrorResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
error:
  type: AuthError
  required: True
  description: Описание ошибки авторизации
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthUserData`

AuthUserData(**kwargs: 'Any') -> 'None'

Сигнатура: `AuthUserData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
client_id:
  type: str
  required: True
  description: ID клиента в системе
client_status:
  type: str
  required: True
  description: Статус клиента (Active, Blocked, и т.п.)
org_name:
  type: str | None
  required: False
  description: Наименование организации
session_id:
  type: str
  required: True
  description: JWT токен активной сессии
user_id:
  type: str
  required: True
  description: ID пользователя
contracts:
  type: list[ContractInfo]
  required: False
  description: Список доступных договоров
role_id:
  type: str | None
  required: False
  description: Код роли (например, Supervisor)
role_name:
  type: str | None
  required: False
  description: Название роли (например, Администратор)
read_only:
  type: bool
  required: False
  description: Флаг режима только чтение
user_name:
  type: str | None
  required: False
  description: Имя пользователя
user_patronymic:
  type: str | None
  required: False
  description: Отчество пользователя
user_surname:
  type: str | None
  required: False
  description: Фамилия пользователя
last_contract:
  type: str | None
  required: False
  description: SID последнего договора
access:
  type: AccessRights | None
  required: False
  description: Права доступа (web/api/mobile)
email:
  type: str | None
  required: False
  description: Электронная почта
phone:
  type: str | None
  required: False
  description: Телефон
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthUserResponse`

AuthUserResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `AuthUserResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusResponse
  required: True
  description: Статус ответа API
data:
  type: AuthUserData
  required: True
  description: Данные авторизованного пользователя
timestamp:
  type: int | None
  required: False
  description: Метка времени (unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ClientInfo`

ClientInfo(**kwargs: 'Any') -> 'None'

Сигнатура: `ClientInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
Client:
  type: str
  required: True
  description: ID клиента
ClientType:
  type: str
  required: True
  description: Тип клиента (например, D)
Contract:
  type: str
  required: True
  description: ID контракта
ContractName:
  type: str
  required: True
  description: Название контракта
PricePlan:
  type: str | None
  required: False
  description: Тарифный план
Cost:
  type: float | None
  required: False
  description: Стоимость запросов
Queries:
  type: int | None
  required: False
  description: Количество запросов
Additional:
  type: int | None
  required: False
  description: Дополнительное значение
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractInfo`

ContractInfo(**kwargs: 'Any') -> 'None'

Сигнатура: `ContractInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID договора
number:
  type: str
  required: True
  description: Номер договора
mpc:
  type: bool
  required: False
  description: Есть ли МПК (виртуальные карты)
template_id:
  type: str | None
  required: False
  description: ID шаблона ВК, если есть
cards_count:
  type: int
  required: False
  description: Количество карт по договору
one_price:
  type: bool
  required: False
  description: Признак единой цены
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `GetInfoResponse`

GetInfoResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `GetInfoResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusResponse
  required: True
  description: Статус ответа API
data:
  type: InfoData
  required: True
  description: Детализированные данные о статистике
timestamp:
  type: int
  required: True
  description: Временная метка (UNIX timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InfoData`

InfoData(**kwargs: 'Any') -> 'None'

Сигнатура: `InfoData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
from_:
  type: datetime
  required: True
  alias: from
  description: Начало периода статистики
to:
  type: datetime
  required: True
  description: Конец периода статистики
client_info:
  type: ClientInfo
  required: True
  description: Информация о клиенте
methods:
  type: MethodsCount
  required: True
  description: Количество вызовов по категориям
methods_info:
  type: MethodsInfo
  required: True
  description: Описание доступных методов API
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LogoffResponse`

LogoffResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `LogoffResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusResponse
  required: True
  description: Статус ответа API
data:
  type: bool
  required: True
  description: True — если выход выполнен успешно
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MethodsCount`

MethodsCount(**kwargs: 'Any') -> 'None'

Сигнатура: `MethodsCount(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
all:
  type: int
  required: False
  description: Общее количество методов
cards:
  type: int | None
  required: False
  description: Методы, связанные с картами
cardgroups:
  type: int | None
  required: False
  description: Методы, связанные с группами карт
card:
  type: int | None
  required: False
  description: Методы, связанные с одной картой
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MethodsInfo`

MethodsInfo(**kwargs: 'Any') -> 'None'

Сигнатура: `MethodsInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
actions_bill:
  type: dict[str, str]
  required: True
  description: Платные методы API (влияют на статистику)
actions_not_bill:
  type: dict[str, str]
  required: True
  description: Бесплатные методы API (не влияют на статистику)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `StatusResponse`

StatusResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `StatusResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
code:
  type: int
  required: True
  description: Код состояния ответа (например, 200 — OK, 400 — ошибка запроса)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.card_group`

Описание отсутствует.

### `CardGroupItem`

Информация о группе карт.

Сигнатура: `CardGroupItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор группы карт
name:
  type: str
  required: True
  description: Название группы карт
cards_count:
  type: int
  required: True
  description: Количество карт в группе
status:
  type: str
  required: True
  description: Статус группы (например, Synchronize)
contract_id:
  type: str
  required: True
  description: Идентификатор договора
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupListData`

Контейнер данных со списком групп карт.

Сигнатура: `CardGroupListData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество групп
result:
  type: list[CardGroupItem]
  required: True
  description: Список групп карт
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupListResponse`

Ответ метода получения списка групп карт.

Сигнатура: `CardGroupListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Информация о статусе запроса (код и описание)
data:
  type: CardGroupListData
  required: True
  description: Основные данные ответа
timestamp:
  type: int
  required: True
  description: Временная метка ответа (UNIX timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveCardGroupResponse`

Ответ метода удаления группы карт.

Сигнатура: `RemoveCardGroupResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Информация о статусе запроса (код и описание)
data:
  type: bool
  required: True
  description: Флаг успешного выполнения операции
timestamp:
  type: int
  required: True
  description: Временная метка ответа (UNIX timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardGroupData`

Информация о созданной или изменённой группе.

Сигнатура: `SetCardGroupData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор созданной или изменённой группы
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardGroupResponse`

Ответ метода установки/изменения группы карт.

Сигнатура: `SetCardGroupResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Информация о статусе запроса (код и описание)
data:
  type: SetCardGroupData
  required: True
  description: Информация о созданной/обновлённой группе
timestamp:
  type: int
  required: True
  description: Временная метка ответа (UNIX timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardsToGroupResponse`

Ответ метода добавления карт в группу.

Сигнатура: `SetCardsToGroupResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Информация о статусе запроса (код и описание)
data:
  type: bool
  required: True
  description: Флаг успешного выполнения операции
timestamp:
  type: int
  required: True
  description: Временная метка ответа (UNIX timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.cards`

Описание отсутствует.

### `BoolResponse`

BoolResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `BoolResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус запроса
data:
  type: bool
  required: True
  description: Флаг результата операции (True — успех)
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDetail`

CardDetail(**kwargs: 'Any') -> 'None'

Сигнатура: `CardDetail(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор карты
contract_id:
  type: str
  required: True
  description: ID договора
number:
  type: str
  required: True
  description: Номер карты
status:
  type: str
  required: True
  description: Статус карты
can_work_offline:
  type: bool | None
  required: False
  description: Может работать офлайн
card_auth_type:
  type: str | None
  required: False
  description: Тип аутентификации карты
comment:
  type: str | None
  required: False
  description: Комментарий к карте
date_last_usage:
  type: datetime | str | None
  required: False
  description: Дата последнего использования (может быть пустой строкой)
date_released:
  type: datetime | str | None
  required: False
  description: Дата выпуска карты
servicecenter_last_usage_name:
  type: str | None
  required: False
  description: Название АЗС последнего использования
transaction_timeout:
  type: TransactionTimeout | None
  required: False
  description: Таймаут транзакции
product:
  type: str | None
  required: False
  description: Тип продукта (limit/wallet)
carrier:
  type: str | None
  required: False
  description: Тип карты (Plastic/Virtual)
available:
  type: str | None
  required: False
  description: Доступный лимит или баланс
currency:
  type: str | None
  required: False
  description: Валюта
payment_of_tolls:
  type: str | None
  required: False
  description: Признак оплаты дорожных сборов
previous:
  type: str | None
  required: False
  description: ID предыдущей карты
next:
  type: str | None
  required: False
  description: ID следующей карты
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`
- `empty_str_to_none(v)`

### `CardDetailData`

CardDetailData(**kwargs: 'Any') -> 'None'

Сигнатура: `CardDetailData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество записей
result:
  type: list[CardDetail]
  required: True
  description: Список карт
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDetailResponse`

CardDetailResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `CardDetailResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа
data:
  type: CardDetailData
  required: True
  description: Основные данные
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriverInfo`

CardDriverInfo(**kwargs: 'Any') -> 'None'

Сигнатура: `CardDriverInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID пользователя/водителя
login:
  type: str
  required: True
  description: Логин (обычно телефон)
first_name:
  type: str
  required: True
  description: Имя водителя
last_name:
  type: str
  required: True
  description: Фамилия водителя
middle_name:
  type: str | None
  required: False
  description: Отчество водителя
date:
  type: str | None
  required: False
  description: Дата рождения или дата регистрации
position:
  type: str | None
  required: False
  description: Должность водителя
role:
  type: str | None
  required: False
  description: Роль пользователя
mobile_phone:
  type: str
  required: True
  description: Номер телефона
email:
  type: str | None
  required: False
  description: Email водителя
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriversData`

CardDriversData(**kwargs: 'Any') -> 'None'

Сигнатура: `CardDriversData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество водителей, связанных с картой
result:
  type: list[CardDriverInfo]
  required: True
  description: Список водителей
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriversResponse`

CardDriversResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `CardDriversResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус запроса
data:
  type: CardDriversData
  required: True
  description: Основные данные
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupData`

CardGroupData(**kwargs: 'Any') -> 'None'

Сигнатура: `CardGroupData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество карт в группе
result:
  type: list[CardGroupInfo]
  required: True
  description: Список карт в группе
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupInfo`

CardGroupInfo(**kwargs: 'Any') -> 'None'

Сигнатура: `CardGroupInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID карты
group:
  type: str
  required: True
  description: ID группы карт
contract_id:
  type: str
  required: True
  description: ID договора
number:
  type: str
  required: True
  description: Номер карты
status:
  type: str
  required: True
  description: Статус карты
comment:
  type: str | None
  required: False
  description: Комментарий
product:
  type: str | None
  required: False
  description: Тип продукта
payment_of_tolls:
  type: str | None
  required: False
  description: Оплата платных дорог ('Y' или 'N')
sync_group_state:
  type: str | None
  required: False
  description: Статус синхронизации группы
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupResponse`

CardGroupResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `CardGroupResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа
data:
  type: CardGroupData
  required: True
  description: Основные данные
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardInfo`

CardInfo(**kwargs: 'Any') -> 'None'

Сигнатура: `CardInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Уникальный идентификатор карты
contract_id:
  type: str
  required: True
  description: Идентификатор договора
number:
  type: str
  required: True
  description: Номер топливной карты
status:
  type: str
  required: True
  description: Статус карты (например, Active, Locked(Client))
can_work_offline:
  type: bool | None
  required: False
  description: Может ли карта работать офлайн
card_auth_type:
  type: str | None
  required: False
  description: Тип авторизации карты (например, PIN)
comment:
  type: str | None
  required: False
  description: Комментарий к карте
date_expired:
  type: datetime | None
  required: False
  description: Дата истечения срока действия карты
date_last_usage:
  type: datetime | None
  required: False
  description: Дата последнего использования карты
date_released:
  type: datetime | None
  required: False
  description: Дата выпуска карты
servicecenter_last_usage_name:
  type: str | None
  required: False
  description: Название последней АЗС, где использовалась карта
transaction_last_detail:
  type: str | None
  required: False
  description: Информация о последней транзакции
transaction_timeout:
  type: TransactionTimeout | None
  required: False
  description: Таймаут последней транзакции
product:
  type: str | None
  required: False
  description: Тип продукта (limit/wallet)
payment_of_tolls:
  type: str | None
  required: False
  description: Оплата платных дорог ('Y' или 'N')
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardV2Item`

Информация об одной топливной карте договора.

Сигнатура: `CardV2Item(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Уникальный идентификатор карты
group_id:
  type: str | None
  required: False
  description: ID группы карт, если назначена
group_name:
  type: str | None
  required: False
  description: Название группы карт
contract_id:
  type: str
  required: True
  description: ID договора, к которому принадлежит карта
contract_name:
  type: str
  required: True
  description: Название договора
number:
  type: str
  required: True
  description: Номер топливной карты
status:
  type: str
  required: True
  description: Системное значение статуса карты
status_name:
  type: str | None
  required: False
  description: Отображаемое имя статуса (например 'Активна')
comment:
  type: str | None
  required: False
  description: Комментарий, установленный пользователем
product:
  type: str
  required: True
  description: Тип продукта, например 'limit' или 'wallet'
product_name:
  type: str | None
  required: False
  description: Отображаемое имя продукта
carrier:
  type: str
  required: True
  description: Тип носителя карты ('Plastic' или 'Virtual Card')
carrier_name:
  type: str | None
  required: False
  description: Название типа носителя карты
platon:
  type: bool
  required: True
  description: Признак наличия поддержки Platon (оплата проезда)
avtodor:
  type: bool
  required: True
  description: Признак наличия поддержки Автодора
sync_group_state:
  type: str | None
  required: False
  description: Состояние синхронизации группы карт
users:
  type: list[str] | None
  required: False
  description: Список ID пользователей, привязанных к карте
mpc:
  type: bool | None
  required: False
  description: Признак наличия мультипроцессингового центра (mpc)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListData`

CardsListData(**kwargs: 'Any') -> 'None'

Сигнатура: `CardsListData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество найденных карт
result:
  type: list[CardInfo]
  required: True
  description: Список найденных карт
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListResponse`

CardsListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `CardsListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект со статусом ответа (например, {'code': 200})
data:
  type: CardsListData
  required: True
  description: Основные данные ответа
timestamp:
  type: int
  required: True
  description: Временная метка сервера (UNIX-timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListResponse`

CardsListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `CardsListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект со статусом ответа (например, {'code': 200})
data:
  type: CardsListData
  required: True
  description: Основные данные ответа
timestamp:
  type: int
  required: True
  description: Временная метка сервера (UNIX-timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsV2Data`

Основной объект данных для списка карт (v2).

Сигнатура: `CardsV2Data(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество найденных карт
result:
  type: list[CardV2Item]
  required: True
  description: Список карт договора
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsV2Response`

Ответ API метода GET /v2/cards.

Сигнатура: `CardsV2Response(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект статуса (например {'code': 200})
data:
  type: CardsV2Data
  required: True
  description: Основные данные (список карт)
timestamp:
  type: int
  required: True
  description: Метка времени ответа (Unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `IDListResponse`

IDListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `IDListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус запроса
data:
  type: list[str]
  required: True
  description: ID карт, которые были заблокированы/разблокированы
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionTimeout`

TransactionTimeout(**kwargs: 'Any') -> 'None'

Сигнатура: `TransactionTimeout(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
type:
  type: str | int
  required: True
  description: Тип таймаута ('H', 'N' или числовое значение)
value:
  type: str | int
  required: True
  description: Значение таймаута
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.contracts`

Описание отсутствует.

### `BalanceData`

Данные по расходу и балансу договора

Сигнатура: `BalanceData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
available_amount:
  type: str
  required: True
  description: Доступный остаток
own_balance:
  type: str
  required: True
  description: Собственные средства
balance:
  type: str
  required: True
  description: Собственные средства клиента с учетом блокировок
consumption_for_month:
  type: str
  required: True
  description: Расход в текущем месяце (в валюте контракта)
consumption_for_month_volume:
  type: str
  required: True
  description: Объем потребления в текущем месяце (в литрах)
consumption_for_prev_month_volume:
  type: str
  required: True
  description: Объем потребления в предыдущем месяце (в литрах)
last_payment_sum:
  type: str | None
  required: False
  description: Сумма последнего платежа
last_payment_date:
  type: str | None
  required: False
  description: Дата последнего платежа
currency:
  type: str
  required: True
  description: Валюта договора
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsData`

Информация по картам договора

Сигнатура: `CardsData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
cards_quantity_all:
  type: str
  required: True
  description: Число карт договора
cards_quantity_active:
  type: str
  required: True
  description: Число активных карт договора
card_groups_quantity_all:
  type: str | None
  required: False
  description: Число групп карт на договоре
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractData`

Основные данные договора

Сигнатура: `ContractData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
contract_id:
  type: str
  required: True
  description: ID договора
way_id:
  type: str
  required: True
  description: ID договора в процессинге
contract_number:
  type: str
  required: True
  description: Номер договора
unique_payment_id:
  type: str
  required: True
  description: Уникальный идентификатор платежа (УИП)
client:
  type: str
  required: True
  description: ID клиента
client_category:
  type: str
  required: True
  description: Категория клиента
contract_category:
  type: str
  required: True
  description: Категория договора
country:
  type: str
  required: True
  description: Страна заключения
region:
  type: str
  required: True
  description: Регион заключения
fin_institution:
  type: str
  required: True
  description: Финансовый институт
invoice_scheme:
  type: str
  required: True
  description: Подключение инвойсирования
invoice_period:
  type: str | None
  required: False
  description: Дни выставления счетов
invoice_pmt_delay:
  type: str | None
  required: False
  description: Количество дней на оплату инвойса
contract_status:
  type: str
  required: True
  description: ID статуса договора
contract_status_name:
  type: str
  required: True
  description: Значение статуса договора
pay_scheme:
  type: str
  required: True
  description: Условия оплаты
discount_scheme:
  type: str
  required: True
  description: Схема расчета скидки (код из справочника DiscountScheme)
auto_pay:
  type: str
  required: True
  description: Признак разрешения для подключения автосписания с р/с
auto_pay_type:
  type: str
  required: True
  description: Тип подключения автоматического платежа
credit_limit:
  type: str | None
  required: False
  description: Кредитный лимит
current_amount_limiter:
  type: str
  required: True
  description: Накопленная сумма по контракту
balance_amount_limiter:
  type: str | None
  required: False
  description: Доступная сумма по контракту (max – current)
max_amount_limiter:
  type: str | None
  required: False
  description: Ограничение лимита на сумму договора
date_open:
  type: str
  required: True
  description: Дата заключения договора
effective_date:
  type: str
  required: True
  description: Дата вступления в силу
end_date:
  type: str
  required: True
  description: Дата окончания
date_expire:
  type: str
  required: True
  description: Дата закрытия
product_type:
  type: bool
  required: True
  description: Признак универсального топливного продукта (false – старый продукт, true – УТП)
type_code:
  type: str
  required: True
  description: Тип договора
supplier_name:
  type: str
  required: True
  description: Имя поставщика
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractResponse`

Полный ответ API по договору

Сигнатура: `ContractResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
mpc:
  type: bool
  required: True
  description: Разрешен ли выпуск виртуальных карт
template_id:
  type: str
  required: True
  description: ID шаблона виртуальных карт
status:
  type: str
  required: True
  description: Статус Way4
status_crm:
  type: str
  required: True
  description: Статус CRM
payment_term_id:
  type: str | None
  required: False
  description: ID справочника условия оплаты
payment_scheme_id:
  type: str | None
  required: False
  description: ID справочника схема оплаты
is_dealer:
  type: bool
  required: True
  description: Признак дилерский
balanceData:
  type: BalanceData
  required: True
  description: Данные по расходу и балансу договора
contractData:
  type: ContractData
  required: True
  description: Данные договора
managerData:
  type: ManagerData | None
  required: False
  description: Данные по менеджеру договора
cardsData:
  type: CardsData
  required: True
  description: Данные по количеству карт и групп карт на договоре
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentItem`

Информация об одном первичном документе.

Сигнатура: `DocumentItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Уникальный идентификатор документа (UUID)
name:
  type: str
  required: True
  description: Название документа, например 'УПД'
name_doc:
  type: str
  required: True
  description: Системное имя документа, например 'СчетФактураВыданный'
number:
  type: str
  required: True
  description: Номер документа, например 'CSC0000000533998'
date:
  type: int
  required: True
  description: Дата документа в формате UNIX timestamp
total:
  type: float
  required: True
  description: Общая сумма документа
vat:
  type: float
  required: True
  description: Сумма НДС
sum:
  type: float
  required: True
  description: Сумма без НДС
currency:
  type: str
  required: True
  description: Валюта документа, например 'руб.'
consignee:
  type: str
  required: True
  description: Грузополучатель (организация)
contract_id:
  type: str
  required: True
  description: ID договора, к которому относится документ
contract_name:
  type: str
  required: True
  description: Номер или название договора
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsData`

Секция 'data' в ответе метода /documents.

Сигнатура: `DocumentsData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество найденных документов
result:
  type: list[DocumentItem]
  required: True
  description: Список найденных документов
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsOrderResponse`

Ответ метода POST /v2/documents (заказ документов).

Сигнатура: `DocumentsOrderResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект статуса, например {'code': 200}
data:
  type: bool
  required: True
  description: Признак успешной отправки (true — заказ выполнен)
timestamp:
  type: int
  required: True
  description: Метка времени ответа (Unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsResponse`

Ответ метода GET /v2/documents.

Сигнатура: `DocumentsResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект статуса, например {'code': 200}
data:
  type: DocumentsData
  required: True
  description: Основные данные — список документов
timestamp:
  type: int
  required: True
  description: Метка времени ответа (Unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoiceItem`

Информация об одном счёте на оплату.

Сигнатура: `InvoiceItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Уникальный идентификатор счёта
contract_id:
  type: str
  required: True
  description: ID договора, к которому относится счёт
ref_number:
  type: str
  required: True
  description: Номер счёта, указанный в системе
date_start:
  type: str
  required: True
  description: Дата начала периода счёта (YYYY-MM-DD)
date_end:
  type: str
  required: True
  description: Дата окончания периода счёта (YYYY-MM-DD)
last_update:
  type: str
  required: True
  description: Дата и время последнего обновления счёта (ISO формат)
currency:
  type: str
  required: True
  description: Код валюты, например '810'
amount:
  type: str
  required: True
  description: Сумма счёта
paid_amount:
  type: str
  required: True
  description: Оплаченная сумма
status:
  type: str
  required: True
  description: Статус счёта, например 'OPEN' или 'PAID'
comment:
  type: str
  required: True
  description: Комментарий к счёту, например 'Intermediate Invoice'
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoiceOrderResponse`

Ответ метода POST /v2/invoice.

Сигнатура: `InvoiceOrderResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект статуса, например {'code': 200}
data:
  type: bool
  required: True
  description: Признак успешного создания счёта
timestamp:
  type: int
  required: True
  description: Метка времени ответа (Unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoicesData`

Секция 'data' в ответе списка счетов.

Сигнатура: `InvoicesData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество найденных счетов
result:
  type: list[InvoiceItem]
  required: True
  description: Список счетов на оплату
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoicesResponse`

Ответ метода GET /v2/invoices.

Сигнатура: `InvoicesResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект статуса, например {'code': 200}
data:
  type: InvoicesData
  required: True
  description: Основные данные — список счетов
timestamp:
  type: int
  required: True
  description: Метка времени ответа (Unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ManagerData`

Данные менеджера по сопровождению договора

Сигнатура: `ManagerData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
email:
  type: str
  required: True
  description: Email менеджера
first_name:
  type: str
  required: True
  description: Имя менеджера
last_name:
  type: str
  required: True
  description: Фамилия менеджера
middle_name:
  type: str | None
  required: False
  description: Отчество менеджера
work_phone:
  type: str | None
  required: False
  description: Рабочий телефон менеджера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `OrderCardsResponse`

Ответ метода POST /v2/orderCards.

Сигнатура: `OrderCardsResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект статуса, например {'code': 200}
data:
  type: bool
  required: True
  description: Результат операции: true — заказ выполнен успешно
timestamp:
  type: int
  required: True
  description: Метка времени ответа (Unix timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentItem`

Информация об одном платеже по договору.

Сигнатура: `PaymentItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор платежа
contract_id:
  type: str
  required: True
  description: ID договора, к которому относится платёж
date:
  type: str
  required: True
  description: Дата и время платежа в формате ISO 8601 (например, 2015-04-15T15:25:20)
amount:
  type: str
  required: True
  description: Сумма платежа в валюте договора
currency:
  type: str
  required: True
  description: Код валюты и её обозначение, например '810;RUR'
amount_client:
  type: str
  required: True
  description: Сумма, поступившая клиенту
description:
  type: str
  required: True
  description: Описание или назначение платежа
payment_name:
  type: str
  required: True
  description: Наименование типа платежа, например 'Payment To Client Contract'
payment_type:
  type: str
  required: True
  description: Тип платежа, например 'P;Advice'
payment_number:
  type: str
  required: True
  description: Номер платёжного документа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentsData`

Секция data из ответа API, содержит список платежей и их количество.

Сигнатура: `PaymentsData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество найденных платежей
result:
  type: list[PaymentItem]
  required: True
  description: Список платежей по договору
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentsResponse`

Основная модель ответа метода /getPayments.

Сигнатура: `PaymentsResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Объект с кодом статуса ответа сервера, например {'code': 200}
data:
  type: PaymentsData
  required: True
  description: Основная часть ответа с данными о платежах
timestamp:
  type: int
  required: True
  description: Метка времени ответа сервера в формате Unix timestamp
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.dictionaries`

Описание отсутствует.

### `AddressV1`

Адрес торговой точки

Сигнатура: `AddressV1(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
track_id:
  type: str | None
  required: False
  description: Номер трассы, если применимо
kmRoad:
  type: str | None
  required: False
  description: Километр трассы
roadSide:
  type: str | None
  required: False
  description: Сторона дороги
city:
  type: str | None
  required: False
  description: Город
street:
  type: str | None
  required: False
  description: Улица
house:
  type: str | None
  required: False
  description: Дом
building:
  type: str | None
  required: False
  description: Строение
phone:
  type: str | None
  required: False
  description: Телефон торговой точки
fax:
  type: str | None
  required: False
  description: Факс
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AddressV2`

Адрес торговой точки

Сигнатура: `AddressV2(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
track_id:
  type: str | None
  required: False
  description: Номер трассы
kmRoad:
  type: str | None
  required: False
  description: Километр трассы
roadSide:
  type: str | None
  required: False
  description: Сторона дороги
city:
  type: str | None
  required: False
  description: Город
street:
  type: str | None
  required: False
  description: Улица
house:
  type: str | None
  required: False
  description: Дом
building:
  type: str | None
  required: False
  description: Строение
phone:
  type: str | None
  required: False
  description: Телефон
fax:
  type: str | None
  required: False
  description: Факс
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFilterItem`

Описание фильтра торговых точек

Сигнатура: `AzsFilterItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
filter:
  type: str | None
  required: False
  description: Ключ фильтра (например: services_with_card, countries и т.д.)
name:
  type: str | None
  required: False
  description: Название фильтра (человекочитаемое)
values:
  type: dict[str, AzsFilterValue] | None
  required: False
  description: Список значений для данного фильтра
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFilterValue`

Отдельное значение фильтра

Сигнатура: `AzsFilterValue(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
name:
  type: str | None
  required: False
  description: Название значения фильтра
code:
  type: str | None
  required: False
  description: Код значения фильтра
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFiltersResponse`

Ответ метода /azs/filters

Сигнатура: `AzsFiltersResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус выполнения запроса
data:
  type: list[AzsFilterItem] | None
  required: False
  description: Список доступных фильтров торговых точек
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsItemV1`

Информация о торговой точке (v1)

Сигнатура: `AzsItemV1(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str | None
  required: False
  description: ID торговой точки (АЗС)
siebelId:
  type: str | None
  required: False
  description: ID торговой точки в CRM
contractNumber:
  type: str | None
  required: False
  description: Код торговой точки (договор)
contractName:
  type: str | None
  required: False
  description: Название торговой точки
status:
  type: str | None
  required: False
  description: Статус точки (257 – работает, 258 – не работает)
countryCode:
  type: str | None
  required: False
  description: Код страны
regionCode:
  type: str | None
  required: False
  description: Код региона
secessionGPN:
  type: str | None
  required: False
  description: Отделение ГПН по географии
belongsTo:
  type: str | None
  required: False
  description: Название владельца или оператора
partner:
  type: str | None
  required: False
  description: ID партнера
ownType:
  type: str | None
  required: False
  description: Тип собственности (Own / FRAN и др.)
locationType:
  type: str | None
  required: False
  description: Тип расположения (ROAD и т.д.)
brand:
  type: str | None
  required: False
  description: Бренд торговой точки
openDate:
  type: str | None
  required: False
  description: Дата открытия точки
closeDate:
  type: str | None
  required: False
  description: Дата закрытия (если закрыта)
latitude:
  type: str | None
  required: False
  description: Координата широты
longitude:
  type: str | None
  required: False
  description: Координата долготы
type:
  type: str | None
  required: False
  description: Тип торговой точки (АЗС, СТО и т.д.)
timeZone:
  type: str | None
  required: False
  description: Часовой пояс точки
services:
  type: list[int] | None
  required: False
  description: Массив ID услуг
terminals:
  type: list[TerminalV1] | None
  required: False
  description: Список терминалов торговой точки
address:
  type: AddressV1 | None
  required: False
  description: Адрес торговой точки
prices:
  type: list[PriceItemV1] | None
  required: False
  description: Цены товаров на точке
searchTxt:
  type: str | None
  required: False
  description: Строка поиска
phone:
  type: str | None
  required: False
  description: Контактный телефон
height_post:
  type: str | None
  required: False
  description: Высота поста (в метрах)
working_time:
  type: list[WorkingTimeV1] | None
  required: False
  description: Режим работы
only_virtual_card:
  type: bool | None
  required: False
  description: Принимаются ли только виртуальные карты
accept_cards:
  type: bool | None
  required: False
  description: Принимаются ли карты
hidden_on_map:
  type: bool | None
  required: False
  description: Скрыта ли точка на карте
active:
  type: bool | None
  required: False
  description: Активна ли торговая точка
POIType:
  type: str | None
  required: False
  description: Тип торговой точки (POI-код)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsItemV2`

Информация о торговой точке (АЗС)

Сигнатура: `AzsItemV2(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID торговой точки
siebel_id:
  type: str
  required: True
  description: Идентификатор Siebel
status:
  type: str | None
  required: False
  description: Статус торговой точки (257 – работает, 258 – не работает)
full_name:
  type: str | None
  required: False
  description: Полное наименование торговой точки
brand:
  type: str | None
  required: False
  description: Бренд
poi_type_name:
  type: str | None
  required: False
  description: Именование типа
poi_type_code:
  type: str | None
  required: False
  description: Код типа
own_type_name:
  type: str
  required: True
  description: Тип собственности (наименование)
own_type_code:
  type: str
  required: True
  description: Код типа собственности (по отношению к ГПН)
contract_name:
  type: str | None
  required: False
  description: Название договора
contract_number:
  type: str | None
  required: False
  description: Номер договора
phone:
  type: str | None
  required: False
  description: Телефон контактный
utc_timezone:
  type: str | None
  required: False
  description: UTC часовой пояс АЗС (+5)
time_zone:
  type: str | None
  required: False
  description: Часовой пояс АЗС относительно Москвы
open_date:
  type: str | None
  required: False
  description: Дата открытия
close_date:
  type: str | None
  required: False
  description: Дата закрытия
last_update:
  type: str | None
  required: False
  description: Дата последнего обновления
height_post:
  type: str | None
  required: False
  description: Высота поста (в метрах)
country_name:
  type: str | None
  required: True
  description: Название страны
country_code:
  type: str | None
  required: True
  description: Код страны
region_name:
  type: str | None
  required: False
  description: Название региона
region_code:
  type: str | None
  required: False
  description: Код региона
address_full:
  type: str | None
  required: False
  description: Полный адрес торговой точки
location:
  type: Coordinates | None
  required: False
  description: Географические координаты
latitude:
  type: str | None
  required: False
  description: Широта
longitude:
  type: str | None
  required: False
  description: Долгота
location_type:
  type: str | None
  required: False
  description: Тип локации
secession_gpn:
  type: str | None
  required: False
  description: Отделение ГПН
partner:
  type: str | None
  required: False
  description: ID партнёра
belongs_to:
  type: str | None
  required: False
  description: Принадлежность
info:
  type: str | None
  required: False
  description: Дополнительная информация о точке
search_txt:
  type: str | None
  required: True
  description: Строка для запроса поиска
accept_cards:
  type: bool | None
  required: True
  description: Принимаются ли банковские карты
adblue:
  type: ServiceGroup | None
  required: False
  description: Услуги AdBlue
electric_charging_station:
  type: ServiceGroup | None
  required: False
  description: Электрозарядные станции
services_with_card:
  type: ServiceGroup | None
  required: False
  description: Услуги, доступные при оплате картой
services_without_card:
  type: ServiceGroup | None
  required: False
  description: Услуги, доступные без карты
prices:
  type: list[PriceItemV2] | None
  required: False
  description: Список товаров с указанием цен
payment_type:
  type: list[dict] | None
  required: False
  description: Доступные способы оплаты
terminals:
  type: list[TerminalV2] | None
  required: False
  description: Список терминалов
address:
  type: AddressV2 | None
  required: False
  description: Адрес торговой точки
working_time:
  type: list[WorkingTimeV2] | None
  required: False
  description: Расписание работы торговой точки
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`
- `fix_empty_service_groups(cls, v)`

### `AzsListV1Data`

Основные данные списка торговых точек (v1)

Сигнатура: `AzsListV1Data(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int | None
  required: False
  description: Количество найденных торговых точек
result:
  type: list[AzsItemV1] | None
  required: False
  description: Список торговых точек
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV1Response`

Ответ метода GET /vip/v1/AZS

Сигнатура: `AzsListV1Response(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус выполнения запроса
data:
  type: AzsListV1Data | None
  required: False
  description: Основные данные торговых точек (v1)
timestamp:
  type: int | None
  required: False
  description: Временная метка (UNIX-время запроса)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV2Data`

Данные списка торговых точек (v2)

Сигнатура: `AzsListV2Data(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество торговых точек
result:
  type: list[AzsItemV2]
  required: True
  description: Список торговых точек (АЗС)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV2Response`

Ответ метода получения списка торговых точек (v2)

Сигнатура: `AzsListV2Response(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: True
  description: Информация о статусе запроса
data:
  type: AzsListV2Data | None
  required: True
  description: Основные данные торговых точек
timestamp:
  type: int | None
  required: True
  description: Метка времени запроса
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `Coordinates`

Географические координаты торговой точки

Сигнатура: `Coordinates(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
type:
  type: str | None
  required: False
  description: Тип геоданных (обычно 'Point')
coordinates:
  type: list[float]
  required: False
  description: Координаты в формате [долгота, широта]
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryData`

Основные данные справочника

Сигнатура: `DictionaryData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int | None
  required: False
  description: Количество элементов в справочнике
result:
  type: list[DictionaryItem] | None
  required: False
  description: Список элементов справочника
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryItem`

Элемент справочника (универсальная модель)

Сигнатура: `DictionaryItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Уникальный идентификатор элемента справочника
code:
  type: str | None
  required: False
  description: Код элемента (например, код валюты)
value:
  type: str | None
  required: False
  description: Значение элемента (используется в старых справочниках)
name:
  type: str | None
  required: False
  description: Название элемента (используется в новых справочниках)
deleted:
  type: int | None
  required: False
  description: Признак удаления элемента (0 — активен)
last_update:
  type: str | None
  required: False
  description: Дата последнего обновления записи
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryResponse`

Ответ метода GET /vip/v1/getDictionary

Сигнатура: `DictionaryResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус выполнения запроса
data:
  type: DictionaryData | None
  required: False
  description: Основные данные справочника
timestamp:
  type: int | None
  required: False
  description: Временная метка (UNIX-время запроса)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PriceItemV1`

Цена товара на торговой точке

Сигнатура: `PriceItemV1(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
ID:
  type: str | None
  required: False
  description: Идентификатор записи цены
GasStationID:
  type: str | None
  required: False
  description: ID торговой точки (АЗС)
GoodsCode:
  type: str | None
  required: False
  description: Код товара (см. справочник GoodsCode)
Price:
  type: str | None
  required: False
  description: Цена товара
Currency:
  type: str | None
  required: False
  description: Валюта (код и наименование через ';')
DateTo:
  type: str | None
  required: False
  description: Дата окончания действия цены
DateFrom:
  type: str | None
  required: False
  description: Дата начала действия цены
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PriceItemV2`

Информация о цене товара на торговой точке

Сигнатура: `PriceItemV2(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
ID:
  type: str | None
  required: False
  description: Идентификатор цены
GasStationID:
  type: str | None
  required: False
  description: ID торговой точки (АЗС)
GoodsCode:
  type: str | None
  required: False
  description: Код товара (из справочника GoodsCode)
Price:
  type: str | None
  required: False
  description: Цена товара
Currency:
  type: str | None
  required: False
  description: Код валюты, например '810;RUR'
DateTo:
  type: str | None
  required: False
  description: Дата действия цены до
DateFrom:
  type: str | None
  required: False
  description: Дата начала действия цены
hex_color:
  type: str | None
  required: False
  description: HEX-код цвета товара (если указан)
name:
  type: str | None
  required: False
  description: Название товара
CurrencyName:
  type: str | None
  required: False
  description: Наименование валюты
sort:
  type: int | None
  required: False
  description: Порядковый номер отображения
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ServiceGroup`

Группа услуг, доступных на торговой точке

Сигнатура: `ServiceGroup(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
name:
  type: str | None
  required: False
  description: Наименование группы услуг
items:
  type: list[ServiceItem] | None
  required: False
  description: Список услуг, входящих в группу
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ServiceItem`

Описание отдельной услуги

Сигнатура: `ServiceItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
name:
  type: str | None
  required: False
  description: Наименование услуги
code:
  type: int | str | None
  required: False
  description: Код услуги (числовой или строковый)
sort:
  type: int | None
  required: False
  description: Порядок сортировки
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TerminalV1`

Терминал торговой точки

Сигнатура: `TerminalV1(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str | None
  required: False
  description: Идентификатор терминала
active:
  type: bool | None
  required: False
  description: Статус активности терминала (True — включен, False — выключен)
name:
  type: str | None
  required: False
  description: Наименование терминала
status:
  type: str | None
  required: False
  description: Статус терминала
type:
  type: str | None
  required: False
  description: Тип терминала
connectionType:
  type: str | None
  required: False
  description: Тип подключения терминала
number:
  type: str | None
  required: False
  description: Номер терминала
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TerminalV2`

Информация о терминале, установленном на торговой точке

Сигнатура: `TerminalV2(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str | None
  required: False
  description: Идентификатор терминала
active:
  type: bool | None
  required: False
  description: Активен ли терминал (true — включен)
name:
  type: str | None
  required: False
  description: Наименование терминала
status:
  type: str | None
  required: False
  description: Статус терминала
type:
  type: str | None
  required: False
  description: Тип терминала
connectionType:
  type: str | None
  required: False
  description: Тип подключения
number:
  type: str | None
  required: False
  description: Номер терминала
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `WorkingTimeV1`

Рабочее время торговой точки

Сигнатура: `WorkingTimeV1(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
Weekday:
  type: str | None
  required: False
  description: День недели или режим работы
StartWorkTime:
  type: str | None
  required: False
  description: Время открытия
FinishWorkTime:
  type: str | None
  required: False
  description: Время закрытия
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `WorkingTimeV2`

Расписание работы торговой точки

Сигнатура: `WorkingTimeV2(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
Weekday:
  type: str | None
  required: False
  description: День недели или режим работы (Monday, Everyday, Round-The-Clock)
StartWorkTime:
  type: str | None
  required: False
  description: Время открытия, формат HH:MM
FinishWorkTime:
  type: str | None
  required: False
  description: Время закрытия, формат HH:MM
Everyday:
  type: bool | None
  required: False
  description: Признак работы ежедневно
Round_The_Clock:
  type: bool | None
  required: False
  alias: Round-The-Clock
  description: Признак круглосуточного режима
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.ewallet`

Описание отсутствует.

### `MoveToCardResponse`

Ответ на запрос перевода денег с договора на карту-кошелёк (moveToCard).
Пример ответа:
{
    "status": {"code": 200},
    "data": true,
    "timestamp": 1596024392
}

Сигнатура: `MoveToCardResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: Status
  required: True
  description: Статус выполнения операции.
data:
  type: bool
  required: True
  description: Результат выполнения операции (true — успешно).
timestamp:
  type: int
  required: True
  description: Метка времени ответа (UNIX timestamp).
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MoveToContractResponse`

Ответ на запрос перевода денег с кошелька на договор (moveToContract).
Пример ответа:
{
    "status": {"code": 200},
    "data": true,
    "timestamp": 1596024392
}

Сигнатура: `MoveToContractResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: Status
  required: True
  description: Статус выполнения операции.
data:
  type: bool
  required: True
  description: Результат выполнения операции (true — успешно).
timestamp:
  type: int
  required: True
  description: Метка времени ответа (UNIX timestamp).
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardProductResponse`

Ответ на запрос изменения типа продукта карты (setCardProduct).
Пример ответа:
{
    "status": {"code": 200},
    "data": ["11148025"],
    "timestamp": 1596024392
}

Сигнатура: `SetCardProductResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: Status
  required: True
  description: Статус выполнения операции.
data:
  type: list[str]
  required: True
  description: Список идентификаторов карт, у которых изменён продукт.
timestamp:
  type: int
  required: True
  description: Метка времени ответа (UNIX timestamp).
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `Status`

Модель для статуса ответа API.

Сигнатура: `Status(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
code:
  type: int
  required: True
  description: Код HTTP-статуса ответа (например, 200).
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.final_prices`

Описание отсутствует.

### `CheckPurchaseRequest`

Параметры запроса для проверки покупки

Сигнатура: `CheckPurchaseRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
poi_id:
  type: str
  required: True
  description: ID точки продажи (АЗС)
goods:
  type: list[PurchaseGoodItem]
  required: True
  description: Список товаров для проверки возможности покупки
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CheckPurchaseResponse`

Ответ метода проверки возможности проведения транзакции

Сигнатура: `CheckPurchaseResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа API, например {'code': 200}
data:
  type: bool
  required: True
  description: Результат проверки — True, если покупка возможна
timestamp:
  type: int
  required: True
  description: Время ответа (UNIX timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPriceItem`

Информация о финальной цене товара на АЗС

Сигнатура: `FinalPriceItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
code:
  type: str
  required: True
  description: Код товарной позиции
price:
  type: float
  required: True
  description: Финальная цена товара (с учетом всех скидок и тарифов)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPricesData`

Основные данные о финальных ценах

Сигнатура: `FinalPricesData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество товарных позиций в ответе
goods:
  type: list[FinalPriceItem]
  required: True
  description: Список товарных позиций с рассчитанными финальными ценами
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPricesResponse`

Ответ метода получения финальных цен на АЗС

Сигнатура: `FinalPricesResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа API, например {'code': 200}
data:
  type: FinalPricesData
  required: True
  description: Основные данные ответа (цены)
timestamp:
  type: int
  required: True
  description: Время формирования ответа в формате UNIX
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PurchaseGoodItem`

Описание товарной позиции для проверки возможности покупки

Сигнатура: `PurchaseGoodItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
code:
  type: str
  required: True
  description: Код товара (SKU или PLU на АЗС)
quantity:
  type: float
  required: True
  description: Количество товара для покупки
price:
  type: float
  required: True
  description: Цена за единицу товара
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.invites`

Описание отсутствует.

### `InviteActionResult`

Результат действий с приглашениями (создание, продление, повторная отправка)

Сигнатура: `InviteActionResult(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID приглашения
url:
  type: str
  required: True
  description: Ссылка на приглашение
attempts:
  type: int | None
  required: False
  description: Количество попыток отправки
expired_at:
  type: int | None
  required: False
  description: Дата истечения срока действия ссылки (timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteBoolResponse`

Результат простых действий (удаление, продление и т.п.)

Сигнатура: `InviteBoolResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
data:
  type: bool
  required: True
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteCard`

Информация о карте, привязанной к приглашению

Сигнатура: `InviteCard(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
sid:
  type: str
  required: True
  description: ID карты (SID)
number:
  type: str
  required: True
  description: Номер карты
product:
  type: str
  required: True
  description: Тип продукта ('wallet' и т.п.)
comment:
  type: str | None
  required: False
  description: Комментарий к карте (например, имя водителя)
status:
  type: str | None
  required: False
  description: Технический статус карты
status_name:
  type: str | None
  required: False
  description: Отображаемое название статуса
contract_id:
  type: str | None
  required: False
  description: ID договора, к которому относится карта
contract_name:
  type: str | None
  required: False
  description: Номер договора
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteContract`

Информация о договоре, привязанном к приглашению

Сигнатура: `InviteContract(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
sid:
  type: str
  required: True
  description: ID договора
number:
  type: str
  required: True
  description: Номер договора
status:
  type: str | None
  required: False
  description: Технический статус договора
status_name:
  type: str | None
  required: False
  description: Название статуса
template_id:
  type: str | None
  required: False
  description: ID шаблона виртуальной карты, если есть
cards_count:
  type: int | None
  required: False
  description: Количество карт по договору
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteItem`

Элемент списка приглашений

Сигнатура: `InviteItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID приглашения
user_id:
  type: str | None
  required: False
  description: ID пользователя, если уже создан
url:
  type: str
  required: True
  description: Ссылка на регистрацию (уникальная, активна 3 дня)
status:
  type: str
  required: True
  description: Технический статус приглашения (Active, Finished и т.п.)
status_name:
  type: str
  required: True
  description: Отображаемое название статуса
role:
  type: str
  required: True
  description: Роль пользователя ('Driver', 'Admin' и т.п.)
role_name:
  type: str
  required: True
  description: Название роли
attempts:
  type: int | None
  required: False
  description: Количество отправок приглашения
cards:
  type: list[InviteCard] | None
  required: False
  description: Список карт, связанных с приглашением
initiator:
  type: str | None
  required: False
  description: Пользователь, создавший приглашение
contracts:
  type: list[InviteContract] | None
  required: False
  description: Список договоров, привязанных к приглашению
mobile:
  type: str | None
  required: False
  description: Номер телефона приглашенного
email:
  type: str | None
  required: False
  description: Email приглашенного
communication_type:
  type: str | None
  required: False
  description: Тип отправки ('sms', 'email' и т.п.)
sended_at:
  type: int | None
  required: False
  description: Время отправки (timestamp)
expired_at:
  type: int | None
  required: False
  description: Время истечения срока действия ссылки (timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteList`

Ответ на запрос списка приглашений

Сигнатура: `InviteList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество приглашений
result:
  type: list[InviteItem]
  required: True
  description: Список приглашений
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteResponse`

Обертка для InviteActionResult

Сигнатура: `InviteResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
data:
  type: InviteActionResult
  required: True
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.limits`

Описание отсутствует.

### `LimitAmount`

Объёмный лимит (например, литры).

Сигнатура: `LimitAmount(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
value:
  type: float
  required: True
  description: Установленное значение лимита
used:
  type: float | None
  required: False
  description: Использованное значение лимита
unit:
  type: str
  required: True
  description: Единица измерения (например, 'LIT' или 'RUB')
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitItem`

Продуктовый лимит (карта, группа или договор).

Сигнатура: `LimitItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str | None
  required: False
  description: ID лимита (для изменения — обязателен)
card_id:
  type: str | None
  required: False
  description: ID карты, если лимит задан для карты
group_id:
  type: str | None
  required: False
  description: ID группы карт, если лимит задан для группы
contract_id:
  type: str
  required: True
  description: ID договора, к которому относится лимит
productGroup:
  type: str | None
  required: False
  description: ID группы продуктов
productType:
  type: str | None
  required: False
  description: ID типа продукта
amount:
  type: LimitAmount | None
  required: False
  description: Ограничение по объёму (литры и т.д.)
sum:
  type: LimitSum | None
  required: False
  description: Ограничение по сумме в валюте договора
term:
  type: LimitTerm | None
  required: False
  description: Периодичность и временные ограничения
transactions:
  type: LimitTransactions | None
  required: False
  description: Ограничения по количеству транзакций
time:
  type: LimitTime | None
  required: False
  description: Периодичность сброса лимита
date:
  type: str | None
  required: False
  description: Дата создания лимита (формат dd/mm/yyyy hh:mm:ss)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitSum`

Денежный лимит.

Сигнатура: `LimitSum(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
currency:
  type: str
  required: True
  description: Код валюты (например, 810)
value:
  type: float
  required: True
  description: Сумма лимита
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTerm`

Периодичность и временные ограничения.

Сигнатура: `LimitTerm(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
days:
  type: str | None
  required: False
  description: Дни недели (например, '1111100' для Пн–Пт)
type:
  type: int | None
  required: False
  description: Тип периода (1 — будни, 2 — ежедневно и т.д.)
time:
  type: LimitTermTime | None
  required: False
  description: Временной диапазон действия
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTermTime`

Временной диапазон действия лимита.

Сигнатура: `LimitTermTime(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
from_:
  type: str
  required: True
  alias: from
  description: Время начала действия лимита (HH:MM)
to:
  type: str
  required: True
  description: Время окончания действия лимита (HH:MM)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTime`

Периодичность сброса лимита.

Сигнатура: `LimitTime(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
number:
  type: int | None
  required: False
  description: Период в числовом виде (например, 3)
type:
  type: int | None
  required: False
  description: Тип периода (например, 7 — неделя)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTransactions`

Ограничения по количеству транзакций.

Сигнатура: `LimitTransactions(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
count:
  type: int | None
  required: False
  description: Максимальное количество транзакций
occured:
  type: int | None
  required: False
  description: Фактическое количество транзакций
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitsData`

Данные по лимитам.

Сигнатура: `LimitsData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество лимитов
result:
  type: list[LimitItem]
  required: True
  description: Список лимитов
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitsResponse`

Ответ на запрос списка лимитов.

Сигнатура: `LimitsResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения (например, {'code': 200})
data:
  type: LimitsData
  required: True
  description: Данные с лимитами
timestamp:
  type: int
  required: True
  description: Временная метка ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveLimitResponse`

Ответ на удаление продуктового лимита.

Сигнатура: `RemoveLimitResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса
data:
  type: bool
  required: True
  description: Результат операции (True — успешно)
timestamp:
  type: int
  required: True
  description: Временная метка ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetLimitResponse`

Ответ на установку/изменение продуктового лимита.

Сигнатура: `SetLimitResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса
data:
  type: list[str]
  required: True
  description: ID созданных/обновлённых лимитов
timestamp:
  type: int
  required: True
  description: Временная метка ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.region_limits`

Описание отсутствует.

### `RegionLimit`

Региональный лимит по договору, карте или группе карт.

Сигнатура: `RegionLimit(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str | None
  required: True
  description: ID регионального лимита
contract_id:
  type: str
  required: True
  description: ID договора, к которому относится лимит
card_id:
  type: str | None
  required: False
  description: ID карты, если лимит задан для карты
group_id:
  type: str | None
  required: False
  description: ID группы карт, если лимит задан для группы
country:
  type: str
  required: True
  description: Код страны обслуживания, пример - RUS
region:
  type: str | None
  required: False
  description: Код регион обслуживания
service_center:
  type: str | None
  required: False
  description: ID АЗС
date:
  type: str | None
  required: False
  description: Дата последнего изменения
limit_type:
  type: int
  required: True
  description: Тип лимита
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RegionLimitList`

Коллекция региональных лимитов.

Сигнатура: `RegionLimitList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество лимитов
result:
  type: list[RegionLimit]
  required: True
  description: Данные с лимитами
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RegionLimitResponse`

Коллекция региональных лимитов.

Сигнатура: `RegionLimitResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа
data:
  type: RegionLimitList
  required: True
  description: Данные с лимитами
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveRegionLimit`

Удаление регионального лимита.

Сигнатура: `RemoveRegionLimit(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса
data:
  type: bool
  required: True
  description: Результат операции (True — успешно)
timestamp:
  type: int
  required: True
  description: Временная метка ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.reports`

Описание отсутствует.

### `ReportFileResponse`

Ответ при генерации файла отчета.

Сигнатура: `ReportFileResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
content:
  type: bytes | None
  required: False
  description: Бинарное содержимое файла (application/octet-stream)
format:
  type: str | None
  required: False
  description: Формат файла (pdf, xlsx, csv и т.д.)
filename:
  type: str | None
  required: False
  description: Имя файла отчета
size:
  type: int | None
  required: False
  description: Размер файла в байтах
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportItem`

Описание доступного отчета (v2).

Сигнатура: `ReportItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор отчета
name:
  type: str
  required: True
  description: Название отчета
formats:
  type: list[str]
  required: True
  description: Список поддерживаемых форматов (pdf, xlsx, csv и т.д.)
parameters:
  type: list[ReportParameter]
  required: True
  description: Список параметров отчета
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportJobItem`

Элемент списка заказанных отчетов.

Сигнатура: `ReportJobItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
date:
  type: str
  required: True
  description: Дата создания заказа отчета
client_id:
  type: str | None
  required: False
  description: ID клиента
user_id:
  type: str | None
  required: False
  description: ID пользователя
contract_id:
  type: str | None
  required: False
  description: ID договора
contract_name:
  type: str | None
  required: False
  description: Название договора
job_id:
  type: str
  required: True
  description: Идентификатор задания (Job ID)
report_name:
  type: str
  required: True
  description: Название отчета
report_format:
  type: str
  required: True
  description: Формат отчета (pdf, xlsx и т.д.)
available_after:
  type: int | None
  required: False
  description: Количество секунд до доступности отчета
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportJobList`

Ответ со списком заказанных отчетов (v1/v2).

Сигнатура: `ReportJobList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int | None
  required: False
  description: Количество найденных отчетов
result:
  type: list[ReportJobItem]
  required: True
  description: Список заказанных отчетов
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportList`

Ответ метода /v2/reports — список доступных отчетов.

Сигнатура: `ReportList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество доступных отчетов
result:
  type: list[ReportItem]
  required: True
  description: Массив отчетов
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderParams`

Параметры заказа отчета.

Сигнатура: `ReportOrderParams(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
start_date:
  type: str | None
  required: False
  description: Дата начала периода
end_date:
  type: str | None
  required: False
  description: Дата окончания периода
id_agreement:
  type: str | None
  required: False
  description: Список ID договоров
id_card:
  type: list[str] | None
  required: False
  description: Список карт
card_group_code:
  type: list[str] | None
  required: False
  description: Список групп карт
id_client:
  type: list[str] | None
  required: False
  description: Список клиентов
additional:
  type: dict | None
  required: False
  description: Дополнительные параметры
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderRequest`

Тело запроса для заказа отчета (v2).

Сигнатура: `ReportOrderRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор отчета
format:
  type: str
  required: True
  description: Формат отчета (pdf, xlsx и т.д.)
emails:
  type: str | None
  required: False
  description: Email-адреса для отправки отчета
params:
  type: ReportOrderParams
  required: True
  description: Параметры отчета
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderResponse`

Ответ на заказ отчета (v2).

Сигнатура: `ReportOrderResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
job_id:
  type: list[str]
  required: True
  description: Идентификаторы созданных заданий на генерацию отчета
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportParameter`

Параметр отчета (например, дата, карта, договор).

Сигнатура: `ReportParameter(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
name:
  type: str
  required: True
  description: Имя параметра, используемое в запросах
value:
  type: Any | None
  required: False
  description: Значение параметра
label:
  type: str | None
  required: False
  description: Отображаемое название параметра
default_value:
  type: str | None
  required: False
  description: Значение по умолчанию
menu_values:
  type: list[ReportParameterMenuValue] | None
  required: False
  description: Список возможных значений для выбора из меню
type:
  type: str | None
  required: False
  description: Тип параметра (например, date, Contract, Group)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportParameterMenuValue`

Значения меню для параметра отчета.

Сигнатура: `ReportParameterMenuValue(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
labels:
  type: str | None
  required: False
  description: Отображаемое имя пункта меню
values:
  type: str | None
  required: False
  description: Значение пункта меню
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1JobItem`

Элемент списка ранее заказанных отчетов (v1).

Сигнатура: `ReportV1JobItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
date:
  type: str
  required: True
  description: Дата создания отчета
client_id:
  type: str | None
  required: False
  description: ID клиента
user_id:
  type: str | None
  required: False
  description: ID пользователя
contract_id:
  type: str | None
  required: False
  description: ID договора
job_id:
  type: str
  required: True
  description: Идентификатор задания (Job ID)
report_name:
  type: str
  required: True
  description: Название отчета
report_format:
  type: str
  required: True
  description: Формат отчета (pdf, xlsx, xml и т.д.)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1JobList`

Список заказанных отчетов (v1).

Сигнатура: `ReportV1JobList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
jobs:
  type: list[ReportV1JobItem]
  required: True
  description: Массив заказанных отчетов
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1OrderResponse`

Ответ для v1 метода /reports.

Сигнатура: `ReportV1OrderResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
report_ids:
  type: list[str]
  required: True
  description: ID заказанных отчетов
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.restrictions`

Описание отсутствует.

### `RestrictionGetResponse`

Ответ на запрос списка ограничителей (GET /restriction).

Сигнатура: `RestrictionGetResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
data:
  type: RestrictionList
  required: True
  description: Данные с ограничителями
timestamp:
  type: int
  required: True
  description: Временная метка ответа (Unix time)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionItem`

Модель одного товарного ограничителя (ограничение по продукту).

Сигнатура: `RestrictionItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID ограничителя
card_id:
  type: str | None
  required: False
  description: ID карты, если ограничитель задан для карты
group_id:
  type: str | None
  required: False
  description: ID группы карт, если ограничитель задан для группы
contract_id:
  type: str
  required: True
  description: ID договора
productType:
  type: str | None
  required: False
  description: ID типа продукта (например, '1-CK231')
productGroup:
  type: str | None
  required: False
  description: ID группы продуктов (если применимо)
productTypeName:
  type: str | None
  required: False
  description: Название типа продукта
productGroupName:
  type: str | None
  required: False
  description: Название группы продуктов
restriction_type:
  type: int
  required: True
  description: Тип ограничения (1 – Разрешающий ограничитель, 2 – Запрещающий ограничитель)
date:
  type: str | None
  required: False
  description: Дата установки ограничителя (в формате MM/DD/YYYY HH:mm:ss)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionList`

Список товарных ограничителей.

Сигнатура: `RestrictionList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество ограничителей
result:
  type: list[RestrictionItem]
  required: True
  description: Список ограничителей
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionRemoveResponse`

Ответ на удаление ограничителя (POST /removeRestriction).

Сигнатура: `RestrictionRemoveResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения (например, {'code': 200})
data:
  type: bool
  required: True
  description: Результат операции (True — успешно)
timestamp:
  type: int
  required: False
  description: Временная метка ответа (Unix time)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionSetResponse`

Ответ на установку или изменение ограничителя (POST /setRestriction).

Сигнатура: `RestrictionSetResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
data:
  type: list[str]
  required: True
  description: Список ID созданных или изменённых ограничителей
timestamp:
  type: int
  required: True
  description: Временная метка ответа (Unix time)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.templates`

Описание отсутствует.

### `LimitAmount`

LimitAmount(**kwargs: 'Any') -> 'None'

Сигнатура: `LimitAmount(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
unit:
  type: str | None
  required: False
  description: Единица измерения (например, 'LIT')
value:
  type: float | None
  required: False
  description: Количество или объем в единицах измерения
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitSum`

LimitSum(**kwargs: 'Any') -> 'None'

Сигнатура: `LimitSum(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
currency:
  type: str | None
  required: False
  description: Код валюты (например, '810')
currencyName:
  type: str | None
  required: False
  description: Название валюты (например, 'р.')
value:
  type: float | None
  required: False
  description: Сумма лимита в указанной валюте
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTerm`

LimitTerm(**kwargs: 'Any') -> 'None'

Сигнатура: `LimitTerm(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
days:
  type: str | None
  required: False
  description: Маска дней действия лимита (например, '1111100')
type:
  type: int | None
  required: False
  description: Тип временного ограничения
time:
  type: LimitTermTime | None
  required: False
  description: Временные границы лимита
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTermTime`

LimitTermTime(**kwargs: 'Any') -> 'None'

Сигнатура: `LimitTermTime(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
from_:
  type: str | None
  required: False
  alias: from
  description: Начало временного диапазона (например, '03:00')
to:
  type: str | None
  required: False
  description: Конец временного диапазона (например, '08:00')
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTime`

LimitTime(**kwargs: 'Any') -> 'None'

Сигнатура: `LimitTime(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
type:
  type: int | None
  required: False
  description: Тип периода лимита (например, 3 — день, 5 — месяц)
number:
  type: int | None
  required: False
  description: Количество единиц выбранного периода
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTransactions`

LimitTransactions(**kwargs: 'Any') -> 'None'

Сигнатура: `LimitTransactions(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
count:
  type: int | None
  required: False
  description: Количество транзакций, на которое распространяется лимит
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateCreateRequest`

TemplateCreateRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateCreateRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
contract_id:
  type: str
  required: True
  description: Идентификатор договора
type:
  type: str
  required: True
  description: Тип создаваемого шаблона (Limit или Wallet)
name:
  type: str
  required: True
  description: Имя (название) нового шаблона ВК
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateCreateResponse`

TemplateCreateResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateCreateResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: str
  required: True
  description: ID созданного шаблона
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateDeleteResponse`

TemplateDeleteResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateDeleteResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: bool
  required: True
  description: Результат операции (true — успешно, false — ошибка)
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestriction`

TemplateGeoRestriction(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateGeoRestriction(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор геоограничителя шаблона
template_id:
  type: str
  required: True
  description: Идентификатор шаблона
contract_id:
  type: str
  required: True
  description: Идентификатор договора
date:
  type: str | None
  required: False
  description: Дата создания записи
country:
  type: str | None
  required: False
  description: Код страны (например, 'RUS')
countryName:
  type: str | None
  required: False
  description: Название страны
region:
  type: str | None
  required: False
  description: Код региона
regionName:
  type: str | None
  required: False
  description: Название региона
partner:
  type: str | None
  required: False
  description: Код партнера (АЗС)
partnerName:
  type: str | None
  required: False
  description: Название партнера (АЗС)
service_center:
  type: str | None
  required: False
  description: Код сервисного центра
service_centerName:
  type: str | None
  required: False
  description: Название сервисного центра
restriction_type:
  type: int
  required: True
  description: Тип геоограничителя (1 — разрешение, 2 — запрет)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionCreateRequest`

TemplateGeoRestrictionCreateRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateGeoRestrictionCreateRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
contract_id:
  type: str
  required: True
  description: Идентификатор договора
country:
  type: str
  required: True
  description: Код страны (например, 'RUS')
region:
  type: str | None
  required: False
  description: Код региона (например, '45')
partner:
  type: str | None
  required: False
  description: Код партнера (АЗС)
service_center:
  type: str | None
  required: False
  description: Код сервисного центра
restriction_type:
  type: int
  required: True
  description: Тип геоограничителя (1 — разрешение, 2 — запрет)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionCreateResponse`

TemplateGeoRestrictionCreateResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateGeoRestrictionCreateResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: str
  required: True
  description: ID созданного геоограничителя шаблона
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionDeleteResponse`

TemplateGeoRestrictionDeleteResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateGeoRestrictionDeleteResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: bool
  required: True
  description: Результат удаления геоограничителя (true — успешно)
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionListData`

TemplateGeoRestrictionListData(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateGeoRestrictionListData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество найденных геоограничителей
result:
  type: list[TemplateGeoRestriction]
  required: True
  description: Список геоограничителей шаблона
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionListResponse`

TemplateGeoRestrictionListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateGeoRestrictionListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: TemplateGeoRestrictionListData
  required: True
  description: Основные данные списка геоограничителей
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateItem`

TemplateItem(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор шаблона ВК
name:
  type: str
  required: True
  description: Название шаблона ВК
type:
  type: str
  required: True
  description: Тип шаблона (Limit — лимитная, Wallet — электронная карта)
contract_id:
  type: str
  required: True
  description: Идентификатор договора, к которому относится шаблон
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimit`

TemplateLimit(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateLimit(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор лимита шаблона
template_id:
  type: str
  required: True
  description: Идентификатор шаблона, которому принадлежит лимит
contract_id:
  type: str
  required: True
  description: Идентификатор договора, на который распространяется лимит
amount:
  type: LimitAmount | None
  required: False
  description: Объемный лимит (в литрах и т.д.)
sum:
  type: LimitSum | None
  required: False
  description: Суммовой лимит (в рублях и т.д.)
time:
  type: LimitTime | None
  required: False
  description: Период действия лимита
term:
  type: LimitTerm | None
  required: False
  description: Дополнительные временные ограничения
transactions:
  type: LimitTransactions | None
  required: False
  description: Информация по транзакциям лимита
date:
  type: str | None
  required: False
  description: Дата создания лимита
productType:
  type: str | None
  required: False
  description: Тип продукта (топливо, услуга и т.д.)
productGroup:
  type: str | None
  required: False
  description: Группа продукта (например, G-95)
productTypeName:
  type: str | None
  required: False
  description: Название типа продукта
productGroupName:
  type: str | None
  required: False
  description: Название группы продукта
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitCreateRequest`

TemplateLimitCreateRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateLimitCreateRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
contract_id:
  type: str
  required: True
  description: Идентификатор договора
product_type:
  type: str
  required: True
  description: Тип продукта (например, '1-276PF01')
product_group:
  type: str | None
  required: False
  description: Группа продукта (например, '1-276PF0E')
sum:
  type: LimitSum | None
  required: False
  description: Суммовой лимит
amount:
  type: LimitAmount | None
  required: False
  description: Объемный лимит
time:
  type: LimitTime
  required: True
  description: Период лимита
term:
  type: LimitTerm | None
  required: False
  description: Дополнительные временные ограничения
create_restriction:
  type: bool | None
  required: False
  description: Создать ограничитель автоматически
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitCreateResponse`

TemplateLimitCreateResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateLimitCreateResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: str
  required: True
  description: ID созданного лимита шаблона
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitDeleteResponse`

TemplateLimitDeleteResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateLimitDeleteResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: bool
  required: True
  description: Результат удаления лимита (true — успешно)
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitListData`

TemplateLimitListData(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateLimitListData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество найденных лимитов
result:
  type: list[TemplateLimit]
  required: True
  description: Список лимитов шаблона
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitListResponse`

TemplateLimitListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateLimitListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: TemplateLimitListData
  required: True
  description: Основные данные списка лимитов
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestriction`

TemplateRestriction(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateRestriction(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: Идентификатор ограничителя шаблона
template_id:
  type: str
  required: True
  description: Идентификатор шаблона
contract_id:
  type: str
  required: True
  description: Идентификатор договора
date:
  type: str | None
  required: False
  description: Дата создания ограничителя
productType:
  type: str | None
  required: False
  description: Тип продукта
productGroup:
  type: str | None
  required: False
  description: Группа продукта
productTypeName:
  type: str | None
  required: False
  description: Название типа продукта
productGroupName:
  type: str | None
  required: False
  description: Название группы продукта
restriction_type:
  type: int
  required: True
  description: Тип ограничителя (1 — разрешение, 2 — запрет)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionCreateRequest`

TemplateRestrictionCreateRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateRestrictionCreateRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
contract_id:
  type: str
  required: True
  description: Идентификатор договора
product_type:
  type: str
  required: True
  description: Тип продукта (например, '1-276PF01')
product_group:
  type: str | None
  required: False
  description: Группа продукта (например, '1-276PF0E')
restriction_type:
  type: int
  required: True
  description: Тип ограничителя (1 — разрешение, 2 — запрет)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionCreateResponse`

TemplateRestrictionCreateResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateRestrictionCreateResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: str
  required: True
  description: ID созданного ограничителя шаблона
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionDeleteResponse`

TemplateRestrictionDeleteResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateRestrictionDeleteResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: bool
  required: True
  description: Результат удаления ограничителя
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionListData`

TemplateRestrictionListData(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateRestrictionListData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Количество найденных ограничителей
result:
  type: list[TemplateRestriction]
  required: True
  description: Список ограничителей шаблона
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionListResponse`

TemplateRestrictionListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplateRestrictionListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа
data:
  type: TemplateRestrictionListData
  required: True
  description: Основные данные списка ограничителей
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplatesListData`

TemplatesListData(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplatesListData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество найденных шаблонов
result:
  type: list[TemplateItem]
  required: True
  description: Список найденных шаблонов ВК
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplatesListResponse`

TemplatesListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `TemplatesListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict | None
  required: False
  description: Статус ответа (код, сообщение и т.д.)
data:
  type: TemplatesListData
  required: True
  description: Основные данные списка шаблонов
timestamp:
  type: int | None
  required: False
  description: Метка времени ответа (Unix)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.transactions`

Описание отсутствует.

### `RequestInfo`

Информация о типе и названии запроса.

Сигнатура: `RequestInfo(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
type:
  type: str
  required: True
  description: Тип операции (например, Advice)
name:
  type: str
  required: True
  description: Название операции (например, Покупка)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionDetailResponse`

Ответ метода получения детальной информации по транзакции (v2).

Сигнатура: `TransactionDetailResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа
data:
  type: TransactionsV2Data
  required: True
  description: Информация по одной транзакции
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionItem`

Позиция (товар) внутри транзакции.

Сигнатура: `TransactionItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID позиции транзакции
rrn:
  type: str
  required: True
  description: Уникальный номер RRN
product:
  type: str
  required: True
  description: Наименование продукта (топлива)
amount:
  type: str
  required: True
  description: Количество продукта
price:
  type: str
  required: True
  description: Цена за единицу
base_cost:
  type: str
  required: True
  description: Базовая стоимость
cost:
  type: str
  required: True
  description: Итоговая стоимость с учетом скидки
discount:
  type: str
  required: True
  description: Скидка по позиции
discount_cost:
  type: str
  required: True
  description: Стоимость с учётом скидки
transaction:
  type: str
  required: True
  description: ID транзакции
currency:
  type: str
  required: True
  description: Валюта
unit:
  type: str
  required: True
  description: Единица измерения
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionItemV2`

Позиция в транзакции (v2).

Для спорных полей здесь сознательно приоритет отдан примерам из спецификации
и реальным ответам DEMO-стенда, а не табличным типам, которые местами
противоречат самим же payload-примерам.

Сигнатура: `TransactionItemV2(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: int
  required: True
  description: ID транзакции
timestamp:
  type: datetime
  required: True
  description: Время транзакции (локальное)
utc_time:
  type: datetime | None
  required: False
  description: Время транзакции в UTC
card_id:
  type: str
  required: True
  description: ID карты
poi_id:
  type: str
  required: True
  description: ID точки продаж (АЗС)
terminal_id:
  type: str
  required: True
  description: ID терминала
type:
  type: str
  required: True
  description: Тип операции (P — покупка, R — возврат)
product_id:
  type: str
  required: True
  description: ID продукта
product_name:
  type: str | None
  required: False
  description: Наименование продукта
product_category_id:
  type: str
  required: True
  description: Категория продукта (например, НП)
currency:
  type: str
  required: True
  description: Код валюты (например, RUR)
check_id:
  type: int
  required: True
  description: Номер чека
stor_transaction_id:
  type: int
  required: True
  description: ID сторнируемой транзакции
is_storno:
  type: bool
  required: True
  description: Признак сторно
is_manual_corrention:
  type: bool
  required: True
  description: Признак ручной корректировки
qty:
  type: float
  required: True
  description: Количество
price:
  type: float
  required: True
  description: Цена за единицу
price_no_discount:
  type: float
  required: True
  description: Цена без скидки
sum:
  type: float
  required: True
  description: Сумма с учетом скидки
sum_no_discount:
  type: float
  required: True
  description: Сумма без скидки
discount:
  type: float
  required: True
  description: Размер скидки
exchange_rate:
  type: float
  required: True
  description: Курс обмена
card_number:
  type: str
  required: True
  description: Номер карты
payment_type:
  type: str
  required: True
  description: Тип оплаты (например, Карта)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionV1`

Транзакция для версии v1.

Сигнатура: `TransactionV1(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID транзакции
time:
  type: datetime
  required: True
  description: Дата и время транзакции
host_date:
  type: datetime
  required: True
  description: Дата и время на хосте
currency:
  type: str
  required: True
  description: Код валюты (например, 810)
card_id:
  type: str
  required: True
  description: ID карты
service_center:
  type: str
  required: True
  description: ID сервисного центра (АЗС)
card_number:
  type: str
  required: True
  description: Номер карты
base_cost:
  type: str
  required: True
  description: Базовая стоимость транзакции
cost:
  type: str
  required: True
  description: Фактическая стоимость с учётом скидок
discount:
  type: str
  required: True
  description: Размер скидки
discount_cost:
  type: str
  required: True
  description: Стоимость после применения скидки
incoming:
  type: bool
  required: True
  description: Признак входящей транзакции
request:
  type: RequestInfo
  required: True
  description: Информация о типе операции
transaction_items:
  type: list[TransactionItem]
  required: True
  description: Список товаров в транзакции
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV1Data`

TransactionsV1Data(**kwargs: 'Any') -> 'None'

Сигнатура: `TransactionsV1Data(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество транзакций
result:
  type: list[TransactionV1]
  required: True
  description: Список транзакций
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV1Response`

TransactionsV1Response(**kwargs: 'Any') -> 'None'

Сигнатура: `TransactionsV1Response(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа
data:
  type: TransactionsV1Data
  required: True
  description: Данные ответа
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV2Data`

TransactionsV2Data(**kwargs: 'Any') -> 'None'

Сигнатура: `TransactionsV2Data(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество транзакций
result:
  type: list[TransactionItemV2]
  required: True
  description: Список транзакций (v2)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV2Response`

TransactionsV2Response(**kwargs: 'Any') -> 'None'

Сигнатура: `TransactionsV2Response(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус ответа
data:
  type: TransactionsV2Data
  required: True
  description: Данные ответа
timestamp:
  type: int
  required: True
  description: Метка времени сервера
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.users`

Описание отсутствует.

### `UserAccess`

UserAccess(**kwargs: 'Any') -> 'None'

Сигнатура: `UserAccess(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
web:
  type: bool
  required: True
  description: Доступ через веб-интерфейс
api:
  type: bool
  required: True
  description: Доступ через API
mobile:
  type: bool
  required: True
  description: Доступ через мобильное приложение
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserBoolResponse`

UserBoolResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `UserBoolResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса
data:
  type: bool
  required: True
  description: Результат операции (true/false)
timestamp:
  type: int | None
  required: False
  description: Метка времени
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserCardItem`

UserCardItem(**kwargs: 'Any') -> 'None'

Сигнатура: `UserCardItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
sid:
  type: str
  required: True
  description: SID карты
number:
  type: str
  required: True
  description: Номер карты
mpc:
  type: bool
  required: True
  description: Признак мультикарты
product:
  type: str | None
  required: False
  description: Тип продукта карты (wallet, limit и т.д.)
comment:
  type: str | None
  required: False
  description: Комментарий к карте
status:
  type: str
  required: True
  description: Статус карты (Active, Blocked и т.п.)
contract_id:
  type: str
  required: True
  description: ID договора, к которому привязана карта
contract_name:
  type: str | None
  required: False
  description: Название договора
available:
  type: bool
  required: True
  description: Доступна ли карта пользователю
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserContractItem`

UserContractItem(**kwargs: 'Any') -> 'None'

Сигнатура: `UserContractItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
sid:
  type: str
  required: True
  description: ID договора
number:
  type: str
  required: True
  description: Номер договора
available:
  type: bool
  required: True
  description: Доступен ли договор пользователю
template_id:
  type: str | None
  required: False
  description: ID шаблона договора, если есть
cards_count:
  type: int | None
  required: False
  description: Количество карт по договору
status:
  type: UserStatus | None
  required: False
  description: Статус договора
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserCreateResponse`

UserCreateResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `UserCreateResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса
data:
  type: str
  required: True
  description: ID созданного пользователя
timestamp:
  type: int | None
  required: False
  description: Метка времени
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserItem`

UserItem(**kwargs: 'Any') -> 'None'

Сигнатура: `UserItem(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID пользователя в системе
login:
  type: str
  required: True
  description: Логин пользователя (обычно номер телефона)
first_name:
  type: str
  required: True
  description: Имя пользователя
last_name:
  type: str
  required: True
  description: Фамилия пользователя
middle_name:
  type: str | None
  required: False
  description: Отчество пользователя
date:
  type: str
  required: True
  description: Дата рождения
position:
  type: str | None
  required: False
  description: Должность или UUID должности
role:
  type: UserRole
  required: True
  description: Роль пользователя
active:
  type: bool
  required: True
  description: Активен ли пользователь
access:
  type: UserAccess
  required: True
  description: Информация о доступах пользователя
mobile_phone:
  type: str | None
  required: False
  description: Мобильный телефон пользователя
email:
  type: str | None
  required: False
  description: Email пользователя
contracts:
  type: list[UserContractItem]
  required: False
  description: Список договоров пользователя
cards:
  type: list[UserCardItem]
  required: False
  description: Список карт пользователя
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserList`

UserList(**kwargs: 'Any') -> 'None'

Сигнатура: `UserList(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
total_count:
  type: int
  required: True
  description: Общее количество пользователей
result:
  type: list[UserItem]
  required: True
  description: Список пользователей
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserListResponse`

UserListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `UserListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса (например {'code': 200})
data:
  type: UserList | None
  required: False
  description: Основные данные ответа
timestamp:
  type: int | None
  required: False
  description: Временная метка ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserRole`

UserRole(**kwargs: 'Any') -> 'None'

Сигнатура: `UserRole(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID роли пользователя (Driver, Manager и т.д.)
name:
  type: str
  required: True
  description: Название роли пользователя
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserStatus`

UserStatus(**kwargs: 'Any') -> 'None'

Сигнатура: `UserStatus(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID статуса договора, например Active
name:
  type: str
  required: True
  description: Название статуса договора, например Активен
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserListResponse`

UserListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `UserListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: dict
  required: True
  description: Статус выполнения запроса (например {'code': 200})
data:
  type: UserList | None
  required: False
  description: Основные данные ответа
timestamp:
  type: int | None
  required: False
  description: Временная метка ответа
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.virtual_cards`

Описание отсутствует.

### `ConfirmVirtualCardRequest`

ConfirmVirtualCardRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `ConfirmVirtualCardRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
card_id:
  type: str
  required: True
  description: ID виртуальной карты для подтверждения выпуска
code:
  type: str
  required: True
  description: Код подтверждения из СМС
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ConfirmVirtualCardResponse`

ConfirmVirtualCardResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `ConfirmVirtualCardResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус подтверждения выпуска
data:
  type: bool
  required: True
  description: Результат подтверждения (True — успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DeleteMPCResponse`

DeleteMPCResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `DeleteMPCResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус удаления мобильного профиля карты (МПК)
data:
  type: bool
  required: True
  description: Результат удаления (True — успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DeleteVirtualCardResponse`

DeleteVirtualCardResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `DeleteVirtualCardResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус удаления виртуальной карты
data:
  type: bool
  required: True
  description: Результат удаления карты (True — успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCActionResponse`

MPCActionResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `MPCActionResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус выполнения операции с МПК
data:
  type: bool
  required: True
  description: Результат выполнения операции (True — успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCListResponse`

MPCListResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `MPCListResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус получения списка МПК
data:
  type: Any
  required: True
  description: Список или контейнер с опубликованными МПК/QR
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCPayloadResponse`

MPCPayloadResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `MPCPayloadResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус выполнения операции с МПК
data:
  type: Any
  required: True
  description: Полезная нагрузка операции с МПК
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RerunVirtualCardReleaseRequest`

RerunVirtualCardReleaseRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `RerunVirtualCardReleaseRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
card_id:
  type: str
  required: True
  description: ID виртуальной карты для перезапуска выпуска
reason:
  type: str | None
  required: False
  description: Причина перезапуска выпуска (опционально)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RerunVirtualCardReleaseResponse`

RerunVirtualCardReleaseResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `RerunVirtualCardReleaseResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус перезапуска выпуска карты
data:
  type: VirtualCardData
  required: True
  description: Обновлённая информация о виртуальной карте
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResendSMSRequest`

ResendSMSRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `ResendSMSRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
card_id:
  type: str
  required: True
  description: ID виртуальной карты, для которой нужно повторно отправить СМС-код
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResendSMSResponse`

ResendSMSResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `ResendSMSResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус запроса на повторную отправку СМС-кода
data:
  type: bool
  required: True
  description: Результат операции (True — СМС отправлено успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResetMPCRequest`

ResetMPCRequest(**kwargs: 'Any') -> 'None'

Сигнатура: `ResetMPCRequest(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
type:
  type: str
  required: True
  description: Тип операции сброса ('ResetCounterCode' и т.п.)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResetMPCResponse`

ResetMPCResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `ResetMPCResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус выполнения операции сброса
data:
  type: bool
  required: True
  description: Результат операции (True — успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SimpleActionResponse`

SimpleActionResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `SimpleActionResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус выполнения операции
data:
  type: bool
  required: True
  description: Результат операции (True — успешно)
timestamp:
  type: int
  required: True
  description: Время выполнения запроса (Unix Timestamp)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `StatusModel`

StatusModel(**kwargs: 'Any') -> 'None'

Сигнатура: `StatusModel(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
code:
  type: int
  required: True
  description: Код статуса ответа (200 — успешно, иное — ошибка)
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `VirtualCardData`

VirtualCardData(**kwargs: 'Any') -> 'None'

Сигнатура: `VirtualCardData(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
id:
  type: str
  required: True
  description: ID виртуальной карты
number:
  type: str
  required: True
  description: Номер виртуальной карты
carrier:
  type: str
  required: True
  description: Тип носителя, обычно 'Virtual Card'
product:
  type: str
  required: True
  description: Тип продукта карты ('wallet' или 'limit')
status:
  type: str
  required: True
  description: Статус карты (например, 'Active', 'Blocked', 'Pending')
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `VirtualCardResponse`

VirtualCardResponse(**kwargs: 'Any') -> 'None'

Сигнатура: `VirtualCardResponse(**kwargs: 'Any') -> 'None'`

Описание полей:

```text
status:
  type: StatusModel
  required: True
  description: Статус ответа от сервера
data:
  type: VirtualCardData
  required: True
  description: Информация о выпущенной виртуальной карте
timestamp:
  type: int
  required: True
  description: Время ответа сервера в формате Unix Timestamp
```

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.registry`

Описание отсутствует.

### `MethodRegistry`

Описание отсутствует.

Сигнатура: `MethodRegistry(specs: 'dict[str, MethodSpec] | None' = None) -> 'None'`

Публичные методы:

- `find_by_endpoint(self, endpoint: 'str', version: 'str', http_method: 'str | None' = None) -> 'MethodSpec | None'`
- `get(self, name: 'str') -> 'MethodSpec'`
- `list_all(self) -> 'tuple[MethodSpec, ...]'`
- `list_domain(self, domain: 'str') -> 'tuple[MethodSpec, ...]'`
- `register(self, spec: 'MethodSpec') -> 'None'`

### `MethodSpec`

MethodSpec(name: 'str', domain: 'str', http_method: 'str', endpoint: 'str', supported_versions: 'tuple[str, ...]', default_version: 'str', demo_available: 'bool', idempotent: 'bool', timeout_class: 'str' = 'default', retry_class: 'str' = 'safe', route_variants: 'tuple[RouteVariant, ...]' = ())

Сигнатура: `MethodSpec(name: 'str', domain: 'str', http_method: 'str', endpoint: 'str', supported_versions: 'tuple[str, ...]', default_version: 'str', demo_available: 'bool', idempotent: 'bool', timeout_class: 'str' = 'default', retry_class: 'str' = 'safe', route_variants: 'tuple[RouteVariant, ...]' = ()) -> None`

Публичные методы:

- `iter_routes(self) -> 'tuple[RouteVariant, ...]'`
- `supports(self, version: 'str') -> 'bool'`

### `RouteVariant`

RouteVariant(http_method: 'str', endpoint: 'str', api_version: 'str', demo_available: 'bool')

Сигнатура: `RouteVariant(http_method: 'str', endpoint: 'str', api_version: 'str', demo_available: 'bool') -> None`

Публичные методы:

- `supports(self, version: 'str') -> 'bool'`

### `build_default_registry`

Описание отсутствует.

Сигнатура: `build_default_registry() -> 'MethodRegistry'`

## `api_client_opti24.services`

Описание отсутствует.

_Публичные классы и функции не обнаружены._

## `api_client_opti24.services.Invites`

Описание отсутствует.

### `InviteMixin`

Методы для работы с приглашениями пользователей (v2).
Invites – функционал регистрации пользователей.
Приглашение можно отправить по Email/SMS или получить уникальную ссылку и отправить удобным для вас способом.
Ссылка действует 3 календарных дня, повторно направить Email/SMS по одному приглашению можно не чаще 3х раз в день.
С помощью приглашения можно зарегистрировать, например, водителя и сразу привязать шаблон виртуальной карты,
либо привязать физические топливные карты.

Сигнатура: `InviteMixin()`

Публичные методы:

- `create_invite(self, *, data: dict[str, typing.Any], with_send: bool = True, api_version: str = 'v2') -> api_client_opti24.models.invites.InviteResponse`
- `delete_invite(self, *, invite_id: str, api_version: str = 'v2') -> api_client_opti24.models.invites.InviteBoolResponse`
- `get_invites(self, *, role: Optional[str] = None, user_id: Optional[str] = None, sort: Optional[str] = None, status: Optional[str] = None, q: Optional[str] = None, page: Optional[int] = None, on_page: Optional[int] = None, api_version: str = 'v2') -> api_client_opti24.models.invites.InviteList`
- `prolong_invite(self, *, invite_id: str, with_send: bool = True, api_version: str = 'v2') -> api_client_opti24.models.invites.InviteBoolResponse`
- `resend_invite(self, *, invite_id: str, api_version: str = 'v2') -> api_client_opti24.models.invites.InviteResponse`

## `api_client_opti24.services.auth`

Описание отсутствует.

### `AuthMixin`

Описание отсутствует.

Сигнатура: `AuthMixin()`

Публичные методы:

- `auth_user(self, *, api_version: str = 'v1', contract_id: str | None = None, contract_number: str | None = None) -> api_client_opti24.models.auth.AuthUserResponse`
- `get_info(self, api_version: str = 'v1', period: str | None = None) -> dict`
- `logoff(self, api_version: str = 'v1') -> dict`

## `api_client_opti24.services.card_group`

Описание отсутствует.

### `CardGroupsMixin`

Методы для работы с группами карт (v1).

Сигнатура: `CardGroupsMixin()`

Публичные методы:

- `get_card_groups(self, *, contract_id: str, api_version: str = 'v1') -> api_client_opti24.models.card_group.CardGroupListResponse`
- `remove_card_group(self, *, contract_id: str, group_id: str, api_version: str = 'v1') -> api_client_opti24.models.card_group.RemoveCardGroupResponse`
- `set_card_group(self, *, contract_id: str, name: str, group_id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.card_group.SetCardGroupResponse`
- `set_cards_to_group(self, *, contract_id: str, group_id: str, cards_list: list[dict], api_version: str = 'v1') -> api_client_opti24.models.card_group.SetCardsToGroupResponse`

## `api_client_opti24.services.cards`

Описание отсутствует.

### `CardsMixin`

Методы работы с топливными картами.

Сигнатура: `CardsMixin()`

Публичные методы:

- `block_card(self, contract_id: str, card_ids: list[str], block: bool = True, api_version: str = 'v1') -> api_client_opti24.models.cards.IDListResponse`
- `get_card_detail(self, contract_id: str, card_id: str, api_version: str = 'v1') -> api_client_opti24.models.cards.CardDetailResponse`
- `get_card_drivers(self, card_id: str, contract_id: str, api_version: str = 'v2') -> api_client_opti24.models.cards.CardDriversResponse`
- `get_cards_by_group(self, contract_id: str, group_id: str, api_version: str = 'v1') -> api_client_opti24.models.cards.CardGroupResponse`
- `get_cards_v1(self, contract_id: str, cache: bool = True, api_version: str = 'v1') -> api_client_opti24.models.cards.CardsListResponse`
- `get_cards_v2(self, contract_id: str | None = None, sort: str = '-id', q: str | None = None, status: str | None = None, carrier: str | None = None, platon: bool | None = None, avtodor: bool | None = None, users: bool | None = None, group_id: str | None = None, page: int = None, onpage: int = None, api_version: str = 'v2') -> api_client_opti24.models.cards.CardsV2Response`
- `reset_pin(self, card_id: str, contract_id: str, code: str, api_version: str = 'v2') -> api_client_opti24.models.cards.BoolResponse`
- `set_card_comment(self, card_id: str, contract_id: str, comment: str, api_version: str = 'v1') -> api_client_opti24.models.cards.BoolResponse`
- `verify_pin(self, card_id: str, contract_id: str, api_version: str = 'v2') -> api_client_opti24.models.cards.BoolResponse`

## `api_client_opti24.services.contract`

Описание отсутствует.

### `ContractMixin`

Описание отсутствует.

Сигнатура: `ContractMixin()`

Публичные методы:

- `get_contract_data(self, contract_id: str, api_version: str = 'v1') -> api_client_opti24.models.contracts.ContractResponse`
- `get_documents(self, date_start: str, date_end: str, api_version: str = 'v2', page: int = 1, on_page: int = 10) -> dict`
- `get_invoices(self, api_version: str = 'v2') -> dict`
- `get_payments(self, contract_id: str, api_version: str = 'v1') -> dict`
- `order_cards(self, count: int, office_id: str, api_version: str = 'v2') -> dict`
- `order_documents_email(self, ids: list[str], fmt: str, emails: list[str], api_version: str = 'v2') -> dict`
- `order_invoice(self, amount: float, email: str, api_version: str = 'v2') -> dict`

## `api_client_opti24.services.dictionaries`

Описание отсутствует.

### `DictionariesMixin`

Методы для работы со справочниками и торговыми точками

Сигнатура: `DictionariesMixin()`

Публичные методы:

- `get_azs_filters(self, *, api_version: str = 'v2') -> api_client_opti24.models.dictionaries.AzsFiltersResponse`
- `get_azs_list_v1(self, page: int = 1, onpage: int = 10, filter: Optional[dict] = None, id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.dictionaries.AzsListV1Response`
- `get_azs_list_v2(self, filter: Optional[dict] = None, q: Optional[str] = None, api_version: str = 'v2') -> api_client_opti24.models.dictionaries.AzsListV2Response`
- `get_dictionary(self, *, name: str, api_version: str = 'v1') -> api_client_opti24.models.dictionaries.DictionaryResponse`

## `api_client_opti24.services.ewallet`

Описание отсутствует.

### `EwalletMixin`

Методы для работы с электронными кошельками (Ewallet).

Электронный кошелёк — это тип карты, обслуживание которой производится не из средств договора,
а из отдельного кошелькового счёта. Пользователь может:
  • менять тип карты (лимитная ↔ электронный кошелёк);
  • переводить средства со счёта договора на кошелёк;
  • переводить средства обратно с кошелька на договор.

Сигнатура: `EwalletMixin()`

Публичные методы:

- `move_to_card(self, *, contract_id: str | None = None, card_id: str, amount: float, api_version: str = 'v1') -> api_client_opti24.models.ewallet.MoveToCardResponse`
- `move_to_contract(self, *, contract_id: str | None = None, card_id: str, amount: float, api_version: str = 'v1') -> api_client_opti24.models.ewallet.MoveToContractResponse`
- `set_card_product(self, *, contract_id: str | None = None, card_ids: list[str], product: str, api_version: str = 'v1') -> api_client_opti24.models.ewallet.SetCardProductResponse`

## `api_client_opti24.services.final_prices`

Описание отсутствует.

### `FinalPricesMixin`

Методы для получения финальных цен и проверки покупок по карте.

Сигнатура: `FinalPricesMixin()`

Публичные методы:

- `check_purchase(self, *, card_id: str, poi_id: str, goods: list[dict], api_version: str = 'v2') -> api_client_opti24.models.final_prices.CheckPurchaseResponse`
- `get_final_prices(self, *, card_id: str, poi_id: str, goods: list[str], api_version: str = 'v2') -> api_client_opti24.models.final_prices.FinalPricesResponse`

## `api_client_opti24.services.limits`

Описание отсутствует.

### `LimitsMixin`

Методы для работы с продуктовыми лимитами (v1).

Поддерживаются:
  • Получение списка лимитов (по договору, карте или группе)
  • Установка / изменение лимита
  • Удаление лимита

Сигнатура: `LimitsMixin()`

Публичные методы:

- `get_limits(self, *, contract_id: str, card_id: Optional[str] = None, group_id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.limits.LimitsResponse`
- `remove_limit(self, *, contract_id: str, limit_id: str, group_id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.limits.RemoveLimitResponse`
- `set_limit(self, *, limits: list[dict], api_version: str = 'v1') -> api_client_opti24.models.limits.SetLimitResponse`

## `api_client_opti24.services.region_limits`

Описание отсутствует.

### `RegionLimitsMixin`

Методы для работы с региональными лимитами (v1).

Сигнатура: `RegionLimitsMixin()`

Публичные методы:

- `get_region_limits(self, *, contract_id: str, card_id: Optional[str] = None, group_id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.region_limits.RegionLimitResponse`
- `remove_region_limit(self, *, contract_id: str, regionlimit_id: str, group_id: Optional[str] = None, api_version: str = 'v1') -> dict`
- `set_region_limit(self, *, region_limits: list[dict], api_version: str = 'v1') -> dict`

## `api_client_opti24.services.reports`

Описание отсутствует.

### `ReportsMixin`

Методы для работы с отчетами (v1 и v2)
Будет возвращен транзакционный отчет, относящийся к указанному договору.
Дата начала периода должна быть меньше или равна дате окончания периода.
В противном случае сервер автоматически выставит дату окончания периода равной дате начала.
Длина периода не должна превышать 3 календарных месяцев.
Если длина периода будет превышена, то он автоматически будет сокращен до 3 календарных месяцев с указанной даты начала периода.
Карты и группы карт, указанные в запросе, должны принадлежать указанному договору.
Ограничения отправки отчетов на Email составляет 15мб.
Длительность формирования отчетов за период 1 месяц составляет порядка 300 секунд, при выборе периода более 1 месяца, время формирования отчета может занять до 15 минут.
Теперь отчет можно заказать и скачать по ссылке. Заказ производится стандартным образом, только не нужно указывать email, иначе прийдет на email..

Сигнатура: `ReportsMixin()`

Публичные методы:

- `download_report_file(self, *, job_id: str, api_version: str = 'v2') -> bytes`
- `download_report_file_v1(self, *, job_id: str, archive: bool = False, api_version: str = 'v1') -> bytes`
- `get_report_job_list_v1(self, *, api_version: str = 'v1') -> api_client_opti24.models.reports.ReportV1JobList`
- `get_report_jobs(self, *, api_version: str = 'v2') -> api_client_opti24.models.reports.ReportJobList`
- `get_reports(self, *, api_version: str = 'v2') -> api_client_opti24.models.reports.ReportList`
- `order_report(self, *, report_id: str, format: str, params: dict, emails: Optional[str] = None, api_version: str = 'v2') -> api_client_opti24.models.reports.ReportOrderResponse`
- `order_report_v1(self, *, contract_id: str, start: str, end: str, report_format: str, email: str = None, cards_list: Optional[list[str]] = None, group_id: Optional[list[str]] = None, archive: bool = False, api_version: str = 'v1') -> api_client_opti24.models.reports.ReportV1OrderResponse`

## `api_client_opti24.services.restrictions`

Описание отсутствует.

### `RestrictionsMixin`

Методы для работы с товарными ограничителями (v1).

Сигнатура: `RestrictionsMixin()`

Публичные методы:

- `get_restrictions(self, *, contract_id: str, card_id: Optional[str] = None, group_id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.restrictions.RestrictionGetResponse`
- `remove_restriction(self, *, contract_id: str, restriction_id: str, group_id: Optional[str] = None, api_version: str = 'v1') -> api_client_opti24.models.restrictions.RestrictionRemoveResponse`
- `set_restriction(self, *, restrictions: list[dict], api_version: str = 'v1') -> api_client_opti24.models.restrictions.RestrictionSetResponse`

## `api_client_opti24.services.templates`

Описание отсутствует.

### `TemplatesMixin`

ВК – виртуальная карта. Чтобы выпустить ВК, потребуется создать шаблон лимита и прикрепить этот шаблон к пользователю.
Прикрепление происходит на этапе приглашения нового пользователя или методом для существующих пользователей.
Шаблон – это первоначальные параметры (Тип карты, Лимиты, Ограничители), с которыми будет выпущена эта ВК,
и все последующие, если использовать этот шаблон.
Шаблон сделан с точки зрения безопасности,
для того чтобы по-умолчанию все выпускаемые ВК имели ограничения на покупку (Лимит/Ограничитель).

Сигнатура: `TemplatesMixin()`

Публичные методы:

- `create_template(self, contract_id: str, type_: str, name: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateCreateResponse`
- `create_template_georestriction(self, template_id: str, payload: dict, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateGeoRestrictionCreateResponse`
- `create_template_limit(self, template_id: str, payload: dict, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateLimitCreateResponse`
- `create_template_restriction(self, template_id: str, payload: dict, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateRestrictionCreateResponse`
- `delete_template(self, template_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateDeleteResponse`
- `delete_template_georestriction(self, template_id: str, georestriction_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateGeoRestrictionDeleteResponse`
- `delete_template_limit(self, template_id: str, limit_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateLimitDeleteResponse`
- `delete_template_restriction(self, template_id: str, restriction_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateRestrictionDeleteResponse`
- `get_template_georestrictions(self, template_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateGeoRestrictionListResponse`
- `get_template_limits(self, template_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateLimitListResponse`
- `get_template_restrictions(self, template_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateRestrictionListResponse`
- `get_templates(self, contract_id: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplatesListResponse`
- `update_template(self, template_id: str, contract_id: str, type_: str, name: str, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateCreateResponse`
- `update_template_georestriction(self, template_id: str, georestriction_id: str, payload: dict, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateGeoRestrictionCreateResponse`
- `update_template_limit(self, *, template_id: str, limit_id: str, limits: list[dict], use_post: bool = True, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateLimitCreateResponse`
- `update_template_restriction(self, template_id: str, restriction_id: str, payload: dict, api_version: str = 'v2') -> api_client_opti24.models.templates.TemplateRestrictionCreateResponse`

## `api_client_opti24.services.transactions`

Описание отсутствует.

### `TransactionsMixin`

Методы для работы с транзакциями (v1 и v2).

Сигнатура: `TransactionsMixin()`

Публичные методы:

- `get_card_transactions_v2(self, *, card_id: str, contract_id: Optional[str] = None, date_from: str, date_to: str, page_limit: int = 100, page_offset: int = 0, api_version: str = 'v2', filter_fn: Optional[Callable[[api_client_opti24.models.transactions.TransactionItemV2], bool]] = None, sort_by: Optional[str] = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV2Response`
- `get_transaction_detail(self, *, transaction_id: str, contract_id: Optional[str] = None, api_version: str = 'v2') -> api_client_opti24.models.transactions.TransactionDetailResponse`
- `get_transactions_v1(self, *, contract_id: str, card_id: Optional[str] = None, count: int = 20, api_version: str = 'v1', filter_fn: Optional[Callable[[api_client_opti24.models.transactions.TransactionV1], bool]] = None, sort_by: Optional[str] = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV1Response`
- `get_transactions_v2(self, *, contract_id: str, date_from: str, date_to: str, page_limit: int = 100, page_offset: int = 0, api_version: str = 'v2', filter_fn: Optional[Callable[[api_client_opti24.models.transactions.TransactionItemV2], bool]] = None, sort_by: Optional[str] = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV2Response`

## `api_client_opti24.services.users`

Описание отсутствует.

### `UsersMixin`

Методы для работы с пользователями (v2).

Сигнатура: `UsersMixin()`

Публичные методы:

- `attach_card(self, *, user_id: str, card_id: str, api_version: str = 'v2') -> api_client_opti24.models.users.UserBoolResponse`
- `attach_contracts(self, *, user_id: str, contracts: list[dict], api_version: str = 'v2') -> api_client_opti24.models.users.UserBoolResponse`
- `create_user(self, *, uuid: str, mobile: str, api_version: str = 'v2') -> api_client_opti24.models.users.UserCreateResponse`
- `delete_user(self, *, user_id: str, api_version: str = 'v2') -> api_client_opti24.models.users.UserBoolResponse`
- `detach_card(self, *, user_id: str, card_id: str, api_version: str = 'v2') -> api_client_opti24.models.users.UserBoolResponse`
- `detach_contracts(self, *, user_id: str, contracts: list[str], api_version: str = 'v2') -> api_client_opti24.models.users.UserBoolResponse`
- `get_users(self, *, sort: str | None = None, page: int | None = None, on_page: int | None = None, q: str | None = None, filter: dict | None = None, api_version: str = 'v2') -> api_client_opti24.models.users.UserListResponse`

## `api_client_opti24.services.virtual_cards`

Описание отсутствует.

### `VirtualCardsMixin`

Методы для работы с виртуальными картами (ВК) и мобильными профилями карт (МПК)

Сигнатура: `VirtualCardsMixin()`

Публичные методы:

- `confirm_mpc(self, *, card_id: str, payload: dict[str, typing.Any] | None = None, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`
- `create_virtual_card(self, user_id: str, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.VirtualCardResponse`
- `delete_mpc(self, card_id: str, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.SimpleActionResponse`
- `generate_payment_qr(self, *, card_id: str, payload: dict[str, typing.Any] | None = None, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`
- `get_mpc_qr_list(self, *, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.MPCListResponse`
- `init_mpc(self, *, card_id: str, payload: dict[str, typing.Any] | None = None, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`
- `release_virtual_card(self, *, type_: str | None = None, template_id: str | None = None, user_id: str | None = None, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.VirtualCardResponse`
- `reset_mpc(self, card_id: str, type_: str, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.ResetMPCResponse`
- `update_mpc(self, *, card_id: str, payload: dict[str, typing.Any] | None = None, api_version: str = 'v2') -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`

## `api_client_opti24.session`

Описание отсутствует.

### `SessionManager`

Описание отсутствует.

Сигнатура: `SessionManager() -> 'None'`

Публичные методы:

- `ensure_authenticated(self, authenticate) -> 'str'`
- `invalidate(self) -> 'None'`
- `mark_authenticated(self, session_id: 'str', contract_id: 'str | None' = None) -> 'None'`
- `reset(self) -> 'None'`
- `set_contract(self, contract_id: 'str | None') -> 'None'`
- `snapshot(self) -> 'SessionSnapshot'`

### `SessionSnapshot`

SessionSnapshot(state: 'SessionState', session_id: 'str | None', contract_id: 'str | None')

Сигнатура: `SessionSnapshot(state: 'SessionState', session_id: 'str | None', contract_id: 'str | None') -> None`

### `SessionState`

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.

Сигнатура: `SessionState(*values)`

## `api_client_opti24.transport`

Описание отсутствует.

### `AsyncTransport`

Описание отсутствует.

Сигнатура: `AsyncTransport(base_url: 'str', client, default_timeout: 'float' = 30.0)`

Публичные методы:

- `aclose(self) -> 'None'`
- `request(self, method: 'str', endpoint: 'str', api_version: 'str' = 'v1', headers=None, retry_auth: 'bool' = True, timeout: 'float | None' = None, method_name: 'str | None' = None, **kwargs) -> 'Any'`
- `request_stream(self, method: 'str', url: 'str', headers=None, **kwargs) -> 'bytes'`

## `api_client_opti24.utils`

Описание отсутствует.

### `format_date_russian`

Описание отсутствует.

Сигнатура: `format_date_russian(date_str: str) -> str`

### `format_number`

Описание отсутствует.

Сигнатура: `format_number(number: float | int | None) -> str`

### `hash_password`

SHA-512 хэш пароля в нижнем регистре.

Сигнатура: `hash_password(password: str) -> str`

### `is_sensitive_log_key`

Описание отсутствует.

Сигнатура: `is_sensitive_log_key(key: str) -> bool`

### `message_mentions_sensitive_key`

Описание отсутствует.

Сигнатура: `message_mentions_sensitive_key(text: str) -> bool`

### `print_json`

Описание отсутствует.

Сигнатура: `print_json(data)`

### `sanitize_for_logging`

Описание отсутствует.

Сигнатура: `sanitize_for_logging(value: Any) -> Any`

### `scrub`

Описание отсутствует.

Сигнатура: `scrub(text: str) -> str`

### `to_json_param`

Описание отсутствует.

Сигнатура: `to_json_param(value: Any) -> str`

### `validate_month_span`

Проверка, что разница между датами не больше месяца.

Сигнатура: `validate_month_span(date_from: str, date_to: str)`

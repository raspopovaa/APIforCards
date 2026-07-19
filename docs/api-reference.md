# API Reference

Этот файл сгенерирован автоматически скриптом `scripts/generate_api_docs.py`.

Ниже собраны публичные модули, классы, функции и описание моделей SDK.

## `api_client_opti24`

Описание отсутствует.

_Публичные классы и функции не обнаружены._

## `api_client_opti24.authentication`

Описание отсутствует.

### `AuthenticationCoordinator`

Описание отсутствует.

Сигнатура: `AuthenticationCoordinator(session: 'SessionManager', authenticator: 'Authenticator') -> 'None'`

Публичные методы:

- `authenticate(self) -> 'AuthUserResponse'`
- `ensure_authenticated(self) -> 'str'`
- `recover(self) -> 'str'`

### `Authenticator`

Описание отсутствует.

Сигнатура: `Authenticator(*args, **kwargs)`

Публичные методы:

- `authenticate(self, *, api_version: 'str | None' = None, contract_id: 'str | None' = None, contract_number: 'str | None' = None) -> 'AuthUserResponse'`

### `DefaultAuthenticator`

Описание отсутствует.

Сигнатура: `DefaultAuthenticator(request_executor: 'RequestExecutor', session_mutator: 'SessionMutator', credentials_provider: 'CredentialsProvider', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `authenticate(self, *, api_version: 'str | None' = None, contract_id: 'str | None' = None, contract_number: 'str | None' = None) -> 'AuthUserResponse'`

## `api_client_opti24.client`

Описание отсутствует.

### `APIClient`

Описание отсутствует.

Сигнатура: `APIClient(base_url: str | None = None, api_key: str | None = None, login: str | None = None, password: str | None = None, *, settings: api_client_opti24.config.ConnectionSettings | api_client_opti24.config.APISettings | None = None, transport: api_client_opti24.executor.Transport | None = None, session_manager: api_client_opti24.session.SessionManager | None = None, registry: api_client_opti24.registry.MethodRegistry | None = None, logger: logging.Logger | None = None, clock: api_client_opti24.runtime.Clock | None = None, credentials_provider: api_client_opti24.service_base.CredentialsProvider | None = None, api_key_provider: api_client_opti24.service_base.APIKeyProvider | None = None) -> None`

Публичные методы:

- `aclose(self) -> None`

## `api_client_opti24.composition`

Описание отсутствует.

### `ClientRuntime`

ClientRuntime(authentication: 'AuthenticationCoordinator', request_executor: 'DefaultRequestExecutor', services: 'ServiceContainer')

Сигнатура: `ClientRuntime(authentication: 'AuthenticationCoordinator', request_executor: 'DefaultRequestExecutor', services: 'ServiceContainer') -> None`

### `compose_client_runtime`

Описание отсутствует.

Сигнатура: `compose_client_runtime(*, api_key_provider: 'APIKeyProvider', credentials_provider: 'CredentialsProvider', transport: 'Transport', session_manager: 'SessionManager', registry: 'MethodRegistry', timeouts: 'TimeoutPolicy', logger: 'LoggerLike', clock: 'Clock') -> 'ClientRuntime'`

## `api_client_opti24.config`

Описание отсутствует.

### `APISettings`

APISettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None), api_key: 'str', login: 'str | None' = None, password: 'str | None' = None)

Сигнатура: `APISettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None), api_key: 'str', login: 'str | None' = None, password: 'str | None' = None) -> None`

Публичные методы:

- `connection_settings(self) -> 'ConnectionSettings'`
- `from_env(*, load_dotenv: 'bool' = True, env_file: 'str | Path' = '.env') -> 'APISettings'`

### `ConnectionSettings`

ConnectionSettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None))

Сигнатура: `ConnectionSettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None)) -> None`

Публичные методы:

- `from_env(*, load_dotenv: 'bool' = True, env_file: 'str | Path' = '.env') -> 'ConnectionSettings'`

### `TimeoutPolicy`

TimeoutPolicy(default: 'float' = 30.0, auth: 'float' = 30.0, read_heavy: 'float' = 120.0)

Сигнатура: `TimeoutPolicy(default: 'float' = 30.0, auth: 'float' = 30.0, read_heavy: 'float' = 120.0) -> None`

Публичные методы:

- `resolve(self, timeout_class: 'str') -> 'float'`

## `api_client_opti24.contracts`

Описание отсутствует.

### `serialize_registry_contract`

Описание отсутствует.

Сигнатура: `serialize_registry_contract(registry: 'MethodRegistry') -> 'list[dict[str, object]]'`

## `api_client_opti24.credentials`

Описание отсутствует.

### `EnvironmentCredentialsProvider`

Описание отсутствует.

Сигнатура: `EnvironmentCredentialsProvider(*, api_key: 'str', login: 'str', password: 'str') -> 'None'`

Публичные методы:

- `from_env(*, load_dotenv: 'bool' = True, env_file: 'str | Path' = '.env') -> 'EnvironmentCredentialsProvider'`
- `get_api_key(self) -> 'str'`
- `get_credentials(self) -> 'tuple[str, str]'`

### `StaticAPIKeyProvider`

Описание отсутствует.

Сигнатура: `StaticAPIKeyProvider(api_key: 'str') -> 'None'`

Публичные методы:

- `get_api_key(self) -> 'str'`

### `StaticCredentialsProvider`

Описание отсутствует.

Сигнатура: `StaticCredentialsProvider(*, api_key: 'str', login: 'str', password: 'str') -> 'None'`

Публичные методы:

- `get_api_key(self) -> 'str'`
- `get_credentials(self) -> 'tuple[str, str]'`

### `StaticLoginPasswordProvider`

Описание отсутствует.

Сигнатура: `StaticLoginPasswordProvider(*, login: 'str', password: 'str') -> 'None'`

Публичные методы:

- `get_credentials(self) -> 'tuple[str, str]'`

## `api_client_opti24.decorators`

Описание отсутствует.

### `api_method`

Описание отсутствует.

Сигнатура: `api_method(func: collections.abc.Callable[typing.Concatenate[~ServiceT, ~Params], collections.abc.Awaitable[~ResultT]]) -> collections.abc.Callable[typing.Concatenate[~ServiceT, ~Params], collections.abc.Awaitable[~ResultT]]`

## `api_client_opti24.endpoints`

Описание отсутствует.

### `EndpointSpec`

EndpointSpec(name: 'str', domain: 'str', http_method: 'str', endpoint: 'str', supported_versions: 'tuple[str, ...]', default_version: 'str', demo_available: 'bool', idempotent: 'bool', requires_session: 'bool' = True, timeout_class: 'str' = 'default', retry_class: 'str' = 'safe', route_variants: 'tuple[RouteVariant, ...]' = (), external_code: 'str | None' = None, billable: 'bool | None' = None)

Сигнатура: `EndpointSpec(name: 'str', domain: 'str', http_method: 'str', endpoint: 'str', supported_versions: 'tuple[str, ...]', default_version: 'str', demo_available: 'bool', idempotent: 'bool', requires_session: 'bool' = True, timeout_class: 'str' = 'default', retry_class: 'str' = 'safe', route_variants: 'tuple[RouteVariant, ...]' = (), external_code: 'str | None' = None, billable: 'bool | None' = None) -> None`

Публичные методы:

- `iter_routes(self) -> 'tuple[RouteVariant, ...]'`
- `resolve_route(self, *, api_version: 'str | None' = None, route_name: 'str' = 'default') -> 'RouteVariant'`
- `supports(self, version: 'str') -> 'bool'`

### `RouteVariant`

RouteVariant(http_method: 'str', endpoint: 'str', api_version: 'str', demo_available: 'bool', name: 'str' = 'default', external_code: 'str | None' = None, billable: 'bool | None' = None)

Сигнатура: `RouteVariant(http_method: 'str', endpoint: 'str', api_version: 'str', demo_available: 'bool', name: 'str' = 'default', external_code: 'str | None' = None, billable: 'bool | None' = None) -> None`

Публичные методы:

- `render(self, path_params: 'PathParams | None' = None) -> 'str'`
- `supports(self, version: 'str') -> 'bool'`

### `endpoint`

Описание отсутствует.

Сигнатура: `endpoint(name: 'str', domain: 'str', http_method: 'str', path: 'str', version: 'str', *, demo: 'bool' = True, timeout: 'str' = 'default', retry: 'str | None' = None, requires_session: 'bool' = True, variants: 'tuple[RouteVariant, ...]' = (), external_code: 'str | None' = None, billable: 'bool | None' = None) -> 'EndpointSpec'`

### `route`

Описание отсутствует.

Сигнатура: `route(http_method: 'str', path: 'str', version: 'str', *, demo: 'bool', name: 'str', external_code: 'str | None' = None, billable: 'bool | None' = None) -> 'RouteVariant'`

## `api_client_opti24.env`

Описание отсутствует.

### `load_env_file`

Описание отсутствует.

Сигнатура: `load_env_file(path: 'str | Path' = '.env', *, override: 'bool' = False) -> 'None'`

## `api_client_opti24.errors`

Описание отсутствует.

### `APIError`

Описание отсутствует.

Сигнатура: `APIError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `AccessDeniedError`

Описание отсутствует.

Сигнатура: `AccessDeniedError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `DuplicateConflictError`

Описание отсутствует.

Сигнатура: `DuplicateConflictError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ErrorContext`

ErrorContext(http_status_code: 'int', api_status_code: 'int | None', error_type: 'str | None', messages: 'tuple[str, ...]', raw_payload: 'Any', endpoint: 'str | None', method_name: 'str | None', hint: 'str | None', retryable: 'bool')

Сигнатура: `ErrorContext(http_status_code: 'int', api_status_code: 'int | None', error_type: 'str | None', messages: 'tuple[str, ...]', raw_payload: 'Any', endpoint: 'str | None', method_name: 'str | None', hint: 'str | None', retryable: 'bool') -> None`

### `NotAuthenticatedError`

Описание отсутствует.

Сигнатура: `NotAuthenticatedError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `NotFoundError`

Описание отсутствует.

Сигнатура: `NotFoundError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `RateLimitError`

Описание отсутствует.

Сигнатура: `RateLimitError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ServerError`

Описание отсутствует.

Сигнатура: `ServerError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ValidationError`

Описание отсутствует.

Сигнатура: `ValidationError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `build_api_error`

Описание отсутствует.

Сигнатура: `build_api_error(*, status_code: 'int', body: 'Any', endpoint: 'str | None', method_name: 'str | None' = None, http_status_code: 'int | None' = None) -> 'APIError'`

## `api_client_opti24.executor`

Описание отсутствует.

### `DefaultRequestExecutor`

Описание отсутствует.

Сигнатура: `DefaultRequestExecutor(*, operation_executor: 'OperationExecutor', session_gate: 'SessionGate', session_recovery: 'SessionRecovery', registry: 'MethodRegistry', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `execute(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'JSONPayload'`
- `execute_stream(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'bytes'`
- `headers(self, include_session: 'bool' = False, content_type_json: 'bool' = False) -> 'dict[str, str]'`

### `OperationExecutor`

Описание отсутствует.

Сигнатура: `OperationExecutor(*, api_key_provider: 'APIKeyProvider', transport: 'Transport', session_context: 'SessionContext', registry: 'MethodRegistry', timeouts: 'TimeoutPolicy', logger: 'LoggerLike', clock: 'Clock') -> 'None'`

Публичные методы:

- `execute(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'JSONPayload'`
- `execute_stream(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'bytes'`
- `headers(self, include_session: 'bool' = False, content_type_json: 'bool' = False) -> 'dict[str, str]'`

### `Transport`

Описание отсутствует.

Сигнатура: `Transport(*args, **kwargs)`

Публичные методы:

- `aclose(self) -> 'None'`
- `request(self, method: 'str', endpoint: 'str', *, api_version: 'str' = 'v1', **kwargs: 'Any') -> 'DecodedPayload'`
- `request_stream(self, method: 'str', endpoint: 'str', *, api_version: 'str' = 'v1', headers: 'Mapping[str, str] | None' = None, **kwargs: 'Any') -> 'bytes'`

## `api_client_opti24.modeling`

Описание отсутствует.

### `BaseModel`

Описание отсутствует.

Сигнатура: `BaseModel(**extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `StrictRequestModel`

Описание отсутствует.

Сигнатура: `StrictRequestModel() -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `decode_model`

Описание отсутствует.

Сигнатура: `decode_model(model_type: 'type[ModelT]', payload: 'dict[str, Any]') -> 'ModelT'`

### `validator`

Описание отсутствует.

Сигнатура: `validator(*field_names: 'str', pre: 'bool' = False) -> 'Any'`

## `api_client_opti24.models`

Описание отсутствует.

_Публичные классы и функции не обнаружены._

## `api_client_opti24.models.auth`

Описание отсутствует.

### `AccessRights`

Описание отсутствует.

Сигнатура: `AccessRights(*, web: bool = False, api: bool = False, mobile: bool = False, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthError`

Описание отсутствует.

Сигнатура: `AuthError(*, code: str, message: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthErrorResponse`

Описание отсутствует.

Сигнатура: `AuthErrorResponse(*, error: api_client_opti24.models.auth.AuthError, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthUserData`

Описание отсутствует.

Сигнатура: `AuthUserData(*, client_id: str, client_status: str, org_name: str | None = None, session_id: str, user_id: str, contracts: list[api_client_opti24.models.auth.ContractInfo] = <factory>, role_id: str | None = None, role_name: str | None = None, read_only: bool = False, user_name: str | None = None, user_patronymic: str | None = None, user_surname: str | None = None, last_contract: str | None = None, access: api_client_opti24.models.auth.AccessRights | None = None, email: str | None = None, phone: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthUserResponse`

Описание отсутствует.

Сигнатура: `AuthUserResponse(*, status: api_client_opti24.models.auth.StatusResponse, data: api_client_opti24.models.auth.AuthUserData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ClientInfo`

Описание отсутствует.

Сигнатура: `ClientInfo(*, Client: str, ClientType: str, Contract: str, ContractName: str, PricePlan: str | None = None, Cost: float | None = None, Queries: int | None = None, Additional: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractInfo`

Описание отсутствует.

Сигнатура: `ContractInfo(*, id: str, number: str, mpc: bool = False, template_id: str | None = None, cards_count: int = 0, one_price: bool = False, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `GetInfoResponse`

Описание отсутствует.

Сигнатура: `GetInfoResponse(*, status: api_client_opti24.models.auth.StatusResponse, data: api_client_opti24.models.auth.InfoData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InfoData`

Описание отсутствует.

Сигнатура: `InfoData(*, from_: datetime.datetime, to: datetime.datetime, client_info: api_client_opti24.models.auth.ClientInfo, methods: api_client_opti24.models.auth.MethodsCount, methods_info: api_client_opti24.models.auth.MethodsInfo, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LogoffResponse`

Описание отсутствует.

Сигнатура: `LogoffResponse(*, status: api_client_opti24.models.auth.StatusResponse, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MethodsCount`

Описание отсутствует.

Сигнатура: `MethodsCount(*, all: int = 0, cards: int | None = 0, cardgroups: int | None = 0, card: int | None = 0, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MethodsInfo`

Описание отсутствует.

Сигнатура: `MethodsInfo(*, actions_bill: dict[str, str], actions_not_bill: dict[str, str], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `StatusResponse`

Описание отсутствует.

Сигнатура: `StatusResponse(*, code: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.card_group`

Описание отсутствует.

### `CardGroupItem`

Информация о группе карт.

Сигнатура: `CardGroupItem(*, id: str, name: str, cards_count: int, status: str, contract_id: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupListData`

Контейнер данных со списком групп карт.

Сигнатура: `CardGroupListData(*, total_count: int, result: list[api_client_opti24.models.card_group.CardGroupItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupListResponse`

Ответ метода получения списка групп карт.

Сигнатура: `CardGroupListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.card_group.CardGroupListData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveCardGroupResponse`

Ответ метода удаления группы карт.

Сигнатура: `RemoveCardGroupResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardGroupData`

Информация о созданной или изменённой группе.

Сигнатура: `SetCardGroupData(*, id: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardGroupResponse`

Ответ метода установки/изменения группы карт.

Сигнатура: `SetCardGroupResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.card_group.SetCardGroupData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardsToGroupResponse`

Ответ метода добавления карт в группу.

Сигнатура: `SetCardsToGroupResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.cards`

Описание отсутствует.

### `BoolResponse`

Описание отсутствует.

Сигнатура: `BoolResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDetail`

Описание отсутствует.

Сигнатура: `CardDetail(*, id: str, contract_id: str, number: str, status: str, can_work_offline: bool | None = None, card_auth_type: str | None = None, comment: str | None = None, date_last_usage: datetime.datetime | str | None = None, date_released: datetime.datetime | str | None = None, servicecenter_last_usage_name: str | None = None, transaction_timeout: api_client_opti24.models.cards.TransactionTimeout | None = None, product: str | None = None, carrier: str | None = None, available: str | None = None, currency: str | None = None, payment_of_tolls: str | None = None, previous: str | None = None, next: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`
- `empty_str_to_none(v: 'Any') -> 'Any'`

### `CardDetailData`

Описание отсутствует.

Сигнатура: `CardDetailData(*, total_count: int, result: list[api_client_opti24.models.cards.CardDetail], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDetailResponse`

Описание отсутствует.

Сигнатура: `CardDetailResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardDetailData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriverInfo`

Описание отсутствует.

Сигнатура: `CardDriverInfo(*, id: str, login: str, first_name: str, last_name: str, middle_name: str | None = None, date: str | None = None, position: str | None = None, role: str | None = None, mobile_phone: str, email: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriversData`

Описание отсутствует.

Сигнатура: `CardDriversData(*, total_count: int, result: list[api_client_opti24.models.cards.CardDriverInfo], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriversResponse`

Описание отсутствует.

Сигнатура: `CardDriversResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardDriversData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupData`

Описание отсутствует.

Сигнатура: `CardGroupData(*, total_count: int, result: list[api_client_opti24.models.cards.CardGroupInfo], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupInfo`

Описание отсутствует.

Сигнатура: `CardGroupInfo(*, id: str, group: str, contract_id: str, number: str, status: str, comment: str | None = None, product: str | None = None, payment_of_tolls: str | None = None, sync_group_state: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupResponse`

Описание отсутствует.

Сигнатура: `CardGroupResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardGroupData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardInfo`

Описание отсутствует.

Сигнатура: `CardInfo(*, id: str, contract_id: str, number: str, status: str, can_work_offline: bool | None = None, card_auth_type: str | None = None, comment: str | None = None, date_expired: datetime.datetime | None = None, date_last_usage: datetime.datetime | None = None, date_released: datetime.datetime | None = None, servicecenter_last_usage_name: str | None = None, transaction_last_detail: str | None = None, transaction_timeout: api_client_opti24.models.cards.TransactionTimeout | None = None, product: str | None = None, payment_of_tolls: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardV2Item`

Информация об одной топливной карте договора.

Сигнатура: `CardV2Item(*, id: str, group_id: str | None = None, group_name: str | None = None, contract_id: str, contract_name: str, number: str, status: str, status_name: str | None = None, comment: str | None = None, product: str, product_name: str | None = None, carrier: str, carrier_name: str | None = None, platon: bool, avtodor: bool, sync_group_state: str | None = None, users: list[str] | None = <factory>, mpc: bool | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListData`

Описание отсутствует.

Сигнатура: `CardsListData(*, total_count: int, result: list[api_client_opti24.models.cards.CardInfo], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListResponse`

Описание отсутствует.

Сигнатура: `CardsListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardsListData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListResponse`

Описание отсутствует.

Сигнатура: `CardsListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardsListData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsV2Data`

Основной объект данных для списка карт (v2).

Сигнатура: `CardsV2Data(*, total_count: int, result: list[api_client_opti24.models.cards.CardV2Item], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsV2Response`

Ответ API метода GET /v2/cards.

Сигнатура: `CardsV2Response(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardsV2Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `IDListResponse`

Описание отсутствует.

Сигнатура: `IDListResponse(*, status: dict[str, typing.Any], data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionTimeout`

Описание отсутствует.

Сигнатура: `TransactionTimeout(*, type: str | int, value: str | int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.contracts`

Описание отсутствует.

### `BalanceData`

Данные по расходу и балансу договора

Сигнатура: `BalanceData(*, available_amount: str, own_balance: str, balance: str, consumption_for_month: str, consumption_for_month_volume: str, consumption_for_prev_month_volume: str, last_payment_sum: str | None = None, last_payment_date: str | None = None, currency: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsData`

Информация по картам договора

Сигнатура: `CardsData(*, cards_quantity_all: str, cards_quantity_active: str, card_groups_quantity_all: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractData`

Основные данные договора

Сигнатура: `ContractData(*, contract_id: str, way_id: str, contract_number: str, unique_payment_id: str, client: str, client_category: str, contract_category: str, country: str, region: str, fin_institution: str, invoice_scheme: str, invoice_period: str | None = None, invoice_pmt_delay: str | None = None, contract_status: str, contract_status_name: str, pay_scheme: str, discount_scheme: str, auto_pay: str, auto_pay_type: str, credit_limit: str | None = None, current_amount_limiter: str, balance_amount_limiter: str | None = None, max_amount_limiter: str | None = None, date_open: str, effective_date: str, end_date: str, date_expire: str, product_type: bool, type_code: str, supplier_name: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractResponse`

Полный ответ API по договору

Сигнатура: `ContractResponse(*, mpc: bool, template_id: str, status: str, status_crm: str, payment_term_id: str | None = None, payment_scheme_id: str | None = None, is_dealer: bool, balanceData: api_client_opti24.models.contracts.BalanceData, contractData: api_client_opti24.models.contracts.ContractData, managerData: api_client_opti24.models.contracts.ManagerData | None = None, cardsData: api_client_opti24.models.contracts.CardsData, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentItem`

Информация об одном первичном документе.

Сигнатура: `DocumentItem(*, id: str, name: str, name_doc: str, number: str, date: int, total: float, vat: float, sum: float, currency: str, consignee: str, contract_id: str, contract_name: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsData`

Секция 'data' в ответе метода /documents.

Сигнатура: `DocumentsData(*, total_count: int, result: list[api_client_opti24.models.contracts.DocumentItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsOrderResponse`

Ответ метода POST /v2/documents (заказ документов).

Сигнатура: `DocumentsOrderResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsResponse`

Ответ метода GET /v2/documents.

Сигнатура: `DocumentsResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.contracts.DocumentsData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoiceItem`

Информация об одном счёте на оплату.

Сигнатура: `InvoiceItem(*, id: str, contract_id: str, ref_number: str, date_start: str, date_end: str, last_update: str, currency: str, amount: str, paid_amount: str, status: str, comment: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoiceOrderResponse`

Ответ метода POST /v2/invoice.

Сигнатура: `InvoiceOrderResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoicesData`

Секция 'data' в ответе списка счетов.

Сигнатура: `InvoicesData(*, total_count: int, result: list[api_client_opti24.models.contracts.InvoiceItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoicesResponse`

Ответ метода GET /v2/invoices.

Сигнатура: `InvoicesResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.contracts.InvoicesData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ManagerData`

Данные менеджера по сопровождению договора

Сигнатура: `ManagerData(*, email: str, first_name: str, last_name: str, middle_name: str | None = None, work_phone: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `OrderCardsResponse`

Ответ метода POST /v2/orderCards.

Сигнатура: `OrderCardsResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentItem`

Информация об одном платеже по договору.

Сигнатура: `PaymentItem(*, id: str, contract_id: str, date: str, amount: str, currency: str, amount_client: str, description: str, payment_name: str, payment_type: str, payment_number: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentsData`

Секция data из ответа API, содержит список платежей и их количество.

Сигнатура: `PaymentsData(*, total_count: int, result: list[api_client_opti24.models.contracts.PaymentItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentsResponse`

Основная модель ответа метода /getPayments.

Сигнатура: `PaymentsResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.contracts.PaymentsData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.dictionaries`

Описание отсутствует.

### `AddressV1`

Адрес торговой точки

Сигнатура: `AddressV1(*, track_id: str | None = None, kmRoad: str | None = None, roadSide: str | None = None, city: str | None = None, street: str | None = None, house: str | None = None, building: str | None = None, phone: str | None = None, fax: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AddressV2`

Адрес торговой точки

Сигнатура: `AddressV2(*, track_id: str | None = None, kmRoad: str | None = None, roadSide: str | None = None, city: str | None = None, street: str | None = None, house: str | None = None, building: str | None = None, phone: str | None = None, fax: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFilterItem`

Описание фильтра торговых точек

Сигнатура: `AzsFilterItem(*, filter: str | None = None, name: str | None = None, values: dict[str, api_client_opti24.models.dictionaries.AzsFilterValue] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFilterValue`

Отдельное значение фильтра

Сигнатура: `AzsFilterValue(*, name: str | None = None, code: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFiltersResponse`

Ответ метода /azs/filters

Сигнатура: `AzsFiltersResponse(*, status: dict[str, Any] | None = None, data: list[api_client_opti24.models.dictionaries.AzsFilterItem] | None = <factory>, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsItemV1`

Информация о торговой точке (v1)

Сигнатура: `AzsItemV1(*, id: str | None = None, siebelId: str | None = None, contractNumber: str | None = None, contractName: str | None = None, status: str | None = None, countryCode: str | None = None, regionCode: str | None = None, secessionGPN: str | None = None, belongsTo: str | None = None, partner: str | None = None, ownType: str | None = None, locationType: str | None = None, brand: str | None = None, openDate: str | None = None, closeDate: str | None = None, latitude: str | None = None, longitude: str | None = None, type: str | None = None, timeZone: str | None = None, services: list[int] | None = <factory>, terminals: list[api_client_opti24.models.dictionaries.TerminalV1] | None = <factory>, address: api_client_opti24.models.dictionaries.AddressV1 | None = None, prices: list[api_client_opti24.models.dictionaries.PriceItemV1] | None = <factory>, searchTxt: str | None = None, phone: str | None = None, height_post: str | None = None, working_time: list[api_client_opti24.models.dictionaries.WorkingTimeV1] | None = <factory>, only_virtual_card: bool | None = None, accept_cards: bool | None = None, hidden_on_map: bool | None = None, active: bool | None = None, POIType: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsItemV2`

Информация о торговой точке (АЗС)

Сигнатура: `AzsItemV2(*, id: str, siebel_id: str, status: str | None = None, full_name: str | None = None, brand: str | None = None, poi_type_name: str | None = None, poi_type_code: str | None = None, own_type_name: str, own_type_code: str, contract_name: str | None = None, contract_number: str | None = None, phone: str | None = None, utc_timezone: str | None = None, time_zone: str | None = None, open_date: str | None = None, close_date: str | None = None, last_update: str | None = None, height_post: str | None = None, country_name: str | None, country_code: str | None, region_name: str | None = None, region_code: str | None = None, address_full: str | None = None, location: api_client_opti24.models.dictionaries.Coordinates | None = None, latitude: str | None = None, longitude: str | None = None, location_type: str | None = None, secession_gpn: str | None = None, partner: str | None = None, belongs_to: str | None = None, info: str | None = None, search_txt: str | None, accept_cards: bool | None, adblue: api_client_opti24.models.dictionaries.ServiceGroup | None = None, electric_charging_station: api_client_opti24.models.dictionaries.ServiceGroup | None = None, services_with_card: api_client_opti24.models.dictionaries.ServiceGroup | None = None, services_without_card: api_client_opti24.models.dictionaries.ServiceGroup | None = None, prices: list[api_client_opti24.models.dictionaries.PriceItemV2] | None = <factory>, payment_type: list[dict[str, Any]] | None = <factory>, terminals: list[api_client_opti24.models.dictionaries.TerminalV2] | None = <factory>, address: api_client_opti24.models.dictionaries.AddressV2 | None = None, working_time: list[api_client_opti24.models.dictionaries.WorkingTimeV2] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`
- `fix_empty_service_groups(v: Any) -> Any`

### `AzsListV1Data`

Основные данные списка торговых точек (v1)

Сигнатура: `AzsListV1Data(*, total_count: int | None = None, result: list[api_client_opti24.models.dictionaries.AzsItemV1] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV1Response`

Ответ метода GET /vip/v1/AZS

Сигнатура: `AzsListV1Response(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.dictionaries.AzsListV1Data | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV2Data`

Данные списка торговых точек (v2)

Сигнатура: `AzsListV2Data(*, total_count: int, result: list[api_client_opti24.models.dictionaries.AzsItemV2], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV2Response`

Ответ метода получения списка торговых точек (v2)

Сигнатура: `AzsListV2Response(*, status: dict[str, Any] | None, data: api_client_opti24.models.dictionaries.AzsListV2Data | None, timestamp: int | None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `Coordinates`

Географические координаты торговой точки

Сигнатура: `Coordinates(*, type: str | None = None, coordinates: list[float] = <factory>, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryData`

Основные данные справочника

Сигнатура: `DictionaryData(*, total_count: int | None = None, result: list[api_client_opti24.models.dictionaries.DictionaryItem] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryItem`

Элемент справочника (универсальная модель)

Сигнатура: `DictionaryItem(*, id: str, code: str | None = None, value: str | None = None, name: str | None = None, deleted: int | None = 0, last_update: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryResponse`

Ответ метода GET /vip/v1/getDictionary

Сигнатура: `DictionaryResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.dictionaries.DictionaryData | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PriceItemV1`

Цена товара на торговой точке

Сигнатура: `PriceItemV1(*, ID: str | None = None, GasStationID: str | None = None, GoodsCode: str | None = None, Price: str | None = None, Currency: str | None = None, DateTo: str | None = None, DateFrom: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PriceItemV2`

Информация о цене товара на торговой точке

Сигнатура: `PriceItemV2(*, ID: str | None = None, GasStationID: str | None = None, GoodsCode: str | None = None, Price: str | None = None, Currency: str | None = None, DateTo: str | None = None, DateFrom: str | None = None, hex_color: str | None = None, name: str | None = None, CurrencyName: str | None = None, sort: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ServiceGroup`

Группа услуг, доступных на торговой точке

Сигнатура: `ServiceGroup(*, name: str | None = None, items: list[api_client_opti24.models.dictionaries.ServiceItem] | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ServiceItem`

Описание отдельной услуги

Сигнатура: `ServiceItem(*, name: str | None = None, code: int | str | None = None, sort: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TerminalV1`

Терминал торговой точки

Сигнатура: `TerminalV1(*, id: str | None = None, active: bool | None = None, name: str | None = None, status: str | None = None, type: str | None = None, connectionType: str | None = None, number: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TerminalV2`

Информация о терминале, установленном на торговой точке

Сигнатура: `TerminalV2(*, id: str | None = None, active: bool | None = None, name: str | None = None, status: str | None = None, type: str | None = None, connectionType: str | None = None, number: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `WorkingTimeV1`

Рабочее время торговой точки

Сигнатура: `WorkingTimeV1(*, Weekday: str | None = None, StartWorkTime: str | None = None, FinishWorkTime: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `WorkingTimeV2`

Расписание работы торговой точки

Сигнатура: `WorkingTimeV2(*, Weekday: str | None = None, StartWorkTime: str | None = None, FinishWorkTime: str | None = None, Everyday: bool | None = False, Round_The_Clock: bool | None = False, **extra_data: Any) -> None`

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

Сигнатура: `MoveToCardResponse(*, status: api_client_opti24.models.ewallet.Status, data: bool, timestamp: int, **extra_data: Any) -> None`

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

Сигнатура: `MoveToContractResponse(*, status: api_client_opti24.models.ewallet.Status, data: bool, timestamp: int, **extra_data: Any) -> None`

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

Сигнатура: `SetCardProductResponse(*, status: api_client_opti24.models.ewallet.Status, data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `Status`

Модель для статуса ответа API.

Сигнатура: `Status(*, code: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.final_prices`

Описание отсутствует.

### `CheckPurchaseRequest`

Параметры запроса для проверки покупки

Сигнатура: `CheckPurchaseRequest(*, poi_id: str, goods: list[api_client_opti24.models.final_prices.PurchaseGoodItem]) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `CheckPurchaseResponse`

Ответ метода проверки возможности проведения транзакции

Сигнатура: `CheckPurchaseResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPriceItem`

Информация о финальной цене товара на АЗС

Сигнатура: `FinalPriceItem(*, code: str, price: float, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPricesData`

Основные данные о финальных ценах

Сигнатура: `FinalPricesData(*, total_count: int, goods: list[api_client_opti24.models.final_prices.FinalPriceItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPricesResponse`

Ответ метода получения финальных цен на АЗС

Сигнатура: `FinalPricesResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.final_prices.FinalPricesData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `PurchaseGoodItem`

Описание товарной позиции для проверки возможности покупки

Сигнатура: `PurchaseGoodItem(*, code: str, quantity: float, price: float, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.invites`

Описание отсутствует.

### `InviteActionResult`

Результат действий с приглашениями (создание, продление, повторная отправка)

Сигнатура: `InviteActionResult(*, id: str, url: str, attempts: int | None = None, expired_at: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteBoolResponse`

Результат простых действий (удаление, продление и т.п.)

Сигнатура: `InviteBoolResponse(*, data: bool, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteCard`

Информация о карте, привязанной к приглашению

Сигнатура: `InviteCard(*, sid: str, number: str, product: str, comment: str | None = None, status: str | None = None, status_name: str | None = None, contract_id: str | None = None, contract_name: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteContract`

Информация о договоре, привязанном к приглашению

Сигнатура: `InviteContract(*, sid: str, number: str, status: str | None = None, status_name: str | None = None, template_id: str | None = None, cards_count: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteItem`

Элемент списка приглашений

Сигнатура: `InviteItem(*, id: str, user_id: str | None = None, url: str, status: str, status_name: str, role: str, role_name: str, attempts: int | None = None, cards: list[api_client_opti24.models.invites.InviteCard] | None = None, initiator: str | None = None, contracts: list[api_client_opti24.models.invites.InviteContract] | None = None, mobile: str | None = None, email: str | None = None, communication_type: str | None = None, sended_at: int | None = None, expired_at: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteList`

Ответ на запрос списка приглашений

Сигнатура: `InviteList(*, total_count: int, result: list[api_client_opti24.models.invites.InviteItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteResponse`

Обертка для InviteActionResult

Сигнатура: `InviteResponse(*, data: api_client_opti24.models.invites.InviteActionResult, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.limits`

Описание отсутствует.

### `LimitAmount`

Объёмный лимит (например, литры).

Сигнатура: `LimitAmount(*, value: float, used: float | None = None, unit: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitItem`

Продуктовый лимит (карта, группа или договор).

Сигнатура: `LimitItem(*, id: str | None = None, card_id: str | None = None, group_id: str | None = None, contract_id: str, productGroup: str | None = None, productType: str | None = None, amount: api_client_opti24.models.limits.LimitAmount | None = None, sum: api_client_opti24.models.limits.LimitSum | None = None, term: api_client_opti24.models.limits.LimitTerm | None = None, transactions: api_client_opti24.models.limits.LimitTransactions | None = None, time: api_client_opti24.models.limits.LimitTime | None = None, date: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitSum`

Денежный лимит.

Сигнатура: `LimitSum(*, currency: str, value: float, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTerm`

Периодичность и временные ограничения.

Сигнатура: `LimitTerm(*, days: str | None = None, type: int | None = None, time: api_client_opti24.models.limits.LimitTermTime | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTermTime`

Временной диапазон действия лимита.

Сигнатура: `LimitTermTime(*, from_: str, to: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTime`

Периодичность сброса лимита.

Сигнатура: `LimitTime(*, number: int | None = None, type: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTransactions`

Ограничения по количеству транзакций.

Сигнатура: `LimitTransactions(*, count: int | None = None, occured: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitsData`

Данные по лимитам.

Сигнатура: `LimitsData(*, total_count: int, result: list[api_client_opti24.models.limits.LimitItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitsResponse`

Ответ на запрос списка лимитов.

Сигнатура: `LimitsResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.limits.LimitsData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveLimitResponse`

Ответ на удаление продуктового лимита.

Сигнатура: `RemoveLimitResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SetLimitResponse`

Ответ на установку/изменение продуктового лимита.

Сигнатура: `SetLimitResponse(*, status: dict[str, typing.Any], data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.region_limits`

Описание отсутствует.

### `RegionLimit`

Региональный лимит по договору, карте или группе карт.

Сигнатура: `RegionLimit(*, id: str | None, contract_id: str, card_id: str | None = None, group_id: str | None = None, country: str, region: str | None = None, service_center: str | None = None, date: str | None = None, limit_type: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RegionLimitList`

Коллекция региональных лимитов.

Сигнатура: `RegionLimitList(*, total_count: int, result: list[api_client_opti24.models.region_limits.RegionLimit], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RegionLimitResponse`

Коллекция региональных лимитов.

Сигнатура: `RegionLimitResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.region_limits.RegionLimitList, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveRegionLimit`

Удаление регионального лимита.

Сигнатура: `RemoveRegionLimit(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.reports`

Описание отсутствует.

### `ReportFileResponse`

Ответ при генерации файла отчета.

Сигнатура: `ReportFileResponse(*, content: bytes | None = None, format: str | None = None, filename: str | None = None, size: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportItem`

Описание доступного отчета (v2).

Сигнатура: `ReportItem(*, id: str, name: str, formats: list[str], parameters: list[api_client_opti24.models.reports.ReportParameter], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportJobItem`

Элемент списка заказанных отчетов.

Сигнатура: `ReportJobItem(*, date: str, client_id: str | None = None, user_id: str | None = None, contract_id: str | None = None, contract_name: str | None = None, job_id: str, report_name: str, report_format: str, available_after: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportJobList`

Ответ со списком заказанных отчетов (v1/v2).

Сигнатура: `ReportJobList(*, total_count: int | None = None, result: list[api_client_opti24.models.reports.ReportJobItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportList`

Ответ метода /v2/reports — список доступных отчетов.

Сигнатура: `ReportList(*, total_count: int, result: list[api_client_opti24.models.reports.ReportItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderParams`

Параметры заказа отчета.

Сигнатура: `ReportOrderParams(*, start_date: str | None = None, end_date: str | None = None, id_agreement: str | None = None, id_card: list[str] | None = None, card_group_code: list[str] | None = None, id_client: list[str] | None = None, additional: dict[str, Any] | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderRequest`

Тело запроса для заказа отчета (v2).

Сигнатура: `ReportOrderRequest(*, id: str, format: str, emails: str | None = None, params: api_client_opti24.models.reports.ReportOrderParams) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderResponse`

Ответ на заказ отчета (v2).

Сигнатура: `ReportOrderResponse(*, job_id: list[str], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportParameter`

Параметр отчета (например, дата, карта, договор).

Сигнатура: `ReportParameter(*, name: str, value: Any | None = None, label: str | None = None, default_value: str | None = None, menu_values: list[api_client_opti24.models.reports.ReportParameterMenuValue] | None = None, type: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportParameterMenuValue`

Значения меню для параметра отчета.

Сигнатура: `ReportParameterMenuValue(*, labels: str | None = None, values: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1JobItem`

Элемент списка ранее заказанных отчетов (v1).

Сигнатура: `ReportV1JobItem(*, date: str, client_id: str | None = None, user_id: str | None = None, contract_id: str | None = None, job_id: str, report_name: str, report_format: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1JobList`

Список заказанных отчетов (v1).

Сигнатура: `ReportV1JobList(*, jobs: list[api_client_opti24.models.reports.ReportV1JobItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1OrderResponse`

Ответ для v1 метода /reports.

Сигнатура: `ReportV1OrderResponse(*, report_ids: list[str], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.restrictions`

Описание отсутствует.

### `RestrictionGetResponse`

Ответ на запрос списка ограничителей (GET /restriction).

Сигнатура: `RestrictionGetResponse(*, data: api_client_opti24.models.restrictions.RestrictionList, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionItem`

Модель одного товарного ограничителя (ограничение по продукту).

Сигнатура: `RestrictionItem(*, id: str, card_id: str | None = None, group_id: str | None = None, contract_id: str, productType: str | None = None, productGroup: str | None = None, productTypeName: str | None = None, productGroupName: str | None = None, restriction_type: int, date: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionList`

Список товарных ограничителей.

Сигнатура: `RestrictionList(*, total_count: int, result: list[api_client_opti24.models.restrictions.RestrictionItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionRemoveResponse`

Ответ на удаление ограничителя (POST /removeRestriction).

Сигнатура: `RestrictionRemoveResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionSetResponse`

Ответ на установку или изменение ограничителя (POST /setRestriction).

Сигнатура: `RestrictionSetResponse(*, data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.templates`

Описание отсутствует.

### `LimitAmount`

Описание отсутствует.

Сигнатура: `LimitAmount(*, unit: str | None = None, value: float | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitSum`

Описание отсутствует.

Сигнатура: `LimitSum(*, currency: str | None = None, currencyName: str | None = None, value: float | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTerm`

Описание отсутствует.

Сигнатура: `LimitTerm(*, days: str | None = None, type: int | None = None, time: api_client_opti24.models.templates.LimitTermTime | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTermTime`

Описание отсутствует.

Сигнатура: `LimitTermTime(*, from_: str | None = None, to: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTime`

Описание отсутствует.

Сигнатура: `LimitTime(*, type: int | None = None, number: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTransactions`

Описание отсутствует.

Сигнатура: `LimitTransactions(*, count: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateCreateRequest`

Описание отсутствует.

Сигнатура: `TemplateCreateRequest(*, contract_id: str, type: str, name: str) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateCreateResponse`

Описание отсутствует.

Сигнатура: `TemplateCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateDeleteResponse`

Описание отсутствует.

Сигнатура: `TemplateDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestriction`

Описание отсутствует.

Сигнатура: `TemplateGeoRestriction(*, id: str, template_id: str, contract_id: str, date: str | None = None, country: str | None = None, countryName: str | None = None, region: str | None = None, regionName: str | None = None, partner: str | None = None, partnerName: str | None = None, service_center: str | None = None, service_centerName: str | None = None, restriction_type: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionCreateRequest`

Описание отсутствует.

Сигнатура: `TemplateGeoRestrictionCreateRequest(*, contract_id: str, country: str, region: str | None = None, partner: str | None = None, service_center: str | None = None, restriction_type: int) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionCreateResponse`

Описание отсутствует.

Сигнатура: `TemplateGeoRestrictionCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionDeleteResponse`

Описание отсутствует.

Сигнатура: `TemplateGeoRestrictionDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionListData`

Описание отсутствует.

Сигнатура: `TemplateGeoRestrictionListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateGeoRestriction], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionListResponse`

Описание отсутствует.

Сигнатура: `TemplateGeoRestrictionListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplateGeoRestrictionListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateItem`

Описание отсутствует.

Сигнатура: `TemplateItem(*, id: str, name: str, type: str, contract_id: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimit`

Описание отсутствует.

Сигнатура: `TemplateLimit(*, id: str, template_id: str, contract_id: str, amount: api_client_opti24.models.templates.LimitAmount | None = None, sum: api_client_opti24.models.templates.LimitSum | None = None, time: api_client_opti24.models.templates.LimitTime | None = None, term: api_client_opti24.models.templates.LimitTerm | None = None, transactions: api_client_opti24.models.templates.LimitTransactions | None = None, date: str | None = None, productType: str | None = None, productGroup: str | None = None, productTypeName: str | None = None, productGroupName: str | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitCreateRequest`

Описание отсутствует.

Сигнатура: `TemplateLimitCreateRequest(*, contract_id: str, product_type: str, product_group: str | None = None, sum: api_client_opti24.models.templates.LimitSum | None = None, amount: api_client_opti24.models.templates.LimitAmount | None = None, time: api_client_opti24.models.templates.LimitTime, term: api_client_opti24.models.templates.LimitTerm | None = None, create_restriction: bool | None = None) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitCreateResponse`

Описание отсутствует.

Сигнатура: `TemplateLimitCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitDeleteResponse`

Описание отсутствует.

Сигнатура: `TemplateLimitDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitListData`

Описание отсутствует.

Сигнатура: `TemplateLimitListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateLimit], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitListResponse`

Описание отсутствует.

Сигнатура: `TemplateLimitListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplateLimitListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestriction`

Описание отсутствует.

Сигнатура: `TemplateRestriction(*, id: str, template_id: str, contract_id: str, date: str | None = None, productType: str | None = None, productGroup: str | None = None, productTypeName: str | None = None, productGroupName: str | None = None, restriction_type: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionCreateRequest`

Описание отсутствует.

Сигнатура: `TemplateRestrictionCreateRequest(*, contract_id: str, product_type: str, product_group: str | None = None, restriction_type: int) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionCreateResponse`

Описание отсутствует.

Сигнатура: `TemplateRestrictionCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionDeleteResponse`

Описание отсутствует.

Сигнатура: `TemplateRestrictionDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionListData`

Описание отсутствует.

Сигнатура: `TemplateRestrictionListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateRestriction], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionListResponse`

Описание отсутствует.

Сигнатура: `TemplateRestrictionListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplateRestrictionListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplatesListData`

Описание отсутствует.

Сигнатура: `TemplatesListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplatesListResponse`

Описание отсутствует.

Сигнатура: `TemplatesListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplatesListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.transactions`

Описание отсутствует.

### `RequestInfo`

Информация о типе и названии запроса.

Сигнатура: `RequestInfo(*, type: str, name: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionDetailResponse`

Ответ метода получения детальной информации по транзакции (v2).

Сигнатура: `TransactionDetailResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.transactions.TransactionsV2Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionItem`

Позиция (товар) внутри транзакции.

Сигнатура: `TransactionItem(*, id: str, rrn: str, product: str, amount: str, price: str, base_cost: str, cost: str, discount: str, discount_cost: str, transaction: str, currency: str, unit: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionItemV2`

Позиция в транзакции (v2).

Для спорных полей здесь сознательно приоритет отдан примерам из спецификации
и реальным ответам DEMO-стенда, а не табличным типам, которые местами
противоречат самим же payload-примерам.

Сигнатура: `TransactionItemV2(*, id: int, timestamp: datetime.datetime, utc_time: datetime.datetime | None = None, card_id: str, poi_id: str, terminal_id: str, type: str, product_id: str, product_name: str | None = None, product_category_id: str, currency: str, check_id: int, stor_transaction_id: int, is_storno: bool, is_manual_corrention: bool, qty: float, price: float, price_no_discount: float, sum: float, sum_no_discount: float, discount: float, exchange_rate: float, card_number: str, payment_type: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionV1`

Транзакция для версии v1.

Сигнатура: `TransactionV1(*, id: str, time: datetime.datetime, host_date: datetime.datetime, currency: str, card_id: str, service_center: str, card_number: str, base_cost: str, cost: str, discount: str, discount_cost: str, incoming: bool, request: api_client_opti24.models.transactions.RequestInfo, transaction_items: list[api_client_opti24.models.transactions.TransactionItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV1Data`

Описание отсутствует.

Сигнатура: `TransactionsV1Data(*, total_count: int, result: list[api_client_opti24.models.transactions.TransactionV1], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV1Response`

Описание отсутствует.

Сигнатура: `TransactionsV1Response(*, status: dict[str, typing.Any], data: api_client_opti24.models.transactions.TransactionsV1Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV2Data`

Описание отсутствует.

Сигнатура: `TransactionsV2Data(*, total_count: int, result: list[api_client_opti24.models.transactions.TransactionItemV2], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV2Response`

Описание отсутствует.

Сигнатура: `TransactionsV2Response(*, status: dict[str, typing.Any], data: api_client_opti24.models.transactions.TransactionsV2Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.users`

Описание отсутствует.

### `UserAccess`

Описание отсутствует.

Сигнатура: `UserAccess(*, web: bool, api: bool, mobile: bool, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserBoolResponse`

Описание отсутствует.

Сигнатура: `UserBoolResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserCardItem`

Описание отсутствует.

Сигнатура: `UserCardItem(*, sid: str, number: str, mpc: bool, product: str | None = None, comment: str | None = None, status: str, contract_id: str, contract_name: str | None = None, available: bool, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserContractItem`

Описание отсутствует.

Сигнатура: `UserContractItem(*, sid: str, number: str, available: bool, template_id: str | None = None, cards_count: int | None = None, status: api_client_opti24.models.users.UserStatus | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserCreateResponse`

Описание отсутствует.

Сигнатура: `UserCreateResponse(*, status: dict[str, typing.Any], data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserItem`

Описание отсутствует.

Сигнатура: `UserItem(*, id: str, login: str, first_name: str, last_name: str, middle_name: str | None = None, date: str, position: str | None = None, role: api_client_opti24.models.users.UserRole, active: bool, access: api_client_opti24.models.users.UserAccess, mobile_phone: str | None = None, email: str | None = None, contracts: list[api_client_opti24.models.users.UserContractItem] = <factory>, cards: list[api_client_opti24.models.users.UserCardItem] = <factory>, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserList`

Описание отсутствует.

Сигнатура: `UserList(*, total_count: int, result: list[api_client_opti24.models.users.UserItem], **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserListResponse`

Описание отсутствует.

Сигнатура: `UserListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.users.UserList | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserRole`

Описание отсутствует.

Сигнатура: `UserRole(*, id: str, name: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserStatus`

Описание отсутствует.

Сигнатура: `UserStatus(*, id: str, name: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `UserListResponse`

Описание отсутствует.

Сигнатура: `UserListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.users.UserList | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.virtual_cards`

Описание отсутствует.

### `ConfirmVirtualCardRequest`

Описание отсутствует.

Сигнатура: `ConfirmVirtualCardRequest(*, card_id: str, code: str) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ConfirmVirtualCardResponse`

Описание отсутствует.

Сигнатура: `ConfirmVirtualCardResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DeleteMPCResponse`

Описание отсутствует.

Сигнатура: `DeleteMPCResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `DeleteVirtualCardResponse`

Описание отсутствует.

Сигнатура: `DeleteVirtualCardResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCActionResponse`

Описание отсутствует.

Сигнатура: `MPCActionResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCListResponse`

Описание отсутствует.

Сигнатура: `MPCListResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: Any, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCPayloadResponse`

Описание отсутствует.

Сигнатура: `MPCPayloadResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: Any, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RerunVirtualCardReleaseRequest`

Описание отсутствует.

Сигнатура: `RerunVirtualCardReleaseRequest(*, card_id: str, reason: str | None = None) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `RerunVirtualCardReleaseResponse`

Описание отсутствует.

Сигнатура: `RerunVirtualCardReleaseResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: api_client_opti24.models.virtual_cards.VirtualCardData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResendSMSRequest`

Описание отсутствует.

Сигнатура: `ResendSMSRequest(*, card_id: str) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResendSMSResponse`

Описание отсутствует.

Сигнатура: `ResendSMSResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResetMPCRequest`

Описание отсутствует.

Сигнатура: `ResetMPCRequest(*, type: str) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `ResetMPCResponse`

Описание отсутствует.

Сигнатура: `ResetMPCResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `SimpleActionResponse`

Описание отсутствует.

Сигнатура: `SimpleActionResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `StatusModel`

Описание отсутствует.

Сигнатура: `StatusModel(*, code: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `VirtualCardData`

Описание отсутствует.

Сигнатура: `VirtualCardData(*, id: str, number: str, carrier: str, product: str, status: str, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

### `VirtualCardResponse`

Описание отсутствует.

Сигнатура: `VirtualCardResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: api_client_opti24.models.virtual_cards.VirtualCardData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

- `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.payloads`

Описание отсутствует.

### `with_method_override`

Описание отсутствует.

Сигнатура: `with_method_override(payload: 'Mapping[str, Any] | Sequence[Mapping[str, Any]] | None', method: 'str') -> 'dict[str, Any] | list[dict[str, Any]]'`

## `api_client_opti24.policies`

Описание отсутствует.

### `RateLimitPolicy`

RateLimitPolicy(requests_per_second: 'float | None' = None)

Сигнатура: `RateLimitPolicy(requests_per_second: 'float | None' = None) -> None`

### `RetryClass`

Описание отсутствует.

Сигнатура: `RetryClass(*values)`

### `RetryPolicy`

RetryPolicy(network_attempts: 'int' = 5, rate_limit_attempts: 'int' = 3, network_backoff_min_seconds: 'float' = 2.0, network_backoff_max_seconds: 'float' = 60.0, rate_limit_backoff_seconds: 'float' = 0.5, auth_retry_min_interval_seconds: 'float' = 5.0)

Сигнатура: `RetryPolicy(network_attempts: 'int' = 5, rate_limit_attempts: 'int' = 3, network_backoff_min_seconds: 'float' = 2.0, network_backoff_max_seconds: 'float' = 60.0, rate_limit_backoff_seconds: 'float' = 0.5, auth_retry_min_interval_seconds: 'float' = 5.0) -> None`

Публичные методы:

- `initial_network_backoff(self, retry_class: 'str | RetryClass') -> 'float'`
- `network_attempt_count(self, retry_class: 'str | RetryClass', http_method: 'str', *, idempotent: 'bool | None' = None) -> 'int'`
- `rate_limit_attempt_count(self, retry_class: 'str | RetryClass', http_method: 'str', *, idempotent: 'bool | None' = None) -> 'int'`

## `api_client_opti24.registry`

Описание отсутствует.

### `MethodRegistry`

Описание отсутствует.

Сигнатура: `MethodRegistry(specs: 'dict[str, EndpointSpec] | None' = None) -> 'None'`

Публичные методы:

- `find_by_endpoint(self, endpoint: 'str', version: 'str', http_method: 'str | None' = None) -> 'EndpointSpec | None'`
- `get(self, name: 'str') -> 'EndpointSpec'`
- `list_all(self) -> 'tuple[EndpointSpec, ...]'`
- `list_domain(self, domain: 'str') -> 'tuple[EndpointSpec, ...]'`
- `register(self, spec: 'EndpointSpec') -> 'None'`

### `build_default_registry`

Описание отсутствует.

Сигнатура: `build_default_registry() -> 'MethodRegistry'`

## `api_client_opti24.response`

Описание отсутствует.

### `ResponseDecoder`

Описание отсутствует.

Сигнатура: `ResponseDecoder(*, logger: 'LoggerLike | None' = None) -> 'None'`

Публичные методы:

- `decode(self, response: 'httpx.Response', endpoint: 'str', *, method_name: 'str | None' = None) -> 'DecodedPayload'`
- `decode_bytes(self, response: 'httpx.Response', content: 'bytes', endpoint: 'str', *, method_name: 'str | None' = None) -> 'bytes'`
- `parse(self, response: 'httpx.Response') -> 'DecodedPayload'`

## `api_client_opti24.runtime`

Описание отсутствует.

### `Clock`

Описание отсутствует.

Сигнатура: `Clock(*args, **kwargs)`

Публичные методы:

- `monotonic(self) -> 'float'`
- `now(self) -> 'datetime'`
- `sleep(self, seconds: 'float') -> 'None'`

### `SystemClock`

Описание отсутствует.

Сигнатура: `SystemClock()`

Публичные методы:

- `monotonic(self) -> 'float'`
- `now(self) -> 'datetime'`
- `sleep(self, seconds: 'float') -> 'None'`

## `api_client_opti24.service_base`

Описание отсутствует.

### `APIKeyProvider`

Описание отсутствует.

Сигнатура: `APIKeyProvider(*args, **kwargs)`

Публичные методы:

- `get_api_key(self) -> 'str'`

### `CredentialsProvider`

Описание отсутствует.

Сигнатура: `CredentialsProvider(*args, **kwargs)`

Публичные методы:

- `get_credentials(self) -> 'tuple[str, str]'`

### `RequestExecutor`

Описание отсутствует.

Сигнатура: `RequestExecutor(*args, **kwargs)`

Публичные методы:

- `execute(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'JSONPayload'`
- `execute_stream(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'bytes'`

### `ServiceMethodContext`

Описание отсутствует.

Сигнатура: `ServiceMethodContext(*args, **kwargs)`

### `SessionContext`

Описание отсутствует.

Сигнатура: `SessionContext(*args, **kwargs)`

### `SessionGate`

Описание отсутствует.

Сигнатура: `SessionGate(*args, **kwargs)`

Публичные методы:

- `ensure_authenticated(self) -> 'str'`

### `SessionMutator`

Описание отсутствует.

Сигнатура: `SessionMutator(*args, **kwargs)`

Публичные методы:

- `invalidate(self) -> 'None'`
- `mark_authenticated(self, session_id: 'str', contract_id: 'str | None' = None) -> 'None'`
- `reset(self) -> 'None'`
- `set_contract(self, contract_id: 'str | None') -> 'None'`

### `SessionRecovery`

Описание отсутствует.

Сигнатура: `SessionRecovery(*args, **kwargs)`

Публичные методы:

- `recover(self) -> 'str'`

## `api_client_opti24.service_groups`

Описание отсутствует.

### `ServiceContainer`

ServiceContainer(auth: 'AuthService', card_groups: 'CardGroupsService', cards: 'CardsService', contracts: 'ContractsService', dictionaries: 'DictionariesService', ewallet: 'EwalletService', final_prices: 'FinalPricesService', invites: 'InvitesService', limits: 'LimitsService', region_limits: 'RegionLimitsService', reports: 'ReportsService', restrictions: 'RestrictionsService', templates: 'TemplatesService', transactions: 'TransactionsService', users: 'UsersService', virtual_cards: 'VirtualCardsService')

Сигнатура: `ServiceContainer(auth: 'AuthService', card_groups: 'CardGroupsService', cards: 'CardsService', contracts: 'ContractsService', dictionaries: 'DictionariesService', ewallet: 'EwalletService', final_prices: 'FinalPricesService', invites: 'InvitesService', limits: 'LimitsService', region_limits: 'RegionLimitsService', reports: 'ReportsService', restrictions: 'RestrictionsService', templates: 'TemplatesService', transactions: 'TransactionsService', users: 'UsersService', virtual_cards: 'VirtualCardsService') -> None`

Публичные методы:

- `create(*, request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike', auth: 'AuthService') -> 'ServiceContainer'`

## `api_client_opti24.services`

Описание отсутствует.

_Публичные классы и функции не обнаружены._

## `api_client_opti24.services.auth`

Описание отсутствует.

### `AuthService`

Описание отсутствует.

Сигнатура: `AuthService(request_executor: api_client_opti24.service_base.RequestExecutor, session_context: api_client_opti24.service_base.SessionContext, session_gate: api_client_opti24.service_base.SessionGate, session_mutator: api_client_opti24.service_base.SessionMutator, authenticator: api_client_opti24.authentication.Authenticator, clock: api_client_opti24.runtime.Clock, logger: logging.Logger) -> None`

Публичные методы:

- `auth_user(self, *, api_version: str | None = None, contract_id: str | None = None, contract_number: str | None = None) -> api_client_opti24.models.auth.AuthUserResponse`
- `get_info(self, api_version: str | None = None, period: str | None = None) -> api_client_opti24.models.auth.GetInfoResponse`
- `logoff(self, api_version: str | None = None) -> dict[str, object]`

## `api_client_opti24.services.card_group`

Описание отсутствует.

### `CardGroupsService`

Методы для работы с группами карт (v1).

Сигнатура: `CardGroupsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_card_groups(self, *, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.card_group.CardGroupListResponse`
- `remove_card_group(self, *, contract_id: str, group_id: str, api_version: str | None = None) -> api_client_opti24.models.card_group.RemoveCardGroupResponse`
- `set_card_group(self, *, contract_id: str, name: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.card_group.SetCardGroupResponse`
- `set_cards_to_group(self, *, contract_id: str, group_id: str, cards_list: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.card_group.SetCardsToGroupResponse`

## `api_client_opti24.services.cards`

Описание отсутствует.

### `CardsService`

Методы работы с топливными картами.

Сигнатура: `CardsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `block_card(self, contract_id: str, card_ids: list[str], block: bool = True, api_version: str | None = None) -> api_client_opti24.models.cards.IDListResponse`
- `get_card_detail(self, contract_id: str, card_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.CardDetailResponse`
- `get_card_drivers(self, card_id: str, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.CardDriversResponse`
- `get_cards_by_group(self, contract_id: str, group_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.CardGroupResponse`
- `get_cards_v1(self, contract_id: str, cache: bool = True, api_version: str | None = None) -> api_client_opti24.models.cards.CardsListResponse`
- `get_cards_v2(self, contract_id: str | None = None, sort: str = '-id', q: str | None = None, status: str | None = None, carrier: str | None = None, platon: bool | None = None, avtodor: bool | None = None, users: bool | None = None, group_id: str | None = None, page: int | None = None, onpage: int | None = None, api_version: str | None = None) -> api_client_opti24.models.cards.CardsV2Response`
- `reset_pin(self, card_id: str, contract_id: str, code: str, api_version: str | None = None) -> api_client_opti24.models.cards.BoolResponse`
- `set_card_comment(self, card_id: str, contract_id: str, comment: str, api_version: str | None = None) -> api_client_opti24.models.cards.BoolResponse`
- `verify_pin(self, card_id: str, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.BoolResponse`

## `api_client_opti24.services.contract`

Описание отсутствует.

### `ContractsService`

Описание отсутствует.

Сигнатура: `ContractsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_contract_data(self, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.contracts.ContractResponse`
- `get_documents(self, date_start: str, date_end: str, api_version: str | None = None, page: int = 1, on_page: int = 10) -> api_client_opti24.models.contracts.DocumentsResponse`
- `get_invoices(self, api_version: str | None = None) -> api_client_opti24.models.contracts.InvoicesResponse`
- `get_payments(self, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.contracts.PaymentsResponse`
- `order_cards(self, count: int, office_id: str, api_version: str | None = None) -> api_client_opti24.models.contracts.OrderCardsResponse`
- `order_documents_email(self, ids: list[str], fmt: str, emails: list[str], api_version: str | None = None) -> api_client_opti24.models.contracts.DocumentsOrderResponse`
- `order_invoice(self, amount: float, email: str, api_version: str | None = None) -> api_client_opti24.models.contracts.InvoiceOrderResponse`

## `api_client_opti24.services.dictionaries`

Описание отсутствует.

### `DictionariesService`

Методы для работы со справочниками и торговыми точками

Сигнатура: `DictionariesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_azs_filters(self, *, api_version: str | None = None) -> api_client_opti24.models.dictionaries.AzsFiltersResponse`
- `get_azs_list_v1(self, page: int = 1, onpage: int = 10, filter: dict[str, Any] | None = None, id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.dictionaries.AzsListV1Response`
- `get_azs_list_v2(self, filter: dict[str, Any] | None = None, q: str | None = None, api_version: str | None = None) -> api_client_opti24.models.dictionaries.AzsListV2Response`
- `get_dictionary(self, *, name: str, api_version: str | None = None) -> api_client_opti24.models.dictionaries.DictionaryResponse`

## `api_client_opti24.services.ewallet`

Описание отсутствует.

### `EwalletService`

Методы для работы с электронными кошельками (Ewallet).

Электронный кошелёк — это тип карты, обслуживание которой производится не из средств договора,
а из отдельного кошелькового счёта. Пользователь может:
  • менять тип карты (лимитная ↔ электронный кошелёк);
  • переводить средства со счёта договора на кошелёк;
  • переводить средства обратно с кошелька на договор.

Сигнатура: `EwalletService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `move_to_card(self, *, contract_id: str | None = None, card_id: str, amount: float, api_version: str | None = None) -> api_client_opti24.models.ewallet.MoveToCardResponse`
- `move_to_contract(self, *, contract_id: str | None = None, card_id: str, amount: float, api_version: str | None = None) -> api_client_opti24.models.ewallet.MoveToContractResponse`
- `set_card_product(self, *, contract_id: str | None = None, card_ids: list[str], product: str, api_version: str | None = None) -> api_client_opti24.models.ewallet.SetCardProductResponse`

## `api_client_opti24.services.final_prices`

Описание отсутствует.

### `FinalPricesService`

Методы для получения финальных цен и проверки покупок по карте.

Сигнатура: `FinalPricesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `check_purchase(self, *, card_id: str, poi_id: str, goods: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.final_prices.CheckPurchaseResponse`
- `get_final_prices(self, *, card_id: str, poi_id: str, goods: list[str], api_version: str | None = None) -> api_client_opti24.models.final_prices.FinalPricesResponse`

## `api_client_opti24.services.invites`

Описание отсутствует.

### `InvitesService`

Методы для работы с приглашениями пользователей (v2).
Invites – функционал регистрации пользователей.
Приглашение можно отправить по Email/SMS или получить уникальную ссылку и отправить удобным для вас способом.
Ссылка действует 3 календарных дня, повторно направить Email/SMS по одному приглашению можно не чаще 3х раз в день.
С помощью приглашения можно зарегистрировать, например, водителя и сразу привязать шаблон виртуальной карты,
либо привязать физические топливные карты.

Сигнатура: `InvitesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `create_invite(self, *, data: dict[str, typing.Any], with_send: bool = True, api_version: str | None = None) -> api_client_opti24.models.invites.InviteResponse`
- `delete_invite(self, *, invite_id: str, use_post: bool = False, api_version: str | None = None) -> api_client_opti24.models.invites.InviteBoolResponse`
- `get_invites(self, *, role: str | None = None, user_id: str | None = None, sort: str | None = None, status: str | None = None, q: str | None = None, page: int | None = None, on_page: int | None = None, api_version: str | None = None) -> api_client_opti24.models.invites.InviteList`
- `prolong_invite(self, *, invite_id: str, with_send: bool = True, api_version: str | None = None) -> api_client_opti24.models.invites.InviteBoolResponse`
- `resend_invite(self, *, invite_id: str, api_version: str | None = None) -> api_client_opti24.models.invites.InviteResponse`

## `api_client_opti24.services.limits`

Описание отсутствует.

### `LimitsService`

Методы для работы с продуктовыми лимитами (v1).

Поддерживаются:
  • Получение списка лимитов (по договору, карте или группе)
  • Установка / изменение лимита
  • Удаление лимита

Сигнатура: `LimitsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_limits(self, *, contract_id: str, card_id: str | None = None, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.limits.LimitsResponse`
- `remove_limit(self, *, contract_id: str, limit_id: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.limits.RemoveLimitResponse`
- `set_limit(self, *, limits: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.limits.SetLimitResponse`

## `api_client_opti24.services.region_limits`

Описание отсутствует.

### `RegionLimitsService`

Методы для работы с региональными лимитами (v1).

Сигнатура: `RegionLimitsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_region_limits(self, *, contract_id: str, card_id: str | None = None, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.region_limits.RegionLimitResponse`
- `remove_region_limit(self, *, contract_id: str, regionlimit_id: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.region_limits.RemoveRegionLimit`
- `set_region_limit(self, *, region_limits: list[dict[str, typing.Any]], api_version: str | None = None) -> dict[str, typing.Any]`

## `api_client_opti24.services.reports`

Описание отсутствует.

### `ReportsService`

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

Сигнатура: `ReportsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `download_report_file(self, *, job_id: str, api_version: str | None = None) -> bytes`
- `download_report_file_v1(self, *, job_id: str, archive: bool = False, api_version: str | None = None) -> bytes`
- `get_report_job_list_v1(self, *, api_version: str | None = None) -> api_client_opti24.models.reports.ReportV1JobList`
- `get_report_jobs(self, *, api_version: str | None = None) -> api_client_opti24.models.reports.ReportJobList`
- `get_reports(self, *, api_version: str | None = None) -> api_client_opti24.models.reports.ReportList`
- `order_report(self, *, report_id: str, format: str, params: dict[str, typing.Any], emails: str | None = None, api_version: str | None = None) -> api_client_opti24.models.reports.ReportOrderResponse`
- `order_report_v1(self, *, contract_id: str, start: str, end: str, report_format: str, email: str | None = None, cards_list: list[str] | None = None, group_id: list[str] | None = None, archive: bool = False, api_version: str | None = None) -> api_client_opti24.models.reports.ReportV1OrderResponse`

## `api_client_opti24.services.restrictions`

Описание отсутствует.

### `RestrictionsService`

Методы для работы с товарными ограничителями (v1).

Сигнатура: `RestrictionsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_restrictions(self, *, contract_id: str, card_id: str | None = None, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.restrictions.RestrictionGetResponse`
- `remove_restriction(self, *, contract_id: str, restriction_id: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.restrictions.RestrictionRemoveResponse`
- `set_restriction(self, *, restrictions: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.restrictions.RestrictionSetResponse`

## `api_client_opti24.services.templates`

Описание отсутствует.

### `TemplatesService`

ВК – виртуальная карта. Чтобы выпустить ВК, потребуется создать шаблон лимита и прикрепить этот шаблон к пользователю.
Прикрепление происходит на этапе приглашения нового пользователя или методом для существующих пользователей.
Шаблон – это первоначальные параметры (Тип карты, Лимиты, Ограничители), с которыми будет выпущена эта ВК,
и все последующие, если использовать этот шаблон.
Шаблон сделан с точки зрения безопасности,
для того чтобы по-умолчанию все выпускаемые ВК имели ограничения на покупку (Лимит/Ограничитель).

Сигнатура: `TemplatesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `create_template(self, contract_id: str, type_: str, name: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateCreateResponse`
- `create_template_georestriction(self, template_id: str, payload: dict[str, typing.Any], api_version: str | None = None) -> api_client_opti24.models.templates.TemplateGeoRestrictionCreateResponse`
- `create_template_limit(self, template_id: str, payload: dict[str, typing.Any], api_version: str | None = None) -> api_client_opti24.models.templates.TemplateLimitCreateResponse`
- `create_template_restriction(self, template_id: str, payload: dict[str, typing.Any], api_version: str | None = None) -> api_client_opti24.models.templates.TemplateRestrictionCreateResponse`
- `delete_template(self, template_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateDeleteResponse`
- `delete_template_georestriction(self, template_id: str, georestriction_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateGeoRestrictionDeleteResponse`
- `delete_template_limit(self, template_id: str, limit_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateLimitDeleteResponse`
- `delete_template_restriction(self, template_id: str, restriction_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateRestrictionDeleteResponse`
- `get_template_georestrictions(self, template_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateGeoRestrictionListResponse`
- `get_template_limits(self, template_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateLimitListResponse`
- `get_template_restrictions(self, template_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateRestrictionListResponse`
- `get_templates(self, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplatesListResponse`
- `update_template(self, template_id: str, contract_id: str, type_: str, name: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateCreateResponse`
- `update_template_georestriction(self, template_id: str, georestriction_id: str, payload: dict[str, typing.Any], api_version: str | None = None, use_post: bool = True) -> api_client_opti24.models.templates.TemplateGeoRestrictionCreateResponse`
- `update_template_limit(self, *, template_id: str, limit_id: str, limits: list[dict[str, typing.Any]], use_post: bool = True, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateLimitCreateResponse`
- `update_template_restriction(self, template_id: str, restriction_id: str, payload: dict[str, typing.Any], api_version: str | None = None, use_post: bool = True) -> api_client_opti24.models.templates.TemplateRestrictionCreateResponse`

## `api_client_opti24.services.transactions`

Описание отсутствует.

### `TransactionsService`

Методы для работы с транзакциями (v1 и v2).

Сигнатура: `TransactionsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `get_card_transactions_v2(self, *, card_id: str, contract_id: str | None = None, date_from: str, date_to: str, page_limit: int = 100, page_offset: int = 0, api_version: str | None = None, filter_fn: collections.abc.Callable[[api_client_opti24.models.transactions.TransactionItemV2], bool] | None = None, sort_by: str | None = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV2Response`
- `get_transaction_detail(self, *, transaction_id: str, contract_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.transactions.TransactionDetailResponse`
- `get_transactions_v1(self, *, contract_id: str, card_id: str | None = None, count: int = 20, api_version: str | None = None, filter_fn: collections.abc.Callable[[api_client_opti24.models.transactions.TransactionV1], bool] | None = None, sort_by: str | None = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV1Response`
- `get_transactions_v2(self, *, contract_id: str, date_from: str, date_to: str, page_limit: int = 100, page_offset: int = 0, api_version: str | None = None, filter_fn: collections.abc.Callable[[api_client_opti24.models.transactions.TransactionItemV2], bool] | None = None, sort_by: str | None = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV2Response`

## `api_client_opti24.services.users`

Описание отсутствует.

### `UsersService`

Методы для работы с пользователями (v2).

Сигнатура: `UsersService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `attach_card(self, *, user_id: str, card_id: str, api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`
- `attach_contracts(self, *, user_id: str, contracts: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`
- `create_user(self, *, uuid: str, mobile: str, api_version: str | None = None) -> api_client_opti24.models.users.UserCreateResponse`
- `delete_user(self, *, user_id: str, use_post: bool = False, api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`
- `detach_card(self, *, user_id: str, card_id: str, api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`
- `detach_contracts(self, *, user_id: str, contracts: list[str], api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`
- `get_users(self, *, sort: str | None = None, page: int | None = None, on_page: int | None = None, q: str | None = None, filter: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.users.UserListResponse`

## `api_client_opti24.services.virtual_cards`

Описание отсутствует.

### `VirtualCardsService`

Методы для работы с виртуальными картами (ВК) и мобильными профилями карт (МПК)

Сигнатура: `VirtualCardsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

- `confirm_mpc(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`
- `create_virtual_card(self, user_id: str, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.VirtualCardResponse`
- `delete_mpc(self, card_id: str, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.SimpleActionResponse`
- `generate_payment_qr(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`
- `get_mpc_qr_list(self, *, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCListResponse`
- `init_mpc(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`
- `release_virtual_card(self, *, type_: str | None = None, template_id: str | None = None, user_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.VirtualCardResponse`
- `reset_mpc(self, card_id: str, type_: str, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.ResetMPCResponse`
- `update_mpc(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`

## `api_client_opti24.session`

Описание отсутствует.

### `SessionManager`

Описание отсутствует.

Сигнатура: `SessionManager() -> 'None'`

Публичные методы:

- `ensure_authenticated(self, authenticate: 'Callable[[], Awaitable[object]]') -> 'str'`
- `invalidate(self) -> 'None'`
- `mark_authenticated(self, session_id: 'str', contract_id: 'str | None' = None) -> 'None'`
- `reset(self) -> 'None'`
- `set_contract(self, contract_id: 'str | None') -> 'None'`
- `snapshot(self) -> 'SessionSnapshot'`

### `SessionSnapshot`

SessionSnapshot(state: 'SessionState', session_id: 'str | None', contract_id: 'str | None')

Сигнатура: `SessionSnapshot(state: 'SessionState', session_id: 'str | None', contract_id: 'str | None') -> None`

### `SessionState`

Описание отсутствует.

Сигнатура: `SessionState(*values)`

## `api_client_opti24.transport`

Описание отсутствует.

### `AsyncHTTPClient`

Описание отсутствует.

Сигнатура: `AsyncHTTPClient(*args, **kwargs)`

Публичные методы:

- `aclose(self) -> 'None'`
- `request(self, method: 'str', url: 'str', **kwargs: 'Any') -> 'httpx.Response'`
- `stream(self, method: 'str', url: 'str', **kwargs: 'Any') -> 'AbstractAsyncContextManager[httpx.Response]'`

### `AsyncTransport`

Описание отсутствует.

Сигнатура: `AsyncTransport(base_url: 'str', default_timeout: 'float' = 30.0, *, http_client: 'AsyncHTTPClient | None' = None, retry_policy: 'RetryPolicy | None' = None, rate_limit_policy: 'RateLimitPolicy | None' = None, allow_insecure_http: 'bool' = False, response_decoder: 'ResponseDecoder | None' = None, logger: 'LoggerLike | None' = None, clock: 'Clock | None' = None, sleep: 'AsyncSleep' = <function sleep>, monotonic: 'Callable[[], float]' = <built-in function monotonic>)`

Публичные методы:

- `aclose(self) -> 'None'`
- `request(self, method: 'str', endpoint: 'str', api_version: 'str' = 'v1', headers: 'Mapping[str, str] | None' = None, timeout: 'float | None' = None, method_name: 'str | None' = None, retry_class: 'str | RetryClass | None' = None, idempotent: 'bool | None' = None, **kwargs: 'Any') -> 'DecodedPayload'`
- `request_stream(self, method: 'str', endpoint: 'str', api_version: 'str' = 'v1', headers: 'Mapping[str, str] | None' = None, *, method_name: 'str | None' = None, **kwargs: 'Any') -> 'bytes'`

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

Сигнатура: `print_json(data: Any) -> None`

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

Сигнатура: `validate_month_span(date_from: str, date_to: str) -> None`

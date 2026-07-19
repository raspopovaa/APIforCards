# API Reference

Этот файл сгенерирован автоматически скриптом `scripts/generate_api_docs.py`.

Ниже собраны публичные модули, классы, функции и описание моделей SDK.

## `api_client_opti24`

_Публичные классы и функции не обнаружены._

## `api_client_opti24.authentication`

### `AuthenticationCoordinator`

Сигнатура: `AuthenticationCoordinator(session: 'SessionManager', authenticator: 'Authenticator') -> 'None'`

Публичные методы:

#### `authenticate`

Сигнатура: `authenticate(self) -> 'AuthUserResponse'`

#### `ensure_authenticated`

Сигнатура: `ensure_authenticated(self) -> 'str'`

#### `recover`

Сигнатура: `recover(self) -> 'str'`

### `Authenticator`

Сигнатура: `Authenticator(*args, **kwargs)`

Публичные методы:

#### `authenticate`

Сигнатура: `authenticate(self, *, api_version: 'str | None' = None, contract_id: 'str | None' = None, contract_number: 'str | None' = None) -> 'AuthUserResponse'`

### `DefaultAuthenticator`

Сигнатура: `DefaultAuthenticator(request_executor: 'RequestExecutor', session_mutator: 'SessionMutator', credentials_provider: 'CredentialsProvider', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `authenticate`

Сигнатура: `authenticate(self, *, api_version: 'str | None' = None, contract_id: 'str | None' = None, contract_number: 'str | None' = None) -> 'AuthUserResponse'`

## `api_client_opti24.client`

### `APIClient`

Сигнатура: `APIClient(base_url: str | None = None, api_key: str | None = None, login: str | None = None, password: str | None = None, *, settings: api_client_opti24.config.ConnectionSettings | api_client_opti24.config.APISettings | None = None, transport: api_client_opti24.executor.Transport | None = None, session_manager: api_client_opti24.session.SessionManager | None = None, registry: api_client_opti24.registry.MethodRegistry | None = None, logger: logging.Logger | None = None, clock: api_client_opti24.runtime.Clock | None = None, credentials_provider: api_client_opti24.service_base.CredentialsProvider | None = None, api_key_provider: api_client_opti24.service_base.APIKeyProvider | None = None) -> None`

Публичные методы:

#### `aclose`

Сигнатура: `aclose(self) -> None`

## `api_client_opti24.composition`

### `ClientRuntime`

ClientRuntime(authentication: 'AuthenticationCoordinator', request_executor: 'DefaultRequestExecutor', services: 'ServiceContainer')

Сигнатура: `ClientRuntime(authentication: 'AuthenticationCoordinator', request_executor: 'DefaultRequestExecutor', services: 'ServiceContainer') -> None`

### `compose_client_runtime`

Сигнатура: `compose_client_runtime(*, api_key_provider: 'APIKeyProvider', credentials_provider: 'CredentialsProvider', transport: 'Transport', session_manager: 'SessionManager', registry: 'MethodRegistry', timeouts: 'TimeoutPolicy', logger: 'LoggerLike', clock: 'Clock') -> 'ClientRuntime'`

## `api_client_opti24.config`

### `APISettings`

APISettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None), api_key: 'str', login: 'str | None' = None, password: 'str | None' = None)

Сигнатура: `APISettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None), api_key: 'str', login: 'str | None' = None, password: 'str | None' = None) -> None`

Публичные методы:

#### `connection_settings`

Сигнатура: `connection_settings(self) -> 'ConnectionSettings'`

#### `from_env`

Сигнатура: `from_env(*, load_dotenv: 'bool' = True, env_file: 'str | Path' = '.env') -> 'APISettings'`

### `ConnectionSettings`

ConnectionSettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None))

Сигнатура: `ConnectionSettings(*, base_url: 'str', request_log_file: 'str' = './api_requests.jsonl', logger_file: 'str' = './api.log', log_level: 'str' = 'INFO', allow_insecure_http: 'bool' = False, timeouts: 'TimeoutPolicy' = TimeoutPolicy(default=30.0, auth=30.0, read_heavy=120.0), retry_policy: 'RetryPolicy' = RetryPolicy(network_attempts=5, rate_limit_attempts=3, network_backoff_min_seconds=2.0, network_backoff_max_seconds=60.0, rate_limit_backoff_seconds=0.5, auth_retry_min_interval_seconds=5.0), rate_limit_policy: 'RateLimitPolicy' = RateLimitPolicy(requests_per_second=None)) -> None`

Публичные методы:

#### `from_env`

Сигнатура: `from_env(*, load_dotenv: 'bool' = True, env_file: 'str | Path' = '.env') -> 'ConnectionSettings'`

### `TimeoutPolicy`

TimeoutPolicy(default: 'float' = 30.0, auth: 'float' = 30.0, read_heavy: 'float' = 120.0)

Сигнатура: `TimeoutPolicy(default: 'float' = 30.0, auth: 'float' = 30.0, read_heavy: 'float' = 120.0) -> None`

Публичные методы:

#### `resolve`

Сигнатура: `resolve(self, timeout_class: 'str') -> 'float'`

## `api_client_opti24.contracts`

### `serialize_registry_contract`

Сигнатура: `serialize_registry_contract(registry: 'MethodRegistry') -> 'list[dict[str, object]]'`

## `api_client_opti24.credentials`

### `EnvironmentCredentialsProvider`

Сигнатура: `EnvironmentCredentialsProvider(*, api_key: 'str', login: 'str', password: 'str') -> 'None'`

Публичные методы:

#### `from_env`

Сигнатура: `from_env(*, load_dotenv: 'bool' = True, env_file: 'str | Path' = '.env') -> 'EnvironmentCredentialsProvider'`

#### `get_api_key`

Сигнатура: `get_api_key(self) -> 'str'`

#### `get_credentials`

Сигнатура: `get_credentials(self) -> 'tuple[str, str]'`

### `StaticAPIKeyProvider`

Сигнатура: `StaticAPIKeyProvider(api_key: 'str') -> 'None'`

Публичные методы:

#### `get_api_key`

Сигнатура: `get_api_key(self) -> 'str'`

### `StaticCredentialsProvider`

Сигнатура: `StaticCredentialsProvider(*, api_key: 'str', login: 'str', password: 'str') -> 'None'`

Публичные методы:

#### `get_api_key`

Сигнатура: `get_api_key(self) -> 'str'`

#### `get_credentials`

Сигнатура: `get_credentials(self) -> 'tuple[str, str]'`

### `StaticLoginPasswordProvider`

Сигнатура: `StaticLoginPasswordProvider(*, login: 'str', password: 'str') -> 'None'`

Публичные методы:

#### `get_credentials`

Сигнатура: `get_credentials(self) -> 'tuple[str, str]'`

## `api_client_opti24.decorators`

### `api_method`

Сигнатура: `api_method(func: collections.abc.Callable[typing.Concatenate[~ServiceT, ~Params], collections.abc.Awaitable[~ResultT]]) -> collections.abc.Callable[typing.Concatenate[~ServiceT, ~Params], collections.abc.Awaitable[~ResultT]]`

## `api_client_opti24.endpoints`

### `EndpointSpec`

EndpointSpec(name: 'str', domain: 'str', http_method: 'str', endpoint: 'str', supported_versions: 'tuple[str, ...]', default_version: 'str', demo_available: 'bool', idempotent: 'bool', requires_session: 'bool' = True, timeout_class: 'str' = 'default', retry_class: 'str' = 'safe', route_variants: 'tuple[RouteVariant, ...]' = (), external_code: 'str | None' = None, billable: 'bool | None' = None)

Сигнатура: `EndpointSpec(name: 'str', domain: 'str', http_method: 'str', endpoint: 'str', supported_versions: 'tuple[str, ...]', default_version: 'str', demo_available: 'bool', idempotent: 'bool', requires_session: 'bool' = True, timeout_class: 'str' = 'default', retry_class: 'str' = 'safe', route_variants: 'tuple[RouteVariant, ...]' = (), external_code: 'str | None' = None, billable: 'bool | None' = None) -> None`

Публичные методы:

#### `iter_routes`

Сигнатура: `iter_routes(self) -> 'tuple[RouteVariant, ...]'`

#### `resolve_route`

Сигнатура: `resolve_route(self, *, api_version: 'str | None' = None, route_name: 'str' = 'default') -> 'RouteVariant'`

#### `supports`

Сигнатура: `supports(self, version: 'str') -> 'bool'`

### `RouteVariant`

RouteVariant(http_method: 'str', endpoint: 'str', api_version: 'str', demo_available: 'bool', name: 'str' = 'default', external_code: 'str | None' = None, billable: 'bool | None' = None)

Сигнатура: `RouteVariant(http_method: 'str', endpoint: 'str', api_version: 'str', demo_available: 'bool', name: 'str' = 'default', external_code: 'str | None' = None, billable: 'bool | None' = None) -> None`

Публичные методы:

#### `render`

Сигнатура: `render(self, path_params: 'PathParams | None' = None) -> 'str'`

#### `supports`

Сигнатура: `supports(self, version: 'str') -> 'bool'`

### `endpoint`

Сигнатура: `endpoint(name: 'str', domain: 'str', http_method: 'str', path: 'str', version: 'str', *, demo: 'bool' = True, timeout: 'str' = 'default', retry: 'str | None' = None, requires_session: 'bool' = True, variants: 'tuple[RouteVariant, ...]' = (), external_code: 'str | None' = None, billable: 'bool | None' = None) -> 'EndpointSpec'`

### `route`

Сигнатура: `route(http_method: 'str', path: 'str', version: 'str', *, demo: 'bool', name: 'str', external_code: 'str | None' = None, billable: 'bool | None' = None) -> 'RouteVariant'`

## `api_client_opti24.env`

### `load_env_file`

Сигнатура: `load_env_file(path: 'str | Path' = '.env', *, override: 'bool' = False) -> 'None'`

## `api_client_opti24.errors`

### `APIError`

Сигнатура: `APIError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `AccessDeniedError`

Сигнатура: `AccessDeniedError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `DuplicateConflictError`

Сигнатура: `DuplicateConflictError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ErrorContext`

ErrorContext(http_status_code: 'int', api_status_code: 'int | None', error_type: 'str | None', messages: 'tuple[str, ...]', raw_payload: 'Any', endpoint: 'str | None', method_name: 'str | None', hint: 'str | None', retryable: 'bool')

Сигнатура: `ErrorContext(http_status_code: 'int', api_status_code: 'int | None', error_type: 'str | None', messages: 'tuple[str, ...]', raw_payload: 'Any', endpoint: 'str | None', method_name: 'str | None', hint: 'str | None', retryable: 'bool') -> None`

### `NotAuthenticatedError`

Сигнатура: `NotAuthenticatedError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `NotFoundError`

Сигнатура: `NotFoundError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `RateLimitError`

Сигнатура: `RateLimitError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ServerError`

Сигнатура: `ServerError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `ValidationError`

Сигнатура: `ValidationError(status_code: 'int', message: 'str' = '', body: 'Any' = None, endpoint: 'str | None' = None, *, http_status_code: 'int | None' = None, api_status_code: 'int | None' = None, error_type: 'str | None' = None, messages: 'tuple[str, ...] | None' = None, method_name: 'str | None' = None, hint: 'str | None' = None, retryable: 'bool' = False) -> 'None'`

### `build_api_error`

Сигнатура: `build_api_error(*, status_code: 'int', body: 'Any', endpoint: 'str | None', method_name: 'str | None' = None, http_status_code: 'int | None' = None) -> 'APIError'`

## `api_client_opti24.executor`

### `DefaultRequestExecutor`

Сигнатура: `DefaultRequestExecutor(*, operation_executor: 'OperationExecutor', session_gate: 'SessionGate', session_recovery: 'SessionRecovery', registry: 'MethodRegistry', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `execute`

Сигнатура: `execute(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'JSONPayload'`

#### `execute_stream`

Сигнатура: `execute_stream(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'bytes'`

#### `headers`

Сигнатура: `headers(self, include_session: 'bool' = False, content_type_json: 'bool' = False) -> 'dict[str, str]'`

### `OperationExecutor`

Сигнатура: `OperationExecutor(*, api_key_provider: 'APIKeyProvider', transport: 'Transport', session_context: 'SessionContext', registry: 'MethodRegistry', timeouts: 'TimeoutPolicy', logger: 'LoggerLike', clock: 'Clock') -> 'None'`

Публичные методы:

#### `execute`

Сигнатура: `execute(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'JSONPayload'`

#### `execute_stream`

Сигнатура: `execute_stream(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'bytes'`

#### `headers`

Сигнатура: `headers(self, include_session: 'bool' = False, content_type_json: 'bool' = False) -> 'dict[str, str]'`

### `Transport`

Сигнатура: `Transport(*args, **kwargs)`

Публичные методы:

#### `aclose`

Сигнатура: `aclose(self) -> 'None'`

#### `request`

Сигнатура: `request(self, method: 'str', endpoint: 'str', *, api_version: 'str' = 'v1', **kwargs: 'Any') -> 'DecodedPayload'`

#### `request_stream`

Сигнатура: `request_stream(self, method: 'str', endpoint: 'str', *, api_version: 'str' = 'v1', headers: 'Mapping[str, str] | None' = None, **kwargs: 'Any') -> 'bytes'`

## `api_client_opti24.modeling`

### `BaseModel`

Сигнатура: `BaseModel(**extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `StrictRequestModel`

Сигнатура: `StrictRequestModel() -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `decode_model`

Сигнатура: `decode_model(model_type: 'type[ModelT]', payload: 'dict[str, Any]') -> 'ModelT'`

### `validator`

Сигнатура: `validator(*field_names: 'str', pre: 'bool' = False) -> 'Any'`

## `api_client_opti24.models`

_Публичные классы и функции не обнаружены._

## `api_client_opti24.models.auth`

### `AccessRights`

Сигнатура: `AccessRights(*, web: bool = False, api: bool = False, mobile: bool = False, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthError`

Сигнатура: `AuthError(*, code: str, message: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthErrorResponse`

Сигнатура: `AuthErrorResponse(*, error: api_client_opti24.models.auth.AuthError, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthUserData`

Сигнатура: `AuthUserData(*, client_id: str, client_status: str, org_name: str | None = None, session_id: str, user_id: str, contracts: list[api_client_opti24.models.auth.ContractInfo] = <factory>, role_id: str | None = None, role_name: str | None = None, read_only: bool = False, user_name: str | None = None, user_patronymic: str | None = None, user_surname: str | None = None, last_contract: str | None = None, access: api_client_opti24.models.auth.AccessRights | None = None, email: str | None = None, phone: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AuthUserResponse`

Сигнатура: `AuthUserResponse(*, status: api_client_opti24.models.auth.StatusResponse, data: api_client_opti24.models.auth.AuthUserData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ClientInfo`

Сигнатура: `ClientInfo(*, Client: str, ClientType: str, Contract: str, ContractName: str, PricePlan: str | None = None, Cost: float | None = None, Queries: int | None = None, Additional: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractInfo`

Сигнатура: `ContractInfo(*, id: str, number: str, mpc: bool = False, template_id: str | None = None, cards_count: int = 0, one_price: bool = False, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `GetInfoResponse`

Сигнатура: `GetInfoResponse(*, status: api_client_opti24.models.auth.StatusResponse, data: api_client_opti24.models.auth.InfoData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InfoData`

Сигнатура: `InfoData(*, from_: datetime.datetime, to: datetime.datetime, client_info: api_client_opti24.models.auth.ClientInfo, methods: api_client_opti24.models.auth.MethodsCount, methods_info: api_client_opti24.models.auth.MethodsInfo, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LogoffResponse`

Сигнатура: `LogoffResponse(*, status: api_client_opti24.models.auth.StatusResponse, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `MethodsCount`

Сигнатура: `MethodsCount(*, all: int = 0, cards: int | None = 0, cardgroups: int | None = 0, card: int | None = 0, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `MethodsInfo`

Сигнатура: `MethodsInfo(*, actions_bill: dict[str, str], actions_not_bill: dict[str, str], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `StatusResponse`

Сигнатура: `StatusResponse(*, code: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.card_group`

### `CardGroupItem`

Информация о группе карт.

Сигнатура: `CardGroupItem(*, id: str, name: str, cards_count: int, status: str, contract_id: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupListData`

Контейнер данных со списком групп карт.

Сигнатура: `CardGroupListData(*, total_count: int, result: list[api_client_opti24.models.card_group.CardGroupItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupListResponse`

Ответ метода получения списка групп карт.

Сигнатура: `CardGroupListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.card_group.CardGroupListData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveCardGroupResponse`

Ответ метода удаления группы карт.

Сигнатура: `RemoveCardGroupResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardGroupData`

Информация о созданной или изменённой группе.

Сигнатура: `SetCardGroupData(*, id: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardGroupResponse`

Ответ метода установки/изменения группы карт.

Сигнатура: `SetCardGroupResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.card_group.SetCardGroupData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `SetCardsToGroupResponse`

Ответ метода добавления карт в группу.

Сигнатура: `SetCardsToGroupResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.cards`

### `BoolResponse`

Сигнатура: `BoolResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDetail`

Сигнатура: `CardDetail(*, id: str, contract_id: str, number: str, status: str, can_work_offline: bool | None = None, card_auth_type: str | None = None, comment: str | None = None, date_last_usage: datetime.datetime | str | None = None, date_released: datetime.datetime | str | None = None, servicecenter_last_usage_name: str | None = None, transaction_timeout: api_client_opti24.models.cards.TransactionTimeout | None = None, product: str | None = None, carrier: str | None = None, available: str | None = None, currency: str | None = None, payment_of_tolls: str | None = None, previous: str | None = None, next: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

#### `empty_str_to_none`

Сигнатура: `empty_str_to_none(v: 'Any') -> 'Any'`

### `CardDetailData`

Сигнатура: `CardDetailData(*, total_count: int, result: list[api_client_opti24.models.cards.CardDetail], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDetailResponse`

Сигнатура: `CardDetailResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardDetailData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriverInfo`

Сигнатура: `CardDriverInfo(*, id: str, login: str, first_name: str, last_name: str, middle_name: str | None = None, date: str | None = None, position: str | None = None, role: str | None = None, mobile_phone: str, email: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriversData`

Сигнатура: `CardDriversData(*, total_count: int, result: list[api_client_opti24.models.cards.CardDriverInfo], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardDriversResponse`

Сигнатура: `CardDriversResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardDriversData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupData`

Сигнатура: `CardGroupData(*, total_count: int, result: list[api_client_opti24.models.cards.CardGroupInfo], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupInfo`

Сигнатура: `CardGroupInfo(*, id: str, group: str, contract_id: str, number: str, status: str, comment: str | None = None, product: str | None = None, payment_of_tolls: str | None = None, sync_group_state: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardGroupResponse`

Сигнатура: `CardGroupResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardGroupData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardInfo`

Сигнатура: `CardInfo(*, id: str, contract_id: str, number: str, status: str, can_work_offline: bool | None = None, card_auth_type: str | None = None, comment: str | None = None, date_expired: datetime.datetime | None = None, date_last_usage: datetime.datetime | None = None, date_released: datetime.datetime | None = None, servicecenter_last_usage_name: str | None = None, transaction_last_detail: str | None = None, transaction_timeout: api_client_opti24.models.cards.TransactionTimeout | None = None, product: str | None = None, payment_of_tolls: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardV2Item`

Информация об одной топливной карте договора.

Сигнатура: `CardV2Item(*, id: str, group_id: str | None = None, group_name: str | None = None, contract_id: str, contract_name: str, number: str, status: str, status_name: str | None = None, comment: str | None = None, product: str, product_name: str | None = None, carrier: str, carrier_name: str | None = None, platon: bool, avtodor: bool, sync_group_state: str | None = None, users: list[str] | None = <factory>, mpc: bool | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListData`

Сигнатура: `CardsListData(*, total_count: int, result: list[api_client_opti24.models.cards.CardInfo], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsListResponse`

Сигнатура: `CardsListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardsListData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsV2Data`

Основной объект данных для списка карт (v2).

Сигнатура: `CardsV2Data(*, total_count: int, result: list[api_client_opti24.models.cards.CardV2Item], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsV2Response`

Ответ API метода GET /v2/cards.

Сигнатура: `CardsV2Response(*, status: dict[str, typing.Any], data: api_client_opti24.models.cards.CardsV2Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `IDListResponse`

Сигнатура: `IDListResponse(*, status: dict[str, typing.Any], data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionTimeout`

Сигнатура: `TransactionTimeout(*, type: str | int, value: str | int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.contracts`

### `BalanceData`

Данные по расходу и балансу договора

Сигнатура: `BalanceData(*, available_amount: str, own_balance: str, balance: str, consumption_for_month: str, consumption_for_month_volume: str, consumption_for_prev_month_volume: str, last_payment_sum: str | None = None, last_payment_date: str | None = None, currency: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CardsData`

Информация по картам договора

Сигнатура: `CardsData(*, cards_quantity_all: str, cards_quantity_active: str, card_groups_quantity_all: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractData`

Основные данные договора

Сигнатура: `ContractData(*, contract_id: str, way_id: str, contract_number: str, unique_payment_id: str, client: str, client_category: str, contract_category: str, country: str, region: str, fin_institution: str, invoice_scheme: str, invoice_period: str | None = None, invoice_pmt_delay: str | None = None, contract_status: str, contract_status_name: str, pay_scheme: str, discount_scheme: str, auto_pay: str, auto_pay_type: str, credit_limit: str | None = None, current_amount_limiter: str, balance_amount_limiter: str | None = None, max_amount_limiter: str | None = None, date_open: str, effective_date: str, end_date: str, date_expire: str, product_type: bool, type_code: str, supplier_name: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ContractResponse`

Полный ответ API по договору

Сигнатура: `ContractResponse(*, mpc: bool, template_id: str, status: str, status_crm: str, payment_term_id: str | None = None, payment_scheme_id: str | None = None, is_dealer: bool, balanceData: api_client_opti24.models.contracts.BalanceData, contractData: api_client_opti24.models.contracts.ContractData, managerData: api_client_opti24.models.contracts.ManagerData | None = None, cardsData: api_client_opti24.models.contracts.CardsData, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentItem`

Информация об одном первичном документе.

Сигнатура: `DocumentItem(*, id: str, name: str, name_doc: str, number: str, date: int, total: float, vat: float, sum: float, currency: str, consignee: str, contract_id: str, contract_name: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsData`

Секция 'data' в ответе метода /documents.

Сигнатура: `DocumentsData(*, total_count: int, result: list[api_client_opti24.models.contracts.DocumentItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsOrderResponse`

Ответ метода POST /v2/documents (заказ документов).

Сигнатура: `DocumentsOrderResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DocumentsResponse`

Ответ метода GET /v2/documents.

Сигнатура: `DocumentsResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.contracts.DocumentsData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoiceItem`

Информация об одном счёте на оплату.

Сигнатура: `InvoiceItem(*, id: str, contract_id: str, ref_number: str, date_start: str, date_end: str, last_update: str, currency: str, amount: str, paid_amount: str, status: str, comment: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoiceOrderResponse`

Ответ метода POST /v2/invoice.

Сигнатура: `InvoiceOrderResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoicesData`

Секция 'data' в ответе списка счетов.

Сигнатура: `InvoicesData(*, total_count: int, result: list[api_client_opti24.models.contracts.InvoiceItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InvoicesResponse`

Ответ метода GET /v2/invoices.

Сигнатура: `InvoicesResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.contracts.InvoicesData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ManagerData`

Данные менеджера по сопровождению договора

Сигнатура: `ManagerData(*, email: str, first_name: str, last_name: str, middle_name: str | None = None, work_phone: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `OrderCardsResponse`

Ответ метода POST /v2/orderCards.

Сигнатура: `OrderCardsResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentItem`

Информация об одном платеже по договору.

Сигнатура: `PaymentItem(*, id: str, contract_id: str, date: str, amount: str, currency: str, amount_client: str, description: str, payment_name: str, payment_type: str, payment_number: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentsData`

Секция data из ответа API, содержит список платежей и их количество.

Сигнатура: `PaymentsData(*, total_count: int, result: list[api_client_opti24.models.contracts.PaymentItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `PaymentsResponse`

Основная модель ответа метода /getPayments.

Сигнатура: `PaymentsResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.contracts.PaymentsData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.dictionaries`

### `AddressV1`

Адрес торговой точки

Сигнатура: `AddressV1(*, track_id: str | None = None, kmRoad: str | None = None, roadSide: str | None = None, city: str | None = None, street: str | None = None, house: str | None = None, building: str | None = None, phone: str | None = None, fax: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AddressV2`

Адрес торговой точки

Сигнатура: `AddressV2(*, track_id: str | None = None, kmRoad: str | None = None, roadSide: str | None = None, city: str | None = None, street: str | None = None, house: str | None = None, building: str | None = None, phone: str | None = None, fax: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFilterItem`

Описание фильтра торговых точек

Сигнатура: `AzsFilterItem(*, filter: str | None = None, name: str | None = None, values: dict[str, api_client_opti24.models.dictionaries.AzsFilterValue] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFilterValue`

Отдельное значение фильтра

Сигнатура: `AzsFilterValue(*, name: str | None = None, code: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsFiltersResponse`

Ответ метода /azs/filters

Сигнатура: `AzsFiltersResponse(*, status: dict[str, Any] | None = None, data: list[api_client_opti24.models.dictionaries.AzsFilterItem] | None = <factory>, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsItemV1`

Информация о торговой точке (v1)

Сигнатура: `AzsItemV1(*, id: str | None = None, siebelId: str | None = None, contractNumber: str | None = None, contractName: str | None = None, status: str | None = None, countryCode: str | None = None, regionCode: str | None = None, secessionGPN: str | None = None, belongsTo: str | None = None, partner: str | None = None, ownType: str | None = None, locationType: str | None = None, brand: str | None = None, openDate: str | None = None, closeDate: str | None = None, latitude: str | None = None, longitude: str | None = None, type: str | None = None, timeZone: str | None = None, services: list[int] | None = <factory>, terminals: list[api_client_opti24.models.dictionaries.TerminalV1] | None = <factory>, address: api_client_opti24.models.dictionaries.AddressV1 | None = None, prices: list[api_client_opti24.models.dictionaries.PriceItemV1] | None = <factory>, searchTxt: str | None = None, phone: str | None = None, height_post: str | None = None, working_time: list[api_client_opti24.models.dictionaries.WorkingTimeV1] | None = <factory>, only_virtual_card: bool | None = None, accept_cards: bool | None = None, hidden_on_map: bool | None = None, active: bool | None = None, POIType: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsItemV2`

Информация о торговой точке (АЗС)

Сигнатура: `AzsItemV2(*, id: str, siebel_id: str, status: str | None = None, full_name: str | None = None, brand: str | None = None, poi_type_name: str | None = None, poi_type_code: str | None = None, own_type_name: str, own_type_code: str, contract_name: str | None = None, contract_number: str | None = None, phone: str | None = None, utc_timezone: str | None = None, time_zone: str | None = None, open_date: str | None = None, close_date: str | None = None, last_update: str | None = None, height_post: str | None = None, country_name: str | None, country_code: str | None, region_name: str | None = None, region_code: str | None = None, address_full: str | None = None, location: api_client_opti24.models.dictionaries.Coordinates | None = None, latitude: str | None = None, longitude: str | None = None, location_type: str | None = None, secession_gpn: str | None = None, partner: str | None = None, belongs_to: str | None = None, info: str | None = None, search_txt: str | None, accept_cards: bool | None, adblue: api_client_opti24.models.dictionaries.ServiceGroup | None = None, electric_charging_station: api_client_opti24.models.dictionaries.ServiceGroup | None = None, services_with_card: api_client_opti24.models.dictionaries.ServiceGroup | None = None, services_without_card: api_client_opti24.models.dictionaries.ServiceGroup | None = None, prices: list[api_client_opti24.models.dictionaries.PriceItemV2] | None = <factory>, payment_type: list[dict[str, Any]] | None = <factory>, terminals: list[api_client_opti24.models.dictionaries.TerminalV2] | None = <factory>, address: api_client_opti24.models.dictionaries.AddressV2 | None = None, working_time: list[api_client_opti24.models.dictionaries.WorkingTimeV2] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

#### `fix_empty_service_groups`

Сигнатура: `fix_empty_service_groups(v: Any) -> Any`

Исправляет ошибку, когда API возвращает [] вместо объекта.
Конвертирует [] → None, чтобы избежать ValidationError.

### `AzsListV1Data`

Основные данные списка торговых точек (v1)

Сигнатура: `AzsListV1Data(*, total_count: int | None = None, result: list[api_client_opti24.models.dictionaries.AzsItemV1] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV1Response`

Ответ метода GET /vip/v1/AZS

Сигнатура: `AzsListV1Response(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.dictionaries.AzsListV1Data | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV2Data`

Данные списка торговых точек (v2)

Сигнатура: `AzsListV2Data(*, total_count: int, result: list[api_client_opti24.models.dictionaries.AzsItemV2], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `AzsListV2Response`

Ответ метода получения списка торговых точек (v2)

Сигнатура: `AzsListV2Response(*, status: dict[str, Any] | None, data: api_client_opti24.models.dictionaries.AzsListV2Data | None, timestamp: int | None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `Coordinates`

Географические координаты торговой точки

Сигнатура: `Coordinates(*, type: str | None = None, coordinates: list[float] = <factory>, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryData`

Основные данные справочника

Сигнатура: `DictionaryData(*, total_count: int | None = None, result: list[api_client_opti24.models.dictionaries.DictionaryItem] | None = <factory>, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryItem`

Элемент справочника (универсальная модель)

Сигнатура: `DictionaryItem(*, id: str, code: str | None = None, value: str | None = None, name: str | None = None, deleted: int | None = 0, last_update: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DictionaryResponse`

Ответ метода GET /vip/v1/getDictionary

Сигнатура: `DictionaryResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.dictionaries.DictionaryData | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `PriceItemV1`

Цена товара на торговой точке

Сигнатура: `PriceItemV1(*, ID: str | None = None, GasStationID: str | None = None, GoodsCode: str | None = None, Price: str | None = None, Currency: str | None = None, DateTo: str | None = None, DateFrom: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `PriceItemV2`

Информация о цене товара на торговой точке

Сигнатура: `PriceItemV2(*, ID: str | None = None, GasStationID: str | None = None, GoodsCode: str | None = None, Price: str | None = None, Currency: str | None = None, DateTo: str | None = None, DateFrom: str | None = None, hex_color: str | None = None, name: str | None = None, CurrencyName: str | None = None, sort: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ServiceGroup`

Группа услуг, доступных на торговой точке

Сигнатура: `ServiceGroup(*, name: str | None = None, items: list[api_client_opti24.models.dictionaries.ServiceItem] | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ServiceItem`

Описание отдельной услуги

Сигнатура: `ServiceItem(*, name: str | None = None, code: int | str | None = None, sort: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TerminalV1`

Терминал торговой точки

Сигнатура: `TerminalV1(*, id: str | None = None, active: bool | None = None, name: str | None = None, status: str | None = None, type: str | None = None, connectionType: str | None = None, number: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TerminalV2`

Информация о терминале, установленном на торговой точке

Сигнатура: `TerminalV2(*, id: str | None = None, active: bool | None = None, name: str | None = None, status: str | None = None, type: str | None = None, connectionType: str | None = None, number: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `WorkingTimeV1`

Рабочее время торговой точки

Сигнатура: `WorkingTimeV1(*, Weekday: str | None = None, StartWorkTime: str | None = None, FinishWorkTime: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `WorkingTimeV2`

Расписание работы торговой точки

Сигнатура: `WorkingTimeV2(*, Weekday: str | None = None, StartWorkTime: str | None = None, FinishWorkTime: str | None = None, Everyday: bool | None = False, Round_The_Clock: bool | None = False, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.ewallet`

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

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

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

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

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

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `Status`

Модель для статуса ответа API.

Сигнатура: `Status(*, code: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.final_prices`

### `CheckPurchaseRequest`

Параметры запроса для проверки покупки

Сигнатура: `CheckPurchaseRequest(*, poi_id: str, goods: list[api_client_opti24.models.final_prices.PurchaseGoodItem]) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `CheckPurchaseResponse`

Ответ метода проверки возможности проведения транзакции

Сигнатура: `CheckPurchaseResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPriceItem`

Информация о финальной цене товара на АЗС

Сигнатура: `FinalPriceItem(*, code: str, price: float, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPricesData`

Основные данные о финальных ценах

Сигнатура: `FinalPricesData(*, total_count: int, goods: list[api_client_opti24.models.final_prices.FinalPriceItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `FinalPricesResponse`

Ответ метода получения финальных цен на АЗС

Сигнатура: `FinalPricesResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.final_prices.FinalPricesData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `PurchaseGoodItem`

Описание товарной позиции для проверки возможности покупки

Сигнатура: `PurchaseGoodItem(*, code: str, quantity: float, price: float, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.invites`

### `InviteActionResult`

Результат действий с приглашениями (создание, продление, повторная отправка)

Сигнатура: `InviteActionResult(*, id: str, url: str, attempts: int | None = None, expired_at: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteBoolResponse`

Результат простых действий (удаление, продление и т.п.)

Сигнатура: `InviteBoolResponse(*, data: bool, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteCard`

Информация о карте, привязанной к приглашению

Сигнатура: `InviteCard(*, sid: str, number: str, product: str, comment: str | None = None, status: str | None = None, status_name: str | None = None, contract_id: str | None = None, contract_name: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteContract`

Информация о договоре, привязанном к приглашению

Сигнатура: `InviteContract(*, sid: str, number: str, status: str | None = None, status_name: str | None = None, template_id: str | None = None, cards_count: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteItem`

Элемент списка приглашений

Сигнатура: `InviteItem(*, id: str, user_id: str | None = None, url: str, status: str, status_name: str, role: str, role_name: str, attempts: int | None = None, cards: list[api_client_opti24.models.invites.InviteCard] | None = None, initiator: str | None = None, contracts: list[api_client_opti24.models.invites.InviteContract] | None = None, mobile: str | None = None, email: str | None = None, communication_type: str | None = None, sended_at: int | None = None, expired_at: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteList`

Ответ на запрос списка приглашений

Сигнатура: `InviteList(*, total_count: int, result: list[api_client_opti24.models.invites.InviteItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `InviteResponse`

Обертка для InviteActionResult

Сигнатура: `InviteResponse(*, data: api_client_opti24.models.invites.InviteActionResult, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.limits`

### `LimitAmount`

Объёмный лимит (например, литры).

Сигнатура: `LimitAmount(*, value: float, used: float | None = None, unit: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitItem`

Продуктовый лимит (карта, группа или договор).

Сигнатура: `LimitItem(*, id: str | None = None, card_id: str | None = None, group_id: str | None = None, contract_id: str, productGroup: str | None = None, productType: str | None = None, amount: api_client_opti24.models.limits.LimitAmount | None = None, sum: api_client_opti24.models.limits.LimitSum | None = None, term: api_client_opti24.models.limits.LimitTerm | None = None, transactions: api_client_opti24.models.limits.LimitTransactions | None = None, time: api_client_opti24.models.limits.LimitTime | None = None, date: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitSum`

Денежный лимит.

Сигнатура: `LimitSum(*, currency: str, value: float, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTerm`

Периодичность и временные ограничения.

Сигнатура: `LimitTerm(*, days: str | None = None, type: int | None = None, time: api_client_opti24.models.limits.LimitTermTime | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTermTime`

Временной диапазон действия лимита.

Сигнатура: `LimitTermTime(*, from_: str, to: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTime`

Периодичность сброса лимита.

Сигнатура: `LimitTime(*, number: int | None = None, type: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTransactions`

Ограничения по количеству транзакций.

Сигнатура: `LimitTransactions(*, count: int | None = None, occured: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitsData`

Данные по лимитам.

Сигнатура: `LimitsData(*, total_count: int, result: list[api_client_opti24.models.limits.LimitItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitsResponse`

Ответ на запрос списка лимитов.

Сигнатура: `LimitsResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.limits.LimitsData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveLimitResponse`

Ответ на удаление продуктового лимита.

Сигнатура: `RemoveLimitResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `SetLimitResponse`

Ответ на установку/изменение продуктового лимита.

Сигнатура: `SetLimitResponse(*, status: dict[str, typing.Any], data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.region_limits`

### `RegionLimit`

Региональный лимит по договору, карте или группе карт.

Сигнатура: `RegionLimit(*, id: str | None, contract_id: str, card_id: str | None = None, group_id: str | None = None, country: str, region: str | None = None, service_center: str | None = None, date: str | None = None, limit_type: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RegionLimitList`

Коллекция региональных лимитов.

Сигнатура: `RegionLimitList(*, total_count: int, result: list[api_client_opti24.models.region_limits.RegionLimit], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RegionLimitResponse`

Коллекция региональных лимитов.

Сигнатура: `RegionLimitResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.region_limits.RegionLimitList, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RemoveRegionLimit`

Удаление регионального лимита.

Сигнатура: `RemoveRegionLimit(*, status: dict[str, typing.Any], data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.reports`

### `ReportFileResponse`

Ответ при генерации файла отчета.

Сигнатура: `ReportFileResponse(*, content: bytes | None = None, format: str | None = None, filename: str | None = None, size: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportItem`

Описание доступного отчета (v2).

Сигнатура: `ReportItem(*, id: str, name: str, formats: list[str], parameters: list[api_client_opti24.models.reports.ReportParameter], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportJobItem`

Элемент списка заказанных отчетов.

Сигнатура: `ReportJobItem(*, date: str, client_id: str | None = None, user_id: str | None = None, contract_id: str | None = None, contract_name: str | None = None, job_id: str, report_name: str, report_format: str, available_after: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportJobList`

Ответ со списком заказанных отчетов (v1/v2).

Сигнатура: `ReportJobList(*, total_count: int | None = None, result: list[api_client_opti24.models.reports.ReportJobItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportList`

Ответ метода /v2/reports — список доступных отчетов.

Сигнатура: `ReportList(*, total_count: int, result: list[api_client_opti24.models.reports.ReportItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderParams`

Параметры заказа отчета.

Сигнатура: `ReportOrderParams(*, start_date: str | None = None, end_date: str | None = None, id_agreement: str | None = None, id_card: list[str] | None = None, card_group_code: list[str] | None = None, id_client: list[str] | None = None, additional: dict[str, Any] | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderRequest`

Тело запроса для заказа отчета (v2).

Сигнатура: `ReportOrderRequest(*, id: str, format: str, emails: str | None = None, params: api_client_opti24.models.reports.ReportOrderParams) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportOrderResponse`

Ответ на заказ отчета (v2).

Сигнатура: `ReportOrderResponse(*, job_id: list[str], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportParameter`

Параметр отчета (например, дата, карта, договор).

Сигнатура: `ReportParameter(*, name: str, value: Any | None = None, label: str | None = None, default_value: str | None = None, menu_values: list[api_client_opti24.models.reports.ReportParameterMenuValue] | None = None, type: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportParameterMenuValue`

Значения меню для параметра отчета.

Сигнатура: `ReportParameterMenuValue(*, labels: str | None = None, values: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1JobItem`

Элемент списка ранее заказанных отчетов (v1).

Сигнатура: `ReportV1JobItem(*, date: str, client_id: str | None = None, user_id: str | None = None, contract_id: str | None = None, job_id: str, report_name: str, report_format: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1JobList`

Список заказанных отчетов (v1).

Сигнатура: `ReportV1JobList(*, jobs: list[api_client_opti24.models.reports.ReportV1JobItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ReportV1OrderResponse`

Ответ для v1 метода /reports.

Сигнатура: `ReportV1OrderResponse(*, report_ids: list[str], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.restrictions`

### `RestrictionGetResponse`

Ответ на запрос списка ограничителей (GET /restriction).

Сигнатура: `RestrictionGetResponse(*, data: api_client_opti24.models.restrictions.RestrictionList, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionItem`

Модель одного товарного ограничителя (ограничение по продукту).

Сигнатура: `RestrictionItem(*, id: str, card_id: str | None = None, group_id: str | None = None, contract_id: str, productType: str | None = None, productGroup: str | None = None, productTypeName: str | None = None, productGroupName: str | None = None, restriction_type: int, date: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionList`

Список товарных ограничителей.

Сигнатура: `RestrictionList(*, total_count: int, result: list[api_client_opti24.models.restrictions.RestrictionItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionRemoveResponse`

Ответ на удаление ограничителя (POST /removeRestriction).

Сигнатура: `RestrictionRemoveResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RestrictionSetResponse`

Ответ на установку или изменение ограничителя (POST /setRestriction).

Сигнатура: `RestrictionSetResponse(*, data: list[str], timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.templates`

### `LimitAmount`

Сигнатура: `LimitAmount(*, unit: str | None = None, value: float | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitSum`

Сигнатура: `LimitSum(*, currency: str | None = None, currencyName: str | None = None, value: float | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTerm`

Сигнатура: `LimitTerm(*, days: str | None = None, type: int | None = None, time: api_client_opti24.models.templates.LimitTermTime | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTermTime`

Сигнатура: `LimitTermTime(*, from_: str | None = None, to: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTime`

Сигнатура: `LimitTime(*, type: int | None = None, number: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `LimitTransactions`

Сигнатура: `LimitTransactions(*, count: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateCreateRequest`

Сигнатура: `TemplateCreateRequest(*, contract_id: str, type: str, name: str) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateCreateResponse`

Сигнатура: `TemplateCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateDeleteResponse`

Сигнатура: `TemplateDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestriction`

Сигнатура: `TemplateGeoRestriction(*, id: str, template_id: str, contract_id: str, date: str | None = None, country: str | None = None, countryName: str | None = None, region: str | None = None, regionName: str | None = None, partner: str | None = None, partnerName: str | None = None, service_center: str | None = None, service_centerName: str | None = None, restriction_type: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionCreateRequest`

Сигнатура: `TemplateGeoRestrictionCreateRequest(*, contract_id: str, country: str, region: str | None = None, partner: str | None = None, service_center: str | None = None, restriction_type: int) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionCreateResponse`

Сигнатура: `TemplateGeoRestrictionCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionDeleteResponse`

Сигнатура: `TemplateGeoRestrictionDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionListData`

Сигнатура: `TemplateGeoRestrictionListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateGeoRestriction], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateGeoRestrictionListResponse`

Сигнатура: `TemplateGeoRestrictionListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplateGeoRestrictionListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateItem`

Сигнатура: `TemplateItem(*, id: str, name: str, type: str, contract_id: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimit`

Сигнатура: `TemplateLimit(*, id: str, template_id: str, contract_id: str, amount: api_client_opti24.models.templates.LimitAmount | None = None, sum: api_client_opti24.models.templates.LimitSum | None = None, time: api_client_opti24.models.templates.LimitTime | None = None, term: api_client_opti24.models.templates.LimitTerm | None = None, transactions: api_client_opti24.models.templates.LimitTransactions | None = None, date: str | None = None, productType: str | None = None, productGroup: str | None = None, productTypeName: str | None = None, productGroupName: str | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitCreateRequest`

Сигнатура: `TemplateLimitCreateRequest(*, contract_id: str, product_type: str, product_group: str | None = None, sum: api_client_opti24.models.templates.LimitSum | None = None, amount: api_client_opti24.models.templates.LimitAmount | None = None, time: api_client_opti24.models.templates.LimitTime, term: api_client_opti24.models.templates.LimitTerm | None = None, create_restriction: bool | None = None) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitCreateResponse`

Сигнатура: `TemplateLimitCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitDeleteResponse`

Сигнатура: `TemplateLimitDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitListData`

Сигнатура: `TemplateLimitListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateLimit], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateLimitListResponse`

Сигнатура: `TemplateLimitListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplateLimitListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestriction`

Сигнатура: `TemplateRestriction(*, id: str, template_id: str, contract_id: str, date: str | None = None, productType: str | None = None, productGroup: str | None = None, productTypeName: str | None = None, productGroupName: str | None = None, restriction_type: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionCreateRequest`

Сигнатура: `TemplateRestrictionCreateRequest(*, contract_id: str, product_type: str, product_group: str | None = None, restriction_type: int) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionCreateResponse`

Сигнатура: `TemplateRestrictionCreateResponse(*, status: dict[str, Any] | None = None, data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionDeleteResponse`

Сигнатура: `TemplateRestrictionDeleteResponse(*, status: dict[str, Any] | None = None, data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionListData`

Сигнатура: `TemplateRestrictionListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateRestriction], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplateRestrictionListResponse`

Сигнатура: `TemplateRestrictionListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplateRestrictionListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplatesListData`

Сигнатура: `TemplatesListData(*, total_count: int, result: list[api_client_opti24.models.templates.TemplateItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TemplatesListResponse`

Сигнатура: `TemplatesListResponse(*, status: dict[str, Any] | None = None, data: api_client_opti24.models.templates.TemplatesListData, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.transactions`

### `RequestInfo`

Информация о типе и названии запроса.

Сигнатура: `RequestInfo(*, type: str, name: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionDetailResponse`

Ответ метода получения детальной информации по транзакции (v2).

Сигнатура: `TransactionDetailResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.transactions.TransactionsV2Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionItem`

Позиция (товар) внутри транзакции.

Сигнатура: `TransactionItem(*, id: str, rrn: str, product: str, amount: str, price: str, base_cost: str, cost: str, discount: str, discount_cost: str, transaction: str, currency: str, unit: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionItemV2`

Позиция в транзакции (v2).

Для спорных полей здесь сознательно приоритет отдан примерам из спецификации
и реальным ответам DEMO-стенда, а не табличным типам, которые местами
противоречат самим же payload-примерам.

Сигнатура: `TransactionItemV2(*, id: int, timestamp: datetime.datetime, utc_time: datetime.datetime | None = None, card_id: str, poi_id: str, terminal_id: str, type: str, product_id: str, product_name: str | None = None, product_category_id: str, currency: str, check_id: int, stor_transaction_id: int, is_storno: bool, is_manual_corrention: bool, qty: float, price: float, price_no_discount: float, sum: float, sum_no_discount: float, discount: float, exchange_rate: float, card_number: str, payment_type: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionV1`

Транзакция для версии v1.

Сигнатура: `TransactionV1(*, id: str, time: datetime.datetime, host_date: datetime.datetime, currency: str, card_id: str, service_center: str, card_number: str, base_cost: str, cost: str, discount: str, discount_cost: str, incoming: bool, request: api_client_opti24.models.transactions.RequestInfo, transaction_items: list[api_client_opti24.models.transactions.TransactionItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV1Data`

Сигнатура: `TransactionsV1Data(*, total_count: int, result: list[api_client_opti24.models.transactions.TransactionV1], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV1Response`

Сигнатура: `TransactionsV1Response(*, status: dict[str, typing.Any], data: api_client_opti24.models.transactions.TransactionsV1Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV2Data`

Сигнатура: `TransactionsV2Data(*, total_count: int, result: list[api_client_opti24.models.transactions.TransactionItemV2], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `TransactionsV2Response`

Сигнатура: `TransactionsV2Response(*, status: dict[str, typing.Any], data: api_client_opti24.models.transactions.TransactionsV2Data, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.users`

### `UserAccess`

Сигнатура: `UserAccess(*, web: bool, api: bool, mobile: bool, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserBoolResponse`

Сигнатура: `UserBoolResponse(*, status: dict[str, typing.Any], data: bool, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserCardItem`

Сигнатура: `UserCardItem(*, sid: str, number: str, mpc: bool, product: str | None = None, comment: str | None = None, status: str, contract_id: str, contract_name: str | None = None, available: bool, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserContractItem`

Сигнатура: `UserContractItem(*, sid: str, number: str, available: bool, template_id: str | None = None, cards_count: int | None = None, status: api_client_opti24.models.users.UserStatus | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserCreateResponse`

Сигнатура: `UserCreateResponse(*, status: dict[str, typing.Any], data: str, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserItem`

Сигнатура: `UserItem(*, id: str, login: str, first_name: str, last_name: str, middle_name: str | None = None, date: str, position: str | None = None, role: api_client_opti24.models.users.UserRole, active: bool, access: api_client_opti24.models.users.UserAccess, mobile_phone: str | None = None, email: str | None = None, contracts: list[api_client_opti24.models.users.UserContractItem] = <factory>, cards: list[api_client_opti24.models.users.UserCardItem] = <factory>, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserList`

Сигнатура: `UserList(*, total_count: int, result: list[api_client_opti24.models.users.UserItem], **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserListResponse`

Сигнатура: `UserListResponse(*, status: dict[str, typing.Any], data: api_client_opti24.models.users.UserList | None = None, timestamp: int | None = None, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserRole`

Сигнатура: `UserRole(*, id: str, name: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `UserStatus`

Сигнатура: `UserStatus(*, id: str, name: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.models.virtual_cards`

### `ConfirmVirtualCardRequest`

Сигнатура: `ConfirmVirtualCardRequest(*, card_id: str, code: str) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ConfirmVirtualCardResponse`

Сигнатура: `ConfirmVirtualCardResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DeleteMPCResponse`

Сигнатура: `DeleteMPCResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `DeleteVirtualCardResponse`

Сигнатура: `DeleteVirtualCardResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCActionResponse`

Сигнатура: `MPCActionResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCListResponse`

Сигнатура: `MPCListResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: Any, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `MPCPayloadResponse`

Сигнатура: `MPCPayloadResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: Any, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RerunVirtualCardReleaseRequest`

Сигнатура: `RerunVirtualCardReleaseRequest(*, card_id: str, reason: str | None = None) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `RerunVirtualCardReleaseResponse`

Сигнатура: `RerunVirtualCardReleaseResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: api_client_opti24.models.virtual_cards.VirtualCardData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ResendSMSRequest`

Сигнатура: `ResendSMSRequest(*, card_id: str) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ResendSMSResponse`

Сигнатура: `ResendSMSResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ResetMPCRequest`

Сигнатура: `ResetMPCRequest(*, type: str) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `ResetMPCResponse`

Сигнатура: `ResetMPCResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `SimpleActionResponse`

Сигнатура: `SimpleActionResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: bool, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `StatusModel`

Сигнатура: `StatusModel(*, code: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `VirtualCardData`

Сигнатура: `VirtualCardData(*, id: str, number: str, carrier: str, product: str, status: str, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

### `VirtualCardResponse`

Сигнатура: `VirtualCardResponse(*, status: api_client_opti24.models.virtual_cards.StatusModel, data: api_client_opti24.models.virtual_cards.VirtualCardData, timestamp: int, **extra_data: Any) -> None`

Публичные методы:

#### `describe`

Сигнатура: `describe() -> 'dict[str, dict[str, Any]]'`

## `api_client_opti24.payloads`

### `with_method_override`

Сигнатура: `with_method_override(payload: 'Mapping[str, Any] | Sequence[Mapping[str, Any]] | None', method: 'str') -> 'dict[str, Any] | list[dict[str, Any]]'`

## `api_client_opti24.policies`

### `RateLimitPolicy`

RateLimitPolicy(requests_per_second: 'float | None' = None)

Сигнатура: `RateLimitPolicy(requests_per_second: 'float | None' = None) -> None`

### `RetryClass`

Сигнатура: `RetryClass(*values)`

### `RetryPolicy`

RetryPolicy(network_attempts: 'int' = 5, rate_limit_attempts: 'int' = 3, network_backoff_min_seconds: 'float' = 2.0, network_backoff_max_seconds: 'float' = 60.0, rate_limit_backoff_seconds: 'float' = 0.5, auth_retry_min_interval_seconds: 'float' = 5.0)

Сигнатура: `RetryPolicy(network_attempts: 'int' = 5, rate_limit_attempts: 'int' = 3, network_backoff_min_seconds: 'float' = 2.0, network_backoff_max_seconds: 'float' = 60.0, rate_limit_backoff_seconds: 'float' = 0.5, auth_retry_min_interval_seconds: 'float' = 5.0) -> None`

Публичные методы:

#### `initial_network_backoff`

Сигнатура: `initial_network_backoff(self, retry_class: 'str | RetryClass') -> 'float'`

#### `network_attempt_count`

Сигнатура: `network_attempt_count(self, retry_class: 'str | RetryClass', http_method: 'str', *, idempotent: 'bool | None' = None) -> 'int'`

#### `rate_limit_attempt_count`

Сигнатура: `rate_limit_attempt_count(self, retry_class: 'str | RetryClass', http_method: 'str', *, idempotent: 'bool | None' = None) -> 'int'`

## `api_client_opti24.registry`

### `MethodRegistry`

Сигнатура: `MethodRegistry(specs: 'dict[str, EndpointSpec] | None' = None) -> 'None'`

Публичные методы:

#### `find_by_endpoint`

Сигнатура: `find_by_endpoint(self, endpoint: 'str', version: 'str', http_method: 'str | None' = None) -> 'EndpointSpec | None'`

#### `get`

Сигнатура: `get(self, name: 'str') -> 'EndpointSpec'`

#### `list_all`

Сигнатура: `list_all(self) -> 'tuple[EndpointSpec, ...]'`

#### `list_domain`

Сигнатура: `list_domain(self, domain: 'str') -> 'tuple[EndpointSpec, ...]'`

#### `register`

Сигнатура: `register(self, spec: 'EndpointSpec') -> 'None'`

### `build_default_registry`

Сигнатура: `build_default_registry() -> 'MethodRegistry'`

## `api_client_opti24.response`

### `ResponseDecoder`

Сигнатура: `ResponseDecoder(*, logger: 'LoggerLike | None' = None) -> 'None'`

Публичные методы:

#### `decode`

Сигнатура: `decode(self, response: 'httpx.Response', endpoint: 'str', *, method_name: 'str | None' = None) -> 'DecodedPayload'`

#### `decode_bytes`

Сигнатура: `decode_bytes(self, response: 'httpx.Response', content: 'bytes', endpoint: 'str', *, method_name: 'str | None' = None) -> 'bytes'`

#### `parse`

Сигнатура: `parse(self, response: 'httpx.Response') -> 'DecodedPayload'`

## `api_client_opti24.runtime`

### `Clock`

Сигнатура: `Clock(*args, **kwargs)`

Публичные методы:

#### `monotonic`

Сигнатура: `monotonic(self) -> 'float'`

#### `now`

Сигнатура: `now(self) -> 'datetime'`

#### `sleep`

Сигнатура: `sleep(self, seconds: 'float') -> 'None'`

### `SystemClock`

Сигнатура: `SystemClock()`

Публичные методы:

#### `monotonic`

Сигнатура: `monotonic(self) -> 'float'`

#### `now`

Сигнатура: `now(self) -> 'datetime'`

#### `sleep`

Сигнатура: `sleep(self, seconds: 'float') -> 'None'`

## `api_client_opti24.service_base`

### `APIKeyProvider`

Сигнатура: `APIKeyProvider(*args, **kwargs)`

Публичные методы:

#### `get_api_key`

Сигнатура: `get_api_key(self) -> 'str'`

### `CredentialsProvider`

Сигнатура: `CredentialsProvider(*args, **kwargs)`

Публичные методы:

#### `get_credentials`

Сигнатура: `get_credentials(self) -> 'tuple[str, str]'`

### `RequestExecutor`

Сигнатура: `RequestExecutor(*args, **kwargs)`

Публичные методы:

#### `execute`

Сигнатура: `execute(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'JSONPayload'`

#### `execute_stream`

Сигнатура: `execute_stream(self, operation: 'str', *, api_version: 'str | None' = None, route_name: 'str' = 'default', path_params: 'PathParams | None' = None, **kwargs: 'Any') -> 'bytes'`

### `ServiceMethodContext`

Сигнатура: `ServiceMethodContext(*args, **kwargs)`

### `SessionContext`

Сигнатура: `SessionContext(*args, **kwargs)`

### `SessionGate`

Сигнатура: `SessionGate(*args, **kwargs)`

Публичные методы:

#### `ensure_authenticated`

Сигнатура: `ensure_authenticated(self) -> 'str'`

### `SessionMutator`

Сигнатура: `SessionMutator(*args, **kwargs)`

Публичные методы:

#### `invalidate`

Сигнатура: `invalidate(self) -> 'None'`

#### `mark_authenticated`

Сигнатура: `mark_authenticated(self, session_id: 'str', contract_id: 'str | None' = None) -> 'None'`

#### `reset`

Сигнатура: `reset(self) -> 'None'`

#### `set_contract`

Сигнатура: `set_contract(self, contract_id: 'str | None') -> 'None'`

### `SessionRecovery`

Сигнатура: `SessionRecovery(*args, **kwargs)`

Публичные методы:

#### `recover`

Сигнатура: `recover(self) -> 'str'`

## `api_client_opti24.service_groups`

### `ServiceContainer`

ServiceContainer(auth: 'AuthService', card_groups: 'CardGroupsService', cards: 'CardsService', contracts: 'ContractsService', dictionaries: 'DictionariesService', ewallet: 'EwalletService', final_prices: 'FinalPricesService', invites: 'InvitesService', limits: 'LimitsService', region_limits: 'RegionLimitsService', reports: 'ReportsService', restrictions: 'RestrictionsService', templates: 'TemplatesService', transactions: 'TransactionsService', users: 'UsersService', virtual_cards: 'VirtualCardsService')

Сигнатура: `ServiceContainer(auth: 'AuthService', card_groups: 'CardGroupsService', cards: 'CardsService', contracts: 'ContractsService', dictionaries: 'DictionariesService', ewallet: 'EwalletService', final_prices: 'FinalPricesService', invites: 'InvitesService', limits: 'LimitsService', region_limits: 'RegionLimitsService', reports: 'ReportsService', restrictions: 'RestrictionsService', templates: 'TemplatesService', transactions: 'TransactionsService', users: 'UsersService', virtual_cards: 'VirtualCardsService') -> None`

Публичные методы:

#### `create`

Сигнатура: `create(*, request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike', auth: 'AuthService') -> 'ServiceContainer'`

## `api_client_opti24.services`

_Публичные классы и функции не обнаружены._

## `api_client_opti24.services.auth`

### `AuthService`

Сигнатура: `AuthService(request_executor: api_client_opti24.service_base.RequestExecutor, session_context: api_client_opti24.service_base.SessionContext, session_gate: api_client_opti24.service_base.SessionGate, session_mutator: api_client_opti24.service_base.SessionMutator, authenticator: api_client_opti24.authentication.Authenticator, clock: api_client_opti24.runtime.Clock, logger: logging.Logger) -> None`

Публичные методы:

#### `auth_user`

Сигнатура: `auth_user(self, *, api_version: str | None = None, contract_id: str | None = None, contract_number: str | None = None) -> api_client_opti24.models.auth.AuthUserResponse`

Авторизоваться и выбрать договор для последующих запросов.

Типовой сценарий:
    Выполнить авторизацию в начале интеграционного сценария и сохранить
    только идентификатор выбранного договора. Session ID SDK хранит и
    обновляет самостоятельно.

Пример вызова:
```python
auth = await client.auth.auth_user(contract_number="TEST-001")
contract_id = auth.data.contracts[0].id
```

Payload формируется из ``CredentialsProvider`` и выбранного договора;
логин, пароль и session ID не должны попадать в журналирование.

#### `get_info`

Сигнатура: `get_info(self, api_version: str | None = None, period: str | None = None) -> api_client_opti24.models.auth.GetInfoResponse`

Получение статистических данных по вызовам всех методов.

#### `logoff`

Сигнатура: `logoff(self, api_version: str | None = None) -> dict[str, object]`

Завершить серверную сессию и очистить локальное состояние клиента.

Вызывайте метод в ``finally`` или используйте контекстный менеджер
``APIClient``. Session ID не следует выводить в логи.

## `api_client_opti24.services.card_group`

### `CardGroupsService`

Методы для работы с группами карт (v1).

Сигнатура: `CardGroupsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_card_groups`

Сигнатура: `get_card_groups(self, *, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.card_group.CardGroupListResponse`

Получить список групп карт по договору.

#### `remove_card_group`

Сигнатура: `remove_card_group(self, *, contract_id: str, group_id: str, api_version: str | None = None) -> api_client_opti24.models.card_group.RemoveCardGroupResponse`

Удалить группу карт по ID.

Args:
    contract_id: Идентификатор договора.
    group_id: Идентификатор группы карт.

#### `set_card_group`

Сигнатура: `set_card_group(self, *, contract_id: str, name: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.card_group.SetCardGroupResponse`

Создать новую или изменить существующую группу карт.

Args:
    contract_id: Идентификатор договора.
    name: Название группы карт.
    group_id: (опционально) ID группы для изменения.

Типовой сценарий:
    Создать группу для отдельного подразделения, затем добавить карты
    через ``set_cards_to_group``.

Пример вызова:
```python
group = await client.card_groups.set_card_group(
    contract_id="contract-id",
    name="Служебные автомобили",
)
```

Пример payload:
```json
{"contract_id": "contract-id", "name": "Служебные автомобили"}
```

#### `set_cards_to_group`

Сигнатура: `set_cards_to_group(self, *, contract_id: str, group_id: str, cards_list: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.card_group.SetCardsToGroupResponse`

Добавление карт в группу.

Args:
    contract_id: Идентификатор договора.
    group_id: Идентификатор группы карт.
    cards_list: Список карт и действий, например:
        [{"id": "2728111", "type": "Attach"}, {"id": "2728112", "type": "Attach"}]

## `api_client_opti24.services.cards`

### `CardsService`

Методы работы с топливными картами.

Сигнатура: `CardsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `block_card`

Сигнатура: `block_card(self, contract_id: str, card_ids: list[str], block: bool = True, api_version: str | None = None) -> api_client_opti24.models.cards.IDListResponse`

Блокировка или разблокировка топливных карт.

Типовой сценарий:
    Немедленно заблокировать одну или несколько утраченных карт. Для
    обратной операции передайте ``block=False``.

Пример вызова:
```python
result = await client.cards.block_card(
    contract_id="contract-id",
    card_ids=["card-id-1", "card-id-2"],
    block=True,
)
```

Пример payload:
```json
{
  "contract_id": "contract-id",
  "card_id": ["card-id-1", "card-id-2"],
  "block": "true"
}
```

#### `get_card_detail`

Сигнатура: `get_card_detail(self, contract_id: str, card_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.CardDetailResponse`

Получение детальной информации по карте.

#### `get_card_drivers`

Сигнатура: `get_card_drivers(self, card_id: str, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.CardDriversResponse`

Получение списка водителей по карте.

#### `get_cards_by_group`

Сигнатура: `get_cards_by_group(self, contract_id: str, group_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.CardGroupResponse`

Получение списка топливных карт по группе карт.

#### `get_cards_v1`

Сигнатура: `get_cards_v1(self, contract_id: str, cache: bool = True, api_version: str | None = None) -> api_client_opti24.models.cards.CardsListResponse`

Список топливных карт (Процессинг).
:param contract_id: Идентификатор договора
:param cache: Кеш карт. false или не задан - данные берутся по прямому запросу из процессинга.
:return: Объект CardsListResponse с данными о картах

#### `get_cards_v2`

Сигнатура: `get_cards_v2(self, contract_id: str | None = None, sort: str = '-id', q: str | None = None, status: str | None = None, carrier: str | None = None, platon: bool | None = None, avtodor: bool | None = None, users: bool | None = None, group_id: str | None = None, page: int | None = None, onpage: int | None = None, api_version: str | None = None) -> api_client_opti24.models.cards.CardsV2Response`

Получение списка карт договора (v2).
:param contract_id: Идентификатор договора
:param sort: Поле сортировки (по умолчанию '-id')
:param q: Поисковый запрос (например, часть номера карты)
:param status: Фильтр по статусу карты (Active, Locked и т.д.)
:param carrier: Тип носителя карты ('Plastic', 'Virtual Card')
:param platon: Фильтр по поддержке Платон
:param avtodor: Фильтр по поддержке Автодор
:param users: Фильтр по наличию пользователей
:param group_id: Идентификатор группы карт (опционально)
:param page: Номер страницы (по умолчанию 1)
:param onpage: Количество элементов на странице (по умолчанию 10)
:return: Объект CardsV2Response с данными о картах

#### `reset_pin`

Сигнатура: `reset_pin(self, card_id: str, contract_id: str, code: str, api_version: str | None = None) -> api_client_opti24.models.cards.BoolResponse`

Подтверждение сброса PIN карты.
Данный метод позволяет завершить операцию со сбросом попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
Код подтверждения будет отправлен на почту, которая привязана к вашей учетной записи.

#### `set_card_comment`

Сигнатура: `set_card_comment(self, card_id: str, contract_id: str, comment: str, api_version: str | None = None) -> api_client_opti24.models.cards.BoolResponse`

Установить комментарий на топливную карту.

#### `verify_pin`

Сигнатура: `verify_pin(self, card_id: str, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.cards.BoolResponse`

Запрос одноразового кода для сброса PIN карты.
Данный метод позволяет инициировать запрос на сброс попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
Вам будет отправлено письмо с кодом подтверждения на почту, которая привязана к вашей учетной записи.
Данный код нужно ввести в метод resetPIN для завершения операции сброса попыток.

## `api_client_opti24.services.contract`

### `ContractsService`

Сигнатура: `ContractsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_contract_data`

Сигнатура: `get_contract_data(self, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.contracts.ContractResponse`

Получение информации о контракте.

#### `get_documents`

Сигнатура: `get_documents(self, date_start: str, date_end: str, api_version: str | None = None, page: int = 1, on_page: int = 10) -> api_client_opti24.models.contracts.DocumentsResponse`

Получение списка первичных документов (номер документа, дата, сумма, НДС, номер договора и пр.).

#### `get_invoices`

Сигнатура: `get_invoices(self, api_version: str | None = None) -> api_client_opti24.models.contracts.InvoicesResponse`

Получение списка счетов на оплату.

#### `get_payments`

Сигнатура: `get_payments(self, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.contracts.PaymentsResponse`

Получение данных о платежах по контракту.

#### `order_cards`

Сигнатура: `order_cards(self, count: int, office_id: str, api_version: str | None = None) -> api_client_opti24.models.contracts.OrderCardsResponse`

Заказ необходимого количества топливных карт в определенном офисе продаж.

#### `order_documents_email`

Сигнатура: `order_documents_email(self, ids: list[str], fmt: str, emails: list[str], api_version: str | None = None) -> api_client_opti24.models.contracts.DocumentsOrderResponse`

Заказ первичных документов по ID документа на указанные email – адреса (до 5 адресов).

#### `order_invoice`

Сигнатура: `order_invoice(self, amount: float, email: str, api_version: str | None = None) -> api_client_opti24.models.contracts.InvoiceOrderResponse`

Заказать счёт на оплату и отправить его на email.

Типовой сценарий:
    Сформировать счёт на заданную сумму после проверки адреса
    получателя. Повтор запроса выполняйте только после проверки статуса
    предыдущей операции.

Пример вызова:
```python
invoice = await client.contracts.order_invoice(
    amount=15000.0,
    email="billing@example.org",
)
```

Пример payload:
```json
{"sum": 15000.0, "email": "billing@example.org"}
```

## `api_client_opti24.services.dictionaries`

### `DictionariesService`

Методы для работы со справочниками и торговыми точками

Сигнатура: `DictionariesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_azs_filters`

Сигнатура: `get_azs_filters(self, *, api_version: str | None = None) -> api_client_opti24.models.dictionaries.AzsFiltersResponse`

Получить список доступных фильтров для поиска торговых точек (АЗС)

#### `get_azs_list_v1`

Сигнатура: `get_azs_list_v1(self, page: int = 1, onpage: int = 10, filter: dict[str, Any] | None = None, id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.dictionaries.AzsListV1Response`

Получение списка торговых точек (АЗС, версия 1)

Позволяет получить список АЗС с фильтрацией и пагинацией.

#### `get_azs_list_v2`

Сигнатура: `get_azs_list_v2(self, filter: dict[str, Any] | None = None, q: str | None = None, api_version: str | None = None) -> api_client_opti24.models.dictionaries.AzsListV2Response`

Получение списка торговых точек (АЗС, версия 2)

Новая версия метода с расширенной фильтрацией и улучшенной структурой ответа.

Типовой сценарий:
    Получить доступные торговые точки перед расчётом финальных цен или
    построением маршрута.

Пример вызова:
```python
stations = await client.dictionaries.get_azs_list_v2(
    filter={"services": ["fuel"]},
    q="Новосибирск",
)
```

Пример query-параметров:
```json
{"filter": {"services": ["fuel"]}, "q": "Новосибирск"}
```

#### `get_dictionary`

Сигнатура: `get_dictionary(self, *, name: str, api_version: str | None = None) -> api_client_opti24.models.dictionaries.DictionaryResponse`

Получить общий справочник по имени.

Примеры доступных справочников:
- CardStatus – статусы карт
- ContractStatus – статусы договоров
- Country – список стран
- Currency – список валют
- Goods – виды топлива
- PaymentScheme – схемы оплаты
- PaymentTerm – условия оплаты
- ProductGroup – группы продуктов
- ProductType – типы продуктов
- POIType – типы торговых точек
- Region – регионы
- Services – услуги на АЗС
- Unit – единицы измерения
- Office – офисы продаж
- POIPartner – партнёры
- DiscountScheme – схемы расчёта скидок

## `api_client_opti24.services.ewallet`

### `EwalletService`

Методы для работы с электронными кошельками (Ewallet).

Электронный кошелёк — это тип карты, обслуживание которой производится не из средств договора,
а из отдельного кошелькового счёта. Пользователь может:
  • менять тип карты (лимитная ↔ электронный кошелёк);
  • переводить средства со счёта договора на кошелёк;
  • переводить средства обратно с кошелька на договор.

Сигнатура: `EwalletService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `move_to_card`

Сигнатура: `move_to_card(self, *, contract_id: str | None = None, card_id: str, amount: float, api_version: str | None = None) -> api_client_opti24.models.ewallet.MoveToCardResponse`

Перевести деньги со счёта договора на электронный кошелёк карты.

Args:
    contract_id: Идентификатор договора.
    card_id: Идентификатор карты-кошелька.
    amount: Сумма перевода.
    api_version: Версия API (по умолчанию v1).

Returns:
    MoveToCardResponse: Результат перевода.

Типовой сценарий:
    Пополнить электронный кошелёк конкретной карты перед поездкой.
    Операция изменяет баланс и не должна повторяться вслепую после
    неопределённого сетевого результата.

Пример вызова:
```python
transfer = await client.ewallet.move_to_card(
    contract_id="contract-id",
    card_id="card-id",
    amount=2500.0,
)
```

Пример payload:
```json
{"contract_id": "contract-id", "card_id": "card-id", "amount": 2500.0}
```

#### `move_to_contract`

Сигнатура: `move_to_contract(self, *, contract_id: str | None = None, card_id: str, amount: float, api_version: str | None = None) -> api_client_opti24.models.ewallet.MoveToContractResponse`

Перевести деньги с электронного кошелька карты обратно на договор.

Args:
    contract_id: Идентификатор договора.
    card_id: Идентификатор карты.
    amount: Сумма перевода.
    api_version: Версия API (по умолчанию v1).

Returns:
    MoveToContractResponse: Результат перевода.

#### `set_card_product`

Сигнатура: `set_card_product(self, *, contract_id: str | None = None, card_ids: list[str], product: str, api_version: str | None = None) -> api_client_opti24.models.ewallet.SetCardProductResponse`

Изменить тип карты (лимитная ↔ электронный кошелёк).

Args:
    contract_id: Идентификатор договора (если не указан — берётся из сессии).
    card_ids: Список ID карт для изменения.
    product: Тип продукта ("limit" или "wallet").
    api_version: Версия API (по умолчанию v1).

Returns:
    SetCardProductResponse: Результат изменения продукта карт.

## `api_client_opti24.services.final_prices`

### `FinalPricesService`

Методы для получения финальных цен и проверки покупок по карте.

Сигнатура: `FinalPricesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `check_purchase`

Сигнатура: `check_purchase(self, *, card_id: str, poi_id: str, goods: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.final_prices.CheckPurchaseResponse`

Проверка возможности проведения транзакции по карте
(POST /vip/v2/cards/{card_id}/checkPurchase)

#### `get_final_prices`

Сигнатура: `get_final_prices(self, *, card_id: str, poi_id: str, goods: list[str], api_version: str | None = None) -> api_client_opti24.models.final_prices.FinalPricesResponse`

Получение финальных цен на АЗС по карте (POST /vip/v2/cards/{card_id}/calculatePrices)

Типовой сценарий:
    Перед оплатой получить персональные цены для выбранной карты,
    торговой точки и перечня товаров.

Пример вызова:
```python
prices = await client.final_prices.get_final_prices(
    card_id="card-id",
    poi_id="poi-id",
    goods=["fuel-code-1", "fuel-code-2"],
)
```

Пример payload:
```json
{"poi_id": "poi-id", "goods": ["fuel-code-1", "fuel-code-2"]}
```

## `api_client_opti24.services.invites`

### `InvitesService`

Методы для работы с приглашениями пользователей (v2).
Invites – функционал регистрации пользователей.
Приглашение можно отправить по Email/SMS или получить уникальную ссылку и отправить удобным для вас способом.
Ссылка действует 3 календарных дня, повторно направить Email/SMS по одному приглашению можно не чаще 3х раз в день.
С помощью приглашения можно зарегистрировать, например, водителя и сразу привязать шаблон виртуальной карты,
либо привязать физические топливные карты.

Сигнатура: `InvitesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `create_invite`

Сигнатура: `create_invite(self, *, data: dict[str, typing.Any], with_send: bool = True, api_version: str | None = None) -> api_client_opti24.models.invites.InviteResponse`

Создать приглашение.

with_send=True  → POST /v2/invites  (с отправкой SMS/Email)
with_send=False → POST /v2/invites_free (без отправки)

Типовой сценарий:
    Зарегистрировать водителя и передать ему приглашение. Если доставку
    выполняет внешняя система, используйте ``with_send=False``.

Пример вызова:
```python
invite = await client.invites.create_invite(
    data={
        "role": "Driver",
        "mobile": "79990000000",
        "contracts": [{"sid": "contract-id"}],
    },
    with_send=False,
)
```

Пример payload:
```json
{
  "role": "Driver",
  "mobile": "79990000000",
  "contracts": [{"sid": "contract-id"}]
}
```

#### `delete_invite`

Сигнатура: `delete_invite(self, *, invite_id: str, use_post: bool = False, api_version: str | None = None) -> api_client_opti24.models.invites.InviteBoolResponse`

Удалить приглашение (v2).

#### `get_invites`

Сигнатура: `get_invites(self, *, role: str | None = None, user_id: str | None = None, sort: str | None = None, status: str | None = None, q: str | None = None, page: int | None = None, on_page: int | None = None, api_version: str | None = None) -> api_client_opti24.models.invites.InviteList`

Получить список приглашений (v2).

Параметры фильтрации:
- role: Фильтрация по ID роли (Supervisor, Regulatory, Driver, Readonly)
- user_id: Отобразить инвайты по которым произошла регистрация пользователя (true)
- sort: поле для сортировки ('sended_at', 'status' и т.д.)
- status: Фильтрация по статусу заявки (Active, Expired, Finished)
- q: Поисковый запрос (Ищет email и mobile)
- page, on_page: пагинация

#### `prolong_invite`

Сигнатура: `prolong_invite(self, *, invite_id: str, with_send: bool = True, api_version: str | None = None) -> api_client_opti24.models.invites.InviteBoolResponse`

Продлить приглашение.

with_send=True  → POST /v2/invites/{invite_id}/prolong  (с отправкой)
with_send=False → POST /v2/invites/{invite_id}/prolong_free (без отправки)

#### `resend_invite`

Сигнатура: `resend_invite(self, *, invite_id: str, api_version: str | None = None) -> api_client_opti24.models.invites.InviteResponse`

Повторно отправить приглашение (v2).

## `api_client_opti24.services.limits`

### `LimitsService`

Методы для работы с продуктовыми лимитами (v1).

Поддерживаются:
  • Получение списка лимитов (по договору, карте или группе)
  • Установка / изменение лимита
  • Удаление лимита

Сигнатура: `LimitsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_limits`

Сигнатура: `get_limits(self, *, contract_id: str, card_id: str | None = None, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.limits.LimitsResponse`

Получить список продуктовых лимитов по договору, карте или группе карт.

:param contract_id: ID договора
:param card_id: ID карты (опционально)
:param group_id: ID группы карт (опционально)
:param api_version: версия API (по умолчанию v1)

#### `remove_limit`

Сигнатура: `remove_limit(self, *, contract_id: str, limit_id: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.limits.RemoveLimitResponse`

Удалить продуктовый лимит по карте или группе карт.
Если ID группы карты не передано, то будет удален лимит по карте.
 Если передан ID группы карт, то будет удален лимит по группе карт
:param contract_id: ID договора
:param limit_id: ID лимита
:param group_id: ID группы карт (опционально)

#### `set_limit`

Сигнатура: `set_limit(self, *, limits: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.limits.SetLimitResponse`

Для изменения уже ранее созданного лимита, требуется передавать в запросе его ID.
Для договора нельзя выставить продуктовый лимит, можно для карты или группы карт.
:param limits: список лимитов в виде словарей (см. документацию API)

Типовой сценарий:
    Ограничить дневной расход конкретной карты. Для изменения ранее
    созданного лимита добавьте его ``id`` в тот же словарь.

Пример вызова:
```python
result = await client.limits.set_limit(
    limits=[{
        "contract_id": "contract-id",
        "card_id": "card-id",
        "sum": {"currency": "810", "value": 5000.0},
        "time": {"number": 1, "type": 1},
    }]
)
```

Пример логического payload до сериализации поля ``limit``:
```json
{
  "contract_id": "contract-id",
  "card_id": "card-id",
  "sum": {"currency": "810", "value": 5000.0},
  "time": {"number": 1, "type": 1}
}
```

## `api_client_opti24.services.region_limits`

### `RegionLimitsService`

Методы для работы с региональными лимитами (v1).

Сигнатура: `RegionLimitsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_region_limits`

Сигнатура: `get_region_limits(self, *, contract_id: str, card_id: str | None = None, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.region_limits.RegionLimitResponse`

Получение списка региональных лимитов по договору, карте или группе карт.

#### `remove_region_limit`

Сигнатура: `remove_region_limit(self, *, contract_id: str, regionlimit_id: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.region_limits.RemoveRegionLimit`

Удаление регионального лимита по карте или группе карт.

#### `set_region_limit`

Сигнатура: `set_region_limit(self, *, region_limits: list[dict[str, typing.Any]], api_version: str | None = None) -> dict[str, typing.Any]`

Установка/изменение регионального лимита по карте или группе карт.
Для изменения лимита необходимо передавать его ID.

Типовой сценарий:
    Разрешить обслуживание карты только в выбранной стране или регионе.

Пример вызова:
```python
result = await client.region_limits.set_region_limit(
    region_limits=[{
        "contract_id": "contract-id",
        "card_id": "card-id",
        "country": "RUS",
        "region": "54",
        "limit_type": 1,
    }]
)
```

Пример логического payload до сериализации поля ``region_limit``:
```json
{
  "contract_id": "contract-id",
  "card_id": "card-id",
  "country": "RUS",
  "region": "54",
  "limit_type": 1
}
```

## `api_client_opti24.services.reports`

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

#### `download_report_file`

Сигнатура: `download_report_file(self, *, job_id: str, api_version: str | None = None) -> bytes`

Скачать файл отчета (по job_id).

⚠️ Важно: успешный запрос возможен только спустя ~300 секунд
после заказа отчета.

#### `download_report_file_v1`

Сигнатура: `download_report_file_v1(self, *, job_id: str, archive: bool = False, api_version: str | None = None) -> bytes`

Скачать файл отчета (v1)
После того как вы узнали Job_ID своего заказанного отчета по ссылке, его содержимое нужно получить и сформировать файл.
Формирование файла вы занимаетесь на своей стороне,
выставить имя файла, формат файл, содержимое и размер, получив от нас данные в виде потока application/octet-stream.
Если заказывать отчет с параметром archive=true, то нужно выставить формат zip и данные прийдут в виде application/zip.
Внутри архива будет находится отчет в заказанном формате (pdf, xlsx, csv, xml и другие)..

#### `get_report_job_list_v1`

Сигнатура: `get_report_job_list_v1(self, *, api_version: str | None = None) -> api_client_opti24.models.reports.ReportV1JobList`

Получить список заказанных отчетов (v1).

#### `get_report_jobs`

Сигнатура: `get_report_jobs(self, *, api_version: str | None = None) -> api_client_opti24.models.reports.ReportJobList`

Получить список заказанных отчетов (v2).

#### `get_reports`

Сигнатура: `get_reports(self, *, api_version: str | None = None) -> api_client_opti24.models.reports.ReportList`

Получить список доступных отчетов (v2).

#### `order_report`

Сигнатура: `order_report(self, *, report_id: str, format: str, params: dict[str, typing.Any], emails: str | None = None, api_version: str | None = None) -> api_client_opti24.models.reports.ReportOrderResponse`

Заказать отчет (на email или по ссылке).

Типовой сценарий:
    Сначала получить идентификатор отчёта через ``get_reports``, затем
    заказать формирование и отслеживать задачу через ``get_report_jobs``.

Пример вызова:
```python
job = await client.reports.order_report(
    report_id="report-id",
    format="xlsx",
    params={
        "contract_id": "contract-id",
        "date_from": "2026-01-01",
        "date_to": "2026-01-31",
    },
)
```

Пример payload:
```json
{
  "id": "report-id",
  "format": "xlsx",
  "params": {
    "contract_id": "contract-id",
    "date_from": "2026-01-01",
    "date_to": "2026-01-31"
  }
}
```

#### `order_report_v1`

Сигнатура: `order_report_v1(self, *, contract_id: str, start: str, end: str, report_format: str, email: str | None = None, cards_list: list[str] | None = None, group_id: list[str] | None = None, archive: bool = False, api_version: str | None = None) -> api_client_opti24.models.reports.ReportV1OrderResponse`

Заказ отчета (v1) – email или файл.

## `api_client_opti24.services.restrictions`

### `RestrictionsService`

Методы для работы с товарными ограничителями (v1).

Сигнатура: `RestrictionsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_restrictions`

Сигнатура: `get_restrictions(self, *, contract_id: str, card_id: str | None = None, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.restrictions.RestrictionGetResponse`

Получение списка товарных ограничителей по договору, карте или группе карт.

#### `remove_restriction`

Сигнатура: `remove_restriction(self, *, contract_id: str, restriction_id: str, group_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.restrictions.RestrictionRemoveResponse`

Удаление товарного ограничителя по карте или группе карт.

#### `set_restriction`

Сигнатура: `set_restriction(self, *, restrictions: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.restrictions.RestrictionSetResponse`

Установка или изменение товарного ограничителя по карте или группе карт.
Для изменения ограничителя необходимо передавать его ID.

Типовой сценарий:
    Разрешить карте покупки только выбранного типа продукта. Для
    изменения существующего ограничителя добавьте его ``id``.

Пример вызова:
```python
result = await client.restrictions.set_restriction(
    restrictions=[{
        "contract_id": "contract-id",
        "card_id": "card-id",
        "productType": "product-type-id",
        "restriction_type": 1,
    }]
)
```

Пример логического payload до сериализации поля ``restriction``:
```json
{
  "contract_id": "contract-id",
  "card_id": "card-id",
  "productType": "product-type-id",
  "restriction_type": 1
}
```

## `api_client_opti24.services.templates`

### `TemplatesService`

ВК – виртуальная карта. Чтобы выпустить ВК, потребуется создать шаблон лимита и прикрепить этот шаблон к пользователю.
Прикрепление происходит на этапе приглашения нового пользователя или методом для существующих пользователей.
Шаблон – это первоначальные параметры (Тип карты, Лимиты, Ограничители), с которыми будет выпущена эта ВК,
и все последующие, если использовать этот шаблон.
Шаблон сделан с точки зрения безопасности,
для того чтобы по-умолчанию все выпускаемые ВК имели ограничения на покупку (Лимит/Ограничитель).

Сигнатура: `TemplatesService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `create_template`

Сигнатура: `create_template(self, contract_id: str, type_: str, name: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateCreateResponse`

Создать новый шаблон виртуальной карты.

Типовой сценарий:
    Создать базовый шаблон, затем добавить к нему лимиты и ограничения
    перед выпуском виртуальной карты.

Пример вызова:
```python
template = await client.templates.create_template(
    contract_id="contract-id",
    type_="wallet",
    name="Командировки",
)
```

Пример payload:
```json
{"contract_id": "contract-id", "type": "wallet", "name": "Командировки"}
```

#### `create_template_georestriction`

Сигнатура: `create_template_georestriction(self, template_id: str, payload: dict[str, typing.Any], api_version: str | None = None) -> api_client_opti24.models.templates.TemplateGeoRestrictionCreateResponse`

Создать геоограничитель для шаблона ВК

#### `create_template_limit`

Сигнатура: `create_template_limit(self, template_id: str, payload: dict[str, typing.Any], api_version: str | None = None) -> api_client_opti24.models.templates.TemplateLimitCreateResponse`

Создать лимит для шаблона ВК

#### `create_template_restriction`

Сигнатура: `create_template_restriction(self, template_id: str, payload: dict[str, typing.Any], api_version: str | None = None) -> api_client_opti24.models.templates.TemplateRestrictionCreateResponse`

Создать ограничитель для шаблона ВК

#### `delete_template`

Сигнатура: `delete_template(self, template_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateDeleteResponse`

Удалить шаблон ВК

#### `delete_template_georestriction`

Сигнатура: `delete_template_georestriction(self, template_id: str, georestriction_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateGeoRestrictionDeleteResponse`

Удалить геоограничитель шаблона ВК

#### `delete_template_limit`

Сигнатура: `delete_template_limit(self, template_id: str, limit_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateLimitDeleteResponse`

Удалить лимит шаблона ВК

#### `delete_template_restriction`

Сигнатура: `delete_template_restriction(self, template_id: str, restriction_id: str, api_version: str | None = None, use_post: bool = False) -> api_client_opti24.models.templates.TemplateRestrictionDeleteResponse`

Удалить ограничитель шаблона ВК

#### `get_template_georestrictions`

Сигнатура: `get_template_georestrictions(self, template_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateGeoRestrictionListResponse`

Получить список геоограничителей шаблона ВК

#### `get_template_limits`

Сигнатура: `get_template_limits(self, template_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateLimitListResponse`

Получить список лимитов шаблона ВК

#### `get_template_restrictions`

Сигнатура: `get_template_restrictions(self, template_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateRestrictionListResponse`

Получить список ограничителей шаблона ВК

#### `get_templates`

Сигнатура: `get_templates(self, contract_id: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplatesListResponse`

Получить список шаблонов ВК

#### `update_template`

Сигнатура: `update_template(self, template_id: str, contract_id: str, type_: str, name: str, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateCreateResponse`

Изменить существующий шаблон ВК

#### `update_template_georestriction`

Сигнатура: `update_template_georestriction(self, template_id: str, georestriction_id: str, payload: dict[str, typing.Any], api_version: str | None = None, use_post: bool = True) -> api_client_opti24.models.templates.TemplateGeoRestrictionCreateResponse`

Изменить геоограничитель шаблона ВК

#### `update_template_limit`

Сигнатура: `update_template_limit(self, *, template_id: str, limit_id: str, limits: list[dict[str, typing.Any]], use_post: bool = True, api_version: str | None = None) -> api_client_opti24.models.templates.TemplateLimitCreateResponse`

Обновить лимит шаблона ВК.
Новые параметры описывается в виде словаря, содержащего параметры amount, sum, time, term и т.д.
Если система не поддерживает PUT — передай `use_post=True`,
тогда запрос будет отправлен методом POST с добавленным `_method="PUT"`.

Args:
    template_id (str): ID шаблона ВК
    limit_id (str): ID лимита, который нужно обновить
    limits (list[dict]): список новых параметров лимита для обновления, пример:
        [
            {
                "contract_id": "1-380B94P",
                "product_type": "1-276PF01",
                "product_group": "1-276PF0E",
                "sum": {"currency": "810", "value": 5000}, 810 - RUB, LIT - литры
                "time": {"type": 5, "number": 1},
                "term": {
                    "time": {"from": "03:00", "to": "08:00"},
                    "days": "1111100",
                    "type": 1
                }
            }
        ]
    use_post (bool): если True — POST с `_method=PUT`, иначе реальный PUT
    api_version (str): версия API (по умолчанию "v2")

Returns:
    TemplateLimitCreateResponse: объект с ID изменённого лимита

#### `update_template_restriction`

Сигнатура: `update_template_restriction(self, template_id: str, restriction_id: str, payload: dict[str, typing.Any], api_version: str | None = None, use_post: bool = True) -> api_client_opti24.models.templates.TemplateRestrictionCreateResponse`

Изменить ограничитель шаблона ВК

## `api_client_opti24.services.transactions`

### `TransactionsService`

Методы для работы с транзакциями (v1 и v2).

Сигнатура: `TransactionsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `get_card_transactions_v2`

Сигнатура: `get_card_transactions_v2(self, *, card_id: str, contract_id: str | None = None, date_from: str, date_to: str, page_limit: int = 100, page_offset: int = 0, api_version: str | None = None, filter_fn: collections.abc.Callable[[api_client_opti24.models.transactions.TransactionItemV2], bool] | None = None, sort_by: str | None = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV2Response`

Получение списка транзакций по карте (v2).

:param card_id: Идентификатор карты
:param contract_id: Идентификатор договора (если не указан, берётся из сессии)
:param date_from: Начало периода (YYYY-MM-DD)
:param date_to: Конец периода (YYYY-MM-DD)

#### `get_transaction_detail`

Сигнатура: `get_transaction_detail(self, *, transaction_id: str, contract_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.transactions.TransactionDetailResponse`

Получение детальной информации по транзакции (v2).

:param transaction_id: ID транзакции
:param contract_id: Идентификатор договора

#### `get_transactions_v1`

Сигнатура: `get_transactions_v1(self, *, contract_id: str, card_id: str | None = None, count: int = 20, api_version: str | None = None, filter_fn: collections.abc.Callable[[api_client_opti24.models.transactions.TransactionV1], bool] | None = None, sort_by: str | None = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV1Response`

Получение списка последних транзакций по договору или карте (v1).

:param contract_id: Идентификатор договора
:param card_id: Идентификатор карты (опционально)
:param count: Количество транзакций (по умолчанию 20)
:param filter_fn: Функция для фильтрации списка
:param sort_by: Поле для сортировки
:param reverse: Обратный порядок сортировки

#### `get_transactions_v2`

Сигнатура: `get_transactions_v2(self, *, contract_id: str, date_from: str, date_to: str, page_limit: int = 100, page_offset: int = 0, api_version: str | None = None, filter_fn: collections.abc.Callable[[api_client_opti24.models.transactions.TransactionItemV2], bool] | None = None, sort_by: str | None = None, reverse: bool = False) -> api_client_opti24.models.transactions.TransactionsV2Response`

Получение списка транзакций по договору (v2).

:param contract_id: Идентификатор договора
:param date_from: Начало периода (YYYY-MM-DD)
:param date_to: Конец периода (YYYY-MM-DD)
:param page_limit: Количество записей на странице
:param page_offset: Смещение страницы

Типовой сценарий:
    Загрузить страницу транзакций за период не более одного месяца,
    затем при необходимости применить локальную фильтрацию и сортировку.

Пример вызова:
```python
transactions = await client.transactions.get_transactions_v2(
    contract_id="contract-id",
    date_from="2026-01-01",
    date_to="2026-01-31",
    page_limit=100,
    page_offset=0,
    sort_by="date",
    reverse=True,
)
```

Пример query-параметров:
```json
{
  "contract_id": "contract-id",
  "date_from": "2026-01-01",
  "date_to": "2026-01-31",
  "page_limit": 100,
  "page_offset": 0
}
```

## `api_client_opti24.services.users`

### `UsersService`

Методы для работы с пользователями (v2).

Сигнатура: `UsersService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `attach_card`

Сигнатура: `attach_card(self, *, user_id: str, card_id: str, api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`

Прикрепление карты к пользователю.

Пример:
await client.users.attach_card(user_id="1-FK485FK", card_id="5050505")

#### `attach_contracts`

Сигнатура: `attach_contracts(self, *, user_id: str, contracts: list[dict[str, typing.Any]], api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`

Прикрепление договоров к пользователю.

Пример:
await client.users.attach_contracts(user_id="1-FK485FK", contracts=[
    {"sid": "1-380B94P", "template_id": "1-3BE470B", "use_mpc": True}
])

#### `create_user`

Сигнатура: `create_user(self, *, uuid: str, mobile: str, api_version: str | None = None) -> api_client_opti24.models.users.UserCreateResponse`

Создание водителя без персональных данных.
Данный метод позволяет создать себе технических водителей без ФИО (персональных данных),
чтобы использовать их для дальнейших интеграций. Реальных водителей стоит создавать через сервис “Инвайты”.


Типовой сценарий:
    Создать технического водителя без ФИО для последующего назначения
    договора или карты. Для реального пользователя используйте invites.

Пример вызова:
```python
await client.users.create_user(
    uuid="62f2e267-4398-4ea2-b02e-6e88b81b0958", mobile="79999999999"
)
```

Пример payload:
```json
{"uuid": "62f2e267-4398-4ea2-b02e-6e88b81b0958", "mobile": "79999999999"}
```

#### `delete_user`

Сигнатура: `delete_user(self, *, user_id: str, use_post: bool = False, api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`

Удаление пользователя.
Если ваша система не умеет отправлять DELETE запросы, то можно отправить POST, но в BODY указать _method=DELETE:
Пример:
await client.users.delete_user(user_id="1-FK485FK")

#### `detach_card`

Сигнатура: `detach_card(self, *, user_id: str, card_id: str, api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`

Открепление карты от пользователя.

Пример:
await client.users.detach_card(user_id="1-FK485FK", card_id="5050505")

#### `detach_contracts`

Сигнатура: `detach_contracts(self, *, user_id: str, contracts: list[str], api_version: str | None = None) -> api_client_opti24.models.users.UserBoolResponse`

Открепление договоров от пользователя.

Пример:
await client.users.detach_contracts(
    user_id="1-FK485FK", contracts=["1-380B94P", "1-37PYW2D"]
)

#### `get_users`

Сигнатура: `get_users(self, *, sort: str | None = None, page: int | None = None, on_page: int | None = None, q: str | None = None, filter: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.users.UserListResponse`

Получить список пользователей.

Пример:
await client.users.get_users(
    sort="id", page=1, on_page=10, q="Кирилл", filter={"role": "Driver"}
)

## `api_client_opti24.services.virtual_cards`

### `VirtualCardsService`

Методы для работы с виртуальными картами (ВК) и мобильными профилями карт (МПК)

Сигнатура: `VirtualCardsService(request_executor: 'RequestExecutor', session_context: 'SessionContext', session_gate: 'SessionGate', logger: 'LoggerLike') -> 'None'`

Публичные методы:

#### `confirm_mpc`

Сигнатура: `confirm_mpc(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`

Подтвердить выпуск МПК (POST /vip/v2/cards/{card_id}/confirmMPC).

#### `create_virtual_card`

Сигнатура: `create_virtual_card(self, user_id: str, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.VirtualCardResponse`

Выпуск виртуальной карты (старый метод POST /vip/v2/cards)

#### `delete_mpc`

Сигнатура: `delete_mpc(self, card_id: str, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.SimpleActionResponse`

Удаление мобильного профиля карты (МПК)

#### `generate_payment_qr`

Сигнатура: `generate_payment_qr(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`

Сгенерировать QR-код оплаты (POST /vip/v2/cards/{card_id}/pay).

#### `get_mpc_qr_list`

Сигнатура: `get_mpc_qr_list(self, *, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCListResponse`

Получить список выпущенных МПК/QR (GET /vip/v2/MPC).

#### `init_mpc`

Сигнатура: `init_mpc(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`

Инициализировать выпуск МПК (POST /vip/v2/cards/{card_id}/initMPC).

#### `release_virtual_card`

Сигнатура: `release_virtual_card(self, *, type_: str | None = None, template_id: str | None = None, user_id: str | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.VirtualCardResponse`

Выпуск виртуальной карты (новый метод /vip/v2/cards/release)
Можно указать:
- type (например, "wallet")
- template_id (ID шаблона ВК)
- user_id (ID пользователя)

Типовой сценарий:
    Выпустить карту пользователю по заранее настроенному шаблону лимитов
    и ограничений.

Пример вызова:
```python
card = await client.virtual_cards.release_virtual_card(
    type_="wallet",
    template_id="template-id",
    user_id="user-id",
)
```

Пример payload:
```json
{"type": "wallet", "template_id": "template-id", "user_id": "user-id"}
```

#### `reset_mpc`

Сигнатура: `reset_mpc(self, card_id: str, type_: str, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.ResetMPCResponse`

Сброс счётчиков МПК (POST /vip/v2/cards/{card_id}/resetMPC)
Тип счетчика (ResetCounterCode/ResetCounterMPC,
по-умолчанию, если не вызывать, вызывается ResetCounterCode)

#### `update_mpc`

Сигнатура: `update_mpc(self, *, card_id: str, payload: dict[str, Any] | None = None, api_version: str | None = None) -> api_client_opti24.models.virtual_cards.MPCPayloadResponse`

Обновить МПК (POST /vip/v2/cards/{card_id}/updateMPC).

## `api_client_opti24.session`

### `SessionManager`

Сигнатура: `SessionManager() -> 'None'`

Публичные методы:

#### `ensure_authenticated`

Сигнатура: `ensure_authenticated(self, authenticate: 'Callable[[], Awaitable[object]]') -> 'str'`

#### `invalidate`

Сигнатура: `invalidate(self) -> 'None'`

#### `mark_authenticated`

Сигнатура: `mark_authenticated(self, session_id: 'str', contract_id: 'str | None' = None) -> 'None'`

#### `reset`

Сигнатура: `reset(self) -> 'None'`

#### `set_contract`

Сигнатура: `set_contract(self, contract_id: 'str | None') -> 'None'`

#### `snapshot`

Сигнатура: `snapshot(self) -> 'SessionSnapshot'`

### `SessionSnapshot`

SessionSnapshot(state: 'SessionState', session_id: 'str | None', contract_id: 'str | None')

Сигнатура: `SessionSnapshot(state: 'SessionState', session_id: 'str | None', contract_id: 'str | None') -> None`

### `SessionState`

Сигнатура: `SessionState(*values)`

## `api_client_opti24.transport`

### `AsyncHTTPClient`

Сигнатура: `AsyncHTTPClient(*args, **kwargs)`

Публичные методы:

#### `aclose`

Сигнатура: `aclose(self) -> 'None'`

#### `request`

Сигнатура: `request(self, method: 'str', url: 'str', **kwargs: 'Any') -> 'httpx.Response'`

#### `stream`

Сигнатура: `stream(self, method: 'str', url: 'str', **kwargs: 'Any') -> 'AbstractAsyncContextManager[httpx.Response]'`

### `AsyncTransport`

Сигнатура: `AsyncTransport(base_url: 'str', default_timeout: 'float' = 30.0, *, http_client: 'AsyncHTTPClient | None' = None, retry_policy: 'RetryPolicy | None' = None, rate_limit_policy: 'RateLimitPolicy | None' = None, allow_insecure_http: 'bool' = False, response_decoder: 'ResponseDecoder | None' = None, logger: 'LoggerLike | None' = None, clock: 'Clock | None' = None, sleep: 'AsyncSleep' = <function sleep>, monotonic: 'Callable[[], float]' = <built-in function monotonic>)`

Публичные методы:

#### `aclose`

Сигнатура: `aclose(self) -> 'None'`

#### `request`

Сигнатура: `request(self, method: 'str', endpoint: 'str', api_version: 'str' = 'v1', headers: 'Mapping[str, str] | None' = None, timeout: 'float | None' = None, method_name: 'str | None' = None, retry_class: 'str | RetryClass | None' = None, idempotent: 'bool | None' = None, **kwargs: 'Any') -> 'DecodedPayload'`

#### `request_stream`

Сигнатура: `request_stream(self, method: 'str', endpoint: 'str', api_version: 'str' = 'v1', headers: 'Mapping[str, str] | None' = None, *, method_name: 'str | None' = None, **kwargs: 'Any') -> 'bytes'`

## `api_client_opti24.utils`

### `format_date_russian`

Сигнатура: `format_date_russian(date_str: str) -> str`

### `format_number`

Сигнатура: `format_number(number: float | int | None) -> str`

### `hash_password`

SHA-512 хэш пароля в нижнем регистре.

Сигнатура: `hash_password(password: str) -> str`

### `is_sensitive_log_key`

Сигнатура: `is_sensitive_log_key(key: str) -> bool`

### `message_mentions_sensitive_key`

Сигнатура: `message_mentions_sensitive_key(text: str) -> bool`

### `print_json`

Сигнатура: `print_json(data: Any) -> None`

### `sanitize_for_logging`

Сигнатура: `sanitize_for_logging(value: Any) -> Any`

### `scrub`

Сигнатура: `scrub(text: str) -> str`

### `to_json_param`

Сигнатура: `to_json_param(value: Any) -> str`

### `validate_month_span`

Проверка, что разница между датами не больше месяца.

Сигнатура: `validate_month_span(date_from: str, date_to: str) -> None`

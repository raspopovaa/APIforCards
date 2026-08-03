import logging
from types import TracebackType
from typing import cast

from .authentication import AuthenticationCoordinator
from .composition import compose_client_runtime
from .config import APISettings, ConnectionSettings
from .credentials import (
    StaticAPIKeyProvider,
    StaticCredentialsProvider,
    StaticLoginPasswordProvider,
)
from .executor import DefaultRequestExecutor, Transport
from .logger import (
    LoggerLike,
    ManagedLogger,
    create_client_logger,
    ensure_sanitizing_filter,
)
from .registry import MethodRegistry, build_default_registry
from .runtime import Clock, SystemClock
from .service_base import APIKeyProvider, CredentialsProvider
from .service_groups import ServiceContainer, _ServiceFacade
from .session import SessionManager
from .transport import AsyncTransport


class APIClient(_ServiceFacade):
    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        login: str | None = None,
        password: str | None = None,
        *,
        settings: ConnectionSettings | APISettings | None = None,
        transport: Transport | None = None,
        session_manager: SessionManager | None = None,
        registry: MethodRegistry | None = None,
        logger: logging.Logger | None = None,
        clock: Clock | None = None,
        credentials_provider: CredentialsProvider | None = None,
        api_key_provider: APIKeyProvider | None = None,
    ) -> None:
        legacy_api_key: str | None = None
        legacy_login: str | None = None
        legacy_password: str | None = None
        if settings is None:
            if base_url is None:
                raise ValueError("Missing APIClient setting: base_url")
            connection_settings = ConnectionSettings(base_url=base_url)
            legacy_api_key = api_key
            legacy_login = login
            legacy_password = password
        elif any(value is not None for value in (base_url, api_key, login, password)):
            raise ValueError("Pass either settings or individual credentials, not both")
        elif isinstance(settings, APISettings):
            connection_settings = settings.connection_settings()
            legacy_api_key = settings.api_key
            legacy_login = settings.login
            legacy_password = settings.password
        else:
            connection_settings = settings

        self.settings: ConnectionSettings = connection_settings
        self.__managed_logger: ManagedLogger | None = None
        if logger is not None:
            self.logger: LoggerLike = logger
            ensure_sanitizing_filter(logger)
        else:
            self.__managed_logger = create_client_logger(
                log_level=self.settings.log_level,
                logger_file=self.settings.logger_file,
                request_log_file=self.settings.request_log_file,
            )
            self.logger = self.__managed_logger.logger
        self.clock = clock or SystemClock()
        self.session_manager: SessionManager = session_manager or SessionManager()
        self.registry = registry or build_default_registry()
        self.transport: Transport = transport or AsyncTransport(
            self.settings.base_url,
            default_timeout=self.settings.timeouts.default,
            retry_policy=self.settings.retry_policy,
            rate_limit_policy=self.settings.rate_limit_policy,
            concurrency_policy=self.settings.concurrency_policy,
            allow_insecure_http=self.settings.allow_insecure_http,
            logger=self.logger,
            clock=self.clock,
        )
        auth_credentials = credentials_provider
        if auth_credentials is None:
            if not legacy_login or not legacy_password:
                raise ValueError(
                    "Missing authentication settings: login, password; "
                    "pass credentials_provider or legacy credentials"
                )
            if legacy_api_key:
                auth_credentials = StaticCredentialsProvider(
                    api_key=legacy_api_key,
                    login=legacy_login,
                    password=legacy_password,
                )
            else:
                auth_credentials = StaticLoginPasswordProvider(
                    login=legacy_login,
                    password=legacy_password,
                )
        resolved_api_key_provider = self._resolve_api_key_provider(
            api_key_provider=api_key_provider,
            credentials_provider=auth_credentials,
            legacy_api_key=legacy_api_key,
        )
        runtime = compose_client_runtime(
            api_key_provider=resolved_api_key_provider,
            credentials_provider=auth_credentials,
            transport=self.transport,
            session_manager=self.session_manager,
            registry=self.registry,
            timeouts=self.settings.timeouts,
            logger=self.logger,
            clock=self.clock,
        )
        self.authentication: AuthenticationCoordinator = runtime.authentication
        self.request_executor: DefaultRequestExecutor = runtime.request_executor
        self.services: ServiceContainer = runtime.services

    @staticmethod
    def _resolve_api_key_provider(
        *,
        api_key_provider: APIKeyProvider | None,
        credentials_provider: CredentialsProvider,
        legacy_api_key: str | None,
    ) -> APIKeyProvider:
        if api_key_provider is not None:
            return api_key_provider
        provider_method = getattr(credentials_provider, "get_api_key", None)
        if callable(provider_method):
            return cast(APIKeyProvider, credentials_provider)
        if legacy_api_key:
            return StaticAPIKeyProvider(legacy_api_key)
        raise ValueError(
            "Missing API key; pass api_key_provider or a combined credentials provider"
        )

    async def aclose(self) -> None:
        try:
            await self.transport.aclose()
        finally:
            if self.__managed_logger is not None:
                self.__managed_logger.close()

    async def __aenter__(self) -> "APIClient":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    @property
    def session_id(self) -> str | None:
        return self.session_manager.session_id

    @session_id.setter
    def session_id(self, value: str | None) -> None:
        if value is None:
            self.session_manager.invalidate()
        else:
            self.session_manager.mark_authenticated(value, self.contract_id)

    @property
    def contract_id(self) -> str | None:
        return self.session_manager.contract_id

    @contract_id.setter
    def contract_id(self, value: str | None) -> None:
        self.session_manager.set_contract(value)

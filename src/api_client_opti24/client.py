import logging
from types import TracebackType

from .authentication import AuthenticationCoordinator, build_credentials_provider
from .config import APISettings
from .executor import DefaultRequestExecutor, Transport
from .logger import LoggerLike, configure_logger, ensure_sanitizing_filter
from .logger import logger as default_logger
from .registry import MethodRegistry, build_default_registry
from .runtime import Clock, SystemClock
from .service_base import CredentialsProvider
from .service_groups import ServiceContainer, _ServiceFacade
from .services.auth import AuthService
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
        settings: APISettings | None = None,
        transport: Transport | None = None,
        session_manager: SessionManager | None = None,
        registry: MethodRegistry | None = None,
        logger: logging.Logger | None = None,
        clock: Clock | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ) -> None:
        if settings is None:
            connection_settings = {
                "base_url": base_url,
                "api_key": api_key,
            }
            missing = [name for name, value in connection_settings.items() if value is None]
            if credentials_provider is None:
                credentials = {"login": login, "password": password}
                missing.extend(name for name, value in credentials.items() if value is None)
            if missing:
                raise ValueError("Missing APIClient settings: " + ", ".join(sorted(missing)))
            assert base_url is not None
            assert api_key is not None
            settings = APISettings(
                base_url=base_url,
                api_key=api_key,
                login=login,
                password=password,
            )
        elif any(value is not None for value in (base_url, api_key, login, password)):
            raise ValueError("Pass either settings or individual credentials, not both")

        self.settings = settings
        self.logger: LoggerLike = logger or default_logger
        if logger is not None:
            ensure_sanitizing_filter(logger)
        self.clock = clock or SystemClock()
        self.session_manager: SessionManager = session_manager or SessionManager()
        self.registry = registry or build_default_registry()
        if logger is None:
            configure_logger(
                log_level=self.settings.log_level,
                logger_file=self.settings.logger_file,
            )
        self.transport: Transport = transport or AsyncTransport(
            self.settings.base_url,
            default_timeout=self.settings.timeouts.default,
            retry_policy=self.settings.retry_policy,
            rate_limit_policy=self.settings.rate_limit_policy,
            allow_insecure_http=self.settings.allow_insecure_http,
            logger=self.logger,
            clock=self.clock,
        )
        self.request_executor = DefaultRequestExecutor(
            api_key=settings.api_key,
            transport=self.transport,
            session_context=self.session_manager,
            registry=self.registry,
            timeouts=settings.timeouts,
            logger=self.logger,
            clock=self.clock,
        )
        self.authentication = AuthenticationCoordinator(
            self.session_manager,
            self.request_executor,
        )
        auth_credentials = credentials_provider
        if auth_credentials is None:
            if not settings.login or not settings.password:
                raise ValueError(
                    "Missing authentication settings: login, password; "
                    "provide them in APISettings or pass credentials_provider"
                )
            auth_credentials = build_credentials_provider(
                settings.login,
                settings.password,
            )
        auth_service = AuthService(
            self.request_executor,
            self.session_manager,
            self.authentication,
            self.session_manager,
            auth_credentials,
            self.clock,
            self.logger,
        )
        self.services = ServiceContainer.create(
            request_executor=self.request_executor,
            session_context=self.session_manager,
            session_gate=self.authentication,
            logger=self.logger,
            auth=auth_service,
        )
        self.authentication.bind(self.services.auth.auth_user)
        self.transport.set_auth_recovery(self.authentication.recover)

    async def aclose(self) -> None:
        await self.transport.aclose()

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

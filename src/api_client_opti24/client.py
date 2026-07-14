import logging
from typing import Literal

from .config import APISettings
from .decorators import get_current_api_method_name
from .logger import configure_logger, ensure_sanitizing_filter
from .logger import logger as default_logger
from .registry import MethodRegistry, MethodSpec, build_default_registry
from .runtime import Clock, SystemClock
from .service_groups import CardsService, ReportsService
from .services.auth import AuthMixin
from .services.card_group import CardGroupsMixin
from .services.cards import CardsMixin
from .services.contract import ContractMixin
from .services.dictionaries import DictionariesMixin
from .services.ewallet import EwalletMixin
from .services.final_prices import FinalPricesMixin
from .services.Invites import InviteMixin
from .services.limits import LimitsMixin
from .services.region_limits import RegionLimitsMixin
from .services.reports import ReportsMixin
from .services.restrictions import RestrictionsMixin
from .services.templates import TemplatesMixin
from .services.transactions import TransactionsMixin
from .services.users import UsersMixin
from .services.virtual_cards import VirtualCardsMixin
from .session import SessionManager
from .transport import AsyncTransport
from .utils import sanitize_for_logging


class APIClient(
    AuthMixin,
    CardsMixin,
    ReportsMixin,
    TransactionsMixin,
    ContractMixin,
    EwalletMixin,
    LimitsMixin,
    RestrictionsMixin,
    RegionLimitsMixin,
    CardGroupsMixin,
    InviteMixin,
    UsersMixin,
    TemplatesMixin,
    VirtualCardsMixin,
    FinalPricesMixin,
    DictionariesMixin,
):
    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        login: str | None = None,
        password: str | None = None,
        *,
        settings: APISettings | None = None,
        transport: AsyncTransport | None = None,
        session_manager: SessionManager | None = None,
        registry: MethodRegistry | None = None,
        logger: logging.Logger | None = None,
        clock: Clock | None = None,
    ):
        if settings is None:
            credentials = {
                "base_url": base_url,
                "api_key": api_key,
                "login": login,
                "password": password,
            }
            missing = [name for name, value in credentials.items() if value is None]
            if missing:
                raise ValueError(
                    "Missing APIClient settings: " + ", ".join(sorted(missing))
                )
            assert base_url is not None
            assert api_key is not None
            assert login is not None
            assert password is not None
            settings = APISettings(
                base_url=base_url,
                api_key=api_key,
                login=login,
                password=password,
            )
        elif any(value is not None for value in (base_url, api_key, login, password)):
            raise ValueError("Pass either settings or individual credentials, not both")

        self.settings = settings
        self.api_key = settings.api_key
        self.login = settings.login
        self.password = settings.password
        self.logger = logger or default_logger
        if logger is not None:
            ensure_sanitizing_filter(logger)
        self.clock = clock or SystemClock()
        self.session_manager = session_manager or SessionManager()
        self.registry = registry or build_default_registry()
        if logger is None:
            configure_logger(
                log_level=self.settings.log_level,
                logger_file=self.settings.logger_file,
            )
        self.transport = transport or AsyncTransport(
            self.settings.base_url,
            default_timeout=self.settings.timeouts.default,
            auth_recovery=self._recover_authentication,
            retry_policy=self.settings.retry_policy,
            rate_limit_policy=self.settings.rate_limit_policy,
            allow_insecure_http=self.settings.allow_insecure_http,
            logger=self.logger,
            clock=self.clock,
        )
        if transport is not None:
            transport.set_auth_recovery(self._recover_authentication)
        self.cards = CardsService(self)
        self.reports = ReportsService(self)

    async def _recover_authentication(self) -> dict[str, str]:
        self.session_manager.invalidate()
        await self.session_manager.ensure_authenticated(self.auth_user)
        return self._headers(include_session=True)

    async def aclose(self) -> None:
        await self.transport.aclose()

    async def __aenter__(self) -> "APIClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.aclose()

    def _headers(
        self,
        include_session: bool = False,
        content_type_json: Literal[True, False] = False,
    ) -> dict[str, str]:
        headers = {
            "api_key": self.api_key,
            "date_time": self.clock.now().strftime("%Y-%m-%d %H:%M:%S"),
            "User-Agent": "apiclientopti24",
            "Content-Type": (
                "application/json" if content_type_json else "application/x-www-form-urlencoded"
            ),
        }
        if include_session and self.session_id:
            headers["session_id"] = self.session_id
        if self.contract_id:
            headers["contract_id"] = self.contract_id
        self.logger.debug("Prepared headers: %s", sanitize_for_logging(headers))
        return headers

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

    def _resolve_method_spec(
        self,
        endpoint: str,
        api_version: str,
        http_method: str | None = None,
    ) -> MethodSpec | None:
        return self.registry.find_by_endpoint(endpoint, api_version, http_method=http_method)

    async def _request(self, *args, **kwargs):
        method_name = get_current_api_method_name()
        http_method = args[0] if len(args) > 0 else kwargs.get("method")
        endpoint = args[1] if len(args) > 1 else kwargs.get("endpoint")
        api_version = kwargs.get("api_version", "v1")
        spec = None
        if method_name is not None:
            try:
                spec = self.registry.get(method_name)
            except KeyError:
                spec = None
        if spec is None and endpoint:
            spec = self._resolve_method_spec(endpoint, api_version, http_method=http_method)
        timeout_class = spec.timeout_class if spec is not None else "default"
        retry_class = spec.retry_class if spec is not None else None
        idempotent = spec.idempotent if spec is not None else None
        self.logger.debug(
            "Preparing API request operation=%s version=%s",
            spec.name if spec is not None else "unregistered",
            api_version,
        )
        result = await self.transport.request(
            *args,
            timeout=self.settings.timeouts.resolve(timeout_class),
            method_name=spec.name if spec is not None else None,
            retry_class=retry_class,
            idempotent=idempotent,
            **kwargs,
        )
        self.logger.debug("Received response type: %s", type(result).__name__)
        return result

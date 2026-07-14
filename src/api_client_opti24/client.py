from datetime import datetime
from typing import Literal, Optional

from .config import APISettings
from .decorators import get_current_api_method_name
from .logger import configure_logger, logger
from .registry import MethodSpec, build_default_registry
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
    def __init__(self, base_url: str, api_key: str, login: str, password: str):
        self.settings = APISettings(
            base_url=base_url,
            api_key=api_key,
            login=login,
            password=password,
        )
        self.api_key = api_key
        self.login = login
        self.password = password
        self.session_manager = SessionManager()
        self.registry = build_default_registry()
        configure_logger(
            log_level=self.settings.log_level,
            logger_file=self.settings.logger_file,
        )
        self.transport = AsyncTransport(
            self.settings.base_url,
            client=self,
            default_timeout=self.settings.timeouts.default,
        )

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
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "User-Agent": "apiclientopti24",
            "Content-Type": (
                "application/json" if content_type_json else "application/x-www-form-urlencoded"
            ),
        }
        if include_session and self.session_id:
            headers["session_id"] = self.session_id
        if self.contract_id:
            headers["contract_id"] = self.contract_id
        logger.debug("Prepared headers: %s", sanitize_for_logging(headers))
        return headers

    @property
    def session_id(self) -> Optional[str]:
        return self.session_manager.session_id

    @session_id.setter
    def session_id(self, value: Optional[str]) -> None:
        if value is None:
            self.session_manager.invalidate()
        else:
            self.session_manager.mark_authenticated(value, self.contract_id)

    @property
    def contract_id(self) -> Optional[str]:
        return self.session_manager.contract_id

    @contract_id.setter
    def contract_id(self, value: Optional[str]) -> None:
        self.session_manager.set_contract(value)

    def _resolve_method_spec(
        self,
        endpoint: str,
        api_version: str,
        http_method: str | None = None,
    ) -> MethodSpec | None:
        return self.registry.find_by_endpoint(endpoint, api_version, http_method=http_method)

    async def _request(self, *args, **kwargs):
        logger.debug(
            "Sending request with args: %s, kwargs: %s",
            sanitize_for_logging(args),
            sanitize_for_logging(kwargs),
        )
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
        result = await self.transport.request(
            *args,
            timeout=self.settings.timeouts.resolve(timeout_class),
            method_name=spec.name if spec is not None else None,
            **kwargs,
        )
        logger.debug("Received response type: %s", type(result).__name__)
        return result

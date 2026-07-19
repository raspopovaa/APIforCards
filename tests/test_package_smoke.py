from __future__ import annotations

import inspect
import logging
from datetime import datetime

import pytest

import api_client_opti24 as sdk
from api_client_opti24 import APIClient, __version__
from api_client_opti24.config import APISettings
from api_client_opti24.registry import build_default_registry

SERVICE_TYPES = {
    "auth": "AuthService",
    "card_groups": "CardGroupsService",
    "cards": "CardsService",
    "contracts": "ContractsService",
    "dictionaries": "DictionariesService",
    "ewallet": "EwalletService",
    "final_prices": "FinalPricesService",
    "invites": "InvitesService",
    "limits": "LimitsService",
    "region_limits": "RegionLimitsService",
    "reports": "ReportsService",
    "restrictions": "RestrictionsService",
    "templates": "TemplatesService",
    "transactions": "TransactionsService",
    "users": "UsersService",
    "virtual_cards": "VirtualCardsService",
}

DOMAIN_SERVICES = {
    "auth": "auth",
    "card_group": "card_groups",
    "cards": "cards",
    "contract": "contracts",
    "dictionaries": "dictionaries",
    "ewallet": "ewallet",
    "final_prices": "final_prices",
    "invites": "invites",
    "limits": "limits",
    "region_limits": "region_limits",
    "reports": "reports",
    "restrictions": "restrictions",
    "templates": "templates",
    "transactions": "transactions",
    "users": "users",
    "virtual_cards": "virtual_cards",
}


def test_package_root_exports_client() -> None:
    assert APIClient.__name__ == "APIClient"


def test_package_root_exports_version() -> None:
    assert __version__ == "2.0.0"


def test_settings_factory_is_available() -> None:
    assert callable(APISettings.from_env)


@pytest.mark.asyncio
async def test_client_exposes_all_composition_services_without_credentials(tmp_path) -> None:
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
        logger_file=str(tmp_path / "sdk.log"),
    )

    client = APIClient(settings=settings)

    for attribute_name, class_name in SERVICE_TYPES.items():
        service = getattr(client, attribute_name)
        assert isinstance(service, getattr(sdk, class_name))
        assert client not in vars(service).values()

    assert isinstance(client.services, sdk.ServiceContainer)
    assert not hasattr(client, "api_key")
    assert not hasattr(client, "login")
    assert not hasattr(client, "password")
    assert not hasattr(client.cards, "settings")
    assert not hasattr(client.cards, "transport")
    container_factory = inspect.signature(sdk.ServiceContainer.create)
    assert "credentials_provider" not in container_factory.parameters
    await client.aclose()


@pytest.mark.asyncio
async def test_credentials_provider_is_injected_only_into_auth_service(tmp_path) -> None:
    class TrackingCredentialsProvider:
        def __init__(self) -> None:
            self.calls = 0

        def get_credentials(self) -> tuple[str, str]:
            self.calls += 1
            return "injected-login", "injected-password"

    provider = TrackingCredentialsProvider()
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="unused-login",
        password="unused-password",
        logger_file=str(tmp_path / "sdk.log"),
    )
    client = APIClient(settings=settings, credentials_provider=provider)

    for name in SERVICE_TYPES:
        if name != "auth":
            assert provider not in vars(getattr(client, name)).values()
    assert provider in vars(client.auth).values()
    assert provider.calls == 0

    await client.aclose()


@pytest.mark.asyncio
async def test_credentials_provider_does_not_require_placeholder_credentials() -> None:
    class ExternalCredentialsProvider:
        def get_credentials(self) -> tuple[str, str]:
            return "external-login", "external-password"

    client = APIClient(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        credentials_provider=ExternalCredentialsProvider(),
    )

    assert client.settings.login is None
    assert client.settings.password is None
    await client.aclose()


@pytest.mark.asyncio
async def test_all_registered_methods_exist_only_on_domain_services(tmp_path) -> None:
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
        logger_file=str(tmp_path / "sdk.log"),
    )
    client = APIClient(settings=settings)

    for spec in build_default_registry().list_all():
        service = getattr(client, DOMAIN_SERVICES[spec.domain])
        assert callable(getattr(service, spec.name))
        assert not hasattr(client, spec.name)

    await client.aclose()


@pytest.mark.asyncio
async def test_client_accepts_logger_and_clock_without_configuring_log_file(tmp_path) -> None:
    class FrozenClock:
        def now(self) -> datetime:
            return datetime(2026, 7, 15, 12, 30, 0)

        def monotonic(self) -> float:
            return 0.0

        async def sleep(self, _seconds: float) -> None:
            return None

    log_path = tmp_path / "must-not-be-created.log"
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
        logger_file=str(log_path),
    )
    injected_logger = logging.getLogger(f"test-client-{id(settings)}")
    injected_logger.addHandler(logging.NullHandler())

    client = APIClient(
        settings=settings,
        logger=injected_logger,
        clock=FrozenClock(),
    )

    assert client.request_executor.headers()["date_time"] == "2026-07-15 12:30:00"
    assert all(getattr(client, name).logger is injected_logger for name in SERVICE_TYPES)
    assert not log_path.exists()
    await client.aclose()


@pytest.mark.asyncio
async def test_client_can_be_created_and_closed() -> None:
    client = APIClient(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
    )

    await client.aclose()


@pytest.mark.asyncio
async def test_client_accepts_settings_object(tmp_path) -> None:
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
        logger_file=str(tmp_path / "sdk.log"),
    )

    client = APIClient(settings=settings)

    assert client.settings is settings
    await client.aclose()


def test_client_rejects_mixed_settings_and_credentials() -> None:
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
    )

    with pytest.raises(ValueError, match="either settings or individual credentials"):
        APIClient(settings=settings, api_key="duplicate")

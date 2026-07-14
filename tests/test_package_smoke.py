from __future__ import annotations

import logging
from datetime import datetime

import pytest

from api_client_opti24 import APIClient, CardsService, ReportsService, __version__
from api_client_opti24.config import APISettings


def test_package_root_exports_client() -> None:
    assert APIClient.__name__ == "APIClient"


def test_package_root_exports_version() -> None:
    assert __version__ == "1.2.0"


def test_settings_factory_is_available() -> None:
    assert callable(APISettings.from_env)


@pytest.mark.asyncio
async def test_client_exposes_composition_services_without_credentials(tmp_path) -> None:
    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
        logger_file=str(tmp_path / "sdk.log"),
    )

    client = APIClient(settings=settings)

    assert isinstance(client.cards, CardsService)
    assert isinstance(client.reports, ReportsService)
    assert not hasattr(client.cards, "api_key")
    assert not hasattr(client.cards, "password")
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

    assert client._headers()["date_time"] == "2026-07-15 12:30:00"
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

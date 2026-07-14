from __future__ import annotations

import pytest

from api_client_opti24 import APIClient
from api_client_opti24.config import APISettings


def test_package_root_exports_client() -> None:
    assert APIClient.__name__ == "APIClient"


def test_settings_factory_is_available() -> None:
    assert callable(APISettings.from_env)


@pytest.mark.asyncio
async def test_client_can_be_created_and_closed() -> None:
    client = APIClient(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
    )

    await client.aclose()

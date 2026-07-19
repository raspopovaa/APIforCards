import logging
from datetime import datetime
from typing import Any

import pytest

from api_client_opti24.config import TimeoutPolicy
from api_client_opti24.executor import DefaultRequestExecutor
from api_client_opti24.registry import build_default_registry
from api_client_opti24.response import DecodedPayload
from api_client_opti24.session import SessionManager
from api_client_opti24.transport import AuthRecovery


class StubTransport:
    def __init__(self, response: DecodedPayload) -> None:
        self.response = response

    def set_auth_recovery(self, auth_recovery: AuthRecovery) -> None:
        self.auth_recovery = auth_recovery

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        **kwargs: Any,
    ) -> DecodedPayload:
        del method, endpoint, api_version, kwargs
        return self.response

    async def request_stream(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes:
        del method, endpoint, api_version, headers, kwargs
        return b""

    async def aclose(self) -> None:
        return None


class FrozenClock:
    def now(self) -> datetime:
        return datetime(2026, 7, 19, 12, 30, 0)

    def monotonic(self) -> float:
        return 0.0

    async def sleep(self, seconds: float) -> None:
        del seconds
        return None


@pytest.mark.asyncio
async def test_executor_builds_headers_and_rejects_non_object_json() -> None:
    session = SessionManager()
    session.mark_authenticated("session-1", "contract-1")
    executor = DefaultRequestExecutor(
        api_key="secret-key",
        transport=StubTransport([]),
        session_context=session,
        registry=build_default_registry(),
        timeouts=TimeoutPolicy(),
        logger=logging.getLogger("test-executor"),
        clock=FrozenClock(),
    )

    assert executor.headers(include_session=True) == {
        "api_key": "secret-key",
        "date_time": "2026-07-19 12:30:00",
        "User-Agent": "apiclientopti24",
        "Content-Type": "application/x-www-form-urlencoded",
        "session_id": "session-1",
        "contract_id": "contract-1",
    }
    with pytest.raises(TypeError, match="JSON object"):
        await executor.request("get", "cards", api_version="v2")

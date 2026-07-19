import logging
from datetime import datetime
from typing import Any


class NoopRequestExecutor:
    def headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]:
        del include_session, content_type_json
        return {}

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        **kwargs: Any,
    ) -> dict[str, Any]:
        del kwargs
        raise AssertionError(f"Unexpected request: {api_version} {method} {endpoint}")

    async def request_stream(
        self,
        method: str,
        endpoint: str,
        *,
        api_version: str = "v1",
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> bytes:
        del headers, kwargs
        raise AssertionError(f"Unexpected stream request: {api_version} {method} {endpoint}")


class StubSessionGate:
    async def ensure_authenticated(self) -> str:
        return "test-session"


class StubCredentialsProvider:
    def __init__(self, login: str = "test_user", password: str = "secret") -> None:
        self.__login = login
        self.__password = password

    def get_credentials(self) -> tuple[str, str]:
        return self.__login, self.__password


class FrozenClock:
    def now(self) -> datetime:
        return datetime(2026, 7, 19, 12, 30, 0)

    def monotonic(self) -> float:
        return 0.0

    async def sleep(self, seconds: float) -> None:
        del seconds


def service_dependencies(session_manager: object) -> tuple[object, ...]:
    return (
        NoopRequestExecutor(),
        session_manager,
        StubSessionGate(),
        logging.getLogger("sdk-service-test"),
    )

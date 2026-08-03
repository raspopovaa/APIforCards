import logging
from datetime import datetime
from typing import Any


class NoopRequestExecutor:
    async def execute(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: object = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        del route_name, path_params, kwargs
        raise AssertionError(f"Unexpected request: {api_version} {operation}")

    async def execute_stream(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: object = None,
        **kwargs: Any,
    ) -> bytes:
        del route_name, path_params, kwargs
        raise AssertionError(f"Unexpected stream request: {api_version} {operation}")


class RecordingRequestExecutor:
    def __init__(self, responses: dict[str, dict[str, Any]]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def execute(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: object = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        call = {
            "api_version": api_version,
            "route_name": route_name,
            "path_params": path_params,
            **kwargs,
        }
        self.calls.append((operation, call))
        return self.responses[operation]

    async def execute_stream(
        self,
        operation: str,
        *,
        api_version: str | None = None,
        route_name: str = "default",
        path_params: object = None,
        **kwargs: Any,
    ) -> bytes:
        del operation, api_version, route_name, path_params, kwargs
        raise AssertionError("Unexpected stream request")


class StubSessionGate:
    async def ensure_authenticated(self) -> str:
        return "test-session"

    async def recover(self) -> str:
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

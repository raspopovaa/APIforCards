from __future__ import annotations

from collections.abc import Awaitable, Callable

from .models.auth import AuthUserResponse
from .service_base import AuthenticationSession, CredentialsProvider, RequestExecutor


class _StaticCredentialsProvider:
    __slots__ = ("__login", "__password")

    def __init__(self, login: str, password: str) -> None:
        self.__login = login
        self.__password = password

    def get_credentials(self) -> tuple[str, str]:
        return self.__login, self.__password


class AuthenticationCoordinator:
    def __init__(
        self,
        session: AuthenticationSession,
        request_executor: RequestExecutor,
    ) -> None:
        self.__session = session
        self.__request_executor = request_executor
        self.__authenticate: Callable[[], Awaitable[AuthUserResponse]] | None = None

    def bind(self, authenticate: Callable[[], Awaitable[AuthUserResponse]]) -> None:
        if self.__authenticate is not None:
            raise RuntimeError("Authentication callback is already configured")
        self.__authenticate = authenticate

    async def authenticate(self) -> AuthUserResponse:
        if self.__authenticate is None:
            raise RuntimeError("Authentication callback is not configured")
        return await self.__authenticate()

    async def ensure_authenticated(self) -> str:
        return await self.__session.ensure_authenticated(self.authenticate)

    async def recover(self) -> dict[str, str]:
        self.__session.invalidate()
        await self.ensure_authenticated()
        return self.__request_executor.headers(include_session=True)


def build_credentials_provider(login: str, password: str) -> CredentialsProvider:
    return _StaticCredentialsProvider(login, password)

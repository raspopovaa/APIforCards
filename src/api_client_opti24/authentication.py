from __future__ import annotations

from collections.abc import Awaitable, Callable

from .models.auth import AuthUserResponse
from .session import SessionManager


class AuthenticationCoordinator:
    def __init__(
        self,
        session: SessionManager,
    ) -> None:
        self.__session = session
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

    async def recover(self) -> str:
        self.__session.invalidate()
        return await self.ensure_authenticated()

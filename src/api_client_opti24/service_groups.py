from __future__ import annotations

import logging
from typing import Any, Protocol

from .runtime import Clock
from .services.cards import CardsMixin
from .services.reports import ReportsMixin
from .session import SessionManager
from .transport import AsyncTransport


class ServiceClient(Protocol):
    session_manager: SessionManager
    transport: AsyncTransport
    logger: logging.Logger
    clock: Clock

    @property
    def session_id(self) -> str | None: ...

    @property
    def contract_id(self) -> str | None: ...

    async def auth_user(self, **kwargs: Any) -> Any: ...

    async def _request(self, *args: Any, **kwargs: Any) -> Any: ...

    def _headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]: ...


class BoundService:
    def __init__(self, client: ServiceClient) -> None:
        self.__client = client

    @property
    def session_manager(self) -> SessionManager:
        return self.__client.session_manager

    @property
    def transport(self) -> AsyncTransport:
        return self.__client.transport

    @property
    def logger(self) -> logging.Logger:
        return self.__client.logger

    @property
    def clock(self) -> Clock:
        return self.__client.clock

    @property
    def session_id(self) -> str | None:
        return self.__client.session_id

    @property
    def contract_id(self) -> str | None:
        return self.__client.contract_id

    async def auth_user(self, **kwargs: Any) -> Any:
        return await self.__client.auth_user(**kwargs)

    async def _request(self, *args: Any, **kwargs: Any) -> Any:
        return await self.__client._request(*args, **kwargs)

    def _headers(
        self,
        include_session: bool = False,
        content_type_json: bool = False,
    ) -> dict[str, str]:
        return self.__client._headers(include_session, content_type_json)


class CardsService(CardsMixin, BoundService):
    pass


class ReportsService(ReportsMixin, BoundService):
    pass

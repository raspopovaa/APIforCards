from __future__ import annotations

import asyncio
from dataclasses import dataclass
from enum import Enum


class SessionState(str, Enum):
    ANONYMOUS = "anonymous"
    AUTHENTICATING = "authenticating"
    AUTHENTICATED = "authenticated"
    INVALID = "invalid"


@dataclass(slots=True)
class SessionSnapshot:
    state: SessionState
    session_id: str | None
    contract_id: str | None


class SessionManager:
    def __init__(self) -> None:
        self._state = SessionState.ANONYMOUS
        self._session_id: str | None = None
        self._contract_id: str | None = None
        self._auth_lock = asyncio.Lock()

    @property
    def state(self) -> SessionState:
        return self._state

    @property
    def session_id(self) -> str | None:
        return self._session_id

    @property
    def contract_id(self) -> str | None:
        return self._contract_id

    def snapshot(self) -> SessionSnapshot:
        return SessionSnapshot(
            state=self._state,
            session_id=self._session_id,
            contract_id=self._contract_id,
        )

    def set_contract(self, contract_id: str | None) -> None:
        self._contract_id = contract_id

    def mark_authenticated(self, session_id: str, contract_id: str | None = None) -> None:
        self._session_id = session_id
        self._contract_id = contract_id
        self._state = SessionState.AUTHENTICATED

    def invalidate(self) -> None:
        self._session_id = None
        self._contract_id = None
        self._state = SessionState.INVALID

    def reset(self) -> None:
        self._session_id = None
        self._contract_id = None
        self._state = SessionState.ANONYMOUS

    async def ensure_authenticated(self, authenticate) -> str:
        if self._state == SessionState.AUTHENTICATED and self._session_id:
            return self._session_id

        async with self._auth_lock:
            if self._state == SessionState.AUTHENTICATED and self._session_id:
                return self._session_id

            self._state = SessionState.AUTHENTICATING
            try:
                await authenticate()
            except Exception:
                self.invalidate()
                raise

            if not self._session_id:
                self.invalidate()
                raise RuntimeError("Authentication completed without session_id")

            self._state = SessionState.AUTHENTICATED
            return self._session_id

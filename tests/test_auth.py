import logging

import pytest

from api_client_opti24.models.auth import AuthUserResponse
from api_client_opti24.services import AuthService
from api_client_opti24.session import SessionManager, SessionState
from tests.service_support import (
    FrozenClock,
    NoopRequestExecutor,
    StubCredentialsProvider,
    StubSessionGate,
)


class DummyClient(AuthService):
    def __init__(self):
        self.session_manager = SessionManager()
        self.calls = []
        super().__init__(
            NoopRequestExecutor(),
            self.session_manager,
            StubSessionGate(),
            self.session_manager,
            StubCredentialsProvider(),
            FrozenClock(),
            logging.getLogger("auth-service-test"),
        )

    async def _request(self, operation, **kwargs):
        self.calls.append((operation, kwargs))
        if operation == "auth_user":
            return {
                "status": {"code": 200},
                "data": {
                    "session_id": "SESSION123",
                    "client_id": "client-1",
                    "client_status": "active",
                    "user_id": "user-1",
                    "contracts": [
                        {"id": "1-AAA", "number": "NV0001"},
                        {"id": "1-BBB", "number": "NV0002"},
                    ],
                },
                "timestamp": 1710000000,
            }
        elif operation == "logoff":
            return {"status": {"code": 200}, "data": True, "timestamp": 1710000000}
        elif operation == "get_info":
            return {
                "status": {"code": 200},
                "data": {
                    "from": "2025-01-01 00:00:00",
                    "to": "2025-01-31 23:59:59",
                    "client_info": {
                        "Client": "client-1",
                        "ClientType": "D",
                        "Contract": "1-AAA",
                        "ContractName": "Demo Client",
                    },
                    "methods": {"all": 42, "cards": 10, "cardgroups": 3, "card": 4},
                    "methods_info": {"actions_bill": {}, "actions_not_bill": {}},
                },
                "timestamp": 1710000000,
            }
        else:
            raise ValueError(f"Unexpected operation: {operation}")

    @property
    def session_id(self):
        return self.session_manager.session_id

    @session_id.setter
    def session_id(self, value):
        if value is None:
            self.session_manager.invalidate()
        else:
            self.session_manager.mark_authenticated(value, self.contract_id)

    @property
    def contract_id(self):
        return self.session_manager.contract_id

    @contract_id.setter
    def contract_id(self, value):
        self.session_manager.set_contract(value)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "contract_id,contract_number,expected_id",
    [
        ("1-AAA", None, "1-AAA"),  # выбор по id
        (None, "NV0002", "1-BBB"),  # выбор по номеру
        (None, None, "1-AAA"),  # автоселект первого по списку
    ],
)
async def test_auth_user_sets_session_and_contract_id(contract_id, contract_number, expected_id):
    client = DummyClient()
    response = await client.auth_user(contract_id=contract_id, contract_number=contract_number)

    assert isinstance(response, AuthUserResponse)
    assert client.session_id == "SESSION123"
    assert client.contract_id == expected_id
    assert client.session_manager.state == SessionState.AUTHENTICATED


@pytest.mark.asyncio
async def test_logoff_returns_true():
    client = DummyClient()
    client.session_id = "SESSION123"  # имитируем авторизацию

    result = await client.logoff()

    assert result["status"]["code"] == 200
    assert result["data"] is True


@pytest.mark.asyncio
async def test_get_info_returns_data():
    client = DummyClient()
    client.session_id = "SESSION123"  # имитируем авторизацию

    result = await client.get_info()

    assert result.status.code == 200
    assert result.data.client_info.ContractName == "Demo Client"
    operation, kwargs = client.calls[-1]
    assert operation == "get_info"
    assert kwargs["params"]["period"] == "2026-07-19 12:30:00"


@pytest.mark.asyncio
async def test_get_info_uses_explicit_period():
    client = DummyClient()
    client.session_id = "SESSION123"

    await client.get_info(period="2025-01-15 12:30:00")

    operation, kwargs = client.calls[-1]
    assert operation == "get_info"
    assert kwargs["params"]["period"] == "2025-01-15 12:30:00"

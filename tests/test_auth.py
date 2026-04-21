import pytest
from api_client_opti24.services import AuthMixin
from api_client_opti24.models.auth import AuthUserResponse
from api_client_opti24.session import SessionManager, SessionState


class DummyClient(AuthMixin):
    def __init__(self):
        self.login = "test_user"
        self.password = "secret"
        self.session_manager = SessionManager()

    def _headers(self, include_session: bool = False):
        headers = {"api_key": "FAKE_API_KEY"}
        if include_session and self.session_id:
            headers["session_id"] = self.session_id
        return headers

    async def _request(self, method, endpoint, **kwargs):
        if endpoint == "authUser":
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
        elif endpoint == "logoff":
            return {"status": {"code": 200}, "data": True, "timestamp": 1710000000}
        elif endpoint == "info":
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
            raise ValueError(f"Unexpected endpoint: {endpoint}")

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

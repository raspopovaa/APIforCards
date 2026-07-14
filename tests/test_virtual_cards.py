import pytest

from api_client_opti24.models.virtual_cards import (
    MPCListResponse,
    MPCPayloadResponse,
    ResetMPCResponse,
    SimpleActionResponse,
    VirtualCardResponse,
)
from api_client_opti24.services.virtual_cards import VirtualCardsMixin


class DummyClient(VirtualCardsMixin):
    def __init__(self):
        self.session_id = "mock-session"
        self._called = []

    def _headers(self, include_session: bool = False, content_type_json: bool = False):
        return {"X-Mock": "true"}

    async def _request(self, method, endpoint, api_version="v2", headers=None, **kwargs):
        self._called.append((method, endpoint, api_version, kwargs))
        if endpoint == "MPC":
            return {
                "status": {"code": 200},
                "data": [{"id": "1-MPC", "card_id": "1-CARD", "state": "Active"}],
                "timestamp": 1710000000,
            }
        if endpoint == "cards/release":
            return {
                "status": {"code": 200},
                "data": {
                    "id": "1-VC",
                    "number": "7005830900073164",
                    "carrier": "Virtual Card",
                    "product": "wallet",
                    "status": "Active",
                },
                "timestamp": 1710000000,
            }
        if endpoint in {
            "cards/1-CARD/pay",
            "cards/1-CARD/initMPC",
            "cards/1-CARD/confirmMPC",
            "cards/1-CARD/updateMPC",
        }:
            return {
                "status": {"code": 200},
                "data": {"ok": True, "endpoint": endpoint},
                "timestamp": 1710000000,
            }
        if endpoint == "cards/1-CARD/deleteMPC":
            return {"status": {"code": 200}, "data": True, "timestamp": 1710000000}
        if endpoint == "cards/1-CARD/resetMPC":
            return {"status": {"code": 200}, "data": True, "timestamp": 1710000000}
        if endpoint == "cards":
            return {
                "status": {"code": 200},
                "data": {
                    "id": "1-VC",
                    "number": "7005830900073164",
                    "carrier": "Virtual Card",
                    "product": "wallet",
                    "status": "Active",
                },
                "timestamp": 1710000000,
            }
        raise AssertionError(f"Unexpected request: {method} {endpoint}")


@pytest.mark.asyncio
async def test_virtual_card_release_methods_return_models():
    client = DummyClient()

    created = await client.create_virtual_card(user_id="1-USER")
    released = await client.release_virtual_card(user_id="1-USER")

    assert isinstance(created, VirtualCardResponse)
    assert isinstance(released, VirtualCardResponse)
    assert created.data.id == "1-VC"
    assert released.data.status == "Active"


@pytest.mark.asyncio
async def test_mpc_methods_return_models():
    client = DummyClient()

    mpc_list = await client.get_mpc_qr_list()
    qr = await client.generate_payment_qr(card_id="1-CARD", payload={"amount": 100})
    init = await client.init_mpc(card_id="1-CARD")
    confirm = await client.confirm_mpc(card_id="1-CARD", payload={"code": "1234"})
    update = await client.update_mpc(card_id="1-CARD", payload={"reason": "refresh"})
    deleted = await client.delete_mpc(card_id="1-CARD")
    reset = await client.reset_mpc(card_id="1-CARD", type_="ResetCounterCode")

    assert isinstance(mpc_list, MPCListResponse)
    assert isinstance(qr, MPCPayloadResponse)
    assert isinstance(init, MPCPayloadResponse)
    assert isinstance(confirm, MPCPayloadResponse)
    assert isinstance(update, MPCPayloadResponse)
    assert isinstance(deleted, SimpleActionResponse)
    assert isinstance(reset, ResetMPCResponse)
    assert mpc_list.data[0]["id"] == "1-MPC"
    assert qr.data["ok"] is True

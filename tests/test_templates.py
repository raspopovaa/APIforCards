import pytest

from api_client_opti24.services.templates import TemplatesMixin
from api_client_opti24.session import SessionManager


class DummyTemplatesClient(TemplatesMixin):
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.session_manager.mark_authenticated("session-1", "contract-1")
        self.calls = []

    @property
    def session_id(self):
        return self.session_manager.session_id

    @property
    def contract_id(self):
        return self.session_manager.contract_id

    def _headers(self, include_session: bool = False):
        return {"session_id": self.session_id} if include_session else {}

    async def _request(self, method, endpoint, **kwargs):
        self.calls.append((method, endpoint, kwargs))
        return {"data": "limit-1"}


@pytest.mark.asyncio
async def test_update_template_limit_does_not_mutate_input() -> None:
    client = DummyTemplatesClient()
    limits = [
        {
            "contract_id": "contract-1",
            "sum": {"currency": "810", "value": 5000},
            "time": {"type": 5, "number": 1},
        }
    ]

    response = await client.update_template_limit(
        template_id="template-1",
        limit_id="limit-1",
        limits=limits,
        use_post=True,
    )

    method, endpoint, kwargs = client.calls[-1]
    assert response.data == "limit-1"
    assert method == "post"
    assert endpoint == "vc/templates/template-1/limits/limit-1"
    assert kwargs["json"][0]["_method"] == "PUT"
    assert "_method" not in limits[0]

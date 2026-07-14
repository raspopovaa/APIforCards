from api_client_opti24.modeling import BaseModel, Field, decode_model
from api_client_opti24.models.auth import AuthUserResponse


class AdapterExample(BaseModel):
    name: str = Field(...)
    count: int = Field(...)


def test_model_descriptions_are_available():
    description = AuthUserResponse.describe()

    assert "status" in description
    assert description["status"]["description"] == "Статус ответа API"


def test_model_descriptions_render_human_readable_types():
    description = AuthUserResponse.describe()

    assert description["status"]["type"] == "StatusResponse"
    assert description["data"]["type"] == "AuthUserData"
    assert description["timestamp"]["type"] == "int | None"


def test_model_validate_and_dump_support_incremental_adapter():
    model = decode_model(AdapterExample, {"name": "demo", "count": "2"})

    assert model.count == 2
    assert model.model_dump() == {"name": "demo", "count": 2}

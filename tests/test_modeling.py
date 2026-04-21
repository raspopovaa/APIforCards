from api_client_opti24.models.auth import AuthUserResponse


def test_model_descriptions_are_available():
    description = AuthUserResponse.describe()

    assert "status" in description
    assert description["status"]["description"] == "Статус ответа API"


def test_model_descriptions_render_human_readable_types():
    description = AuthUserResponse.describe()

    assert description["status"]["type"] == "StatusResponse"
    assert description["data"]["type"] == "AuthUserData"
    assert description["timestamp"]["type"] == "int | None"

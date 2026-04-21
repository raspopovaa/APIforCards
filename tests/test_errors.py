from api_client_opti24.errors import NotAuthenticatedError, ValidationError, build_api_error


def test_build_api_error_preserves_raw_payload_and_error_type():
    body = {
        "status": {
            "code": 400,
            "errors": [
                {
                    "type": "validationFailed",
                    "message": "Invalid contract_id",
                }
            ],
        }
    }

    exc = build_api_error(status_code=400, body=body, endpoint="cards")

    assert isinstance(exc, ValidationError)
    assert exc.context.error_type == "validationFailed"
    assert exc.context.raw_payload == body
    assert exc.context.messages == ("Invalid contract_id",)


def test_build_api_error_maps_auth_errors():
    body = {
        "status": {
            "code": 401,
            "errors": [
                {
                    "type": "notAuthenticated",
                    "message": "Необходима авторизация",
                }
            ],
        }
    }

    exc = build_api_error(status_code=401, body=body, endpoint="info")

    assert isinstance(exc, NotAuthenticatedError)
    assert exc.context.messages == ("Необходима авторизация",)

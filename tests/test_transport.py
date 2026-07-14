import pytest
import httpx
from httpx import Response, Request
from api_client_opti24 import AsyncTransport
from api_client_opti24.errors import (
    APIError,
    AccessDeniedError,
    NotAuthenticatedError,
    NotFoundError,
    RateLimitError,
    ServerError,
)


class DummyResp(Response):
    """Простейший заглушка для имитации ответов httpx.Response"""

    def __init__(self, status_code, text=None, json_data=None):
        self._text = text
        self._json_data = json_data
        self._request = Request(method="GET", url="http://example.com/endpoint")
        super().__init__(status_code=status_code, content=text.encode() if text else b"")

    def json(self):
        if self._json_data is not None:
            return self._json_data
        return self.text  # Возвращаем текст вместо исключения

    @property
    def text(self):
        return self._text or ""


def test_handle_response_success_json():
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(200, json_data={"ok": True})
    result = t._handle_response(resp, "test")
    assert result == {"ok": True}


def test_handle_response_success_text_fallback():
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(200, text="plain text")
    result = t._handle_response(resp, "test")
    assert result == "plain text"


def test_handle_response_raises_on_payload_error_inside_http_200():
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(
        200,
        json_data={
            "status": {
                "code": 401,
                "errors": [{"type": "notAuthenticated", "message": "Session expired"}],
            }
        },
    )

    with pytest.raises(NotAuthenticatedError) as exc_info:
        t._handle_response(resp, "info")

    assert exc_info.value.http_status_code == 200
    assert exc_info.value.api_status_code == 401


@pytest.mark.parametrize(
    "status,exc_type",
    [
        (403, AccessDeniedError),
        (404, NotFoundError),
        (429, RateLimitError),
        (500, ServerError),
        (418, APIError),  # I'm a teapot :)
    ],
)
def test_handle_response_errors(status, exc_type):
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(status, text="error response")
    with pytest.raises(exc_type):
        t._handle_response(resp, "endpoint")


@pytest.mark.asyncio
async def test_request_retries_rate_limit_then_succeeds(monkeypatch):
    class DummyParent:
        session_manager = None

    transport = AsyncTransport(base_url="http://example.com", client=DummyParent())
    transport._rate_limit_backoff_seconds = 0
    calls = 0

    async def fake_request(method, url, headers=None, timeout=None, **kwargs):
        nonlocal calls
        calls += 1
        if calls < 3:
            return DummyResp(509, text="rate limited")
        return DummyResp(200, json_data={"ok": True})

    monkeypatch.setattr(transport.client, "request", fake_request)

    result = await transport.request("get", "endpoint")

    assert result == {"ok": True}
    assert calls == 3


@pytest.mark.asyncio
async def test_request_retries_network_errors_then_succeeds(monkeypatch):
    class DummyParent:
        session_manager = None

    transport = AsyncTransport(base_url="http://example.com", client=DummyParent())
    transport._network_backoff_min_seconds = 0
    transport._network_backoff_max_seconds = 0
    calls = 0

    async def fake_request(method, url, headers=None, timeout=None, **kwargs):
        nonlocal calls
        calls += 1
        if calls < 3:
            raise httpx.RequestError("temporary network failure")
        return DummyResp(200, json_data={"ok": True})

    monkeypatch.setattr(transport.client, "request", fake_request)

    result = await transport.request("get", "endpoint")

    assert result == {"ok": True}
    assert calls == 3

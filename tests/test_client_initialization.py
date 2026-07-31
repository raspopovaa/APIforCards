import logging

import pytest

import api_client_opti24.client as client_module
from api_client_opti24 import APIClient
from api_client_opti24.config import APISettings


def test_client_closes_managed_logger_when_transport_initialization_fails(
    monkeypatch,
) -> None:
    class FakeManagedLogger:
        def __init__(self) -> None:
            self.logger = logging.getLogger("failed-client-init")
            self.closed = False

        def close(self) -> None:
            self.closed = True

    managed_logger = FakeManagedLogger()

    def create_logger(**kwargs):
        del kwargs
        return managed_logger

    class FailingTransport:
        def __init__(self, *args, **kwargs) -> None:
            del args, kwargs
            raise RuntimeError("transport initialization failed")

    monkeypatch.setattr(client_module, "create_client_logger", create_logger)
    monkeypatch.setattr(client_module, "AsyncTransport", FailingTransport)

    settings = APISettings(
        base_url="https://example.invalid/vip/",
        api_key="demo-key",
        login="demo-login",
        password="demo-password",
    )

    with pytest.raises(RuntimeError, match="transport initialization failed"):
        APIClient(settings=settings)

    assert managed_logger.closed is True

from __future__ import annotations

import importlib
import io
import logging
import os
from pathlib import Path

from api_client_opti24 import config as config_module
from api_client_opti24 import env as env_module
from api_client_opti24 import logger as logger_module


def test_config_import_does_not_load_dotenv(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    monkeypatch.setattr(env_module, "load_env_file", lambda: (_ for _ in ()).throw(AssertionError()))

    importlib.reload(config_module)

    assert config_module.API_KEY == ""


def test_from_env_loads_dotenv_when_requested(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)

    def fake_load_env_file(path: str | Path) -> None:
        assert path == ".env"
        os.environ["API_KEY"] = "loaded-from-env-file"

    monkeypatch.setattr(config_module, "load_env_file", fake_load_env_file)

    settings = config_module.APISettings.from_env()

    assert settings.api_key == "loaded-from-env-file"


def test_from_env_uses_explicit_env_file(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    captured_path = None

    def fake_load_env_file(path: str | Path) -> None:
        nonlocal captured_path
        captured_path = path

    monkeypatch.setattr(config_module, "load_env_file", fake_load_env_file)

    config_module.APISettings.from_env(env_file=env_file)

    assert captured_path == env_file


def test_from_env_loads_request_rate_limit(monkeypatch):
    monkeypatch.setenv("API_REQUESTS_PER_SECOND", "2")
    monkeypatch.setattr(config_module, "load_env_file", lambda _path: None)

    settings = config_module.APISettings.from_env()

    assert settings.rate_limit_policy.requests_per_second == 2
    assert settings.rate_limit_policy.minimum_interval_seconds == 0.5


def test_from_env_requires_explicit_insecure_http_opt_in(monkeypatch):
    monkeypatch.setenv("API_ALLOW_INSECURE_HTTP", "true")
    monkeypatch.setattr(config_module, "load_env_file", lambda _path: None)

    settings = config_module.APISettings.from_env()

    assert settings.allow_insecure_http is True


def test_configure_logger_creates_sanitized_file_handler(tmp_path):
    log_path = tmp_path / "sdk.log"

    logger_module.configure_logger("INFO", str(log_path))

    assert any(isinstance(handler, logging.FileHandler) for handler in logger_module.logger.handlers)

    logger_module.logger.info("api_key=%s password=%s", "secret-key", "secret-pass")

    content = log_path.read_text(encoding="utf-8")

    assert "secret-key" not in content
    assert "secret-pass" not in content
    assert "***" in content


def test_bound_logger_receives_service_logs_with_sanitizing_filter():
    stream = io.StringIO()
    injected_logger = logging.getLogger(f"bound-logger-{id(stream)}")
    injected_logger.handlers.clear()
    injected_logger.propagate = False
    injected_logger.setLevel(logging.INFO)
    injected_logger.addHandler(logging.StreamHandler(stream))

    token = logger_module.bind_logger(injected_logger)
    try:
        logger_module.logger.info("card_id=%s", "sensitive-card-id")
    finally:
        logger_module.reset_logger(token)

    assert "sensitive-card-id" not in stream.getvalue()
    assert "***" in stream.getvalue()

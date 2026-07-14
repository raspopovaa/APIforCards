from __future__ import annotations

import importlib
import logging
import os

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

    def fake_load_env_file() -> None:
        os.environ["API_KEY"] = "loaded-from-env-file"

    monkeypatch.setattr(config_module, "load_env_file", fake_load_env_file)

    settings = config_module.APISettings.from_env()

    assert settings.api_key == "loaded-from-env-file"


def test_configure_logger_creates_sanitized_file_handler(tmp_path):
    log_path = tmp_path / "sdk.log"

    logger_module.configure_logger("INFO", str(log_path))

    assert any(isinstance(handler, logging.FileHandler) for handler in logger_module.logger.handlers)

    logger_module.logger.info("api_key=%s password=%s", "secret-key", "secret-pass")

    content = log_path.read_text(encoding="utf-8")

    assert "secret-key" not in content
    assert "secret-pass" not in content
    assert "***" in content

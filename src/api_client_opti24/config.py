from __future__ import annotations

import os
from dataclasses import dataclass

from .env import load_env_file


@dataclass(frozen=True, slots=True)
class TimeoutPolicy:
    default: float = 30.0
    auth: float = 30.0
    read_heavy: float = 120.0

    def resolve(self, timeout_class: str) -> float:
        return getattr(self, timeout_class, self.default)


@dataclass(frozen=True, slots=True)
class APISettings:
    base_url: str
    api_key: str
    login: str
    password: str
    request_log_file: str = "./api_requests.jsonl"
    logger_file: str = "./api.log"
    log_level: str = "INFO"
    timeouts: TimeoutPolicy = TimeoutPolicy()

    @classmethod
    def from_env(cls, *, load_dotenv: bool = True) -> "APISettings":
        if load_dotenv:
            load_env_file()
        return cls(
            base_url=os.getenv("API_BASE_URL", ""),
            api_key=os.getenv("API_KEY", ""),
            login=os.getenv("API_LOGIN", ""),
            password=os.getenv("API_PASSWORD", ""),
            request_log_file=os.getenv("REQUEST_LOG_FILE", "./api_requests.jsonl"),
            logger_file=os.getenv("LOGGER_FILE", "./api.log"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )

SETTINGS = APISettings.from_env(load_dotenv=False)
BASE_URL = SETTINGS.base_url
API_KEY = SETTINGS.api_key
LOGIN = SETTINGS.login
PASSWORD = SETTINGS.password
REQUEST_LOG_FILE = SETTINGS.request_log_file
LOGGER_FILE = SETTINGS.logger_file
LOG_LEVEL = SETTINGS.log_level

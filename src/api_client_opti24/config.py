from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from .env import load_env_file
from .policies import RateLimitPolicy, RetryPolicy


@dataclass(frozen=True, slots=True)
class TimeoutPolicy:
    default: float = 30.0
    auth: float = 30.0
    read_heavy: float = 120.0

    def resolve(self, timeout_class: str) -> float:
        return {
            "default": self.default,
            "auth": self.auth,
            "read_heavy": self.read_heavy,
        }.get(timeout_class, self.default)


@dataclass(frozen=True, slots=True)
class APISettings:
    base_url: str
    api_key: str = field(repr=False)
    login: str | None = field(default=None, repr=False)
    password: str | None = field(default=None, repr=False)
    request_log_file: str = "./api_requests.jsonl"
    logger_file: str = "./api.log"
    log_level: str = "INFO"
    allow_insecure_http: bool = False
    timeouts: TimeoutPolicy = TimeoutPolicy()
    retry_policy: RetryPolicy = RetryPolicy()
    rate_limit_policy: RateLimitPolicy = RateLimitPolicy()

    @classmethod
    def from_env(
        cls,
        *,
        load_dotenv: bool = True,
        env_file: str | Path = ".env",
    ) -> APISettings:
        if load_dotenv:
            load_env_file(env_file)
        requests_per_second = os.getenv("API_REQUESTS_PER_SECOND")
        return cls(
            base_url=os.getenv("API_BASE_URL", ""),
            api_key=os.getenv("API_KEY", ""),
            login=os.getenv("API_LOGIN"),
            password=os.getenv("API_PASSWORD"),
            request_log_file=os.getenv("REQUEST_LOG_FILE", "./api_requests.jsonl"),
            logger_file=os.getenv("LOGGER_FILE", "./api.log"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            allow_insecure_http=os.getenv("API_ALLOW_INSECURE_HTTP", "false").lower()
            in {"1", "true", "yes"},
            rate_limit_policy=RateLimitPolicy(
                requests_per_second=(float(requests_per_second) if requests_per_second else None)
            ),
        )

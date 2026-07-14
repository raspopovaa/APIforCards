import logging
from contextvars import ContextVar, Token
from typing import Any

from .utils import REDACTED, message_mentions_sensitive_key, sanitize_for_logging, scrub

DEFAULT_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(module)s: %(message)s"


class SanitizingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        has_args = bool(record.args)
        if has_args:
            if isinstance(record.args, dict):
                record.args = sanitize_for_logging(record.args)
            else:
                if isinstance(record.msg, str) and message_mentions_sensitive_key(record.msg):
                    record.args = tuple(
                        REDACTED if isinstance(arg, str) else sanitize_for_logging(arg)
                        for arg in record.args
                    )
                else:
                    record.args = tuple(sanitize_for_logging(arg) for arg in record.args)

        if isinstance(record.msg, str) and not has_args:
            record.msg = scrub(record.msg)

        return True

_default_logger = logging.getLogger("api_client_opti24")
sanitizing_filter = SanitizingFilter()
_default_logger.addFilter(sanitizing_filter)
_default_logger.addHandler(logging.NullHandler())
_default_logger.propagate = False
_active_logger: ContextVar[logging.Logger | None] = ContextVar(
    "api_client_opti24_logger",
    default=None,
)


class ContextLogger:
    def __getattr__(self, name: str) -> Any:
        active_logger = _active_logger.get() or _default_logger
        return getattr(active_logger, name)


logger = ContextLogger()

_configured_signature: tuple[str, str] | None = None


def configure_logger(log_level: str, logger_file: str) -> None:
    global _configured_signature

    signature = (log_level.upper(), logger_file)
    if _configured_signature == signature:
        return

    resolved_level = getattr(logging, log_level.upper(), logging.INFO)
    _default_logger.setLevel(resolved_level)

    for handler in list(_default_logger.handlers):
        _default_logger.removeHandler(handler)
        close = getattr(handler, "close", None)
        if callable(close):
            close()

    file_handler = logging.FileHandler(logger_file, mode="w")
    file_handler.setLevel(resolved_level)
    file_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
    file_handler.addFilter(sanitizing_filter)
    _default_logger.addHandler(file_handler)

    _configured_signature = signature


def ensure_sanitizing_filter(target: logging.Logger) -> None:
    if not any(isinstance(item, SanitizingFilter) for item in target.filters):
        target.addFilter(SanitizingFilter())


def bind_logger(target: logging.Logger | ContextLogger) -> Token[logging.Logger | None]:
    if isinstance(target, ContextLogger):
        target = _default_logger
    ensure_sanitizing_filter(target)
    return _active_logger.set(target)


def reset_logger(token: Token[logging.Logger | None]) -> None:
    _active_logger.reset(token)

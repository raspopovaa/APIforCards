import logging

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

logger = logging.getLogger("api_client_opti24")
sanitizing_filter = SanitizingFilter()
logger.addFilter(sanitizing_filter)
logger.addHandler(logging.NullHandler())
logger.propagate = False

_configured_signature: tuple[str, str] | None = None


def configure_logger(log_level: str, logger_file: str) -> None:
    global _configured_signature

    signature = (log_level.upper(), logger_file)
    if _configured_signature == signature:
        return

    resolved_level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(resolved_level)

    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        close = getattr(handler, "close", None)
        if callable(close):
            close()

    file_handler = logging.FileHandler(logger_file, mode="w")
    file_handler.setLevel(resolved_level)
    file_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
    file_handler.addFilter(sanitizing_filter)
    logger.addHandler(file_handler)

    _configured_signature = signature

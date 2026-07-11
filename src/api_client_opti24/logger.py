import logging

from .config import LOG_LEVEL, LOGGER_FILE
from .utils import sanitize_for_logging, scrub


class SanitizingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.args:
            if isinstance(record.args, dict):
                record.args = sanitize_for_logging(record.args)
            else:
                record.args = tuple(sanitize_for_logging(arg) for arg in record.args)

        if isinstance(record.msg, str):
            record.msg = scrub(record.msg)

        return True

log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    filename=LOGGER_FILE,
    filemode="w",
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
)
logger = logging.getLogger("api_client_opti24")
sanitizing_filter = SanitizingFilter()
logger.addFilter(sanitizing_filter)

for handler in logging.getLogger().handlers:
    handler.addFilter(sanitizing_filter)

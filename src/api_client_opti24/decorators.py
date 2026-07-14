import functools
from contextvars import ContextVar

from .logger import bind_logger, reset_logger
from .logger import logger as default_logger
from .session import SessionManager

_current_api_method_name: ContextVar[str | None] = ContextVar(
    "current_api_method_name",
    default=None,
)


def get_current_api_method_name() -> str | None:
    return _current_api_method_name.get()


def api_method(
    require_session: bool = False,
    default_version: str = "v1",
    *,
    http_method: str | None = None,
    endpoint: str | None = None,
    retry_class: str | None = None,
):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            token = _current_api_method_name.set(func.__name__)
            method_name = f"{self.__class__.__name__}.{func.__name__}"
            active_logger = getattr(self, "logger", default_logger)
            logger_token = bind_logger(active_logger)
            if "api_version" not in kwargs:
                kwargs["api_version"] = default_version

            try:
                if require_session:
                    active_logger.info("[%s] ensuring authenticated session", method_name)
                    session_manager = getattr(self, "session_manager", None)
                    if session_manager is None:
                        session_manager = SessionManager()
                        session_id = getattr(self, "session_id", None)
                        contract_id = getattr(self, "contract_id", None)
                        if session_id is not None:
                            session_manager.mark_authenticated(session_id, contract_id)
                        self.session_manager = session_manager

                    current_session_id = getattr(self, "session_id", None)
                    if session_manager.session_id is None and current_session_id:
                        session_manager.mark_authenticated(
                            current_session_id,
                            getattr(self, "contract_id", None),
                        )

                    auth_user = getattr(self, "auth_user", None)
                    if auth_user is not None:
                        await session_manager.ensure_authenticated(auth_user)
                    elif session_manager.session_id is None:
                        raise RuntimeError(
                            f"{method_name} requires session but auth_user is unavailable"
                        )

                active_logger.info(
                    "Calling API method=%s version=%s",
                    method_name,
                    kwargs.get("api_version"),
                )

                result = await func(self, *args, **kwargs)
                active_logger.info(
                    "API method completed method=%s result_type=%s",
                    method_name,
                    type(result).__name__,
                )
                return result
            except Exception as exc:
                active_logger.error(
                    "API method failed method=%s error_type=%s",
                    method_name,
                    type(exc).__name__,
                    exc_info=True,
                )
                raise
            finally:
                reset_logger(logger_token)
                _current_api_method_name.reset(token)

        wrapper.__api_method_config__ = {
            "require_session": require_session,
            "default_version": default_version,
            "http_method": http_method.upper() if http_method is not None else None,
            "endpoint": endpoint,
            "retry_class": retry_class,
        }

        return wrapper

    return decorator

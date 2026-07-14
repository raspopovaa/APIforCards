import functools
from contextvars import ContextVar

from .logger import logger
from .session import SessionManager
from .utils import sanitize_for_logging

_current_api_method_name: ContextVar[str | None] = ContextVar(
    "current_api_method_name",
    default=None,
)


def get_current_api_method_name() -> str | None:
    return _current_api_method_name.get()


def api_method(require_session: bool = False, default_version: str = "v1"):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            token = _current_api_method_name.set(func.__name__)
            method_name = f"{self.__class__.__name__}.{func.__name__}"
            if "api_version" not in kwargs:
                kwargs["api_version"] = default_version

            try:
                if require_session:
                    logger.info("[%s] ensuring authenticated session", method_name)
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

                logger.info(
                    "➡ Вызов %s, args=%s, kwargs=%s",
                    method_name,
                    sanitize_for_logging(args),
                    sanitize_for_logging(kwargs),
                )

                result = await func(self, *args, **kwargs)
                logger.info("✅ %s завершён. Тип результата: %s", method_name, type(result).__name__)
                return result
            except Exception as e:
                logger.error("❌ Ошибка в %s: %s", method_name, e, exc_info=True)
                raise
            finally:
                _current_api_method_name.reset(token)

        wrapper.__api_method_config__ = {
            "require_session": require_session,
            "default_version": default_version,
        }

        return wrapper

    return decorator

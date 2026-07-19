import functools
from collections.abc import Awaitable, Callable
from contextvars import ContextVar
from typing import Concatenate, ParamSpec, TypeVar, cast

from .logger import bind_logger, reset_logger
from .service_base import ServiceMethodContext

ServiceT = TypeVar("ServiceT", bound=ServiceMethodContext)
Params = ParamSpec("Params")
ResultT = TypeVar("ResultT")

_current_api_method_name: ContextVar[str | None] = ContextVar(
    "current_api_method_name",
    default=None,
)


def get_current_api_method_name() -> str | None:
    return _current_api_method_name.get()


def api_method(
    require_session: bool = False,
    default_version: str = "v1",
) -> Callable[
    [Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]]],
    Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]],
]:
    def decorator(
        func: Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]],
    ) -> Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]]:
        @functools.wraps(func)
        async def wrapper(
            self: ServiceT,
            *args: Params.args,
            **kwargs: Params.kwargs,
        ) -> ResultT:
            token = _current_api_method_name.set(func.__name__)
            method_name = f"{self.__class__.__name__}.{func.__name__}"
            active_logger = self.logger
            logger_token = bind_logger(active_logger)
            api_version = dict(kwargs).get("api_version", default_version)

            try:
                if require_session:
                    active_logger.info("[%s] ensuring authenticated session", method_name)
                    await self.session_gate.ensure_authenticated()

                active_logger.info(
                    "Calling API method=%s version=%s",
                    method_name,
                    api_version,
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

        return cast(
            Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]],
            wrapper,
        )

    return decorator

import functools
from collections.abc import Awaitable, Callable
from typing import Concatenate, ParamSpec, TypeVar, cast

from .service_base import ServiceMethodContext

ServiceT = TypeVar("ServiceT", bound=ServiceMethodContext)
Params = ParamSpec("Params")
ResultT = TypeVar("ResultT")


def api_method(
    func: Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]],
) -> Callable[
    Concatenate[ServiceT, Params],
    Awaitable[ResultT],
]:
    @functools.wraps(func)
    async def wrapper(
        self: ServiceT,
        *args: Params.args,
        **kwargs: Params.kwargs,
    ) -> ResultT:
        method_name = f"{self.__class__.__name__}.{func.__name__}"
        active_logger = self.logger
        api_version = dict(kwargs).get("api_version", "registry-default")

        try:
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

    return cast(
        Callable[Concatenate[ServiceT, Params], Awaitable[ResultT]],
        wrapper,
    )

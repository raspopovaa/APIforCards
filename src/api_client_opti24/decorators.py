from collections.abc import Awaitable, Callable
from typing import Concatenate, ParamSpec, TypeVar

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
    return func

from __future__ import annotations

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
from typing import Any

try:
    __version__ = version("api-client-opti24")
except PackageNotFoundError:
    __version__ = "0+unknown"

__all__ = [
    "APIClient",
    "APISettings",
    "AsyncTransport",
    "CardsService",
    "Clock",
    "EndpointSpec",
    "MethodRegistry",
    "MethodSpec",
    "RateLimitPolicy",
    "RetryClass",
    "RetryPolicy",
    "ReportsService",
    "ResponseDecoder",
    "SessionManager",
    "SessionState",
    "SystemClock",
    "TimeoutPolicy",
    "__version__",
]

_EXPORTS = {
    "APIClient": (".client", "APIClient"),
    "APISettings": (".config", "APISettings"),
    "AsyncTransport": (".transport", "AsyncTransport"),
    "CardsService": (".service_groups", "CardsService"),
    "Clock": (".runtime", "Clock"),
    "EndpointSpec": (".endpoints", "EndpointSpec"),
    "MethodRegistry": (".registry", "MethodRegistry"),
    "MethodSpec": (".registry", "MethodSpec"),
    "RateLimitPolicy": (".policies", "RateLimitPolicy"),
    "RetryClass": (".policies", "RetryClass"),
    "RetryPolicy": (".policies", "RetryPolicy"),
    "ReportsService": (".service_groups", "ReportsService"),
    "ResponseDecoder": (".response", "ResponseDecoder"),
    "SessionManager": (".session", "SessionManager"),
    "SessionState": (".session", "SessionState"),
    "SystemClock": (".runtime", "SystemClock"),
    "TimeoutPolicy": (".config", "TimeoutPolicy"),
}


def __getattr__(name: str) -> Any:
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError as exc:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from exc

    module = import_module(module_name, __name__)
    value = getattr(module, attribute_name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))

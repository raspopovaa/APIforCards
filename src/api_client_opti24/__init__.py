from __future__ import annotations

from importlib import import_module
from typing import Any

__all__ = [
    "APIClient",
    "AsyncTransport",
    "MethodRegistry",
    "MethodSpec",
    "SessionManager",
    "SessionState",
]

_EXPORTS = {
    "APIClient": (".client", "APIClient"),
    "AsyncTransport": (".transport", "AsyncTransport"),
    "MethodRegistry": (".registry", "MethodRegistry"),
    "MethodSpec": (".registry", "MethodSpec"),
    "SessionManager": (".session", "SessionManager"),
    "SessionState": (".session", "SessionState"),
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

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ErrorContext:
    error_type: str | None
    messages: tuple[str, ...]
    raw_payload: Any
    endpoint: str | None
    method_name: str | None


class APIError(Exception):
    def __init__(
        self,
        status_code: int,
        message: str = "",
        body: Any = None,
        endpoint: str | None = None,
        *,
        error_type: str | None = None,
        messages: tuple[str, ...] | None = None,
        method_name: str | None = None,
    ) -> None:
        super().__init__(f"{status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.body = body
        self.endpoint = endpoint
        self.context = ErrorContext(
            error_type=error_type,
            messages=messages or (() if not message else (message,)),
            raw_payload=body,
            endpoint=endpoint,
            method_name=method_name,
        )

    def __str__(self) -> str:
        location = f" during {self.endpoint}" if self.endpoint else ""
        return f"{self.__class__.__name__}: [{self.status_code}] {self.message}{location}"


class ValidationError(APIError):
    pass


class NotAuthenticatedError(APIError):
    pass


class AccessDeniedError(APIError):
    pass


class NotFoundError(APIError):
    pass


class DuplicateConflictError(APIError):
    pass


class ServerError(APIError):
    pass


def build_api_error(
    *,
    status_code: int,
    body: Any,
    endpoint: str | None,
    method_name: str | None = None,
) -> APIError:
    error_map: dict[str, type[APIError]] = {
        "validationFailed": ValidationError,
        "notAuthenticated": NotAuthenticatedError,
        "accessDenied": AccessDeniedError,
        "notFound": NotFoundError,
        "duplicateConflict": DuplicateConflictError,
        "internalError": ServerError,
    }

    error_type: str | None = None
    messages: tuple[str, ...] = ()
    message = "Unknown API error"

    if isinstance(body, dict):
        status = body.get("status")
        errors = status.get("errors") if isinstance(status, dict) else None
        if isinstance(errors, list) and errors:
            first_error = errors[0]
            if isinstance(first_error, dict):
                error_type = first_error.get("type")
                raw_message = first_error.get("message")
                if isinstance(raw_message, list):
                    messages = tuple(str(item) for item in raw_message)
                elif raw_message is not None:
                    messages = (str(raw_message),)
                message = messages[0] if messages else message

    if not messages and isinstance(body, str) and body:
        messages = (body,)
        message = body

    if error_type is None:
        if status_code == 400:
            exc_type = ValidationError
        elif status_code == 401:
            exc_type = NotAuthenticatedError
        elif status_code == 403:
            exc_type = AccessDeniedError
        elif status_code == 404:
            exc_type = NotFoundError
        elif status_code == 409:
            exc_type = DuplicateConflictError
        elif status_code >= 500:
            exc_type = ServerError
        else:
            exc_type = APIError
    else:
        exc_type = error_map.get(error_type, ServerError if status_code >= 500 else APIError)

    return exc_type(
        status_code=status_code,
        message=message,
        body=body,
        endpoint=endpoint,
        error_type=error_type,
        messages=messages,
        method_name=method_name,
    )

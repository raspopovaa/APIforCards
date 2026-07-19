from __future__ import annotations

from dataclasses import is_dataclass
from types import UnionType
from typing import Any, TypeVar, Union, cast, get_args, get_origin

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, Field, ValidationError, field_validator

ModelT = TypeVar("ModelT")


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        coerce_numbers_to_str=True,
        extra="allow",
        populate_by_name=True,
        validate_default=True,
    )

    @classmethod
    def describe(cls) -> dict[str, dict[str, Any]]:
        return {
            name: {
                "type": cls._format_type(model_field.annotation),
                "alias": model_field.alias,
                "description": model_field.description,
                "required": model_field.is_required(),
            }
            for name, model_field in cls.model_fields.items()
        }

    @classmethod
    def _format_type(cls, annotation: Any) -> str:
        if annotation is None or annotation is Any:
            return "Any"
        if annotation is type(None):
            return "None"

        origin = get_origin(annotation)
        args = get_args(annotation)

        if origin in {Union, UnionType}:
            return " | ".join(cls._format_type(item) for item in args)
        if origin is list:
            item_type = cls._format_type(args[0]) if args else "Any"
            return f"list[{item_type}]"
        if origin is dict:
            key_type = cls._format_type(args[0]) if args else "Any"
            value_type = cls._format_type(args[1]) if len(args) > 1 else "Any"
            return f"dict[{key_type}, {value_type}]"
        if origin is tuple:
            if len(args) == 2 and args[1] is Ellipsis:
                return f"tuple[{cls._format_type(args[0])}, ...]"
            return f"tuple[{', '.join(cls._format_type(item) for item in args)}]"
        if isinstance(annotation, type):
            return annotation.__name__
        return str(annotation).replace("typing.", "")


class StrictRequestModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


def validator(*field_names: str, pre: bool = False) -> Any:
    return field_validator(*field_names, mode="before" if pre else "after")


def decode_model(model_type: type[ModelT], payload: dict[str, Any]) -> ModelT:
    model_validator = getattr(model_type, "model_validate", None)
    if callable(model_validator):
        return cast(ModelT, model_validator(payload))
    if is_dataclass(model_type):
        return model_type(**payload)
    raise TypeError(f"Unsupported response model: {model_type.__name__}")


__all__ = [
    "BaseModel",
    "Field",
    "StrictRequestModel",
    "ValidationError",
    "decode_model",
    "field_validator",
    "validator",
]

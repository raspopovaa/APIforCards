from __future__ import annotations

import inspect
from collections.abc import Callable
from dataclasses import MISSING, dataclass, field, fields, is_dataclass
from dataclasses import Field as DataclassField
from datetime import datetime
from types import UnionType
from typing import (
    Any,
    ClassVar,
    Self,
    TypeVar,
    Union,
    cast,
    dataclass_transform,
    get_args,
    get_origin,
    get_type_hints,
)

REQUIRED = object()
ModelT = TypeVar("ModelT")


class ValidationError(ValueError):
    pass


class FieldInfo:
    def __init__(
        self,
        default: Any = REQUIRED,
        *,
        default_factory: Callable[[], Any] | Any = MISSING,
        alias: str | None = None,
        description: str | None = None,
    ) -> None:
        self.default = default
        self.default_factory = default_factory
        self.alias = alias
        self.description = description


def Field(
    default: Any = REQUIRED,
    *,
    default_factory: Callable[[], Any] | Any = MISSING,
    alias: str | None = None,
    description: str | None = None,
) -> Any:
    return FieldInfo(
        default=default,
        default_factory=default_factory,
        alias=alias,
        description=description,
    )


def field_validator(
    *field_names: str,
    mode: str = "after",
    **_: Any,
) -> Callable[[Callable[..., Any]], Any]:
    def decorator(func: Callable[..., Any]) -> Any:
        func.__dict__["__field_validator_config__"] = {
            "fields": field_names,
            "mode": mode,
        }
        return func

    return decorator


def validator(*field_names: str, pre: bool = False) -> Callable[[Callable[..., Any]], Any]:
    return field_validator(*field_names, mode="before" if pre else "after")


@dataclass_transform(field_specifiers=(Field,), kw_only_default=True)
class BaseModel:
    __resolved_types__: ClassVar[dict[str, Any]]
    __field_validators__: ClassVar[dict[str, dict[str, list[Callable[[Any], Any]]]]]

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()

        annotations = dict(getattr(cls, "__annotations__", {}))
        for name in annotations:
            raw_default = getattr(cls, name, MISSING)
            if isinstance(raw_default, FieldInfo):
                metadata = {
                    "alias": raw_default.alias,
                    "description": raw_default.description,
                }
                if raw_default.default_factory is not MISSING:
                    setattr(
                        cls,
                        name,
                        field(default_factory=raw_default.default_factory, metadata=metadata),
                    )
                elif raw_default.default is REQUIRED or raw_default.default is ...:
                    setattr(cls, name, field(metadata=metadata))
                else:
                    setattr(cls, name, field(default=raw_default.default, metadata=metadata))

        dataclass(cls, init=False, repr=True, eq=True)
        cls.__resolved_types__ = get_type_hints(cls)
        cls.__field_validators__ = cls._collect_field_validators()

    @classmethod
    def _collect_field_validators(cls) -> dict[str, dict[str, list[Callable[[Any], Any]]]]:
        collected: dict[str, dict[str, list[Callable[[Any], Any]]]] = {}

        for base in reversed(cls.__mro__):
            for name, attribute in getattr(base, "__dict__", {}).items():
                raw_callable = (
                    attribute.__func__
                    if isinstance(attribute, (classmethod, staticmethod))
                    else attribute
                )
                config = getattr(raw_callable, "__field_validator_config__", None)
                if config is None:
                    continue

                bound = getattr(cls, name)
                for field_name in config["fields"]:
                    field_validators = collected.setdefault(field_name, {"before": [], "after": []})
                    field_validators[config["mode"]].append(bound)

        return collected

    def __init__(self, **kwargs: Any) -> None:
        for model_field in fields(cast(Any, self)):
            raw_value, has_value = self._extract_input_value(model_field, kwargs)
            validators = self.__field_validators__.get(
                model_field.name, {"before": [], "after": []}
            )

            if has_value:
                raw_value = self._apply_validators(type(self), validators["before"], raw_value)
                value = self._convert_value(
                    raw_value, self.__resolved_types__[model_field.name], model_field.name
                )
                value = self._apply_validators(type(self), validators["after"], value)
            else:
                value = self._resolve_default(model_field)

            setattr(self, model_field.name, value)

    @classmethod
    def model_validate(cls, payload: dict[str, Any]) -> Self:
        return cls(**payload)

    def model_dump(self, *, by_alias: bool = False) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for model_field in fields(cast(Any, self)):
            key = (
                model_field.metadata.get("alias") or model_field.name
                if by_alias
                else model_field.name
            )
            result[key] = self._dump_value(getattr(self, model_field.name))
        return result

    @classmethod
    def _dump_value(cls, value: Any) -> Any:
        if isinstance(value, BaseModel):
            return value.model_dump()
        if isinstance(value, list):
            return [cls._dump_value(item) for item in value]
        if isinstance(value, tuple):
            return tuple(cls._dump_value(item) for item in value)
        if isinstance(value, dict):
            return {key: cls._dump_value(item) for key, item in value.items()}
        return value

    @classmethod
    def _extract_input_value(
        cls, model_field: DataclassField[Any], payload: dict[str, Any]
    ) -> tuple[Any, bool]:
        if model_field.name in payload:
            return payload[model_field.name], True

        alias = model_field.metadata.get("alias")
        if alias and alias in payload:
            return payload[alias], True

        return None, False

    @classmethod
    def _resolve_default(cls, model_field: DataclassField[Any]) -> Any:
        if model_field.default is not MISSING:
            return model_field.default
        if model_field.default_factory is not MISSING:
            return model_field.default_factory()
        raise ValidationError(f"{cls.__name__}.{model_field.name}: field required")

    @staticmethod
    def _apply_validators(
        model_cls: type[BaseModel],
        validators: list[Callable[..., Any]],
        value: Any,
    ) -> Any:
        current = value
        for callback in validators:
            parameter_count = len(inspect.signature(callback).parameters)
            if parameter_count == 1:
                current = callback(current)
            elif parameter_count == 2:
                current = callback(model_cls, current)
            else:
                raise TypeError(f"Unsupported validator signature for {callback}")
        return current

    @classmethod
    def _convert_value(cls, value: Any, annotation: Any, field_name: str) -> Any:
        if annotation is Any:
            return value

        origin = get_origin(annotation)
        args = get_args(annotation)

        if value is None:
            if cls._is_optional(annotation):
                return None
            raise ValidationError(f"{cls.__name__}.{field_name}: null is not allowed")

        if origin in {list, list[Any]}:
            if not isinstance(value, list):
                raise ValidationError(f"{cls.__name__}.{field_name}: list expected")
            item_type = args[0] if args else Any
            return [cls._convert_value(item, item_type, field_name) for item in value]

        if origin is dict:
            if not isinstance(value, dict):
                raise ValidationError(f"{cls.__name__}.{field_name}: dict expected")
            return value

        if origin is tuple:
            if not isinstance(value, (list, tuple)):
                raise ValidationError(f"{cls.__name__}.{field_name}: tuple expected")
            item_types = args or ()
            if len(item_types) == 2 and item_types[1] is Ellipsis:
                return tuple(cls._convert_value(item, item_types[0], field_name) for item in value)
            return tuple(
                cls._convert_value(item, item_types[index], field_name)
                for index, item in enumerate(value)
            )

        if origin in {Union, UnionType}:
            return cls._convert_union(value, args, field_name)

        if isinstance(annotation, type):
            if issubclass(annotation, BaseModel):
                if isinstance(value, annotation):
                    return value
                if not isinstance(value, dict):
                    raise ValidationError(
                        f"{cls.__name__}.{field_name}: dict expected for nested model"
                    )
                return annotation(**value)

            if annotation is datetime:
                return cls._coerce_datetime(value, field_name)
            if annotation is bool:
                return cls._coerce_bool(value)
            if annotation is int:
                return cls._coerce_scalar(int, value, field_name)
            if annotation is float:
                return cls._coerce_scalar(float, value, field_name)
            if annotation is str:
                return cls._coerce_scalar(str, value, field_name)

        return value

    @classmethod
    def _convert_union(cls, value: Any, args: tuple[Any, ...], field_name: str) -> Any:
        optional_args = [arg for arg in args if arg is not type(None)]
        if value is None and len(optional_args) != len(args):
            return None

        for union_type in optional_args:
            try:
                return cls._convert_value(value, union_type, field_name)
            except ValidationError:
                continue

        allowed = ", ".join(getattr(arg, "__name__", str(arg)) for arg in optional_args)
        raise ValidationError(f"{cls.__name__}.{field_name}: expected one of {allowed}")

    @staticmethod
    def _is_optional(annotation: Any) -> bool:
        origin = get_origin(annotation)
        if origin is None:
            return False
        if origin not in {Union, UnionType}:
            return False
        return any(arg is type(None) for arg in get_args(annotation))

    @staticmethod
    def _coerce_scalar(expected_type: type[Any], value: Any, field_name: str) -> Any:
        if isinstance(value, expected_type):
            return value
        if expected_type is str and isinstance(value, (dict, list, tuple, set)):
            raise ValidationError(f"{field_name}: scalar value expected")
        try:
            return expected_type(value)
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"{field_name}: {expected_type.__name__} expected") from exc

    @staticmethod
    def _coerce_bool(value: Any) -> bool:
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"true", "1", "yes", "y"}:
                return True
            if normalized in {"false", "0", "no", "n"}:
                return False
        if isinstance(value, int):
            return bool(value)
        raise ValidationError("bool expected")

    @staticmethod
    def _coerce_datetime(value: Any, field_name: str) -> datetime:
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            formats = (
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%d",
            )
            for fmt in formats:
                try:
                    return datetime.strptime(value, fmt)
                except ValueError:
                    continue
            try:
                return datetime.fromisoformat(value)
            except ValueError as exc:
                raise ValidationError(f"{field_name}: datetime format is invalid") from exc
        raise ValidationError(f"{field_name}: datetime expected")

    @classmethod
    def describe(cls) -> dict[str, dict[str, Any]]:
        description: dict[str, dict[str, Any]] = {}
        for model_field in fields(cast(Any, cls)):
            description[model_field.name] = {
                "type": cls._format_type(cls.__resolved_types__.get(model_field.name)),
                "alias": model_field.metadata.get("alias"),
                "description": model_field.metadata.get("description"),
                "required": model_field.default is MISSING
                and model_field.default_factory is MISSING,
            }
        return description

    @classmethod
    def _format_type(cls, annotation: Any) -> str:
        if annotation is None:
            return "Any"
        if annotation is Any:
            return "Any"
        if annotation is type(None):
            return "None"

        origin = get_origin(annotation)
        args = get_args(annotation)

        if origin in {Union, UnionType}:
            return " | ".join(cls._format_type(arg) for arg in args)

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
            return f"tuple[{', '.join(cls._format_type(arg) for arg in args)}]"

        if isinstance(annotation, type):
            return annotation.__name__

        return str(annotation).replace("typing.", "")


def decode_model(model_type: type[ModelT], payload: dict[str, Any]) -> ModelT:
    validator = getattr(model_type, "model_validate", None)
    if callable(validator):
        return cast(ModelT, validator(payload))
    if is_dataclass(model_type):
        return model_type(**payload)
    raise TypeError(f"Unsupported response model: {model_type.__name__}")

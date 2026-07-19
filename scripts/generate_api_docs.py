from __future__ import annotations

import importlib
import inspect
import pkgutil
import re
import sys
from dataclasses import is_dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
DOCS_PATH = PROJECT_ROOT / "docs"
REFERENCE_PATH = DOCS_PATH / "api-reference.md"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from api_client_opti24.modeling import BaseModel

PACKAGE_NAME = "api_client_opti24"
EXCLUDED_MODULES = {
    "api_client_opti24.logger",
}


def iter_package_modules(package_name: str) -> list[str]:
    package = importlib.import_module(package_name)
    modules = [package_name]
    if hasattr(package, "__path__"):
        for module_info in pkgutil.walk_packages(package.__path__, prefix=f"{package_name}."):
            if module_info.name in EXCLUDED_MODULES:
                continue
            modules.append(module_info.name)
    return sorted(set(modules))


def format_signature(obj: object) -> str:
    try:
        signature = str(inspect.signature(obj))
        return re.sub(r" at 0x[0-9a-fA-F]+", "", signature)
    except (TypeError, ValueError):
        return "()"


def clean_docstring(obj: object) -> str:
    return inspect.getdoc(obj) or "Описание отсутствует."


def iter_public_classes(module) -> list[type]:
    classes: list[type] = []
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if name.startswith("_"):
            continue
        if obj.__module__ != module.__name__:
            continue
        classes.append(obj)
    return classes


def iter_public_functions(module) -> list[object]:
    functions: list[object] = []
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_"):
            continue
        if obj.__module__ != module.__name__:
            continue
        functions.append(obj)
    return functions


def iter_public_methods(cls: type) -> list[tuple[str, object]]:
    methods: list[tuple[str, object]] = []
    for name, obj in inspect.getmembers(cls):
        if name.startswith("_"):
            continue
        if name in {"describe", "from_env"}:
            methods.append((name, obj))
            continue
        if inspect.isfunction(obj) or inspect.ismethod(obj):
            method_module = getattr(obj, "__module__", "")
            if method_module == cls.__module__ or method_module.startswith(
                "api_client_opti24.services."
            ):
                methods.append((name, obj))
    return methods


def render_model_block(cls: type[BaseModel]) -> str:
    description = cls.describe()
    lines: list[str] = []
    for field_name, metadata in description.items():
        lines.append(f"{field_name}:")
        lines.append(f"  type: {metadata.get('type')}")
        lines.append(f"  required: {metadata.get('required')}")
        if metadata.get("alias"):
            lines.append(f"  alias: {metadata.get('alias')}")
        if metadata.get("description"):
            lines.append(f"  description: {metadata.get('description')}")
    return f"```text\n" + "\n".join(lines) + "\n```"


def render_class(cls: type) -> list[str]:
    lines = [f"### `{cls.__name__}`", ""]
    lines.append(clean_docstring(cls))
    lines.append("")
    lines.append(f"Сигнатура: `{cls.__name__}{format_signature(cls)}`")
    lines.append("")

    if issubclass(cls, BaseModel) and is_dataclass(cls):
        lines.append("Описание полей:")
        lines.append("")
        lines.append(render_model_block(cls))
        lines.append("")

    methods = iter_public_methods(cls)
    if methods:
        lines.append("Публичные методы:")
        lines.append("")
        for method_name, method in methods:
            lines.append(f"- `{method_name}{format_signature(method)}`")
        lines.append("")

    return lines


def render_function(func: object) -> list[str]:
    lines = [f"### `{func.__name__}`", ""]
    lines.append(clean_docstring(func))
    lines.append("")
    lines.append(f"Сигнатура: `{func.__name__}{format_signature(func)}`")
    lines.append("")
    return lines


def render_module(module_name: str) -> list[str]:
    module = importlib.import_module(module_name)
    lines = [f"## `{module_name}`", ""]
    lines.append(clean_docstring(module))
    lines.append("")

    classes = iter_public_classes(module)
    functions = iter_public_functions(module)

    if not classes and not functions:
        lines.append("_Публичные классы и функции не обнаружены._")
        lines.append("")
        return lines

    for cls in classes:
        lines.extend(render_class(cls))

    for func in functions:
        lines.extend(render_function(func))

    return lines


def build_document() -> str:
    lines = [
        "# API Reference",
        "",
        "Этот файл сгенерирован автоматически скриптом `scripts/generate_api_docs.py`.",
        "",
        "Ниже собраны публичные модули, классы, функции и описание моделей SDK.",
        "",
    ]

    for module_name in iter_package_modules(PACKAGE_NAME):
        lines.extend(render_module(module_name))

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    DOCS_PATH.mkdir(parents=True, exist_ok=True)
    REFERENCE_PATH.write_text(build_document(), encoding="utf-8")
    print(f"Generated {REFERENCE_PATH}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_docs.py"


def load_generator():
    module_name = "generate_docs"
    spec = importlib.util.spec_from_file_location(module_name, GENERATOR_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_generator_covers_every_publishable_registry_operation() -> None:
    generator = load_generator()
    registry = generator.build_default_registry()
    publishable = {
        operation.name
        for operation in registry.list_all()
        if operation.name not in generator.EXCLUDED_OPERATIONS
    }
    documented = {operation.name for operation in generator.documented_specs()}

    assert documented == publishable
    assert len(registry.list_all()) == 89
    assert not documented.intersection(generator.EXCLUDED_OPERATIONS)

    services = generator.service_classes()
    missing = []
    for operation in generator.documented_specs():
        service_name = generator.SERVICE_NAMES[operation.domain]
        methods = generator.public_service_methods(services[service_name])
        if operation.name not in methods:
            missing.append(f"{service_name}.{operation.name}")

    assert not missing, "Undocumented operations: " + ", ".join(missing)


def test_every_documented_operation_has_docstring_and_return_annotation() -> None:
    generator = load_generator()
    services = generator.service_classes()
    errors = []

    for operation in generator.documented_specs():
        service_name = generator.SERVICE_NAMES[operation.domain]
        method = generator.public_service_methods(services[service_name]).get(operation.name)
        if method is None:
            continue
        if not generator.clean_docstring(method):
            errors.append(f"{service_name}.{operation.name}: missing docstring")
        if "return" not in generator.get_type_hints(method):
            errors.append(f"{service_name}.{operation.name}: missing return annotation")

    assert not errors, "\n".join(errors)


def test_generated_output_is_idempotent_and_has_required_sections() -> None:
    generator = load_generator()
    first = generator.build_all()
    second = generator.build_all()

    assert first == second
    assert generator.DOCS_PATH / "methods.md" in first
    assert generator.DATA_TYPES_PATH / "index.md" in first

    method_pages = {
        path: content for path, content in first.items() if path.parent == generator.METHODS_PATH
    }
    assert method_pages
    for path, content in method_pages.items():
        assert "### Параметры" in content, path
        assert "### Возвращаемое значение" in content, path
        assert "### Пример" in content, path


def test_generated_python_examples_are_syntactically_valid() -> None:
    generator = load_generator()
    output = generator.build_all()
    for path, content in output.items():
        if path.parent != generator.METHODS_PATH:
            continue
        blocks = content.split("```python")[1:]
        for block in blocks:
            source = block.split("```", 1)[0].strip()
            ast.parse(source)


def test_qr_operations_are_not_documented() -> None:
    generator = load_generator()
    output = generator.build_all()
    combined = "\n".join(output.values()).lower()

    for operation_name in generator.EXCLUDED_OPERATIONS:
        assert operation_name.lower() not in combined
    assert "confirmmpc" not in combined
    assert "resetmpc" not in combined

from __future__ import annotations

import ast
import importlib
import inspect
import pkgutil
import re
import textwrap
from dataclasses import dataclass

PACKAGE_NAME = "api_client_opti24.services"
READ_HEAVY_PREFIXES = (
    "get_",
    "download_",
)
TIMEOUT_CLASS_OVERRIDES = {
    "auth_user": "auth",
}
RETRY_CLASS_OVERRIDES = {
    "auth_user": "network_only",
}


@dataclass(frozen=True, slots=True)
class MethodSpec:
    name: str
    domain: str
    http_method: str
    endpoint: str
    supported_versions: tuple[str, ...]
    default_version: str
    demo_available: bool
    idempotent: bool
    timeout_class: str = "default"
    retry_class: str = "safe"

    def supports(self, version: str) -> bool:
        return version in self.supported_versions


class MethodRegistry:
    def __init__(self, specs: dict[str, MethodSpec] | None = None) -> None:
        self._specs: dict[str, MethodSpec] = specs or {}

    def register(self, spec: MethodSpec) -> None:
        self._specs[spec.name] = spec

    def get(self, name: str) -> MethodSpec:
        try:
            return self._specs[name]
        except KeyError as exc:
            raise KeyError(f"Method '{name}' is not registered") from exc

    def find_by_endpoint(self, endpoint: str, version: str) -> MethodSpec | None:
        matches = [
            spec
            for spec in self._specs.values()
            if spec.endpoint == endpoint and spec.supports(version)
        ]
        if not matches:
            return None
        return sorted(
            matches,
            key=lambda spec: (
                not spec.idempotent,
                spec.http_method != "GET",
                spec.name,
            ),
        )[0]

    def list_domain(self, domain: str) -> tuple[MethodSpec, ...]:
        return tuple(spec for spec in self._specs.values() if spec.domain == domain)

    def list_all(self) -> tuple[MethodSpec, ...]:
        return tuple(self._specs.values())


def _iter_service_modules() -> list[object]:
    package = importlib.import_module(PACKAGE_NAME)
    modules: list[object] = []
    for module_info in pkgutil.walk_packages(package.__path__, prefix=f"{PACKAGE_NAME}."):
        if module_info.name.endswith(".__init__"):
            continue
        modules.append(importlib.import_module(module_info.name))
    return modules


def _iter_service_methods() -> list[tuple[str, object]]:
    methods: list[tuple[str, object]] = []
    for module in _iter_service_modules():
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != module.__name__ or not cls.__name__.endswith("Mixin"):
                continue
            for method_name, method in inspect.getmembers(cls, inspect.iscoroutinefunction):
                if getattr(method, "__api_method_config__", None) is None:
                    continue
                methods.append((module.__name__, method))
    return methods


def _resolve_parameter_defaults(function_node: ast.AsyncFunctionDef | ast.FunctionDef) -> dict[str, object]:
    positional = list(function_node.args.args) + list(function_node.args.kwonlyargs)
    defaults = [None] * (len(positional) - len(function_node.args.defaults + function_node.args.kw_defaults))
    defaults.extend(function_node.args.defaults + function_node.args.kw_defaults)

    resolved: dict[str, object] = {}
    for argument, default in zip(positional, defaults):
        if isinstance(default, ast.Constant):
            resolved[argument.arg] = default.value
    return resolved


def _render_template(
    node: ast.AST,
    *,
    local_values: dict[str, str] | None = None,
    parameter_defaults: dict[str, object] | None = None,
) -> str:
    local_values = local_values or {}
    parameter_defaults = parameter_defaults or {}

    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in local_values:
            return local_values[node.id]
        raise ValueError(f"Unknown template variable: {node.id}")
    if isinstance(node, ast.IfExp) and isinstance(node.test, ast.Name):
        default = parameter_defaults.get(node.test.id)
        if isinstance(default, bool):
            branch = node.body if default else node.orelse
            return _render_template(
                branch,
                local_values=local_values,
                parameter_defaults=parameter_defaults,
            )
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            elif isinstance(value, ast.FormattedValue):
                inner = value.value
                if isinstance(inner, ast.Name):
                    if inner.id in local_values:
                        parts.append(local_values[inner.id])
                    else:
                        parts.append(f"{{{inner.id}}}")
                else:
                    parts.append(f"{{{ast.unparse(inner)}}}")
        return "".join(parts)
    raise ValueError(f"Unsupported endpoint node: {ast.dump(node)}")


def _normalize_request_stream_endpoint(endpoint: str) -> str:
    normalized = endpoint.lstrip("/")
    return re.sub(r"^vip/(?:\{api_version\}|v\d+)/", "", normalized)


def _extract_call_metadata(method: object) -> tuple[str, str]:
    source = textwrap.dedent(inspect.getsource(getattr(method, "__wrapped__", method)))
    tree = ast.parse(source)
    function_node = next(
        node for node in tree.body if isinstance(node, (ast.AsyncFunctionDef, ast.FunctionDef))
    )
    parameter_defaults = _resolve_parameter_defaults(function_node)
    local_values: dict[str, str] = {}

    for node in function_node.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        try:
            local_values[target.id] = _render_template(
                node.value,
                local_values=local_values,
                parameter_defaults=parameter_defaults,
            )
        except ValueError:
            continue

    for node in ast.walk(function_node):
        if not isinstance(node, ast.Await) or not isinstance(node.value, ast.Call):
            continue

        call = node.value
        if isinstance(call.func, ast.Attribute) and call.func.attr == "_request":
            method_node = call.args[0] if len(call.args) >= 1 else None
            endpoint_node = call.args[1] if len(call.args) >= 2 else None
            for keyword in call.keywords:
                if keyword.arg == "method" and method_node is None:
                    method_node = keyword.value
                if keyword.arg == "endpoint" and endpoint_node is None:
                    endpoint_node = keyword.value
            if method_node is None or endpoint_node is None:
                continue
            http_method = _render_template(
                method_node,
                local_values=local_values,
                parameter_defaults=parameter_defaults,
            ).upper()
            endpoint = _render_template(
                endpoint_node,
                local_values=local_values,
                parameter_defaults=parameter_defaults,
            )
            return http_method, endpoint

        if (
            isinstance(call.func, ast.Attribute)
            and call.func.attr == "request_stream"
            and isinstance(call.func.value, ast.Attribute)
            and call.func.value.attr == "transport"
        ):
            method_node = call.args[0] if len(call.args) >= 1 else None
            endpoint_node = call.args[1] if len(call.args) >= 2 else None
            if method_node is None or endpoint_node is None:
                continue
            http_method = _render_template(
                method_node,
                local_values=local_values,
                parameter_defaults=parameter_defaults,
            ).upper()
            endpoint = _normalize_request_stream_endpoint(
                _render_template(
                    endpoint_node,
                    local_values=local_values,
                    parameter_defaults=parameter_defaults,
                )
            )
            return http_method, endpoint

    raise ValueError(f"Could not extract request metadata for {method.__qualname__}")


def _infer_timeout_class(method_name: str, http_method: str) -> str:
    if method_name in TIMEOUT_CLASS_OVERRIDES:
        return TIMEOUT_CLASS_OVERRIDES[method_name]
    if http_method == "GET" and method_name.startswith(READ_HEAVY_PREFIXES):
        return "read_heavy"
    return "default"


def _build_method_spec(module_name: str, method: object) -> MethodSpec:
    config = getattr(method, "__api_method_config__")
    method_name = method.__name__
    http_method, endpoint = _extract_call_metadata(method)
    default_version = config["default_version"]
    return MethodSpec(
        name=method_name,
        domain=module_name.rsplit(".", 1)[-1].lower(),
        http_method=http_method,
        endpoint=endpoint,
        supported_versions=(default_version,),
        default_version=default_version,
        demo_available=True,
        idempotent=http_method == "GET",
        timeout_class=_infer_timeout_class(method_name, http_method),
        retry_class=RETRY_CLASS_OVERRIDES.get(method_name, "safe"),
    )


def build_default_registry() -> MethodRegistry:
    registry = MethodRegistry()
    for module_name, method in sorted(_iter_service_methods(), key=lambda item: item[1].__name__):
        registry.register(_build_method_spec(module_name, method))
    return registry

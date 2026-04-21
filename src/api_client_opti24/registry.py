from __future__ import annotations

from dataclasses import dataclass


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
        for spec in self._specs.values():
            if spec.endpoint == endpoint and spec.supports(version):
                return spec
        return None

    def list_domain(self, domain: str) -> tuple[MethodSpec, ...]:
        return tuple(spec for spec in self._specs.values() if spec.domain == domain)


def build_default_registry() -> MethodRegistry:
    registry = MethodRegistry()

    registry.register(
        MethodSpec(
            name="auth_user",
            domain="auth",
            http_method="POST",
            endpoint="authUser",
            supported_versions=("v1",),
            default_version="v1",
            demo_available=True,
            idempotent=False,
            timeout_class="auth",
            retry_class="network_only",
        )
    )
    registry.register(
        MethodSpec(
            name="logoff",
            domain="auth",
            http_method="GET",
            endpoint="logoff",
            supported_versions=("v1",),
            default_version="v1",
            demo_available=True,
            idempotent=True,
        )
    )
    registry.register(
        MethodSpec(
            name="get_info",
            domain="auth",
            http_method="GET",
            endpoint="info",
            supported_versions=("v1",),
            default_version="v1",
            demo_available=True,
            idempotent=True,
        )
    )
    registry.register(
        MethodSpec(
            name="get_cards_v1",
            domain="cards",
            http_method="GET",
            endpoint="cards",
            supported_versions=("v1",),
            default_version="v1",
            demo_available=True,
            idempotent=True,
            timeout_class="read_heavy",
        )
    )
    registry.register(
        MethodSpec(
            name="get_cards_v2",
            domain="cards",
            http_method="GET",
            endpoint="cards",
            supported_versions=("v2",),
            default_version="v2",
            demo_available=True,
            idempotent=True,
            timeout_class="read_heavy",
        )
    )
    registry.register(
        MethodSpec(
            name="list_qr_mpc",
            domain="qr",
            http_method="GET",
            endpoint="MPC",
            supported_versions=("v2",),
            default_version="v2",
            demo_available=True,
            idempotent=True,
            timeout_class="read_heavy",
        )
    )

    return registry

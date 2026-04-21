from api_client_opti24.registry import build_default_registry


def test_registry_contains_default_versions_for_supported_methods():
    registry = build_default_registry()

    auth_spec = registry.get("auth_user")
    cards_spec = registry.get("get_cards_v2")

    assert auth_spec.default_version == "v1"
    assert auth_spec.supported_versions == ("v1",)
    assert cards_spec.default_version == "v2"
    assert cards_spec.supported_versions == ("v2",)


def test_registry_can_resolve_method_by_endpoint_and_version():
    registry = build_default_registry()

    spec = registry.find_by_endpoint("cards", "v2")

    assert spec is not None
    assert spec.name == "get_cards_v2"
    assert spec.domain == "cards"

from api_client_opti24.registry import build_default_registry


def test_registry_covers_all_decorated_service_methods():
    registry = build_default_registry()

    assert len(registry.list_all()) == 89
    assert all(spec.name != "list_qr_mpc" for spec in registry.list_all())


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


def test_registry_extracts_dynamic_endpoints_and_stream_methods():
    registry = build_default_registry()

    card_drivers = registry.get("get_card_drivers")
    report_file = registry.get("download_report_file")

    assert card_drivers.endpoint == "cards/{card_id}/drivers"
    assert card_drivers.http_method == "GET"
    assert report_file.endpoint == "reports/jobs/{job_id}"
    assert report_file.supported_versions == ("v2",)


def test_registry_resolves_alias_routes_for_invites_and_templates():
    registry = build_default_registry()

    invite_free = registry.find_by_endpoint("invites_free", "v2", http_method="POST")
    prolong_free = registry.find_by_endpoint(
        "invites/{invite_id}/prolong_free",
        "v2",
        http_method="POST",
    )
    update_template_limit = registry.find_by_endpoint(
        "vc/templates/{template_id}/limits/{limit_id}",
        "v2",
        http_method="PUT",
    )

    assert invite_free is not None
    assert invite_free.name == "create_invite"
    assert prolong_free is not None
    assert prolong_free.name == "prolong_invite"
    assert update_template_limit is not None
    assert update_template_limit.name == "update_template_limit"


def test_registry_contains_demo_flags_for_demo_restricted_methods():
    registry = build_default_registry()

    assert registry.get("get_cards_v1").demo_available is True
    assert registry.get("get_cards_by_group").demo_available is False
    assert registry.get("create_invite").demo_available is False
    assert registry.get("get_mpc_qr_list").demo_available is False

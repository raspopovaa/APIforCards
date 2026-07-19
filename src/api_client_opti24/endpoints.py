from __future__ import annotations

from dataclasses import dataclass

from .policies import IDEMPOTENT_HTTP_METHODS, SAFE_HTTP_METHODS, RetryClass


@dataclass(frozen=True, slots=True)
class RouteVariant:
    http_method: str
    endpoint: str
    api_version: str
    demo_available: bool

    def supports(self, version: str) -> bool:
        return self.api_version == version


@dataclass(frozen=True, slots=True)
class EndpointSpec:
    name: str
    domain: str
    http_method: str
    endpoint: str
    supported_versions: tuple[str, ...]
    default_version: str
    demo_available: bool
    idempotent: bool
    timeout_class: str = "default"
    retry_class: str = RetryClass.SAFE.value
    route_variants: tuple[RouteVariant, ...] = ()

    def supports(self, version: str) -> bool:
        return version in self.supported_versions

    def iter_routes(self) -> tuple[RouteVariant, ...]:
        primary_route = RouteVariant(
            http_method=self.http_method,
            endpoint=self.endpoint,
            api_version=self.default_version,
            demo_available=self.demo_available,
        )
        return (primary_route, *self.route_variants)


def route(
    http_method: str,
    path: str,
    version: str,
    *,
    demo: bool,
) -> RouteVariant:
    return RouteVariant(http_method, path, version, demo)


def endpoint(
    name: str,
    domain: str,
    http_method: str,
    path: str,
    version: str,
    *,
    demo: bool = True,
    timeout: str = "default",
    retry: str | None = None,
    variants: tuple[RouteVariant, ...] = (),
) -> EndpointSpec:
    normalized_method = http_method.upper()
    retry_class = retry or (
        RetryClass.SAFE.value if normalized_method in SAFE_HTTP_METHODS else RetryClass.NEVER.value
    )
    return EndpointSpec(
        name=name,
        domain=domain,
        http_method=normalized_method,
        endpoint=path,
        supported_versions=(version,),
        default_version=version,
        demo_available=demo,
        idempotent=normalized_method in IDEMPOTENT_HTTP_METHODS,
        timeout_class=timeout,
        retry_class=retry_class,
        route_variants=variants,
    )


ENDPOINT_SPECS = (
    endpoint("attach_card", "users", "POST", "users/{user_id}/attachCard", "v2"),
    endpoint("attach_contracts", "users", "POST", "users/{user_id}/attachContracts", "v2"),
    endpoint("auth_user", "auth", "POST", "authUser", "v1", timeout="auth", retry="network_only"),
    endpoint("block_card", "cards", "POST", "blockCard", "v1"),
    endpoint(
        "check_purchase", "final_prices", "POST", "cards/{card_id}/checkPurchase", "v2", demo=False
    ),
    endpoint(
        "confirm_mpc", "virtual_cards", "POST", "cards/{card_id}/confirmMPC", "v2", demo=False
    ),
    endpoint(
        "create_invite",
        "invites",
        "POST",
        "invites",
        "v2",
        demo=False,
        variants=(route("POST", "invites_free", "v2", demo=True),),
    ),
    endpoint("create_template", "templates", "POST", "vc/templates", "v2"),
    endpoint(
        "create_template_georestriction",
        "templates",
        "POST",
        "vc/templates/{template_id}/georestrictions",
        "v2",
    ),
    endpoint(
        "create_template_limit", "templates", "POST", "vc/templates/{template_id}/limits", "v2"
    ),
    endpoint(
        "create_template_restriction",
        "templates",
        "POST",
        "vc/templates/{template_id}/restrictions",
        "v2",
    ),
    endpoint("create_user", "users", "POST", "users", "v2"),
    endpoint("create_virtual_card", "virtual_cards", "POST", "cards", "v2", demo=False),
    endpoint("delete_invite", "invites", "DELETE", "invites/{invite_id}", "v2"),
    endpoint("delete_mpc", "virtual_cards", "POST", "cards/{card_id}/deleteMPC", "v2", demo=False),
    endpoint("delete_template", "templates", "DELETE", "vc/templates/{template_id}", "v2"),
    endpoint(
        "delete_template_georestriction",
        "templates",
        "DELETE",
        "vc/templates/{template_id}/georestrictions/{georestriction_id}",
        "v2",
        variants=(
            route(
                "DELETE",
                "vc/templates/{template_id}/georestrictions/{georestrictions_id}",
                "v2",
                demo=True,
            ),
        ),
    ),
    endpoint(
        "delete_template_limit",
        "templates",
        "DELETE",
        "vc/templates/{template_id}/limits/{limit_id}",
        "v2",
    ),
    endpoint(
        "delete_template_restriction",
        "templates",
        "DELETE",
        "vc/templates/{template_id}/restrictions/{restriction_id}",
        "v2",
        variants=(
            route(
                "DELETE",
                "vc/templates/{template_id}/restrictions/{restrictions_id}",
                "v2",
                demo=True,
            ),
        ),
    ),
    endpoint("delete_user", "users", "DELETE", "users/{user_id}", "v2"),
    endpoint("detach_card", "users", "POST", "users/{user_id}/detachCard", "v2"),
    endpoint("detach_contracts", "users", "POST", "users/{user_id}/detachContracts", "v2"),
    endpoint(
        "download_report_file",
        "reports",
        "GET",
        "reports/jobs/{job_id}",
        "v2",
        demo=False,
        timeout="read_heavy",
    ),
    endpoint(
        "download_report_file_v1",
        "reports",
        "GET",
        "getReportFile",
        "v1",
        demo=False,
        timeout="read_heavy",
    ),
    endpoint(
        "generate_payment_qr", "virtual_cards", "POST", "cards/{card_id}/pay", "v2", demo=False
    ),
    endpoint(
        "get_azs_filters",
        "dictionaries",
        "GET",
        "azs/filters",
        "v2",
        demo=False,
        timeout="read_heavy",
    ),
    endpoint("get_azs_list_v1", "dictionaries", "GET", "AZS", "v1", timeout="read_heavy"),
    endpoint(
        "get_azs_list_v2", "dictionaries", "GET", "azs", "v2", demo=False, timeout="read_heavy"
    ),
    endpoint("get_card_detail", "cards", "GET", "cards", "v1", timeout="read_heavy"),
    endpoint(
        "get_card_drivers", "cards", "GET", "cards/{card_id}/drivers", "v2", timeout="read_heavy"
    ),
    endpoint("get_card_groups", "card_group", "GET", "cardGroups", "v1", timeout="read_heavy"),
    endpoint(
        "get_card_transactions_v2",
        "transactions",
        "GET",
        "cards/{card_id}/transactions",
        "v2",
        timeout="read_heavy",
    ),
    endpoint("get_cards_by_group", "cards", "GET", "cards", "v1", demo=False, timeout="read_heavy"),
    endpoint("get_cards_v1", "cards", "GET", "cards", "v1", timeout="read_heavy"),
    endpoint("get_cards_v2", "cards", "GET", "cards", "v2", timeout="read_heavy"),
    endpoint(
        "get_contract_data", "contract", "GET", "getPartContractData", "v1", timeout="read_heavy"
    ),
    endpoint("get_dictionary", "dictionaries", "GET", "getDictionary", "v1", timeout="read_heavy"),
    endpoint(
        "get_documents", "contract", "GET", "documents", "v2", demo=False, timeout="read_heavy"
    ),
    endpoint(
        "get_final_prices",
        "final_prices",
        "POST",
        "cards/{card_id}/calculatePrices",
        "v2",
        demo=False,
    ),
    endpoint("get_info", "auth", "GET", "info", "v1", timeout="read_heavy"),
    endpoint("get_invites", "invites", "GET", "invites", "v2", timeout="read_heavy"),
    endpoint("get_invoices", "contract", "GET", "invoices", "v2", timeout="read_heavy"),
    endpoint("get_limits", "limits", "GET", "limit", "v1", timeout="read_heavy"),
    endpoint(
        "get_mpc_qr_list", "virtual_cards", "GET", "MPC", "v2", demo=False, timeout="read_heavy"
    ),
    endpoint("get_payments", "contract", "GET", "getPayments", "v1", timeout="read_heavy"),
    endpoint(
        "get_region_limits", "region_limits", "GET", "regionLimit", "v1", timeout="read_heavy"
    ),
    endpoint(
        "get_report_job_list_v1", "reports", "GET", "getReportJobList", "v1", timeout="read_heavy"
    ),
    endpoint("get_report_jobs", "reports", "GET", "reports/jobs", "v2", timeout="read_heavy"),
    endpoint("get_reports", "reports", "GET", "reports", "v2", timeout="read_heavy"),
    endpoint("get_restrictions", "restrictions", "GET", "restriction", "v1", timeout="read_heavy"),
    endpoint(
        "get_template_georestrictions",
        "templates",
        "GET",
        "vc/templates/{template_id}/georestrictions",
        "v2",
        timeout="read_heavy",
    ),
    endpoint(
        "get_template_limits",
        "templates",
        "GET",
        "vc/templates/{template_id}/limits",
        "v2",
        timeout="read_heavy",
    ),
    endpoint(
        "get_template_restrictions",
        "templates",
        "GET",
        "vc/templates/{template_id}/restrictions",
        "v2",
        timeout="read_heavy",
    ),
    endpoint("get_templates", "templates", "GET", "vc/templates", "v2", timeout="read_heavy"),
    endpoint(
        "get_transaction_detail",
        "transactions",
        "GET",
        "transactions/{transaction_id}",
        "v2",
        timeout="read_heavy",
    ),
    endpoint(
        "get_transactions_v1",
        "transactions",
        "GET",
        "transactions",
        "v1",
        demo=False,
        timeout="read_heavy",
    ),
    endpoint(
        "get_transactions_v2", "transactions", "GET", "transactions", "v2", timeout="read_heavy"
    ),
    endpoint("get_users", "users", "GET", "users", "v2", timeout="read_heavy"),
    endpoint("init_mpc", "virtual_cards", "POST", "cards/{card_id}/initMPC", "v2", demo=False),
    endpoint("logoff", "auth", "GET", "logoff", "v1"),
    endpoint("move_to_card", "ewallet", "POST", "moveToCard", "v1"),
    endpoint("move_to_contract", "ewallet", "POST", "moveToContract", "v1"),
    endpoint("order_cards", "contract", "POST", "orderCards", "v2", demo=False),
    endpoint("order_documents_email", "contract", "POST", "documents", "v2", demo=False),
    endpoint("order_invoice", "contract", "POST", "invoice", "v2", demo=False),
    endpoint("order_report", "reports", "POST", "reports", "v2"),
    endpoint("order_report_v1", "reports", "GET", "reports", "v1", demo=False),
    endpoint(
        "prolong_invite",
        "invites",
        "POST",
        "invites/{invite_id}/prolong",
        "v2",
        demo=False,
        variants=(route("POST", "invites/{invite_id}/prolong_free", "v2", demo=True),),
    ),
    endpoint("release_virtual_card", "virtual_cards", "POST", "cards/release", "v2", demo=False),
    endpoint("remove_card_group", "card_group", "POST", "removeCardGroup", "v1"),
    endpoint("remove_limit", "limits", "POST", "removeLimit", "v1"),
    endpoint("remove_region_limit", "region_limits", "POST", "removeRegionLimit", "v1"),
    endpoint("remove_restriction", "restrictions", "POST", "removeRestriction", "v1"),
    endpoint("resend_invite", "invites", "GET", "invites/{invite_id}/send", "v2", demo=False),
    endpoint("reset_mpc", "virtual_cards", "POST", "cards/{card_id}/resetMPC", "v2", demo=False),
    endpoint("reset_pin", "cards", "POST", "cards/{card_id}/resetPIN", "v2", demo=False),
    endpoint("set_card_comment", "cards", "POST", "setCardComment", "v1"),
    endpoint("set_card_group", "card_group", "POST", "setCardGroup", "v1"),
    endpoint("set_card_product", "ewallet", "POST", "setCardProduct", "v1"),
    endpoint("set_cards_to_group", "card_group", "POST", "setCardsToGroup", "v1"),
    endpoint("set_limit", "limits", "POST", "setLimit", "v1"),
    endpoint("set_region_limit", "region_limits", "POST", "setRegionLimit", "v1"),
    endpoint("set_restriction", "restrictions", "POST", "setRestriction", "v1", demo=False),
    endpoint("update_mpc", "virtual_cards", "POST", "cards/{card_id}/updateMPC", "v2", demo=False),
    endpoint(
        "update_template",
        "templates",
        "POST",
        "vc/templates/{template_id}",
        "v2",
        variants=(route("PUT", "vc/templates/{template_id}", "v2", demo=True),),
    ),
    endpoint(
        "update_template_georestriction",
        "templates",
        "POST",
        "vc/templates/{template_id}/georestrictions/{georestriction_id}",
        "v2",
        variants=(
            route(
                "PUT",
                "vc/templates/{template_id}/georestrictions/{georestriction_id}",
                "v2",
                demo=True,
            ),
            route(
                "PUT",
                "vc/templates/{template_id}/georestrictions/{georestrictions_id}",
                "v2",
                demo=True,
            ),
        ),
    ),
    endpoint(
        "update_template_limit",
        "templates",
        "POST",
        "vc/templates/{template_id}/limits/{limit_id}",
        "v2",
        variants=(route("PUT", "vc/templates/{template_id}/limits/{limit_id}", "v2", demo=True),),
    ),
    endpoint(
        "update_template_restriction",
        "templates",
        "POST",
        "vc/templates/{template_id}/restrictions/{restriction_id}",
        "v2",
        variants=(
            route(
                "PUT", "vc/templates/{template_id}/restrictions/{restriction_id}", "v2", demo=True
            ),
            route(
                "PUT", "vc/templates/{template_id}/restrictions/{restrictions_id}", "v2", demo=True
            ),
        ),
    ),
    endpoint("verify_pin", "cards", "POST", "cards/{card_id}/verifyPIN", "v2"),
)

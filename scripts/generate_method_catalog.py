from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
DOCS_PATH = PROJECT_ROOT / "docs"
CONTRACT_PATH = PROJECT_ROOT / "specifications" / "api-methods.yaml"
OUTPUT_PATH = DOCS_PATH / "methods.md"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from api_client_opti24.registry import build_default_registry

SERVICE_NAMES = {
    "auth": "auth",
    "card_group": "card_groups",
    "cards": "cards",
    "contract": "contracts",
    "dictionaries": "dictionaries",
    "ewallet": "ewallet",
    "final_prices": "final_prices",
    "invites": "invites",
    "limits": "limits",
    "region_limits": "region_limits",
    "reports": "reports",
    "restrictions": "restrictions",
    "templates": "templates",
    "transactions": "transactions",
    "users": "users",
    "virtual_cards": "virtual_cards",
}


def _yes_no(value: bool) -> str:
    return "Да" if value else "Нет"


def _escape_table(value: str) -> str:
    return value.replace("|", "\\|")


def _load_discrepancies() -> dict[str, dict[str, object]]:
    document = yaml.safe_load(CONTRACT_PATH.read_text(encoding="utf-8"))
    return {
        item["external_code"]: item for item in document["methods"] if item.get("known_discrepancy")
    }


def build_document() -> str:
    registry = build_default_registry()
    grouped: dict[str, list[tuple[object, object]]] = defaultdict(list)
    fallback_routes: list[tuple[object, object]] = []
    external_route_count = 0

    for spec in registry.list_all():
        for route in spec.iter_routes():
            if route.external_code is None:
                if route.name != "default":
                    fallback_routes.append((spec, route))
                continue
            external_route_count += 1
            grouped[spec.domain].append((spec, route))

    lines = [
        "# Методы API",
        "",
        "Каталог генерируется из runtime registry и сверяется с независимым "
        "`specifications/api-methods.yaml`.",
        "",
        "!!! info \"Покрытие\"",
        f"    SDK содержит **{len(registry.list_all())} операций** и "
        f"**{external_route_count} внешних маршрутов**.",
        "    DEMO-доступность и тарификация отражают предоставленную сводную "
        "спецификацию, но фактический доступ также зависит от роли и договора.",
        "",
        "## Обозначения",
        "",
        "- **DEMO** — метод отмечен как доступный на демонстрационном стенде.",
        "- **Тарифицируется** — вызов отмечен как платный во внешней спецификации.",
        "- **Route** — относительный путь после базового `/vip/`.",
        "",
    ]

    for domain in sorted(grouped, key=lambda item: SERVICE_NAMES[item]):
        service_name = SERVICE_NAMES[domain]
        lines.extend(
            [
                f"## `client.{service_name}`",
                "",
                "| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |",
                "|---|---|---:|---:|---|:---:|:---:|",
            ]
        )
        for spec, route in sorted(
            grouped[domain],
            key=lambda item: (item[0].name, item[1].name),
        ):
            lines.append(
                "| "
                + " | ".join(
                    (
                        f"`client.{service_name}.{spec.name}()`",
                        f"`{route.external_code}`",
                        route.http_method,
                        route.api_version,
                        f"`{_escape_table(route.endpoint)}`",
                        _yes_no(route.demo_available),
                        _yes_no(bool(route.billable)),
                    )
                )
                + " |"
            )
        lines.append("")

    if fallback_routes:
        lines.extend(
            [
                "## Дополнительные варианты маршрутов",
                "",
                "Эти варианты поддерживаются SDK для совместимости или POST-fallback, "
                "но не имеют отдельного external code в сводной спецификации.",
                "",
                "| Операция | Variant | HTTP | Версия | Route |",
                "|---|---|---:|---:|---|",
            ]
        )
        for spec, route in sorted(
            fallback_routes,
            key=lambda item: (item[0].name, item[1].name),
        ):
            lines.append(
                f"| `{spec.name}` | `{route.name}` | {route.http_method} | "
                f"{route.api_version} | `{_escape_table(route.endpoint)}` |"
            )
        lines.append("")

    discrepancies = _load_discrepancies()
    if discrepancies:
        lines.extend(["## Известные расхождения", ""])
        for external_code, item in sorted(discrepancies.items()):
            lines.append(
                f"- `{external_code}`: сводная таблица указывает "
                f"`{item['source_http_method']}`, SDK использует `{item['http_method']}`. "
                f"{item['known_discrepancy']}"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUTPUT_PATH.write_text(build_document(), encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import json
from pathlib import Path

from api_client_opti24.contracts import serialize_registry_contract
from api_client_opti24.registry import build_default_registry


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the endpoint contract snapshot")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    contract = serialize_registry_contract(build_default_registry())
    args.output.write_text(
        json.dumps(contract, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

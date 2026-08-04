import json
from collections.abc import Mapping
from typing import Any

from ..models.limits import (
    LimitRequestItem,
    LimitsResponse,
    RemoveLimitResponse,
    SetLimitResponse,
)
from ..operations import operation
from ..service_base import _BaseService
from ..validation import require_identifier, validate_card_or_group_target

GET_LIMITS = operation("get_limits", LimitsResponse)
SET_LIMIT = operation("set_limit", SetLimitResponse)
REMOVE_LIMIT = operation("remove_limit", RemoveLimitResponse)


class LimitsService(_BaseService):
    """Methods for product limits (v1)."""

    async def get_limits(
        self,
        *,
        contract_id: str | None = None,
        card_id: str | None = None,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> LimitsResponse:
        cid = await self._resolve_contract_id(contract_id)
        card_id, group_id = validate_card_or_group_target(
            card_id=card_id,
            group_id=group_id,
        )
        params = {"contract_id": cid}
        if card_id is not None:
            params["card_id"] = card_id
        if group_id is not None:
            params["group_id"] = group_id
        return await self._request(
            GET_LIMITS,
            api_version=api_version,
            params=params,
            request_contract_id=cid,
        )

    async def set_limit(
        self,
        *,
        limits: list[LimitRequestItem | Mapping[str, Any]],
        contract_id: str | None = None,
        api_version: str | None = None,
    ) -> SetLimitResponse:
        """Create or update limits; every item must target the same contract."""
        if not limits:
            raise ValueError("limits must contain at least one item")
        parsed_limits = [LimitRequestItem.model_validate(item) for item in limits]
        for item in parsed_limits:
            validate_card_or_group_target(
                card_id=item.card_id,
                group_id=item.group_id,
                required=True,
            )
            if item.amount is None and item.sum is None:
                raise ValueError("each limit must contain amount or sum")

        cid = await self._resolve_batch_contract_id(
            contract_id=contract_id,
            item_contract_ids=[item.contract_id for item in parsed_limits],
        )
        serialized_limits: list[dict[str, Any]] = []
        for item in parsed_limits:
            serialized = item.model_dump(by_alias=True, exclude_none=True)
            serialized["contract_id"] = cid
            serialized_limits.append(serialized)

        body = {
            "limit": json.dumps(
                serialized_limits,
                ensure_ascii=False,
                separators=(",", ":"),
            )
        }
        return await self._request(
            SET_LIMIT,
            api_version=api_version,
            data=body,
            request_contract_id=cid,
        )

    async def remove_limit(
        self,
        *,
        contract_id: str | None = None,
        limit_id: str,
        group_id: str | None = None,
        api_version: str | None = None,
    ) -> RemoveLimitResponse:
        cid = await self._resolve_contract_id(contract_id)
        body = {
            "limit_id": require_identifier(limit_id, "limit_id"),
            "contract_id": cid,
        }
        if group_id is not None:
            body["group_id"] = require_identifier(group_id, "group_id")
        return await self._request(
            REMOVE_LIMIT,
            api_version=api_version,
            data=body,
            request_contract_id=cid,
        )

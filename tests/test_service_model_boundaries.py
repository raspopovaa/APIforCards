import logging
from typing import Any

import pytest

from api_client_opti24.modeling import ValidationError
from api_client_opti24.models.final_prices import CheckPurchaseResponse
from api_client_opti24.models.templates import (
    TemplateCreateResponse,
    TemplateLimitCreateResponse,
)
from api_client_opti24.services import final_prices as final_prices_module
from api_client_opti24.services import templates as templates_module
from api_client_opti24.services.final_prices import FinalPricesService
from api_client_opti24.services.templates import TemplatesService


class RecordingExecutor:
    def __init__(self, responses: dict[str, dict[str, Any]]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def execute(self, operation: str, **kwargs: Any) -> dict[str, Any]:
        self.calls.append((operation, kwargs))
        return self.responses[operation]

    async def execute_stream(self, operation: str, **kwargs: Any) -> bytes:
        del kwargs
        raise AssertionError(f"Unexpected stream request: {operation}")


class StubSessionContext:
    session_id = "session"
    contract_id = "contract"


class StubSessionGate:
    async def ensure_authenticated(self) -> str:
        return "session"


def service_dependencies(executor: RecordingExecutor) -> tuple[object, ...]:
    return (
        executor,
        StubSessionContext(),
        StubSessionGate(),
        logging.getLogger("service-model-boundary-test"),
    )


@pytest.mark.asyncio
async def test_check_purchase_validates_payload_and_uses_decoder(monkeypatch):
    executor = RecordingExecutor(
        {"check_purchase": {"status": {"code": 200}, "data": True, "timestamp": 1}}
    )
    service = FinalPricesService(*service_dependencies(executor))
    decoded_models: list[type[object]] = []
    original_decode = final_prices_module.decode_model

    def tracked_decode(model_type, payload):
        decoded_models.append(model_type)
        return original_decode(model_type, payload)

    monkeypatch.setattr(final_prices_module, "decode_model", tracked_decode)

    result = await service.check_purchase(
        card_id="card-1",
        poi_id="poi-1",
        goods=[{"code": "fuel", "quantity": "2", "price": "51.5"}],
    )

    assert isinstance(result, CheckPurchaseResponse)
    assert decoded_models == [CheckPurchaseResponse]
    assert executor.calls[0][1]["data"] == {
        "poi_id": "poi-1",
        "goods": [{"code": "fuel", "quantity": 2.0, "price": 51.5}],
    }


@pytest.mark.asyncio
async def test_check_purchase_rejects_invalid_nested_item_before_request():
    executor = RecordingExecutor({})
    service = FinalPricesService(*service_dependencies(executor))

    with pytest.raises(ValidationError):
        await service.check_purchase(
            card_id="card-1",
            poi_id="poi-1",
            goods=[{"code": "fuel", "quantity": 2}],
        )

    assert executor.calls == []


@pytest.mark.asyncio
async def test_create_template_uses_request_model_and_decoder(monkeypatch):
    executor = RecordingExecutor(
        {
            "create_template": {
                "status": {"code": 200},
                "data": "template-1",
                "timestamp": 1,
            }
        }
    )
    service = TemplatesService(*service_dependencies(executor))
    decoded_models: list[type[object]] = []
    original_decode = templates_module.decode_model

    def tracked_decode(model_type, payload):
        decoded_models.append(model_type)
        return original_decode(model_type, payload)

    monkeypatch.setattr(templates_module, "decode_model", tracked_decode)

    result = await service.create_template("contract-1", "Wallet", "Main")

    assert isinstance(result, TemplateCreateResponse)
    assert decoded_models == [TemplateCreateResponse]
    assert executor.calls[0][1]["data"] == {
        "contract_id": "contract-1",
        "type": "Wallet",
        "name": "Main",
    }


@pytest.mark.asyncio
async def test_update_template_limit_serializes_aliases_and_method_override():
    executor = RecordingExecutor(
        {
            "update_template_limit": {
                "status": {"code": 200},
                "data": "limit-1",
                "timestamp": 1,
            }
        }
    )
    service = TemplatesService(*service_dependencies(executor))

    result = await service.update_template_limit(
        template_id="template-1",
        limit_id="limit-1",
        limits=[
            {
                "contract_id": "contract-1",
                "product_type": "fuel",
                "sum": {"currency": 810, "value": "5000"},
                "time": {"type": "5", "number": 1},
                "term": {"time": {"from": "03:00", "to": "08:00"}},
            }
        ],
    )

    assert isinstance(result, TemplateLimitCreateResponse)
    assert executor.calls[0][1]["json"] == [
        {
            "contract_id": "contract-1",
            "product_type": "fuel",
            "sum": {"currency": "810", "value": 5000.0},
            "time": {"type": 5, "number": 1},
            "term": {"time": {"from": "03:00", "to": "08:00"}},
            "_method": "PUT",
        }
    ]


@pytest.mark.asyncio
async def test_template_payload_rejects_unknown_fields_before_request():
    executor = RecordingExecutor({})
    service = TemplatesService(*service_dependencies(executor))

    with pytest.raises(ValidationError):
        await service.create_template_limit(
            "template-1",
            {
                "contract_id": "contract-1",
                "product_type": "fuel",
                "sum": {"value": 5000},
                "time": {"type": 5, "number": 1},
                "unexpected": True,
            },
        )

    assert executor.calls == []


@pytest.mark.asyncio
async def test_template_limit_requires_amount_or_sum_before_request():
    executor = RecordingExecutor({})
    service = TemplatesService(*service_dependencies(executor))

    with pytest.raises(ValueError, match="amount.*sum"):
        await service.create_template_limit(
            "template-1",
            {
                "contract_id": "contract-1",
                "product_type": "fuel",
                "time": {"type": 5, "number": 1},
            },
        )

    assert executor.calls == []

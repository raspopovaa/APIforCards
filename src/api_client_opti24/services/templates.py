from typing import Any

from ..decorators import api_method
from ..modeling import BaseModel, decode_model
from ..models.templates import (
    TemplateCreateRequest,
    TemplateCreateResponse,
    TemplateDeleteResponse,
    TemplateGeoRestrictionCreateRequest,
    TemplateGeoRestrictionCreateResponse,
    TemplateGeoRestrictionDeleteResponse,
    TemplateGeoRestrictionListResponse,
    TemplateLimitCreateRequest,
    TemplateLimitCreateResponse,
    TemplateLimitDeleteResponse,
    TemplateLimitListResponse,
    TemplateRestrictionCreateRequest,
    TemplateRestrictionCreateResponse,
    TemplateRestrictionDeleteResponse,
    TemplateRestrictionListResponse,
    TemplatesListResponse,
)
from ..payloads import with_method_override
from ..service_base import _BaseService


def _dump_request(model: BaseModel) -> dict[str, Any]:
    return model.model_dump(by_alias=True, exclude_none=True)


def _validate_limit_payload(payload: dict[str, Any]) -> dict[str, Any]:
    request = TemplateLimitCreateRequest.model_validate(payload)
    if request.amount is None and request.sum is None:
        raise ValueError("Лимит должен содержать либо 'amount', либо 'sum'.")
    return _dump_request(request)


class TemplatesService(_BaseService):
    """Методы работы с шаблонами виртуальных карт."""

    @api_method
    async def get_templates(
        self, contract_id: str, api_version: str | None = None
    ) -> TemplatesListResponse:
        """Получить список шаблонов ВК."""
        self.logger.info("Requesting templates")
        data = await self._request(
            "get_templates",
            api_version=api_version,
            params={"contract_id": contract_id},
        )
        return decode_model(TemplatesListResponse, data)

    @api_method
    async def create_template(
        self, contract_id: str, type_: str, name: str, api_version: str | None = None
    ) -> TemplateCreateResponse:
        """Создать новый шаблон виртуальной карты.

        Типовой сценарий:
            Создать основу для выпуска виртуальных карт, а затем добавить к ней
            лимиты, товарные ограничения и географические ограничения.

        Пример вызова:
        ```python
        template = await client.templates.create_template(
            contract_id="contract-id",
            type_="wallet",
            name="Основной шаблон",
        )
        ```
        """
        request = TemplateCreateRequest(contract_id=contract_id, type=type_, name=name)
        self.logger.info("Creating virtual card template")
        data = await self._request(
            "create_template",
            api_version=api_version,
            data=_dump_request(request),
        )
        return decode_model(TemplateCreateResponse, data)

    @api_method
    async def update_template(
        self,
        template_id: str,
        contract_id: str,
        type_: str,
        name: str,
        api_version: str | None = None,
    ) -> TemplateCreateResponse:
        """Изменить существующий шаблон ВК."""
        request = TemplateCreateRequest(contract_id=contract_id, type=type_, name=name)
        self.logger.info("Updating virtual card template")
        data = await self._request(
            "update_template",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=_dump_request(request),
        )
        return decode_model(TemplateCreateResponse, data)

    @api_method
    async def delete_template(
        self,
        template_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateDeleteResponse:
        """Удалить шаблон ВК."""
        self.logger.info("Deleting virtual card template")
        data = await self._request(
            "delete_template",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return decode_model(TemplateDeleteResponse, data)

    @api_method
    async def get_template_limits(
        self, template_id: str, api_version: str | None = None
    ) -> TemplateLimitListResponse:
        """Получить список лимитов шаблона ВК."""
        self.logger.info("Requesting template limits")
        data = await self._request(
            "get_template_limits",
            api_version=api_version,
            path_params={"template_id": template_id},
        )
        return decode_model(TemplateLimitListResponse, data)

    @api_method
    async def create_template_limit(
        self, template_id: str, payload: dict[str, Any], api_version: str | None = None
    ) -> TemplateLimitCreateResponse:
        """Создать лимит для шаблона ВК."""
        request_payload = _validate_limit_payload(payload)
        self.logger.info("Creating template limit")
        data = await self._request(
            "create_template_limit",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=request_payload,
        )
        return decode_model(TemplateLimitCreateResponse, data)

    @api_method
    async def update_template_limit(
        self,
        *,
        template_id: str,
        limit_id: str,
        limits: list[dict[str, Any]],
        use_post: bool = True,
        api_version: str | None = None,
    ) -> TemplateLimitCreateResponse:
        """Обновить лимит шаблона ВК."""
        if not isinstance(limits, list) or not limits:
            raise ValueError("Параметр 'limits' должен быть непустым списком объектов лимитов.")
        validated_limits = [_validate_limit_payload(limit) for limit in limits]
        request_limits = (
            with_method_override(validated_limits, "PUT") if use_post else validated_limits
        )
        self.logger.info(
            "Updating template limit item_count=%d post_fallback=%s",
            len(validated_limits),
            use_post,
        )
        data = await self._request(
            "update_template_limit",
            api_version=api_version,
            route_name="default" if use_post else "put",
            path_params={"template_id": template_id, "limit_id": limit_id},
            json=request_limits,
        )
        return decode_model(TemplateLimitCreateResponse, data)

    @api_method
    async def delete_template_limit(
        self,
        template_id: str,
        limit_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateLimitDeleteResponse:
        """Удалить лимит шаблона ВК."""
        self.logger.info("Deleting template limit")
        data = await self._request(
            "delete_template_limit",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id, "limit_id": limit_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return decode_model(TemplateLimitDeleteResponse, data)

    @api_method
    async def get_template_restrictions(
        self, template_id: str, api_version: str | None = None
    ) -> TemplateRestrictionListResponse:
        """Получить список ограничителей шаблона ВК."""
        self.logger.info("Requesting template restrictions")
        data = await self._request(
            "get_template_restrictions",
            api_version=api_version,
            path_params={"template_id": template_id},
        )
        return decode_model(TemplateRestrictionListResponse, data)

    @api_method
    async def create_template_restriction(
        self, template_id: str, payload: dict[str, Any], api_version: str | None = None
    ) -> TemplateRestrictionCreateResponse:
        """Создать ограничитель для шаблона ВК."""
        request = TemplateRestrictionCreateRequest.model_validate(payload)
        self.logger.info("Creating template restriction")
        data = await self._request(
            "create_template_restriction",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=_dump_request(request),
        )
        return decode_model(TemplateRestrictionCreateResponse, data)

    @api_method
    async def update_template_restriction(
        self,
        template_id: str,
        restriction_id: str,
        payload: dict[str, Any],
        api_version: str | None = None,
        use_post: bool = True,
    ) -> TemplateRestrictionCreateResponse:
        """Изменить ограничитель шаблона ВК."""
        request = TemplateRestrictionCreateRequest.model_validate(payload)
        validated_payload = _dump_request(request)
        request_payload = (
            with_method_override(validated_payload, "PUT") if use_post else validated_payload
        )
        self.logger.info("Updating template restriction post_fallback=%s", use_post)
        data = await self._request(
            "update_template_restriction",
            api_version=api_version,
            route_name="default" if use_post else "put",
            path_params={"template_id": template_id, "restriction_id": restriction_id},
            data=request_payload,
        )
        return decode_model(TemplateRestrictionCreateResponse, data)

    @api_method
    async def delete_template_restriction(
        self,
        template_id: str,
        restriction_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateRestrictionDeleteResponse:
        """Удалить ограничитель шаблона ВК."""
        self.logger.info("Deleting template restriction")
        data = await self._request(
            "delete_template_restriction",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id, "restriction_id": restriction_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return decode_model(TemplateRestrictionDeleteResponse, data)

    @api_method
    async def get_template_georestrictions(
        self, template_id: str, api_version: str | None = None
    ) -> TemplateGeoRestrictionListResponse:
        """Получить список геоограничителей шаблона ВК."""
        self.logger.info("Requesting template geo restrictions")
        data = await self._request(
            "get_template_georestrictions",
            api_version=api_version,
            path_params={"template_id": template_id},
        )
        return decode_model(TemplateGeoRestrictionListResponse, data)

    @api_method
    async def create_template_georestriction(
        self, template_id: str, payload: dict[str, Any], api_version: str | None = None
    ) -> TemplateGeoRestrictionCreateResponse:
        """Создать геоограничитель шаблона ВК."""
        request = TemplateGeoRestrictionCreateRequest.model_validate(payload)
        self.logger.info("Creating template geo restriction")
        data = await self._request(
            "create_template_georestriction",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=_dump_request(request),
        )
        return decode_model(TemplateGeoRestrictionCreateResponse, data)

    @api_method
    async def update_template_georestriction(
        self,
        template_id: str,
        georestriction_id: str,
        payload: dict[str, Any],
        api_version: str | None = None,
        use_post: bool = True,
    ) -> TemplateGeoRestrictionCreateResponse:
        """Изменить геоограничитель шаблона ВК."""
        request = TemplateGeoRestrictionCreateRequest.model_validate(payload)
        validated_payload = _dump_request(request)
        request_payload = (
            with_method_override(validated_payload, "PUT") if use_post else validated_payload
        )
        self.logger.info("Updating template geo restriction post_fallback=%s", use_post)
        data = await self._request(
            "update_template_georestriction",
            api_version=api_version,
            route_name="default" if use_post else "put",
            path_params={
                "template_id": template_id,
                "georestriction_id": georestriction_id,
            },
            data=request_payload,
        )
        return decode_model(TemplateGeoRestrictionCreateResponse, data)

    @api_method
    async def delete_template_georestriction(
        self,
        template_id: str,
        georestriction_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateGeoRestrictionDeleteResponse:
        """Удалить геоограничитель шаблона ВК."""
        self.logger.info("Deleting template geo restriction")
        data = await self._request(
            "delete_template_georestriction",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={
                "template_id": template_id,
                "georestriction_id": georestriction_id,
            },
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return decode_model(TemplateGeoRestrictionDeleteResponse, data)

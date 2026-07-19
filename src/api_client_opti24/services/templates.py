from typing import Any

from ..decorators import api_method
from ..models.templates import (
    TemplateCreateResponse,
    TemplateDeleteResponse,
    TemplateGeoRestrictionCreateResponse,
    TemplateGeoRestrictionDeleteResponse,
    TemplateGeoRestrictionListResponse,
    TemplateLimitCreateResponse,
    TemplateLimitDeleteResponse,
    TemplateLimitListResponse,
    TemplateRestrictionCreateResponse,
    TemplateRestrictionDeleteResponse,
    TemplateRestrictionListResponse,
    TemplatesListResponse,
)
from ..payloads import with_method_override
from ..service_base import _BaseService


class TemplatesService(_BaseService):
    # ---------- ШАБЛОНЫ ВК ----------

    """
    ВК – виртуальная карта. Чтобы выпустить ВК, потребуется создать шаблон лимита и прикрепить этот шаблон к пользователю.
    Прикрепление происходит на этапе приглашения нового пользователя или методом для существующих пользователей.
    Шаблон – это первоначальные параметры (Тип карты, Лимиты, Ограничители), с которыми будет выпущена эта ВК,
    и все последующие, если использовать этот шаблон.
    Шаблон сделан с точки зрения безопасности,
    для того чтобы по-умолчанию все выпускаемые ВК имели ограничения на покупку (Лимит/Ограничитель).
    """

    @api_method
    async def get_templates(
        self, contract_id: str, api_version: str | None = None
    ) -> TemplatesListResponse:
        """Получить список шаблонов ВК"""
        self.logger.info("Requesting templates")
        data = await self._request(
            "get_templates",
            api_version=api_version,
            params={"contract_id": contract_id},
        )
        return TemplatesListResponse(**data)

    @api_method
    async def create_template(
        self, contract_id: str, type_: str, name: str, api_version: str | None = None
    ) -> TemplateCreateResponse:
        """Создать новый шаблон ВК"""
        payload = {"contract_id": contract_id, "type": type_, "name": name}
        self.logger.info("Creating virtual card template")
        data = await self._request(
            "create_template",
            api_version=api_version,
            data=payload,
        )
        return TemplateCreateResponse(**data)

    @api_method
    async def update_template(
        self,
        template_id: str,
        contract_id: str,
        type_: str,
        name: str,
        api_version: str | None = None,
    ) -> TemplateCreateResponse:
        """Изменить существующий шаблон ВК"""
        payload = {"contract_id": contract_id, "type": type_, "name": name}
        self.logger.info("Updating virtual card template")
        data = await self._request(
            "update_template",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=payload,
        )
        return TemplateCreateResponse(**data)

    @api_method
    async def delete_template(
        self,
        template_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateDeleteResponse:
        """Удалить шаблон ВК"""
        self.logger.info("Deleting virtual card template")
        data = await self._request(
            "delete_template",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return TemplateDeleteResponse(**data)

    # ---------- ЛИМИТЫ ----------
    @api_method
    async def get_template_limits(
        self, template_id: str, api_version: str | None = None
    ) -> TemplateLimitListResponse:
        """Получить список лимитов шаблона ВК"""
        self.logger.info("Requesting template limits")
        data = await self._request(
            "get_template_limits",
            api_version=api_version,
            path_params={"template_id": template_id},
        )
        return TemplateLimitListResponse(**data)

    @api_method
    async def create_template_limit(
        self, template_id: str, payload: dict[str, Any], api_version: str | None = None
    ) -> TemplateLimitCreateResponse:
        """Создать лимит для шаблона ВК"""
        self.logger.info("Creating template limit")
        data = await self._request(
            "create_template_limit",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=payload,
        )
        return TemplateLimitCreateResponse(**data)

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
        """
        Обновить лимит шаблона ВК.
        Новые параметры описывается в виде словаря, содержащего параметры amount, sum, time, term и т.д.
        Если система не поддерживает PUT — передай `use_post=True`,
        тогда запрос будет отправлен методом POST с добавленным `_method="PUT"`.

        Args:
            template_id (str): ID шаблона ВК
            limit_id (str): ID лимита, который нужно обновить
            limits (list[dict]): список новых параметров лимита для обновления, пример:
                [
                    {
                        "contract_id": "1-380B94P",
                        "product_type": "1-276PF01",
                        "product_group": "1-276PF0E",
                        "sum": {"currency": "810", "value": 5000}, 810 - RUB, LIT - литры
                        "time": {"type": 5, "number": 1},
                        "term": {
                            "time": {"from": "03:00", "to": "08:00"},
                            "days": "1111100",
                            "type": 1
                        }
                    }
                ]
            use_post (bool): если True — POST с `_method=PUT`, иначе реальный PUT
            api_version (str): версия API (по умолчанию "v2")

        Returns:
            TemplateLimitCreateResponse: объект с ID изменённого лимита
        """
        self.logger.info(
            "Updating template limit item_count=%d post_fallback=%s",
            len(limits),
            use_post,
        )

        # Проверка содержимого
        if not limits or not isinstance(limits, list):
            raise ValueError("Параметр 'limits' должен быть списком объектов лимитов.")

        for limit in limits:
            if "contract_id" not in limit:
                raise ValueError("Каждый лимит должен содержать 'contract_id'.")
            if "time" not in limit:
                raise ValueError("Каждый лимит должен содержать объект 'time'.")
            if "amount" not in limit and "sum" not in limit:
                raise ValueError("Каждый лимит должен содержать либо 'amount', либо 'sum'.")

        request_limits = (
            with_method_override(limits, "PUT") if use_post else [dict(limit) for limit in limits]
        )

        # Отправляем список лимитов
        data = await self._request(
            "update_template_limit",
            api_version=api_version,
            route_name="default" if use_post else "put",
            path_params={"template_id": template_id, "limit_id": limit_id},
            json=request_limits,
        )

        return TemplateLimitCreateResponse(**data)

    @api_method
    async def delete_template_limit(
        self,
        template_id: str,
        limit_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateLimitDeleteResponse:
        """Удалить лимит шаблона ВК"""
        self.logger.info("Deleting template limit")
        data = await self._request(
            "delete_template_limit",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id, "limit_id": limit_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return TemplateLimitDeleteResponse(**data)

    # ---------- ОГРАНИЧИТЕЛИ ----------
    @api_method
    async def get_template_restrictions(
        self, template_id: str, api_version: str | None = None
    ) -> TemplateRestrictionListResponse:
        """Получить список ограничителей шаблона ВК"""
        self.logger.info("Requesting template restrictions")
        data = await self._request(
            "get_template_restrictions",
            api_version=api_version,
            path_params={"template_id": template_id},
        )
        return TemplateRestrictionListResponse(**data)

    @api_method
    async def create_template_restriction(
        self, template_id: str, payload: dict[str, Any], api_version: str | None = None
    ) -> TemplateRestrictionCreateResponse:
        """Создать ограничитель для шаблона ВК"""
        self.logger.info("Creating template restriction")
        data = await self._request(
            "create_template_restriction",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=payload,
        )
        return TemplateRestrictionCreateResponse(**data)

    @api_method
    async def update_template_restriction(
        self,
        template_id: str,
        restriction_id: str,
        payload: dict[str, Any],
        api_version: str | None = None,
        use_post: bool = True,
    ) -> TemplateRestrictionCreateResponse:
        """Изменить ограничитель шаблона ВК"""
        self.logger.info("Updating template restriction post_fallback=%s", use_post)
        request_payload = with_method_override(payload, "PUT") if use_post else dict(payload)
        data = await self._request(
            "update_template_restriction",
            api_version=api_version,
            route_name="default" if use_post else "put",
            path_params={"template_id": template_id, "restriction_id": restriction_id},
            data=request_payload,
        )
        return TemplateRestrictionCreateResponse(**data)

    @api_method
    async def delete_template_restriction(
        self,
        template_id: str,
        restriction_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateRestrictionDeleteResponse:
        """Удалить ограничитель шаблона ВК"""
        self.logger.info("Deleting template restriction")
        data = await self._request(
            "delete_template_restriction",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id, "restriction_id": restriction_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return TemplateRestrictionDeleteResponse(**data)

    # ---------- ГЕООГРАНИЧИТЕЛИ ----------
    @api_method
    async def get_template_georestrictions(
        self, template_id: str, api_version: str | None = None
    ) -> TemplateGeoRestrictionListResponse:
        """Получить список геоограничителей шаблона ВК"""
        self.logger.info("Requesting template geo restrictions")
        data = await self._request(
            "get_template_georestrictions",
            api_version=api_version,
            path_params={"template_id": template_id},
        )
        return TemplateGeoRestrictionListResponse(**data)

    @api_method
    async def create_template_georestriction(
        self, template_id: str, payload: dict[str, Any], api_version: str | None = None
    ) -> TemplateGeoRestrictionCreateResponse:
        """Создать геоограничитель для шаблона ВК"""
        self.logger.info("Creating template geo restriction")
        data = await self._request(
            "create_template_georestriction",
            api_version=api_version,
            path_params={"template_id": template_id},
            data=payload,
        )
        return TemplateGeoRestrictionCreateResponse(**data)

    @api_method
    async def update_template_georestriction(
        self,
        template_id: str,
        georestriction_id: str,
        payload: dict[str, Any],
        api_version: str | None = None,
        use_post: bool = True,
    ) -> TemplateGeoRestrictionCreateResponse:
        """Изменить геоограничитель шаблона ВК"""
        self.logger.info("Updating template geo restriction post_fallback=%s", use_post)
        request_payload = with_method_override(payload, "PUT") if use_post else dict(payload)
        data = await self._request(
            "update_template_georestriction",
            api_version=api_version,
            route_name="default" if use_post else "put",
            path_params={"template_id": template_id, "georestriction_id": georestriction_id},
            data=request_payload,
        )
        return TemplateGeoRestrictionCreateResponse(**data)

    @api_method
    async def delete_template_georestriction(
        self,
        template_id: str,
        georestriction_id: str,
        api_version: str | None = None,
        use_post: bool = False,
    ) -> TemplateGeoRestrictionDeleteResponse:
        """Удалить геоограничитель шаблона ВК"""
        self.logger.info("Deleting template geo restriction")
        data = await self._request(
            "delete_template_georestriction",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"template_id": template_id, "georestriction_id": georestriction_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return TemplateGeoRestrictionDeleteResponse(**data)

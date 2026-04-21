from ..decorators import api_method
from ..logger import logger
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


class TemplatesMixin:
    # ---------- ШАБЛОНЫ ВК ----------

    """
    ВК – виртуальная карта. Чтобы выпустить ВК, потребуется создать шаблон лимита и прикрепить этот шаблон к пользователю.
    Прикрепление происходит на этапе приглашения нового пользователя или методом для существующих пользователей.
    Шаблон – это первоначальные параметры (Тип карты, Лимиты, Ограничители), с которыми будет выпущена эта ВК,
    и все последующие, если использовать этот шаблон.
    Шаблон сделан с точки зрения безопасности,
    для того чтобы по-умолчанию все выпускаемые ВК имели ограничения на покупку (Лимит/Ограничитель).
    """

    @api_method(require_session=True, default_version="v2")
    async def get_templates(
        self, contract_id: str, api_version: str = "v2"
    ) -> TemplatesListResponse:
        """Получить список шаблонов ВК"""
        logger.info("Получение списка шаблонов для договора %s", contract_id)
        data = await self._request(
            "get",
            "vc/templates",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": contract_id},
        )
        return TemplatesListResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def create_template(
        self, contract_id: str, type_: str, name: str, api_version: str = "v2"
    ) -> TemplateCreateResponse:
        """Создать новый шаблон ВК"""
        payload = {"contract_id": contract_id, "type": type_, "name": name}
        logger.info("Создание шаблона ВК: %s", payload)
        data = await self._request(
            "post",
            "vc/templates",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def update_template(
        self,
        template_id: str,
        contract_id: str,
        type_: str,
        name: str,
        api_version: str = "v2",
    ) -> TemplateCreateResponse:
        """Изменить существующий шаблон ВК"""
        payload = {"contract_id": contract_id, "type": type_, "name": name}
        logger.info("Изменение шаблона %s с данными: %s", template_id, payload)
        data = await self._request(
            "post",
            f"vc/templates/{template_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def delete_template(
        self, template_id: str, api_version: str = "v2"
    ) -> TemplateDeleteResponse:
        """Удалить шаблон ВК"""
        logger.info("Удаление шаблона %s", template_id)
        data = await self._request(
            "delete",
            f"vc/templates/{template_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateDeleteResponse(**data)

    # ---------- ЛИМИТЫ ----------
    @api_method(require_session=True, default_version="v2")
    async def get_template_limits(
        self, template_id: str, api_version: str = "v2"
    ) -> TemplateLimitListResponse:
        """Получить список лимитов шаблона ВК"""
        logger.info("Получение списка лимитов шаблона %s", template_id)
        data = await self._request(
            "get",
            f"vc/templates/{template_id}/limits",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateLimitListResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def create_template_limit(
        self, template_id: str, payload: dict, api_version: str = "v2"
    ) -> TemplateLimitCreateResponse:
        """Создать лимит для шаблона ВК"""
        logger.info("Создание лимита для шаблона %s: %s", template_id, payload)
        data = await self._request(
            "post",
            f"vc/templates/{template_id}/limits",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateLimitCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def update_template_limit(
        self,
        *,
        template_id: str,
        limit_id: str,
        limits: list[dict],
        use_post: bool = True,
        api_version: str = "v2",
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
        logger.info(
            "Обновление лимита %s шаблона %s. Кол-во лимитов=%d, use_post=%s",
            limit_id,
            template_id,
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

        # Добавляем _method=PUT если используется POST
        method = "post" if use_post else "put"
        if use_post:
            for limit in limits:
                limit["_method"] = "PUT"

        # Отправляем список лимитов
        data = await self._request(
            method,
            f"vc/templates/{template_id}/limits/{limit_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=limits,
        )

        return TemplateLimitCreateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def delete_template_limit(
        self, template_id: str, limit_id: str, api_version: str = "v2"
    ) -> TemplateLimitDeleteResponse:
        """Удалить лимит шаблона ВК"""
        logger.info("Удаление лимита %s шаблона %s", limit_id, template_id)
        data = await self._request(
            "delete",
            f"vc/templates/{template_id}/limits/{limit_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateLimitDeleteResponse(**data)

    # ---------- ОГРАНИЧИТЕЛИ ----------
    @api_method(require_session=True, default_version="v2")
    async def get_template_restrictions(
        self, template_id: str, api_version: str = "v2"
    ) -> TemplateRestrictionListResponse:
        """Получить список ограничителей шаблона ВК"""
        logger.info("Получение ограничителей шаблона %s", template_id)
        data = await self._request(
            "get",
            f"vc/templates/{template_id}/restrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateRestrictionListResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def create_template_restriction(
        self, template_id: str, payload: dict, api_version: str = "v2"
    ) -> TemplateRestrictionCreateResponse:
        """Создать ограничитель для шаблона ВК"""
        logger.info("Создание ограничителя для шаблона %s: %s", template_id, payload)
        data = await self._request(
            "post",
            f"vc/templates/{template_id}/restrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateRestrictionCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def update_template_restriction(
        self,
        template_id: str,
        restriction_id: str,
        payload: dict,
        api_version: str = "v2",
    ) -> TemplateRestrictionCreateResponse:
        """Изменить ограничитель шаблона ВК"""
        logger.info(
            "Изменение ограничителя %s шаблона %s: %s",
            restriction_id,
            template_id,
            payload,
        )
        data = await self._request(
            "post",
            f"vc/templates/{template_id}/restrictions/{restriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateRestrictionCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def delete_template_restriction(
        self, template_id: str, restriction_id: str, api_version: str = "v2"
    ) -> TemplateRestrictionDeleteResponse:
        """Удалить ограничитель шаблона ВК"""
        logger.info("Удаление ограничителя %s шаблона %s", restriction_id, template_id)
        data = await self._request(
            "delete",
            f"vc/templates/{template_id}/restrictions/{restriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateRestrictionDeleteResponse(**data)

    # ---------- ГЕООГРАНИЧИТЕЛИ ----------
    @api_method(require_session=True, default_version="v2")
    async def get_template_georestrictions(
        self, template_id: str, api_version: str = "v2"
    ) -> TemplateGeoRestrictionListResponse:
        """Получить список геоограничителей шаблона ВК"""
        logger.info("Получение геоограничителей шаблона %s", template_id)
        data = await self._request(
            "get",
            f"vc/templates/{template_id}/georestrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateGeoRestrictionListResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def create_template_georestriction(
        self, template_id: str, payload: dict, api_version: str = "v2"
    ) -> TemplateGeoRestrictionCreateResponse:
        """Создать геоограничитель для шаблона ВК"""
        logger.info("Создание геоограничителя для шаблона %s: %s", template_id, payload)
        data = await self._request(
            "post",
            f"vc/templates/{template_id}/georestrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateGeoRestrictionCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def update_template_georestriction(
        self,
        template_id: str,
        georestriction_id: str,
        payload: dict,
        api_version: str = "v2",
    ) -> TemplateGeoRestrictionCreateResponse:
        """Изменить геоограничитель шаблона ВК"""
        logger.info(
            "Изменение геоограничителя %s шаблона %s: %s",
            georestriction_id,
            template_id,
            payload,
        )
        data = await self._request(
            "post",
            f"vc/templates/{template_id}/georestrictions/{georestriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateGeoRestrictionCreateResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def delete_template_georestriction(
        self, template_id: str, georestriction_id: str, api_version: str = "v2"
    ) -> TemplateGeoRestrictionDeleteResponse:
        """Удалить геоограничитель шаблона ВК"""
        logger.info("Удаление геоограничителя %s шаблона %s", georestriction_id, template_id)
        data = await self._request(
            "delete",
            f"vc/templates/{template_id}/georestrictions/{georestriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateGeoRestrictionDeleteResponse(**data)

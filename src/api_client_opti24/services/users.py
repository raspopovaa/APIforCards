from ..decorators import api_method
from ..logger import logger
from ..models.users import (
    UserBoolResponse,
    UserCreateResponse,
    UserListResponse,
)
from ..utils import to_json_param


class UsersMixin:
    """
    Методы для работы с пользователями (v2).
    """

    # -------------------- Список пользователей --------------------

    @api_method(require_session=True, default_version="v2")
    async def get_users(
        self,
        *,
        sort: str | None = None,
        page: int | None = None,
        on_page: int | None = None,
        q: str | None = None,
        filter: dict | None = None,
        api_version: str = "v2",
    ) -> UserListResponse:
        """
        Получить список пользователей.

        Пример:
        await client.get_users(sort="id", page=1, on_page=10, q="Кирилл", filter={"role": "Driver"})
        """
        params = {
            "sort": sort,
            "page": page,
            "on_page": on_page,
            "q": q,
            "filter": to_json_param(filter) if filter else None,
        }
        params = {k: v for k, v in params.items() if v is not None}

        logger.info(f"Вызов метода get_users с параметрами: {params}")

        raw = await self._request(
            "get",
            "users",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        return UserListResponse(**raw)

    # -------------------- Создание пользователя --------------------

    @api_method(require_session=True, default_version="v2")
    async def create_user(
        self,
        *,
        uuid: str,
        mobile: str,
        api_version: str = "v2",
    ) -> UserCreateResponse:
        """
        Создание водителя без персональных данных.
        Данный метод позволяет создать себе технических водителей без ФИО (персональных данных),
        чтобы использовать их для дальнейших интеграций. Реальных водителей стоит создавать через сервис “Инвайты”.


        Пример:
        await client.create_user(uuid="62f2e267-4398-4ea2-b02e-6e88b81b0958", mobile="79999999999")
        """
        body = {"uuid": uuid, "mobile": mobile}

        logger.info(f"Создание пользователя с тел. {mobile}")

        raw = await self._request(
            "post",
            "users",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        return UserCreateResponse(**raw)

    # -------------------- Прикрепление договоров --------------------

    @api_method(require_session=True, default_version="v2")
    async def attach_contracts(
        self,
        *,
        user_id: str,
        contracts: list[dict],
        api_version: str = "v2",
    ) -> UserBoolResponse:
        """
        Прикрепление договоров к пользователю.

        Пример:
        await client.attach_contracts(user_id="1-FK485FK", contracts=[
            {"sid": "1-380B94P", "template_id": "1-3BE470B", "use_mpc": True}
        ])
        """
        logger.info(f"Прикрепление договоров к пользователю {user_id}")

        raw = await self._request(
            "post",
            f"users/{user_id}/attachContracts",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=contracts,
        )

        return UserBoolResponse(**raw)

    # -------------------- Открепление договоров --------------------

    @api_method(require_session=True, default_version="v2")
    async def detach_contracts(
        self,
        *,
        user_id: str,
        contracts: list[str],
        api_version: str = "v2",
    ) -> UserBoolResponse:
        """
        Открепление договоров от пользователя.

        Пример:
        await client.detach_contracts(user_id="1-FK485FK", contracts=["1-380B94P", "1-37PYW2D"])
        """
        logger.info(f"Открепление договоров от пользователя {user_id}")

        raw = await self._request(
            "post",
            f"users/{user_id}/detachContracts",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=contracts,
        )

        return UserBoolResponse(**raw)

    # -------------------- Прикрепление карты --------------------

    @api_method(require_session=True, default_version="v2")
    async def attach_card(
        self,
        *,
        user_id: str,
        card_id: str,
        api_version: str = "v2",
    ) -> UserBoolResponse:
        """
        Прикрепление карты к пользователю.

        Пример:
        await client.attach_card(user_id="1-FK485FK", card_id="5050505")
        """
        logger.info(f"Прикрепление карты {card_id} к пользователю {user_id}")

        raw = await self._request(
            "post",
            f"users/{user_id}/attachCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data={"card_id": card_id},
        )

        return UserBoolResponse(**raw)

    # -------------------- Открепление карты --------------------

    @api_method(require_session=True, default_version="v2")
    async def detach_card(
        self,
        *,
        user_id: str,
        card_id: str,
        api_version: str = "v2",
    ) -> UserBoolResponse:
        """
        Открепление карты от пользователя.

        Пример:
        await client.detach_card(user_id="1-FK485FK", card_id="5050505")
        """
        logger.info(f"Открепление карты {card_id} от пользователя {user_id}")

        raw = await self._request(
            "post",
            f"users/{user_id}/detachCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data={"card_id": card_id},
        )

        return UserBoolResponse(**raw)

    # -------------------- Удаление пользователя --------------------

    @api_method(require_session=True, default_version="v2")
    async def delete_user(
        self,
        *,
        user_id: str,
        api_version: str = "v2",
    ) -> UserBoolResponse:
        """
        Удаление пользователя.
        Если ваша система не умеет отправлять DELETE запросы, то можно отправить POST, но в BODY указать _method=DELETE:
        Пример:
        await client.delete_user(user_id="1-FK485FK")
        """
        logger.info(f"Удаление пользователя {user_id}")

        raw = await self._request(
            "delete",
            f"users/{user_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )

        return UserBoolResponse(**raw)

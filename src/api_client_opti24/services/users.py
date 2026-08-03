from collections.abc import Mapping
from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.users import (
    UserAttachContractRequest,
    UserBoolResponse,
    UserCreateResponse,
    UserListResponse,
)
from ..payloads import with_method_override
from ..service_base import _BaseService
from ..utils import to_json_param


class UsersService(_BaseService):
    """
    Методы для работы с пользователями (v2).
    """

    # -------------------- Список пользователей --------------------

    @api_method
    async def get_users(
        self,
        *,
        sort: str | None = None,
        page: int | None = None,
        on_page: int | None = None,
        q: str | None = None,
        filter: dict[str, Any] | None = None,
        api_version: str | None = None,
    ) -> UserListResponse:
        """
        Получить список пользователей.

        Пример:
        await client.users.get_users(
            sort="id", page=1, on_page=10, q="Кирилл", filter={"role": "Driver"}
        )
        """
        params = {
            "sort": sort,
            "page": page,
            "on_page": on_page,
            "q": q,
            "filter": to_json_param(filter) if filter else None,
        }
        params = {k: v for k, v in params.items() if v is not None}

        raw = await self._request(
            "get_users",
            api_version=api_version,
            params=params,
        )

        return decode_model(UserListResponse, raw)

    # -------------------- Создание пользователя --------------------

    @api_method
    async def create_user(
        self,
        *,
        uuid: str,
        mobile: str,
        api_version: str | None = None,
    ) -> UserCreateResponse:
        """
        Создание водителя без персональных данных.
        Данный метод позволяет создать себе технических водителей без ФИО (персональных данных),
        чтобы использовать их для дальнейших интеграций. Реальных водителей стоит создавать через сервис “Инвайты”.


        Типовой сценарий:
            Создать технического водителя без ФИО для последующего назначения
            договора или карты. Для реального пользователя используйте invites.

        Пример вызова:
        ```python
        await client.users.create_user(
            uuid="62f2e267-4398-4ea2-b02e-6e88b81b0958", mobile="79999999999"
        )
        ```

        Пример payload:
        ```json
        {"uuid": "62f2e267-4398-4ea2-b02e-6e88b81b0958", "mobile": "79999999999"}
        ```
        """
        body = {"uuid": uuid, "mobile": mobile}

        raw = await self._request(
            "create_user",
            api_version=api_version,
            data=body,
        )

        return decode_model(UserCreateResponse, raw)

    # -------------------- Прикрепление договоров --------------------

    @api_method
    async def attach_contracts(
        self,
        *,
        user_id: str,
        contracts: list[UserAttachContractRequest | Mapping[str, object]],
        api_version: str | None = None,
    ) -> UserBoolResponse:
        """
        Прикрепление договоров к пользователю.

        Пример:
        await client.users.attach_contracts(user_id="1-FK485FK", contracts=[
            {"sid": "1-380B94P", "template_id": "1-3BE470B", "use_mpc": True}
        ])
        """
        payload = [
            UserAttachContractRequest.model_validate(contract).model_dump(exclude_none=True)
            for contract in contracts
        ]

        raw = await self._request(
            "attach_contracts",
            api_version=api_version,
            path_params={"user_id": user_id},
            json=payload,
        )

        return decode_model(UserBoolResponse, raw)

    # -------------------- Открепление договоров --------------------

    @api_method
    async def detach_contracts(
        self,
        *,
        user_id: str,
        contracts: list[str],
        api_version: str | None = None,
    ) -> UserBoolResponse:
        """
        Открепление договоров от пользователя.

        Пример:
        await client.users.detach_contracts(
            user_id="1-FK485FK", contracts=["1-380B94P", "1-37PYW2D"]
        )
        """
        raw = await self._request(
            "detach_contracts",
            api_version=api_version,
            path_params={"user_id": user_id},
            json=contracts,
        )

        return decode_model(UserBoolResponse, raw)

    # -------------------- Прикрепление карты --------------------

    @api_method
    async def attach_card(
        self,
        *,
        user_id: str,
        card_id: str,
        api_version: str | None = None,
    ) -> UserBoolResponse:
        """
        Прикрепление карты к пользователю.

        Пример:
        await client.users.attach_card(user_id="1-FK485FK", card_id="5050505")
        """
        raw = await self._request(
            "attach_card",
            api_version=api_version,
            path_params={"user_id": user_id},
            data={"card_id": card_id},
        )

        return decode_model(UserBoolResponse, raw)

    # -------------------- Открепление карты --------------------

    @api_method
    async def detach_card(
        self,
        *,
        user_id: str,
        card_id: str,
        api_version: str | None = None,
    ) -> UserBoolResponse:
        """
        Открепление карты от пользователя.

        Пример:
        await client.users.detach_card(user_id="1-FK485FK", card_id="5050505")
        """
        raw = await self._request(
            "detach_card",
            api_version=api_version,
            path_params={"user_id": user_id},
            data={"card_id": card_id},
        )

        return decode_model(UserBoolResponse, raw)

    # -------------------- Удаление пользователя --------------------

    @api_method
    async def delete_user(
        self,
        *,
        user_id: str,
        use_post: bool = False,
        api_version: str | None = None,
    ) -> UserBoolResponse:
        """
        Удаление пользователя.
        Если ваша система не умеет отправлять DELETE запросы, то можно отправить POST, но в BODY указать _method=DELETE:
        Пример:
        await client.users.delete_user(user_id="1-FK485FK")
        """
        raw = await self._request(
            "delete_user",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"user_id": user_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )

        return decode_model(UserBoolResponse, raw)

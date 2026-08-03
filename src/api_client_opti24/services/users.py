from collections.abc import AsyncIterator, Mapping
from typing import Any

from ..models.users import (
    UserAttachContractRequest,
    UserBoolResponse,
    UserCreateResponse,
    UserItem,
    UserListResponse,
)
from ..operations import operation
from ..payloads import with_method_override
from ..service_base import _BaseService
from ..utils import to_json_param

GET_USERS = operation("get_users", UserListResponse)
CREATE_USER = operation("create_user", UserCreateResponse)
ATTACH_CONTRACTS = operation("attach_contracts", UserBoolResponse)
DETACH_CONTRACTS = operation("detach_contracts", UserBoolResponse)
ATTACH_CARD = operation("attach_card", UserBoolResponse)
DETACH_CARD = operation("detach_card", UserBoolResponse)
DELETE_USER = operation("delete_user", UserBoolResponse)


class UsersService(_BaseService):
    """
    Методы для работы с пользователями (v2).
    """

    # -------------------- Список пользователей --------------------

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

        self.logger.info("Requesting users")

        return await self._request(
            GET_USERS,
            api_version=api_version,
            params=params,
        )

    async def iter_users(
        self,
        *,
        sort: str | None = None,
        q: str | None = None,
        filter: dict[str, Any] | None = None,
        on_page: int = 100,
        max_pages: int = 100,
        api_version: str | None = None,
    ) -> AsyncIterator[UserItem]:
        """Последовательно получить пользователей, ограничив число страниц."""
        if on_page < 1 or max_pages < 1:
            raise ValueError("on_page and max_pages must be greater than zero")
        yielded = 0
        for page in range(1, max_pages + 1):
            response = await self.get_users(
                sort=sort,
                page=page,
                on_page=on_page,
                q=q,
                filter=filter,
                api_version=api_version,
            )
            for item in response.result:
                yield item
                yielded += 1
            if not response.result or yielded >= response.total_count:
                return

    # -------------------- Создание пользователя --------------------

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

        self.logger.info("Creating user")

        return await self._request(
            CREATE_USER,
            api_version=api_version,
            data=body,
        )

    # -------------------- Прикрепление договоров --------------------

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

        return await self._request(
            ATTACH_CONTRACTS,
            api_version=api_version,
            path_params={"user_id": user_id},
            json=payload,
        )

    # -------------------- Открепление договоров --------------------

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
        self.logger.info("Detaching contracts from user")

        return await self._request(
            DETACH_CONTRACTS,
            api_version=api_version,
            path_params={"user_id": user_id},
            json=contracts,
        )

    # -------------------- Прикрепление карты --------------------

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
        self.logger.info("Attaching card to user")

        return await self._request(
            ATTACH_CARD,
            api_version=api_version,
            path_params={"user_id": user_id},
            data={"card_id": card_id},
        )

    # -------------------- Открепление карты --------------------

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
        self.logger.info("Detaching card from user")

        return await self._request(
            DETACH_CARD,
            api_version=api_version,
            path_params={"user_id": user_id},
            data={"card_id": card_id},
        )

    # -------------------- Удаление пользователя --------------------

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
        self.logger.info("Deleting user")

        return await self._request(
            DELETE_USER,
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"user_id": user_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )

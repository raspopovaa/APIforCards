from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.invites import (
    InviteBoolResponse,
    InviteListResponse,
    InviteResponse,
)
from ..payloads import with_method_override
from ..service_base import _BaseService


class InvitesService(_BaseService):
    """
    Методы для работы с приглашениями пользователей (v2).
    Invites – функционал регистрации пользователей.
    Приглашение можно отправить по Email/SMS или получить уникальную ссылку и отправить удобным для вас способом.
    Ссылка действует 3 календарных дня, повторно направить Email/SMS по одному приглашению можно не чаще 3х раз в день.
    С помощью приглашения можно зарегистрировать, например, водителя и сразу привязать шаблон виртуальной карты,
    либо привязать физические топливные карты.
    """

    # ---------------------- GET /v2/invites ----------------------
    @api_method
    async def get_invites(
        self,
        *,
        role: str | None = None,
        user_id: str | None = None,
        sort: str | None = None,
        status: str | None = None,
        q: str | None = None,
        page: int | None = None,
        on_page: int | None = None,
        api_version: str | None = None,
    ) -> InviteListResponse:
        """
        Получить список приглашений (v2).

        Параметры фильтрации:
        - role: Фильтрация по ID роли (Supervisor, Regulatory, Driver, Readonly)
        - user_id: Отобразить инвайты по которым произошла регистрация пользователя (true)
        - sort: поле для сортировки ('sended_at', 'status' и т.д.)
        - status: Фильтрация по статусу заявки (Active, Expired, Finished)
        - q: Поисковый запрос (Ищет email и mobile)
        - page, on_page: пагинация
        """
        params = {
            "role": role,
            "user_id": user_id,
            "sort": sort,
            "status": status,
            "q": q,
            "page": page,
            "on_page": on_page,
        }
        params = {k: v for k, v in params.items() if v is not None}

        raw = await self._request(
            "get_invites",
            api_version=api_version,
            params=params,
        )
        return decode_model(InviteListResponse, raw)

    # ---------------------- POST /v2/invites / invites_free ----------------------
    @api_method
    async def create_invite(
        self,
        *,
        data: dict[str, Any],
        with_send: bool = True,
        api_version: str | None = None,
    ) -> InviteResponse:
        """
        Создать приглашение.

        with_send=True  → POST /v2/invites  (с отправкой SMS/Email)
        with_send=False → POST /v2/invites_free (без отправки)

        Типовой сценарий:
            Зарегистрировать водителя и передать ему приглашение. Если доставку
            выполняет внешняя система, используйте ``with_send=False``.

        Пример вызова:
        ```python
        invite = await client.invites.create_invite(
            data={
                "role": "Driver",
                "mobile": "79990000000",
                "contracts": [{"sid": "contract-id"}],
            },
            with_send=False,
        )
        ```

        Пример payload:
        ```json
        {
          "role": "Driver",
          "mobile": "79990000000",
          "contracts": [{"sid": "contract-id"}]
        }
        ```
        """
        raw = await self._request(
            "create_invite",
            api_version=api_version,
            route_name="default" if with_send else "without_send",
            json=data,
        )
        return decode_model(InviteResponse, raw)

    # ---------------------- DELETE /v2/invites/{invite_id} ----------------------
    @api_method
    async def delete_invite(
        self,
        *,
        invite_id: str,
        use_post: bool = False,
        api_version: str | None = None,
    ) -> InviteBoolResponse:
        """
        Удалить приглашение (v2).
        """
        raw = await self._request(
            "delete_invite",
            api_version=api_version,
            route_name="post_override" if use_post else "default",
            path_params={"invite_id": invite_id},
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return decode_model(InviteBoolResponse, raw)

    # ---------------------- GET /v2/invites/{invite_id}/send ----------------------
    @api_method
    async def resend_invite(
        self,
        *,
        invite_id: str,
        api_version: str | None = None,
    ) -> InviteResponse:
        """
        Повторно отправить приглашение (v2).
        """
        raw = await self._request(
            "resend_invite",
            api_version=api_version,
            path_params={"invite_id": invite_id},
        )
        return decode_model(InviteResponse, raw)

    # ---------------------- POST /v2/invites/{invite_id}/prolong / prolong_free ----------------------
    @api_method
    async def prolong_invite(
        self,
        *,
        invite_id: str,
        with_send: bool = True,
        api_version: str | None = None,
    ) -> InviteBoolResponse:
        """
        Продлить приглашение.

        with_send=True  → POST /v2/invites/{invite_id}/prolong  (с отправкой)
        with_send=False → POST /v2/invites/{invite_id}/prolong_free (без отправки)
        """
        raw = await self._request(
            "prolong_invite",
            api_version=api_version,
            route_name="default" if with_send else "without_send",
            path_params={"invite_id": invite_id},
        )
        return decode_model(InviteBoolResponse, raw)

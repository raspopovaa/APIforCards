from typing import Any, Optional

from ..decorators import api_method
from ..models.invites import (
    InviteBoolResponse,
    InviteList,
    InviteResponse,
)
from ..payloads import with_method_override


class InviteMixin:
    """
    Методы для работы с приглашениями пользователей (v2).
    Invites – функционал регистрации пользователей.
    Приглашение можно отправить по Email/SMS или получить уникальную ссылку и отправить удобным для вас способом.
    Ссылка действует 3 календарных дня, повторно направить Email/SMS по одному приглашению можно не чаще 3х раз в день.
    С помощью приглашения можно зарегистрировать, например, водителя и сразу привязать шаблон виртуальной карты,
    либо привязать физические топливные карты.
    """

    # ---------------------- GET /v2/invites ----------------------
    @api_method(require_session=True, default_version="v2")
    async def get_invites(
        self,
        *,
        role: Optional[str] = None,
        user_id: Optional[str] = None,
        sort: Optional[str] = None,
        status: Optional[str] = None,
        q: Optional[str] = None,
        page: Optional[int] = None,
        on_page: Optional[int] = None,
        api_version: str = "v2",
    ) -> InviteList:
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
            "get",
            "invites",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return InviteList(**raw.get("data", {}))

    # ---------------------- POST /v2/invites / invites_free ----------------------
    @api_method(require_session=True, default_version="v2")
    async def create_invite(
        self,
        *,
        data: dict[str, Any],
        with_send: bool = True,
        api_version: str = "v2",
    ) -> InviteResponse:
        """
        Создать приглашение.

        with_send=True  → POST /v2/invites  (с отправкой SMS/Email)
        with_send=False → POST /v2/invites_free (без отправки)
        """
        endpoint = "invites" if with_send else "invites_free"

        raw = await self._request(
            "post",
            endpoint,
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=data,
        )
        return InviteResponse(**raw)

    # ---------------------- DELETE /v2/invites/{invite_id} ----------------------
    @api_method(require_session=True, default_version="v2")
    async def delete_invite(
        self,
        *,
        invite_id: str,
        use_post: bool = False,
        api_version: str = "v2",
    ) -> InviteBoolResponse:
        """
        Удалить приглашение (v2).
        """
        method = "post" if use_post else "delete"
        raw = await self._request(
            method,
            f"invites/{invite_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=with_method_override(None, "DELETE") if use_post else None,
        )
        return InviteBoolResponse(**raw)

    # ---------------------- GET /v2/invites/{invite_id}/send ----------------------
    @api_method(require_session=True, default_version="v2")
    async def resend_invite(
        self,
        *,
        invite_id: str,
        api_version: str = "v2",
    ) -> InviteResponse:
        """
        Повторно отправить приглашение (v2).
        """
        raw = await self._request(
            "get",
            f"invites/{invite_id}/send",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return InviteResponse(**raw)

    # ---------------------- POST /v2/invites/{invite_id}/prolong / prolong_free ----------------------
    @api_method(require_session=True, default_version="v2")
    async def prolong_invite(
        self,
        *,
        invite_id: str,
        with_send: bool = True,
        api_version: str = "v2",
    ) -> InviteBoolResponse:
        """
        Продлить приглашение.

        with_send=True  → POST /v2/invites/{invite_id}/prolong  (с отправкой)
        with_send=False → POST /v2/invites/{invite_id}/prolong_free (без отправки)
        """
        path = "prolong" if with_send else "prolong_free"

        raw = await self._request(
            "post",
            f"invites/{invite_id}/{path}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return InviteBoolResponse(**raw)

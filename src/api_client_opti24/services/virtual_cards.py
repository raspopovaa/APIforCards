from typing import Any

from ..decorators import api_method
from ..models.virtual_cards import (
    MPCListResponse,
    MPCPayloadResponse,
    ResetMPCResponse,
    SimpleActionResponse,
    VirtualCardResponse,
)
from ..service_base import _BaseService


class VirtualCardsService(_BaseService):
    """
    Методы для работы с виртуальными картами (ВК) и мобильными профилями карт (МПК)
    """

    @api_method(require_session=True, default_version="v2")
    async def get_mpc_qr_list(
        self,
        *,
        api_version: str = "v2",
    ) -> MPCListResponse:
        """Получить список выпущенных МПК/QR (GET /vip/v2/MPC)."""
        self.logger.info("Получение списка выпущенных МПК/QR")
        data = await self._request(
            "get",
            "MPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return MPCListResponse(**data)

    # === Выпуск виртуальной карты (старый метод) ===
    @api_method(require_session=True, default_version="v2")
    async def create_virtual_card(
        self,
        user_id: str,
        api_version: str = "v2",
    ) -> VirtualCardResponse:
        """Выпуск виртуальной карты (старый метод POST /vip/v2/cards)"""
        payload = {"user_id": user_id}
        self.logger.info("Creating virtual card using legacy method")
        data = await self._request(
            "post",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return VirtualCardResponse(**data)

    # === Выпуск виртуальной карты (новый метод /release) ===
    @api_method(require_session=True, default_version="v2")
    async def release_virtual_card(
        self,
        *,
        type_: str | None = None,
        template_id: str | None = None,
        user_id: str | None = None,
        api_version: str = "v2",
    ) -> VirtualCardResponse:
        """
        Выпуск виртуальной карты (новый метод /vip/v2/cards/release)
        Можно указать:
        - type (например, "wallet")
        - template_id (ID шаблона ВК)
        - user_id (ID пользователя)
        """
        payload = {}
        if type_:
            payload["type"] = type_
        if template_id:
            payload["template_id"] = template_id
        if user_id:
            payload["user_id"] = user_id

        self.logger.info("Creating virtual card")
        data = await self._request(
            "post",
            "cards/release",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return VirtualCardResponse(**data)

    # === Удаление МПК ===
    @api_method(require_session=True, default_version="v2")
    async def delete_mpc(
        self,
        card_id: str,
        api_version: str = "v2",
    ) -> SimpleActionResponse:
        """Удаление мобильного профиля карты (МПК)"""
        self.logger.info("Deleting mobile card profile")
        data = await self._request(
            "post",
            f"cards/{card_id}/deleteMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return SimpleActionResponse(**data)

    # === Сброс счётчиков МПК ===
    @api_method(require_session=True, default_version="v2")
    async def reset_mpc(
        self,
        card_id: str,
        type_: str,
        api_version: str = "v2",
    ) -> ResetMPCResponse:
        """
        Сброс счётчиков МПК (POST /vip/v2/cards/{card_id}/resetMPC)
        Тип счетчика (ResetCounterCode/ResetCounterMPC,
        по-умолчанию, если не вызывать, вызывается ResetCounterCode)
        """
        payload = {"type": type_}
        self.logger.info("Resetting mobile card profile counters")
        data = await self._request(
            "post",
            f"cards/{card_id}/resetMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return ResetMPCResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def generate_payment_qr(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str = "v2",
    ) -> MPCPayloadResponse:
        """Сгенерировать QR-код оплаты (POST /vip/v2/cards/{card_id}/pay)."""
        request_payload = payload or {}
        self.logger.info("Generating payment QR")
        data = await self._request(
            "post",
            f"cards/{card_id}/pay",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def init_mpc(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str = "v2",
    ) -> MPCPayloadResponse:
        """Инициализировать выпуск МПК (POST /vip/v2/cards/{card_id}/initMPC)."""
        request_payload = payload or {}
        self.logger.info("Initializing mobile card profile")
        data = await self._request(
            "post",
            f"cards/{card_id}/initMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def confirm_mpc(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str = "v2",
    ) -> MPCPayloadResponse:
        """Подтвердить выпуск МПК (POST /vip/v2/cards/{card_id}/confirmMPC)."""
        request_payload = payload or {}
        self.logger.info("Confirming mobile card profile")
        data = await self._request(
            "post",
            f"cards/{card_id}/confirmMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def update_mpc(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str = "v2",
    ) -> MPCPayloadResponse:
        """Обновить МПК (POST /vip/v2/cards/{card_id}/updateMPC)."""
        request_payload = payload or {}
        self.logger.info("Updating mobile card profile")
        data = await self._request(
            "post",
            f"cards/{card_id}/updateMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

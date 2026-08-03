from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
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

    @api_method
    async def get_mpc_qr_list(
        self,
        *,
        api_version: str | None = None,
    ) -> MPCListResponse:
        """Получить список выпущенных МПК/QR (GET /vip/v2/MPC)."""
        self.logger.info("Получение списка выпущенных МПК/QR")
        data = await self._request(
            "get_mpc_qr_list",
            api_version=api_version,
        )
        return MPCListResponse(**data)

    # === Выпуск виртуальной карты (старый метод) ===
    @api_method
    async def create_virtual_card(
        self,
        *,
        user_id: str,
        api_version: str | None = None,
    ) -> VirtualCardResponse:
        """Выпуск виртуальной карты (старый метод POST /vip/v2/cards)"""
        payload = {"user_id": user_id}
        data = await self._request(
            "create_virtual_card",
            api_version=api_version,
            data=payload,
        )
        return decode_model(VirtualCardResponse, data)

    # === Выпуск виртуальной карты (новый метод /release) ===
    @api_method
    async def release_virtual_card(
        self,
        *,
        type_: str | None = None,
        template_id: str | None = None,
        user_id: str | None = None,
        api_version: str | None = None,
    ) -> VirtualCardResponse:
        """
        Выпуск виртуальной карты (новый метод /vip/v2/cards/release)
        Можно указать:
        - type (например, "wallet")
        - template_id (ID шаблона ВК)
        - user_id (ID пользователя)

        Типовой сценарий:
            Выпустить карту пользователю по заранее настроенному шаблону лимитов
            и ограничений.

        Пример вызова:
        ```python
        card = await client.virtual_cards.release_virtual_card(
            type_="wallet",
            template_id="template-id",
            user_id="user-id",
        )
        ```

        Пример payload:
        ```json
        {"type": "wallet", "template_id": "template-id", "user_id": "user-id"}
        ```
        """
        payload = {}
        if type_:
            payload["type"] = type_
        if template_id:
            payload["template_id"] = template_id
        if user_id:
            payload["user_id"] = user_id

        data = await self._request(
            "release_virtual_card",
            api_version=api_version,
            data=payload,
        )
        return decode_model(VirtualCardResponse, data)

    # === Удаление МПК ===
    @api_method
    async def delete_mpc(
        self,
        card_id: str,
        api_version: str | None = None,
    ) -> SimpleActionResponse:
        """Удаление мобильного профиля карты (МПК)"""
        self.logger.info("Deleting mobile card profile")
        data = await self._request(
            "delete_mpc",
            api_version=api_version,
            path_params={"card_id": card_id},
        )
        return SimpleActionResponse(**data)

    # === Сброс счётчиков МПК ===
    @api_method
    async def reset_mpc(
        self,
        card_id: str,
        type_: str,
        api_version: str | None = None,
    ) -> ResetMPCResponse:
        """
        Сброс счётчиков МПК (POST /vip/v2/cards/{card_id}/resetMPC)
        Тип счетчика (ResetCounterCode/ResetCounterMPC,
        по-умолчанию, если не вызывать, вызывается ResetCounterCode)
        """
        payload = {"type": type_}
        self.logger.info("Resetting mobile card profile counters")
        data = await self._request(
            "reset_mpc",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=payload,
        )
        return ResetMPCResponse(**data)

    @api_method
    async def generate_payment_qr(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str | None = None,
    ) -> MPCPayloadResponse:
        """Сгенерировать QR-код оплаты (POST /vip/v2/cards/{card_id}/pay)."""
        request_payload = payload or {}
        self.logger.info("Generating payment QR")
        data = await self._request(
            "generate_payment_qr",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

    @api_method
    async def init_mpc(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str | None = None,
    ) -> MPCPayloadResponse:
        """Инициализировать выпуск МПК (POST /vip/v2/cards/{card_id}/initMPC)."""
        request_payload = payload or {}
        self.logger.info("Initializing mobile card profile")
        data = await self._request(
            "init_mpc",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

    @api_method
    async def confirm_mpc(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str | None = None,
    ) -> MPCPayloadResponse:
        """Подтвердить выпуск МПК (POST /vip/v2/cards/{card_id}/confirmMPC)."""
        request_payload = payload or {}
        self.logger.info("Confirming mobile card profile")
        data = await self._request(
            "confirm_mpc",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

    @api_method
    async def update_mpc(
        self,
        *,
        card_id: str,
        payload: dict[str, Any] | None = None,
        api_version: str | None = None,
    ) -> MPCPayloadResponse:
        """Обновить МПК (POST /vip/v2/cards/{card_id}/updateMPC)."""
        request_payload = payload or {}
        self.logger.info("Updating mobile card profile")
        data = await self._request(
            "update_mpc",
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )
        return MPCPayloadResponse(**data)

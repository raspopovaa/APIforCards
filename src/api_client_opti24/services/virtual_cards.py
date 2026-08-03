from typing import Any

from ..models.virtual_cards import (
    MPCListResponse,
    MPCPayloadResponse,
    ResetMPCResponse,
    SimpleActionResponse,
    VirtualCardResponse,
)
from ..operations import operation
from ..service_base import _BaseService

GET_MPC_QR_LIST = operation("get_mpc_qr_list", MPCListResponse)
CREATE_VIRTUAL_CARD = operation("create_virtual_card", VirtualCardResponse)
RELEASE_VIRTUAL_CARD = operation("release_virtual_card", VirtualCardResponse)
DELETE_MPC = operation("delete_mpc", SimpleActionResponse)
RESET_MPC = operation("reset_mpc", ResetMPCResponse)
GENERATE_PAYMENT_QR = operation("generate_payment_qr", MPCPayloadResponse)
INIT_MPC = operation("init_mpc", MPCPayloadResponse)
CONFIRM_MPC = operation("confirm_mpc", MPCPayloadResponse)
UPDATE_MPC = operation("update_mpc", MPCPayloadResponse)


class VirtualCardsService(_BaseService):
    """
    Методы для работы с виртуальными картами (ВК) и мобильными профилями карт (МПК)
    """

    async def get_mpc_qr_list(
        self,
        *,
        api_version: str | None = None,
    ) -> MPCListResponse:
        """Получить список выпущенных МПК/QR (GET /vip/v2/MPC)."""
        self.logger.info("Получение списка выпущенных МПК/QR")
        return await self._request(
            GET_MPC_QR_LIST,
            api_version=api_version,
        )

    # === Выпуск виртуальной карты (старый метод) ===
    async def create_virtual_card(
        self,
        *,
        user_id: str,
        api_version: str | None = None,
    ) -> VirtualCardResponse:
        """Выпуск виртуальной карты (старый метод POST /vip/v2/cards)"""
        payload = {"user_id": user_id}
        self.logger.info("Creating virtual card using legacy method")
        return await self._request(
            CREATE_VIRTUAL_CARD,
            api_version=api_version,
            data=payload,
        )

    # === Выпуск виртуальной карты (новый метод /release) ===
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

        self.logger.info("Creating virtual card")
        return await self._request(
            RELEASE_VIRTUAL_CARD,
            api_version=api_version,
            data=payload,
        )

    # === Удаление МПК ===
    async def delete_mpc(
        self,
        card_id: str,
        api_version: str | None = None,
    ) -> SimpleActionResponse:
        """Удаление мобильного профиля карты (МПК)"""
        self.logger.info("Deleting mobile card profile")
        return await self._request(
            DELETE_MPC,
            api_version=api_version,
            path_params={"card_id": card_id},
        )

    # === Сброс счётчиков МПК ===
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
        return await self._request(
            RESET_MPC,
            api_version=api_version,
            path_params={"card_id": card_id},
            data=payload,
        )

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
        return await self._request(
            GENERATE_PAYMENT_QR,
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )

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
        return await self._request(
            INIT_MPC,
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )

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
        return await self._request(
            CONFIRM_MPC,
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )

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
        return await self._request(
            UPDATE_MPC,
            api_version=api_version,
            path_params={"card_id": card_id},
            data=request_payload,
        )

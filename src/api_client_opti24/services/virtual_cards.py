from ..decorators import api_method
from ..logger import logger
from ..models.virtual_cards import (
    ResetMPCResponse,
    SimpleActionResponse,
    VirtualCardResponse,
)


class VirtualCardsMixin:
    """
    Методы для работы с виртуальными картами (ВК) и мобильными профилями карт (МПК)
    """

    # === Выпуск виртуальной карты (старый метод) ===
    @api_method(require_session=True, default_version="v2")
    async def create_virtual_card(
        self,
        user_id: str,
        api_version: str = "v2",
    ) -> VirtualCardResponse:
        """Выпуск виртуальной карты (старый метод POST /vip/v2/cards)"""
        payload = {"user_id": user_id}
        logger.info("Выпуск ВК (старый метод): %s", payload)
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

        logger.info("Выпуск ВК (новый метод): %s", payload)
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
        logger.info("Удаление МПК для карты: %s", card_id)
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
        logger.info("Сброс счётчиков МПК для карты %s: %s", card_id, payload)
        data = await self._request(
            "post",
            f"cards/{card_id}/resetMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return ResetMPCResponse(**data)

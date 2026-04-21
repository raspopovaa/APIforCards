from typing import Optional

from ..modeling import BaseModel, Field


class InviteCard(BaseModel):
    """Информация о карте, привязанной к приглашению"""

    sid: str = Field(..., description="ID карты (SID)")
    number: str = Field(..., description="Номер карты")
    product: str = Field(..., description="Тип продукта ('wallet' и т.п.)")
    comment: Optional[str] = Field(None, description="Комментарий к карте (например, имя водителя)")
    status: Optional[str] = Field(None, description="Технический статус карты")
    status_name: Optional[str] = Field(None, description="Отображаемое название статуса")
    contract_id: Optional[str] = Field(None, description="ID договора, к которому относится карта")
    contract_name: Optional[str] = Field(None, description="Номер договора")


class InviteContract(BaseModel):
    """Информация о договоре, привязанном к приглашению"""

    sid: str = Field(..., description="ID договора")
    number: str = Field(..., description="Номер договора")
    status: Optional[str] = Field(None, description="Технический статус договора")
    status_name: Optional[str] = Field(None, description="Название статуса")
    template_id: Optional[str] = Field(None, description="ID шаблона виртуальной карты, если есть")
    cards_count: Optional[int] = Field(None, description="Количество карт по договору")


class InviteItem(BaseModel):
    """Элемент списка приглашений"""

    id: str = Field(..., description="ID приглашения")
    user_id: Optional[str] = Field(None, description="ID пользователя, если уже создан")
    url: str = Field(..., description="Ссылка на регистрацию (уникальная, активна 3 дня)")
    status: str = Field(..., description="Технический статус приглашения (Active, Finished и т.п.)")
    status_name: str = Field(..., description="Отображаемое название статуса")
    role: str = Field(..., description="Роль пользователя ('Driver', 'Admin' и т.п.)")
    role_name: str = Field(..., description="Название роли")
    attempts: Optional[int] = Field(None, description="Количество отправок приглашения")
    cards: Optional[list[InviteCard]] = Field(
        None, description="Список карт, связанных с приглашением"
    )
    initiator: Optional[str] = Field(None, description="Пользователь, создавший приглашение")
    contracts: Optional[list[InviteContract]] = Field(
        None, description="Список договоров, привязанных к приглашению"
    )
    mobile: Optional[str] = Field(None, description="Номер телефона приглашенного")
    email: Optional[str] = Field(None, description="Email приглашенного")
    communication_type: Optional[str] = Field(
        None, description="Тип отправки ('sms', 'email' и т.п.)"
    )
    sended_at: Optional[int] = Field(None, description="Время отправки (timestamp)")
    expired_at: Optional[int] = Field(
        None, description="Время истечения срока действия ссылки (timestamp)"
    )


class InviteList(BaseModel):
    """Ответ на запрос списка приглашений"""

    total_count: int = Field(..., description="Общее количество приглашений")
    result: list[InviteItem] = Field(..., description="Список приглашений")


class InviteActionResult(BaseModel):
    """Результат действий с приглашениями (создание, продление, повторная отправка)"""

    id: str = Field(..., description="ID приглашения")
    url: str = Field(..., description="Ссылка на приглашение")
    attempts: Optional[int] = Field(None, description="Количество попыток отправки")
    expired_at: Optional[int] = Field(
        None, description="Дата истечения срока действия ссылки (timestamp)"
    )


class InviteResponse(BaseModel):
    """Обертка для InviteActionResult"""

    data: InviteActionResult


class InviteBoolResponse(BaseModel):
    """Результат простых действий (удаление, продление и т.п.)"""

    data: bool

from datetime import datetime

from ..modeling import BaseModel, Field

# -------------------------
# Базовые классы и служебные структуры
# -------------------------


class StatusResponse(BaseModel):
    code: int = Field(
        ...,
        description="Код состояния ответа (например, 200 — OK, 400 — ошибка запроса)",
    )


class AccessRights(BaseModel):
    web: bool = Field(default=False, description="Доступ к веб-интерфейсу")
    api: bool = Field(default=False, description="Доступ к API")
    mobile: bool = Field(default=False, description="Доступ к мобильному приложению")


# -------------------------
# Авторизация пользователя (authUser)
# -------------------------


class ContractInfo(BaseModel):
    id: str = Field(..., description="ID договора")
    number: str = Field(..., description="Номер договора")
    mpc: bool = Field(default=False, description="Есть ли МПК (виртуальные карты)")
    template_id: str | None = Field(None, description="ID шаблона ВК, если есть")
    cards_count: int = Field(default=0, description="Количество карт по договору")
    one_price: bool = Field(default=False, description="Признак единой цены")


class AuthUserData(BaseModel):
    client_id: str = Field(..., description="ID клиента в системе")
    client_status: str = Field(..., description="Статус клиента (Active, Blocked, и т.п.)")
    org_name: str | None = Field(None, description="Наименование организации")
    session_id: str = Field(..., description="JWT токен активной сессии")
    user_id: str = Field(..., description="ID пользователя")
    contracts: list[ContractInfo] = Field(
        default_factory=list, description="Список доступных договоров"
    )
    role_id: str | None = Field(None, description="Код роли (например, Supervisor)")
    role_name: str | None = Field(None, description="Название роли (например, Администратор)")
    read_only: bool = Field(default=False, description="Флаг режима только чтение")
    user_name: str | None = Field(None, description="Имя пользователя")
    user_patronymic: str | None = Field(None, description="Отчество пользователя")
    user_surname: str | None = Field(None, description="Фамилия пользователя")
    last_contract: str | None = Field(None, description="SID последнего договора")
    access: AccessRights | None = Field(None, description="Права доступа (web/api/mobile)")
    email: str | None = Field(None, description="Электронная почта")
    phone: str | None = Field(None, description="Телефон")


class AuthUserResponse(BaseModel):
    status: StatusResponse = Field(..., description="Статус ответа API")
    data: AuthUserData = Field(..., description="Данные авторизованного пользователя")
    timestamp: int | None = Field(None, description="Метка времени (unix timestamp)")


# -------------------------
# Деавторизация пользователя (logoff)
# -------------------------


class LogoffResponse(BaseModel):
    status: StatusResponse = Field(..., description="Статус ответа API")
    data: bool = Field(..., description="True — если выход выполнен успешно")
    timestamp: int | None = Field(None, description="Метка времени ответа")


# -------------------------
# Ошибки авторизации
# -------------------------


class AuthError(BaseModel):
    code: str = Field(..., description="Код ошибки (например, INVALID_CREDENTIALS)")
    message: str = Field(..., description="Текст ошибки")


class AuthErrorResponse(BaseModel):
    error: AuthError = Field(..., description="Описание ошибки авторизации")


# -------------------------
# Статистика использования API (метод info)
# -------------------------


class ClientInfo(BaseModel):
    Client: str = Field(..., description="ID клиента")
    ClientType: str = Field(..., description="Тип клиента (например, D)")
    Contract: str = Field(..., description="ID контракта")
    ContractName: str = Field(..., description="Название контракта")
    PricePlan: str | None = Field(None, description="Тарифный план")
    Cost: float | None = Field(None, description="Стоимость запросов")
    Queries: int | None = Field(None, description="Количество запросов")
    Additional: int | None = Field(None, description="Дополнительное значение")


class MethodsCount(BaseModel):
    all: int = Field(0, description="Общее количество методов")
    cards: int | None = Field(0, description="Методы, связанные с картами")
    cardgroups: int | None = Field(0, description="Методы, связанные с группами карт")
    card: int | None = Field(0, description="Методы, связанные с одной картой")


class MethodsInfo(BaseModel):
    actions_bill: dict[str, str] = Field(
        ..., description="Платные методы API (влияют на статистику)"
    )
    actions_not_bill: dict[str, str] = Field(
        ..., description="Бесплатные методы API (не влияют на статистику)"
    )


class InfoData(BaseModel):
    from_: datetime = Field(..., alias="from", description="Начало периода статистики")
    to: datetime = Field(..., description="Конец периода статистики")
    client_info: ClientInfo = Field(..., description="Информация о клиенте")
    methods: MethodsCount = Field(..., description="Количество вызовов по категориям")
    methods_info: MethodsInfo = Field(..., description="Описание доступных методов API")


class GetInfoResponse(BaseModel):
    status: StatusResponse = Field(..., description="Статус ответа API")
    data: InfoData = Field(..., description="Детализированные данные о статистике")
    timestamp: int = Field(..., description="Временная метка (UNIX timestamp)")

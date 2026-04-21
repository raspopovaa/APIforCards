from __future__ import annotations

from ..modeling import BaseModel, Field

# === Базовые структуры ===


class LimitAmount(BaseModel):
    """Объёмный лимит (например, литры)."""

    value: float = Field(..., description="Установленное значение лимита")
    used: float | None = Field(None, description="Использованное значение лимита")
    unit: str = Field(..., description="Единица измерения (например, 'LIT' или 'RUB')")


class LimitSum(BaseModel):
    """Денежный лимит."""

    currency: str = Field(..., description="Код валюты (например, 810)")
    value: float = Field(..., description="Сумма лимита")


class LimitTermTime(BaseModel):
    """Временной диапазон действия лимита."""

    from_: str = Field(..., alias="from", description="Время начала действия лимита (HH:MM)")
    to: str = Field(..., description="Время окончания действия лимита (HH:MM)")


class LimitTerm(BaseModel):
    """Периодичность и временные ограничения."""

    days: str | None = Field(None, description="Дни недели (например, '1111100' для Пн–Пт)")
    type: int | None = Field(None, description="Тип периода (1 — будни, 2 — ежедневно и т.д.)")
    time: LimitTermTime | None = Field(None, description="Временной диапазон действия")


class LimitTransactions(BaseModel):
    """Ограничения по количеству транзакций."""

    count: int | None = Field(None, description="Максимальное количество транзакций")
    occured: int | None = Field(None, description="Фактическое количество транзакций")


class LimitTime(BaseModel):
    """Периодичность сброса лимита."""

    number: int | None = Field(None, description="Период в числовом виде (например, 3)")
    type: int | None = Field(None, description="Тип периода (например, 7 — неделя)")


# === Основная модель лимита ===


class LimitItem(BaseModel):
    """Продуктовый лимит (карта, группа или договор)."""

    id: str | None = Field(None, description="ID лимита (для изменения — обязателен)")
    card_id: str | None = Field(None, description="ID карты, если лимит задан для карты")
    group_id: str | None = Field(None, description="ID группы карт, если лимит задан для группы")
    contract_id: str = Field(..., description="ID договора, к которому относится лимит")

    productGroup: str | None = Field(None, description="ID группы продуктов")
    productType: str | None = Field(None, description="ID типа продукта")

    amount: LimitAmount | None = Field(None, description="Ограничение по объёму (литры и т.д.)")
    sum: LimitSum | None = Field(None, description="Ограничение по сумме в валюте договора")

    term: LimitTerm | None = Field(None, description="Периодичность и временные ограничения")
    transactions: LimitTransactions | None = Field(
        None, description="Ограничения по количеству транзакций"
    )
    time: LimitTime | None = Field(None, description="Периодичность сброса лимита")

    date: str | None = Field(None, description="Дата создания лимита (формат dd/mm/yyyy hh:mm:ss)")


# === Ответ на GET /limit ===


class LimitsData(BaseModel):
    """Данные по лимитам."""

    total_count: int = Field(..., description="Общее количество лимитов")
    result: list[LimitItem] = Field(..., description="Список лимитов")


class LimitsResponse(BaseModel):
    """Ответ на запрос списка лимитов."""

    status: dict = Field(..., description="Статус выполнения (например, {'code': 200})")
    data: LimitsData = Field(..., description="Данные с лимитами")
    timestamp: int = Field(..., description="Временная метка ответа")


# === Ответ на POST /removeLimit ===


class RemoveLimitResponse(BaseModel):
    """Ответ на удаление продуктового лимита."""

    status: dict = Field(..., description="Статус выполнения запроса")
    data: bool = Field(..., description="Результат операции (True — успешно)")
    timestamp: int = Field(..., description="Временная метка ответа")


# === Ответ на POST /setLimit ===


class SetLimitResponse(BaseModel):
    """Ответ на установку/изменение продуктового лимита."""

    status: dict = Field(..., description="Статус выполнения запроса")
    data: list[str] = Field(..., description="ID созданных/обновлённых лимитов")
    timestamp: int = Field(..., description="Временная метка ответа")

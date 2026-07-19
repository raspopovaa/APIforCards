from typing import Any

from ..modeling import BaseModel, Field


class RestrictionItem(BaseModel):
    """
    Модель одного товарного ограничителя (ограничение по продукту).
    """

    id: str = Field(..., description="ID ограничителя")
    card_id: str | None = Field(None, description="ID карты, если ограничитель задан для карты")
    group_id: str | None = Field(
        None, description="ID группы карт, если ограничитель задан для группы"
    )
    contract_id: str = Field(..., description="ID договора")
    productType: str | None = Field(None, description="ID типа продукта (например, '1-CK231')")
    productGroup: str | None = Field(None, description="ID группы продуктов (если применимо)")
    productTypeName: str | None = Field(None, description="Название типа продукта")
    productGroupName: str | None = Field(None, description="Название группы продуктов")
    restriction_type: int = Field(
        ...,
        description="Тип ограничения (1 – Разрешающий ограничитель, 2 – Запрещающий ограничитель)",
    )
    date: str | None = Field(
        None, description="Дата установки ограничителя (в формате MM/DD/YYYY HH:mm:ss)"
    )


class RestrictionList(BaseModel):
    """
    Список товарных ограничителей.
    """

    total_count: int = Field(..., description="Общее количество ограничителей")
    result: list[RestrictionItem] = Field(..., description="Список ограничителей")


class RestrictionGetResponse(BaseModel):
    """
    Ответ на запрос списка ограничителей (GET /restriction).
    """

    data: RestrictionList = Field(..., description="Данные с ограничителями")
    timestamp: int = Field(..., description="Временная метка ответа (Unix time)")


class RestrictionSetResponse(BaseModel):
    """
    Ответ на установку или изменение ограничителя (POST /setRestriction).
    """

    data: list[str] = Field(..., description="Список ID созданных или изменённых ограничителей")
    timestamp: int = Field(..., description="Временная метка ответа (Unix time)")


class RestrictionRemoveResponse(BaseModel):
    """
    Ответ на удаление ограничителя (POST /removeRestriction).
    """

    status: dict[str, Any] = Field(..., description="Статус выполнения (например, {'code': 200})")
    data: bool = Field(..., description="Результат операции (True — успешно)")
    timestamp: int | None = Field(None, description="Временная метка ответа (Unix time)")

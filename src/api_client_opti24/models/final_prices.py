from ..modeling import BaseModel, Field


class FinalPriceItem(BaseModel):
    """Информация о финальной цене товара на АЗС"""

    code: str = Field(..., description="Код товарной позиции")
    price: float = Field(..., description="Финальная цена товара (с учетом всех скидок и тарифов)")


class FinalPricesData(BaseModel):
    """Основные данные о финальных ценах"""

    total_count: int = Field(..., description="Количество товарных позиций в ответе")
    goods: list[FinalPriceItem] = Field(
        ..., description="Список товарных позиций с рассчитанными финальными ценами"
    )


class FinalPricesResponse(BaseModel):
    """Ответ метода получения финальных цен на АЗС"""

    status: dict = Field(..., description="Статус ответа API, например {'code': 200}")
    data: FinalPricesData = Field(..., description="Основные данные ответа (цены)")
    timestamp: int = Field(..., description="Время формирования ответа в формате UNIX")


class PurchaseGoodItem(BaseModel):
    """Описание товарной позиции для проверки возможности покупки"""

    code: str = Field(..., description="Код товара (SKU или PLU на АЗС)")
    quantity: float = Field(..., description="Количество товара для покупки")
    price: float = Field(..., description="Цена за единицу товара")


class CheckPurchaseRequest(BaseModel):
    """Параметры запроса для проверки покупки"""

    poi_id: str = Field(..., description="ID точки продажи (АЗС)")
    goods: list[PurchaseGoodItem] = Field(
        ..., description="Список товаров для проверки возможности покупки"
    )


class CheckPurchaseResponse(BaseModel):
    """Ответ метода проверки возможности проведения транзакции"""

    status: dict = Field(..., description="Статус ответа API, например {'code': 200}")
    data: bool = Field(..., description="Результат проверки — True, если покупка возможна")
    timestamp: int = Field(..., description="Время ответа (UNIX timestamp)")

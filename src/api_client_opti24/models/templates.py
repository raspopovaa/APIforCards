from typing import Any, Optional

from ..modeling import BaseModel, Field

# ====== ОСНОВНОЙ ШАБЛОН ВК ======


class TemplateItem(BaseModel):
    id: str = Field(..., description="Идентификатор шаблона ВК")
    name: str = Field(..., description="Название шаблона ВК")
    type: str = Field(..., description="Тип шаблона (Limit — лимитная, Wallet — электронная карта)")
    contract_id: str = Field(..., description="Идентификатор договора, к которому относится шаблон")


class TemplatesListData(BaseModel):
    total_count: int = Field(..., description="Общее количество найденных шаблонов")
    result: list[TemplateItem] = Field(..., description="Список найденных шаблонов ВК")


class TemplatesListResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(
        None, description="Статус ответа (код, сообщение и т.д.)"
    )
    data: TemplatesListData = Field(..., description="Основные данные списка шаблонов")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateCreateRequest(BaseModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    type: str = Field(..., description="Тип создаваемого шаблона (Limit или Wallet)")
    name: str = Field(..., description="Имя (название) нового шаблона ВК")


class TemplateCreateResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного шаблона")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateDeleteResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат операции (true — успешно, false — ошибка)")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


# ====== ЛИМИТЫ ШАБЛОНОВ ======


class LimitSum(BaseModel):
    currency: Optional[str] = Field(None, description="Код валюты (например, '810')")
    currencyName: Optional[str] = Field(None, description="Название валюты (например, 'р.')")
    value: Optional[float] = Field(None, description="Сумма лимита в указанной валюте")


class LimitAmount(BaseModel):
    unit: Optional[str] = Field(None, description="Единица измерения (например, 'LIT')")
    value: Optional[float] = Field(None, description="Количество или объем в единицах измерения")


class LimitTime(BaseModel):
    type: Optional[int] = Field(
        None, description="Тип периода лимита (например, 3 — день, 5 — месяц)"
    )
    number: Optional[int] = Field(None, description="Количество единиц выбранного периода")


class LimitTermTime(BaseModel):
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="Начало временного диапазона (например, '03:00')",
    )
    to: Optional[str] = Field(None, description="Конец временного диапазона (например, '08:00')")


class LimitTerm(BaseModel):
    days: Optional[str] = Field(
        None, description="Маска дней действия лимита (например, '1111100')"
    )
    type: Optional[int] = Field(None, description="Тип временного ограничения")
    time: Optional[LimitTermTime] = Field(None, description="Временные границы лимита")


class LimitTransactions(BaseModel):
    count: Optional[int] = Field(
        None, description="Количество транзакций, на которое распространяется лимит"
    )


class TemplateLimit(BaseModel):
    id: str = Field(..., description="Идентификатор лимита шаблона")
    template_id: str = Field(..., description="Идентификатор шаблона, которому принадлежит лимит")
    contract_id: str = Field(
        ..., description="Идентификатор договора, на который распространяется лимит"
    )
    amount: Optional[LimitAmount] = Field(None, description="Объемный лимит (в литрах и т.д.)")
    sum: Optional[LimitSum] = Field(None, description="Суммовой лимит (в рублях и т.д.)")
    time: Optional[LimitTime] = Field(None, description="Период действия лимита")
    term: Optional[LimitTerm] = Field(None, description="Дополнительные временные ограничения")
    transactions: Optional[LimitTransactions] = Field(
        None, description="Информация по транзакциям лимита"
    )
    date: Optional[str] = Field(None, description="Дата создания лимита")
    productType: Optional[str] = Field(None, description="Тип продукта (топливо, услуга и т.д.)")
    productGroup: Optional[str] = Field(None, description="Группа продукта (например, G-95)")
    productTypeName: Optional[str] = Field(None, description="Название типа продукта")
    productGroupName: Optional[str] = Field(None, description="Название группы продукта")


class TemplateLimitListData(BaseModel):
    total_count: int = Field(..., description="Количество найденных лимитов")
    result: list[TemplateLimit] = Field(..., description="Список лимитов шаблона")


class TemplateLimitListResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: TemplateLimitListData = Field(..., description="Основные данные списка лимитов")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateLimitCreateRequest(BaseModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    product_type: str = Field(..., description="Тип продукта (например, '1-276PF01')")
    product_group: Optional[str] = Field(
        None, description="Группа продукта (например, '1-276PF0E')"
    )
    sum: Optional[LimitSum] = Field(None, description="Суммовой лимит")
    amount: Optional[LimitAmount] = Field(None, description="Объемный лимит")
    time: LimitTime = Field(..., description="Период лимита")
    term: Optional[LimitTerm] = Field(None, description="Дополнительные временные ограничения")
    create_restriction: Optional[bool] = Field(
        None, description="Создать ограничитель автоматически"
    )


class TemplateLimitCreateResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного лимита шаблона")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateLimitDeleteResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат удаления лимита (true — успешно)")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


# ====== ОГРАНИЧИТЕЛИ ШАБЛОНА ======


class TemplateRestriction(BaseModel):
    id: str = Field(..., description="Идентификатор ограничителя шаблона")
    template_id: str = Field(..., description="Идентификатор шаблона")
    contract_id: str = Field(..., description="Идентификатор договора")
    date: Optional[str] = Field(None, description="Дата создания ограничителя")
    productType: Optional[str] = Field(None, description="Тип продукта")
    productGroup: Optional[str] = Field(None, description="Группа продукта")
    productTypeName: Optional[str] = Field(None, description="Название типа продукта")
    productGroupName: Optional[str] = Field(None, description="Название группы продукта")
    restriction_type: int = Field(..., description="Тип ограничителя (1 — разрешение, 2 — запрет)")


class TemplateRestrictionListData(BaseModel):
    total_count: int = Field(..., description="Количество найденных ограничителей")
    result: list[TemplateRestriction] = Field(..., description="Список ограничителей шаблона")


class TemplateRestrictionListResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: TemplateRestrictionListData = Field(
        ..., description="Основные данные списка ограничителей"
    )
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateRestrictionCreateRequest(BaseModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    product_type: str = Field(..., description="Тип продукта (например, '1-276PF01')")
    product_group: Optional[str] = Field(
        None, description="Группа продукта (например, '1-276PF0E')"
    )
    restriction_type: int = Field(..., description="Тип ограничителя (1 — разрешение, 2 — запрет)")


class TemplateRestrictionCreateResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного ограничителя шаблона")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateRestrictionDeleteResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат удаления ограничителя")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


# ====== ГЕООГРАНИЧИТЕЛИ ШАБЛОНА ======


class TemplateGeoRestriction(BaseModel):
    id: str = Field(..., description="Идентификатор геоограничителя шаблона")
    template_id: str = Field(..., description="Идентификатор шаблона")
    contract_id: str = Field(..., description="Идентификатор договора")
    date: Optional[str] = Field(None, description="Дата создания записи")
    country: Optional[str] = Field(None, description="Код страны (например, 'RUS')")
    countryName: Optional[str] = Field(None, description="Название страны")
    region: Optional[str] = Field(None, description="Код региона")
    regionName: Optional[str] = Field(None, description="Название региона")
    partner: Optional[str] = Field(None, description="Код партнера (АЗС)")
    partnerName: Optional[str] = Field(None, description="Название партнера (АЗС)")
    service_center: Optional[str] = Field(None, description="Код сервисного центра")
    service_centerName: Optional[str] = Field(None, description="Название сервисного центра")
    restriction_type: int = Field(
        ..., description="Тип геоограничителя (1 — разрешение, 2 — запрет)"
    )


class TemplateGeoRestrictionListData(BaseModel):
    total_count: int = Field(..., description="Количество найденных геоограничителей")
    result: list[TemplateGeoRestriction] = Field(..., description="Список геоограничителей шаблона")


class TemplateGeoRestrictionListResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: TemplateGeoRestrictionListData = Field(
        ..., description="Основные данные списка геоограничителей"
    )
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateGeoRestrictionCreateRequest(BaseModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    country: str = Field(..., description="Код страны (например, 'RUS')")
    region: Optional[str] = Field(None, description="Код региона (например, '45')")
    partner: Optional[str] = Field(None, description="Код партнера (АЗС)")
    service_center: Optional[str] = Field(None, description="Код сервисного центра")
    restriction_type: int = Field(
        ..., description="Тип геоограничителя (1 — разрешение, 2 — запрет)"
    )


class TemplateGeoRestrictionCreateResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного геоограничителя шаблона")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")


class TemplateGeoRestrictionDeleteResponse(BaseModel):
    status: Optional[dict[str, Any]] = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат удаления геоограничителя (true — успешно)")
    timestamp: Optional[int] = Field(None, description="Метка времени ответа (Unix)")

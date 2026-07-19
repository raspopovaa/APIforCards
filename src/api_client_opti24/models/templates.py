from typing import Any

from ..modeling import BaseModel, Field, StrictRequestModel

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
    status: dict[str, Any] | None = Field(None, description="Статус ответа (код, сообщение и т.д.)")
    data: TemplatesListData = Field(..., description="Основные данные списка шаблонов")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateCreateRequest(StrictRequestModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    type: str = Field(..., description="Тип создаваемого шаблона (Limit или Wallet)")
    name: str = Field(..., description="Имя (название) нового шаблона ВК")


class TemplateCreateResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного шаблона")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateDeleteResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат операции (true — успешно, false — ошибка)")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


# ====== ЛИМИТЫ ШАБЛОНОВ ======


class LimitSum(BaseModel):
    currency: str | None = Field(None, description="Код валюты (например, '810')")
    currencyName: str | None = Field(None, description="Название валюты (например, 'р.')")
    value: float | None = Field(None, description="Сумма лимита в указанной валюте")


class LimitAmount(BaseModel):
    unit: str | None = Field(None, description="Единица измерения (например, 'LIT')")
    value: float | None = Field(None, description="Количество или объем в единицах измерения")


class LimitTime(BaseModel):
    type: int | None = Field(None, description="Тип периода лимита (например, 3 — день, 5 — месяц)")
    number: int | None = Field(None, description="Количество единиц выбранного периода")


class LimitTermTime(BaseModel):
    from_: str | None = Field(
        None,
        alias="from",
        description="Начало временного диапазона (например, '03:00')",
    )
    to: str | None = Field(None, description="Конец временного диапазона (например, '08:00')")


class LimitTerm(BaseModel):
    days: str | None = Field(None, description="Маска дней действия лимита (например, '1111100')")
    type: int | None = Field(None, description="Тип временного ограничения")
    time: LimitTermTime | None = Field(None, description="Временные границы лимита")


class LimitTransactions(BaseModel):
    count: int | None = Field(
        None, description="Количество транзакций, на которое распространяется лимит"
    )


class TemplateLimit(BaseModel):
    id: str = Field(..., description="Идентификатор лимита шаблона")
    template_id: str = Field(..., description="Идентификатор шаблона, которому принадлежит лимит")
    contract_id: str = Field(
        ..., description="Идентификатор договора, на который распространяется лимит"
    )
    amount: LimitAmount | None = Field(None, description="Объемный лимит (в литрах и т.д.)")
    sum: LimitSum | None = Field(None, description="Суммовой лимит (в рублях и т.д.)")
    time: LimitTime | None = Field(None, description="Период действия лимита")
    term: LimitTerm | None = Field(None, description="Дополнительные временные ограничения")
    transactions: LimitTransactions | None = Field(
        None, description="Информация по транзакциям лимита"
    )
    date: str | None = Field(None, description="Дата создания лимита")
    productType: str | None = Field(None, description="Тип продукта (топливо, услуга и т.д.)")
    productGroup: str | None = Field(None, description="Группа продукта (например, G-95)")
    productTypeName: str | None = Field(None, description="Название типа продукта")
    productGroupName: str | None = Field(None, description="Название группы продукта")


class TemplateLimitListData(BaseModel):
    total_count: int = Field(..., description="Количество найденных лимитов")
    result: list[TemplateLimit] = Field(..., description="Список лимитов шаблона")


class TemplateLimitListResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: TemplateLimitListData = Field(..., description="Основные данные списка лимитов")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateLimitCreateRequest(StrictRequestModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    product_type: str = Field(..., description="Тип продукта (например, '1-276PF01')")
    product_group: str | None = Field(None, description="Группа продукта (например, '1-276PF0E')")
    sum: LimitSum | None = Field(None, description="Суммовой лимит")
    amount: LimitAmount | None = Field(None, description="Объемный лимит")
    time: LimitTime = Field(..., description="Период лимита")
    term: LimitTerm | None = Field(None, description="Дополнительные временные ограничения")
    create_restriction: bool | None = Field(None, description="Создать ограничитель автоматически")


class TemplateLimitCreateResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного лимита шаблона")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateLimitDeleteResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат удаления лимита (true — успешно)")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


# ====== ОГРАНИЧИТЕЛИ ШАБЛОНА ======


class TemplateRestriction(BaseModel):
    id: str = Field(..., description="Идентификатор ограничителя шаблона")
    template_id: str = Field(..., description="Идентификатор шаблона")
    contract_id: str = Field(..., description="Идентификатор договора")
    date: str | None = Field(None, description="Дата создания ограничителя")
    productType: str | None = Field(None, description="Тип продукта")
    productGroup: str | None = Field(None, description="Группа продукта")
    productTypeName: str | None = Field(None, description="Название типа продукта")
    productGroupName: str | None = Field(None, description="Название группы продукта")
    restriction_type: int = Field(..., description="Тип ограничителя (1 — разрешение, 2 — запрет)")


class TemplateRestrictionListData(BaseModel):
    total_count: int = Field(..., description="Количество найденных ограничителей")
    result: list[TemplateRestriction] = Field(..., description="Список ограничителей шаблона")


class TemplateRestrictionListResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: TemplateRestrictionListData = Field(
        ..., description="Основные данные списка ограничителей"
    )
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateRestrictionCreateRequest(StrictRequestModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    product_type: str = Field(..., description="Тип продукта (например, '1-276PF01')")
    product_group: str | None = Field(None, description="Группа продукта (например, '1-276PF0E')")
    restriction_type: int = Field(..., description="Тип ограничителя (1 — разрешение, 2 — запрет)")


class TemplateRestrictionCreateResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного ограничителя шаблона")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateRestrictionDeleteResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат удаления ограничителя")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


# ====== ГЕООГРАНИЧИТЕЛИ ШАБЛОНА ======


class TemplateGeoRestriction(BaseModel):
    id: str = Field(..., description="Идентификатор геоограничителя шаблона")
    template_id: str = Field(..., description="Идентификатор шаблона")
    contract_id: str = Field(..., description="Идентификатор договора")
    date: str | None = Field(None, description="Дата создания записи")
    country: str | None = Field(None, description="Код страны (например, 'RUS')")
    countryName: str | None = Field(None, description="Название страны")
    region: str | None = Field(None, description="Код региона")
    regionName: str | None = Field(None, description="Название региона")
    partner: str | None = Field(None, description="Код партнера (АЗС)")
    partnerName: str | None = Field(None, description="Название партнера (АЗС)")
    service_center: str | None = Field(None, description="Код сервисного центра")
    service_centerName: str | None = Field(None, description="Название сервисного центра")
    restriction_type: int = Field(
        ..., description="Тип геоограничителя (1 — разрешение, 2 — запрет)"
    )


class TemplateGeoRestrictionListData(BaseModel):
    total_count: int = Field(..., description="Количество найденных геоограничителей")
    result: list[TemplateGeoRestriction] = Field(..., description="Список геоограничителей шаблона")


class TemplateGeoRestrictionListResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: TemplateGeoRestrictionListData = Field(
        ..., description="Основные данные списка геоограничителей"
    )
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateGeoRestrictionCreateRequest(StrictRequestModel):
    contract_id: str = Field(..., description="Идентификатор договора")
    country: str = Field(..., description="Код страны (например, 'RUS')")
    region: str | None = Field(None, description="Код региона (например, '45')")
    partner: str | None = Field(None, description="Код партнера (АЗС)")
    service_center: str | None = Field(None, description="Код сервисного центра")
    restriction_type: int = Field(
        ..., description="Тип геоограничителя (1 — разрешение, 2 — запрет)"
    )


class TemplateGeoRestrictionCreateResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: str = Field(..., description="ID созданного геоограничителя шаблона")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")


class TemplateGeoRestrictionDeleteResponse(BaseModel):
    status: dict[str, Any] | None = Field(None, description="Статус ответа")
    data: bool = Field(..., description="Результат удаления геоограничителя (true — успешно)")
    timestamp: int | None = Field(None, description="Метка времени ответа (Unix)")

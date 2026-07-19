from typing import Any, Optional, Union

from ..modeling import BaseModel, Field, field_validator

# ==========================================================
# 🔹 Универсальные модели для общих справочников
# ==========================================================


class DictionaryItem(BaseModel):
    """Элемент справочника (универсальная модель)"""

    id: str = Field(..., description="Уникальный идентификатор элемента справочника")
    code: Optional[str] = Field(None, description="Код элемента (например, код валюты)")
    value: Optional[str] = Field(
        None, description="Значение элемента (используется в старых справочниках)"
    )
    name: Optional[str] = Field(
        None, description="Название элемента (используется в новых справочниках)"
    )
    deleted: Optional[int] = Field(0, description="Признак удаления элемента (0 — активен)")
    last_update: Optional[str] = Field(None, description="Дата последнего обновления записи")


class DictionaryData(BaseModel):
    """Основные данные справочника"""

    total_count: Optional[int] = Field(None, description="Количество элементов в справочнике")
    result: Optional[list[DictionaryItem]] = Field(
        default_factory=list, description="Список элементов справочника"
    )


class DictionaryResponse(BaseModel):
    """Ответ метода GET /vip/v1/getDictionary"""

    status: Optional[dict[str, Any]] = Field(None, description="Статус выполнения запроса")
    data: Optional[DictionaryData] = Field(None, description="Основные данные справочника")
    timestamp: Optional[int] = Field(None, description="Временная метка (UNIX-время запроса)")


# ==========================================================
# 🔹 Фильтры торговых точек (GET /vip/v2/azs/filters)
# ==========================================================


class AzsFilterValue(BaseModel):
    """Отдельное значение фильтра"""

    name: Optional[str] = Field(default=None, description="Название значения фильтра")
    code: Optional[str] = Field(default=None, description="Код значения фильтра")


class AzsFilterItem(BaseModel):
    """Описание фильтра торговых точек"""

    filter: Optional[str] = Field(
        default=None,
        description="Ключ фильтра (например: services_with_card, countries и т.д.)",
    )
    name: Optional[str] = Field(default=None, description="Название фильтра (человекочитаемое)")
    values: Optional[dict[str, AzsFilterValue]] = Field(
        default_factory=dict, description="Список значений для данного фильтра"
    )


class AzsFiltersResponse(BaseModel):
    """Ответ метода /azs/filters"""

    status: Optional[dict[str, Any]] = Field(default=None, description="Статус выполнения запроса")
    data: Optional[list[AzsFilterItem]] = Field(
        default_factory=list, description="Список доступных фильтров торговых точек"
    )
    timestamp: Optional[int] = Field(default=None, description="Метка времени ответа (timestamp)")


# ==========================================================
# 🔹 Модели для списка торговых точек (GET /vip/v1/AZS)
# ==========================================================


class PriceItemV1(BaseModel):
    """Цена товара на торговой точке"""

    ID: Optional[str] = Field(None, description="Идентификатор записи цены")
    GasStationID: Optional[str] = Field(None, description="ID торговой точки (АЗС)")
    GoodsCode: Optional[str] = Field(None, description="Код товара (см. справочник GoodsCode)")
    Price: Optional[str] = Field(None, description="Цена товара")
    Currency: Optional[str] = Field(None, description="Валюта (код и наименование через ';')")
    DateTo: Optional[str] = Field(None, description="Дата окончания действия цены")
    DateFrom: Optional[str] = Field(None, description="Дата начала действия цены")


class TerminalV1(BaseModel):
    """Терминал торговой точки"""

    id: Optional[str] = Field(None, description="Идентификатор терминала")
    active: Optional[bool] = Field(
        None,
        description="Статус активности терминала (True — включен, False — выключен)",
    )
    name: Optional[str] = Field(None, description="Наименование терминала")
    status: Optional[str] = Field(None, description="Статус терминала")
    type: Optional[str] = Field(None, description="Тип терминала")
    connectionType: Optional[str] = Field(None, description="Тип подключения терминала")
    number: Optional[str] = Field(None, description="Номер терминала")


class AddressV1(BaseModel):
    """Адрес торговой точки"""

    track_id: Optional[str] = Field(None, description="Номер трассы, если применимо")
    kmRoad: Optional[str] = Field(None, description="Километр трассы")
    roadSide: Optional[str] = Field(None, description="Сторона дороги")
    city: Optional[str] = Field(None, description="Город")
    street: Optional[str] = Field(None, description="Улица")
    house: Optional[str] = Field(None, description="Дом")
    building: Optional[str] = Field(None, description="Строение")
    phone: Optional[str] = Field(None, description="Телефон торговой точки")
    fax: Optional[str] = Field(None, description="Факс")


class WorkingTimeV1(BaseModel):
    """Рабочее время торговой точки"""

    Weekday: Optional[str] = Field(None, description="День недели или режим работы")
    StartWorkTime: Optional[str] = Field(None, description="Время открытия")
    FinishWorkTime: Optional[str] = Field(None, description="Время закрытия")


class AzsItemV1(BaseModel):
    """Информация о торговой точке (v1)"""

    id: Optional[str] = Field(None, description="ID торговой точки (АЗС)")
    siebelId: Optional[str] = Field(None, description="ID торговой точки в CRM")
    contractNumber: Optional[str] = Field(None, description="Код торговой точки (договор)")
    contractName: Optional[str] = Field(None, description="Название торговой точки")
    status: Optional[str] = Field(
        None, description="Статус точки (257 – работает, 258 – не работает)"
    )
    countryCode: Optional[str] = Field(None, description="Код страны")
    regionCode: Optional[str] = Field(None, description="Код региона")
    secessionGPN: Optional[str] = Field(None, description="Отделение ГПН по географии")
    belongsTo: Optional[str] = Field(None, description="Название владельца или оператора")
    partner: Optional[str] = Field(None, description="ID партнера")
    ownType: Optional[str] = Field(None, description="Тип собственности (Own / FRAN и др.)")
    locationType: Optional[str] = Field(None, description="Тип расположения (ROAD и т.д.)")
    brand: Optional[str] = Field(None, description="Бренд торговой точки")
    openDate: Optional[str] = Field(None, description="Дата открытия точки")
    closeDate: Optional[str] = Field(None, description="Дата закрытия (если закрыта)")
    latitude: Optional[str] = Field(None, description="Координата широты")
    longitude: Optional[str] = Field(None, description="Координата долготы")
    type: Optional[str] = Field(None, description="Тип торговой точки (АЗС, СТО и т.д.)")
    timeZone: Optional[str] = Field(None, description="Часовой пояс точки")
    services: Optional[list[int]] = Field(default_factory=list, description="Массив ID услуг")
    terminals: Optional[list[TerminalV1]] = Field(
        default_factory=list, description="Список терминалов торговой точки"
    )
    address: Optional[AddressV1] = Field(None, description="Адрес торговой точки")
    prices: Optional[list[PriceItemV1]] = Field(
        default_factory=list, description="Цены товаров на точке"
    )
    searchTxt: Optional[str] = Field(None, description="Строка поиска")
    phone: Optional[str] = Field(None, description="Контактный телефон")
    height_post: Optional[str] = Field(None, description="Высота поста (в метрах)")
    working_time: Optional[list[WorkingTimeV1]] = Field(
        default_factory=list, description="Режим работы"
    )
    only_virtual_card: Optional[bool] = Field(
        None, description="Принимаются ли только виртуальные карты"
    )
    accept_cards: Optional[bool] = Field(None, description="Принимаются ли карты")
    hidden_on_map: Optional[bool] = Field(None, description="Скрыта ли точка на карте")
    active: Optional[bool] = Field(None, description="Активна ли торговая точка")
    POIType: Optional[str] = Field(None, description="Тип торговой точки (POI-код)")


class AzsListV1Data(BaseModel):
    """Основные данные списка торговых точек (v1)"""

    total_count: Optional[int] = Field(None, description="Количество найденных торговых точек")
    result: Optional[list[AzsItemV1]] = Field(
        default_factory=list, description="Список торговых точек"
    )


class AzsListV1Response(BaseModel):
    """Ответ метода GET /vip/v1/AZS"""

    status: Optional[dict[str, Any]] = Field(None, description="Статус выполнения запроса")
    data: Optional[AzsListV1Data] = Field(None, description="Основные данные торговых точек (v1)")
    timestamp: Optional[int] = Field(None, description="Временная метка (UNIX-время запроса)")


# ==========================================================
# 🔹 Список торговых точек (GET /vip/v2/azs)
# ==========================================================
class Coordinates(BaseModel):
    """Географические координаты торговой точки"""

    type: Optional[str] = Field(default=None, description="Тип геоданных (обычно 'Point')")
    coordinates: list[float] = Field(
        default_factory=list, description="Координаты в формате [долгота, широта]"
    )


class ServiceItem(BaseModel):
    """Описание отдельной услуги"""

    name: Optional[str] = Field(default=None, description="Наименование услуги")
    code: Optional[Union[int, str]] = Field(
        default=None, description="Код услуги (числовой или строковый)"
    )
    sort: Optional[int] = Field(default=None, description="Порядок сортировки")


class ServiceGroup(BaseModel):
    """Группа услуг, доступных на торговой точке"""

    name: Optional[str] = Field(default=None, description="Наименование группы услуг")
    items: Optional[list[ServiceItem]] = Field(None, description="Список услуг, входящих в группу")


class PriceItemV2(BaseModel):
    """Информация о цене товара на торговой точке"""

    ID: Optional[str] = Field(default=None, description="Идентификатор цены")
    GasStationID: Optional[str] = Field(default=None, description="ID торговой точки (АЗС)")
    GoodsCode: Optional[str] = Field(
        default=None, description="Код товара (из справочника GoodsCode)"
    )
    Price: Optional[str] = Field(default=None, description="Цена товара")
    Currency: Optional[str] = Field(default=None, description="Код валюты, например '810;RUR'")
    DateTo: Optional[str] = Field(default=None, description="Дата действия цены до")
    DateFrom: Optional[str] = Field(default=None, description="Дата начала действия цены")
    hex_color: Optional[str] = Field(default=None, description="HEX-код цвета товара (если указан)")
    name: Optional[str] = Field(default=None, description="Название товара")
    CurrencyName: Optional[str] = Field(default=None, description="Наименование валюты")
    sort: Optional[int] = Field(default=None, description="Порядковый номер отображения")


class WorkingTimeV2(BaseModel):
    """Расписание работы торговой точки"""

    Weekday: Optional[str] = Field(
        default=None,
        description="День недели или режим работы (Monday, Everyday, Round-The-Clock)",
    )
    StartWorkTime: Optional[str] = Field(default=None, description="Время открытия, формат HH:MM")
    FinishWorkTime: Optional[str] = Field(default=None, description="Время закрытия, формат HH:MM")
    Everyday: Optional[bool] = Field(default=False, description="Признак работы ежедневно")
    Round_The_Clock: Optional[bool] = Field(
        default=False,
        alias="Round-The-Clock",
        description="Признак круглосуточного режима",
    )


class AddressV2(BaseModel):
    """Адрес торговой точки"""

    track_id: Optional[str] = Field(default=None, description="Номер трассы")
    kmRoad: Optional[str] = Field(default=None, description="Километр трассы")
    roadSide: Optional[str] = Field(default=None, description="Сторона дороги")
    city: Optional[str] = Field(default=None, description="Город")
    street: Optional[str] = Field(default=None, description="Улица")
    house: Optional[str] = Field(default=None, description="Дом")
    building: Optional[str] = Field(default=None, description="Строение")
    phone: Optional[str] = Field(default=None, description="Телефон")
    fax: Optional[str] = Field(default=None, description="Факс")


class TerminalV2(BaseModel):
    """Информация о терминале, установленном на торговой точке"""

    id: Optional[str] = Field(default=None, description="Идентификатор терминала")
    active: Optional[bool] = Field(default=None, description="Активен ли терминал (true — включен)")
    name: Optional[str] = Field(default=None, description="Наименование терминала")
    status: Optional[str] = Field(default=None, description="Статус терминала")
    type: Optional[str] = Field(default=None, description="Тип терминала")
    connectionType: Optional[str] = Field(default=None, description="Тип подключения")
    number: Optional[str] = Field(default=None, description="Номер терминала")


class AzsItemV2(BaseModel):
    """Информация о торговой точке (АЗС)"""

    id: str = Field(..., description="ID торговой точки")
    siebel_id: str = Field(..., description="Идентификатор Siebel")
    status: Optional[str] = Field(
        None, description="Статус торговой точки (257 – работает, 258 – не работает)"
    )
    full_name: Optional[str] = Field(default=None, description="Полное наименование торговой точки")
    brand: Optional[str] = Field(default=None, description="Бренд")
    poi_type_name: Optional[str] = Field(default=None, description="Именование типа")
    poi_type_code: Optional[str] = Field(default=None, description="Код типа")
    own_type_name: str = Field(..., description="Тип собственности (наименование)")
    own_type_code: str = Field(..., description="Код типа собственности (по отношению к ГПН)")
    contract_name: Optional[str] = Field(default=None, description="Название договора")
    contract_number: Optional[str] = Field(default=None, description="Номер договора")
    phone: Optional[str] = Field(default=None, description="Телефон контактный")
    utc_timezone: Optional[str] = Field(default=None, description="UTC часовой пояс АЗС (+5)")
    time_zone: Optional[str] = Field(
        default=None, description="Часовой пояс АЗС относительно Москвы"
    )
    open_date: Optional[str] = Field(default=None, description="Дата открытия")
    close_date: Optional[str] = Field(default=None, description="Дата закрытия")
    last_update: Optional[str] = Field(default=None, description="Дата последнего обновления")
    height_post: Optional[str] = Field(default=None, description="Высота поста (в метрах)")
    country_name: Optional[str] = Field(..., description="Название страны")
    country_code: Optional[str] = Field(..., description="Код страны")
    region_name: Optional[str] = Field(default=None, description="Название региона")
    region_code: Optional[str] = Field(default=None, description="Код региона")
    address_full: Optional[str] = Field(default=None, description="Полный адрес торговой точки")
    location: Optional[Coordinates] = Field(default=None, description="Географические координаты")
    latitude: Optional[str] = Field(default=None, description="Широта")
    longitude: Optional[str] = Field(default=None, description="Долгота")
    location_type: Optional[str] = Field(default=None, description="Тип локации")
    secession_gpn: Optional[str] = Field(default=None, description="Отделение ГПН")
    partner: Optional[str] = Field(default=None, description="ID партнёра")
    belongs_to: Optional[str] = Field(default=None, description="Принадлежность")
    info: Optional[str] = Field(default=None, description="Дополнительная информация о точке")
    search_txt: Optional[str] = Field(..., description="Строка для запроса поиска")
    accept_cards: Optional[bool] = Field(..., description="Принимаются ли банковские карты")
    adblue: Optional[ServiceGroup] | None = Field(default=None, description="Услуги AdBlue")
    electric_charging_station: Optional[ServiceGroup] = Field(
        default=None, description="Электрозарядные станции"
    )
    services_with_card: Optional[ServiceGroup] = Field(
        default=None, description="Услуги, доступные при оплате картой"
    )
    services_without_card: Optional[ServiceGroup] = Field(
        default=None, description="Услуги, доступные без карты"
    )
    prices: Optional[list[PriceItemV2]] = Field(
        default_factory=list, description="Список товаров с указанием цен"
    )
    payment_type: Optional[list[dict[str, Any]]] = Field(
        default_factory=list, description="Доступные способы оплаты"
    )
    terminals: Optional[list[TerminalV2]] = Field(
        default_factory=list, description="Список терминалов"
    )
    address: Optional[AddressV2] = Field(default=None, description="Адрес торговой точки")
    working_time: Optional[list[WorkingTimeV2]] = Field(
        default_factory=list, description="Расписание работы торговой точки"
    )

    @field_validator(
        "adblue",
        "electric_charging_station",
        "services_with_card",
        "services_without_card",
        mode="before",
        check_fields=False,
    )
    def fix_empty_service_groups(cls, v: Any) -> Any:
        """
        Исправляет ошибку, когда API возвращает [] вместо объекта.
        Конвертирует [] → None, чтобы избежать ValidationError.
        """
        if v == [] or v is None:
            return None
        return v


class AzsListV2Data(BaseModel):
    """Данные списка торговых точек (v2)"""

    pass
    total_count: int = Field(..., description="Общее количество торговых точек")
    result: list[AzsItemV2] = Field(..., description="Список торговых точек (АЗС)")


class AzsListV2Response(BaseModel):
    """Ответ метода получения списка торговых точек (v2)"""

    status: Optional[dict[str, Any]] = Field(..., description="Информация о статусе запроса")
    data: Optional[AzsListV2Data] = Field(..., description="Основные данные торговых точек")
    timestamp: Optional[int] = Field(..., description="Метка времени запроса")


# ==========================================================

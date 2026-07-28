# `AzsItemV2`

Информация о торговой точке (АЗС)

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `id` | `str` | Да | `—` | ID торговой точки |
| `siebel_id` | `str` | Да | `—` | Идентификатор Siebel |
| `status` | `str | None` | Нет | `—` | Статус торговой точки (257 – работает, 258 – не работает) |
| `full_name` | `str | None` | Нет | `—` | Полное наименование торговой точки |
| `brand` | `str | None` | Нет | `—` | Бренд |
| `poi_type_name` | `str | None` | Нет | `—` | Именование типа |
| `poi_type_code` | `str | None` | Нет | `—` | Код типа |
| `own_type_name` | `str` | Да | `—` | Тип собственности (наименование) |
| `own_type_code` | `str` | Да | `—` | Код типа собственности (по отношению к ГПН) |
| `contract_name` | `str | None` | Нет | `—` | Название договора |
| `contract_number` | `str | None` | Нет | `—` | Номер договора |
| `phone` | `str | None` | Нет | `—` | Телефон контактный |
| `utc_timezone` | `str | None` | Нет | `—` | UTC часовой пояс АЗС (+5) |
| `time_zone` | `str | None` | Нет | `—` | Часовой пояс АЗС относительно Москвы |
| `open_date` | `str | None` | Нет | `—` | Дата открытия |
| `close_date` | `str | None` | Нет | `—` | Дата закрытия |
| `last_update` | `str | None` | Нет | `—` | Дата последнего обновления |
| `height_post` | `str | None` | Нет | `—` | Высота поста (в метрах) |
| `country_name` | `str | None` | Да | `—` | Название страны |
| `country_code` | `str | None` | Да | `—` | Код страны |
| `region_name` | `str | None` | Нет | `—` | Название региона |
| `region_code` | `str | None` | Нет | `—` | Код региона |
| `address_full` | `str | None` | Нет | `—` | Полный адрес торговой точки |
| `location` | `Coordinates | None` | Нет | `—` | Географические координаты |
| `latitude` | `str | None` | Нет | `—` | Широта |
| `longitude` | `str | None` | Нет | `—` | Долгота |
| `location_type` | `str | None` | Нет | `—` | Тип локации |
| `secession_gpn` | `str | None` | Нет | `—` | Отделение ГПН |
| `partner` | `str | None` | Нет | `—` | ID партнёра |
| `belongs_to` | `str | None` | Нет | `—` | Принадлежность |
| `info` | `str | None` | Нет | `—` | Дополнительная информация о точке |
| `search_txt` | `str | None` | Да | `—` | Строка для запроса поиска |
| `accept_cards` | `bool | None` | Да | `—` | Принимаются ли банковские карты |
| `adblue` | `ServiceGroup | None` | Нет | `—` | Услуги AdBlue |
| `electric_charging_station` | `ServiceGroup | None` | Нет | `—` | Электрозарядные станции |
| `services_with_card` | `ServiceGroup | None` | Нет | `—` | Услуги, доступные при оплате картой |
| `services_without_card` | `ServiceGroup | None` | Нет | `—` | Услуги, доступные без карты |
| `prices` | `list[PriceItemV2] | None` | Нет | `—` | Список товаров с указанием цен |
| `payment_type` | `list[dict[str, Any]] | None` | Нет | `—` | Доступные способы оплаты |
| `terminals` | `list[TerminalV2] | None` | Нет | `—` | Список терминалов |
| `address` | `AddressV2 | None` | Нет | `—` | Адрес торговой точки |
| `working_time` | `list[WorkingTimeV2] | None` | Нет | `—` | Расписание работы торговой точки |

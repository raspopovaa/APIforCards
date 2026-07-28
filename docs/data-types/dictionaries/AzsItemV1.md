# `AzsItemV1`

Информация о торговой точке (v1)

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `id` | `str | None` | Нет | `—` | ID торговой точки (АЗС) |
| `siebelId` | `str | None` | Нет | `—` | ID торговой точки в CRM |
| `contractNumber` | `str | None` | Нет | `—` | Код торговой точки (договор) |
| `contractName` | `str | None` | Нет | `—` | Название торговой точки |
| `status` | `str | None` | Нет | `—` | Статус точки (257 – работает, 258 – не работает) |
| `countryCode` | `str | None` | Нет | `—` | Код страны |
| `regionCode` | `str | None` | Нет | `—` | Код региона |
| `secessionGPN` | `str | None` | Нет | `—` | Отделение ГПН по географии |
| `belongsTo` | `str | None` | Нет | `—` | Название владельца или оператора |
| `partner` | `str | None` | Нет | `—` | ID партнера |
| `ownType` | `str | None` | Нет | `—` | Тип собственности (Own / FRAN и др.) |
| `locationType` | `str | None` | Нет | `—` | Тип расположения (ROAD и т.д.) |
| `brand` | `str | None` | Нет | `—` | Бренд торговой точки |
| `openDate` | `str | None` | Нет | `—` | Дата открытия точки |
| `closeDate` | `str | None` | Нет | `—` | Дата закрытия (если закрыта) |
| `latitude` | `str | None` | Нет | `—` | Координата широты |
| `longitude` | `str | None` | Нет | `—` | Координата долготы |
| `type` | `str | None` | Нет | `—` | Тип торговой точки (АЗС, СТО и т.д.) |
| `timeZone` | `str | None` | Нет | `—` | Часовой пояс точки |
| `services` | `list[int] | None` | Нет | `—` | Массив ID услуг |
| `terminals` | `list[TerminalV1] | None` | Нет | `—` | Список терминалов торговой точки |
| `address` | `AddressV1 | None` | Нет | `—` | Адрес торговой точки |
| `prices` | `list[PriceItemV1] | None` | Нет | `—` | Цены товаров на точке |
| `searchTxt` | `str | None` | Нет | `—` | Строка поиска |
| `phone` | `str | None` | Нет | `—` | Контактный телефон |
| `height_post` | `str | None` | Нет | `—` | Высота поста (в метрах) |
| `working_time` | `list[WorkingTimeV1] | None` | Нет | `—` | Режим работы |
| `only_virtual_card` | `bool | None` | Нет | `—` | Принимаются ли только виртуальные карты |
| `accept_cards` | `bool | None` | Нет | `—` | Принимаются ли карты |
| `hidden_on_map` | `bool | None` | Нет | `—` | Скрыта ли точка на карте |
| `active` | `bool | None` | Нет | `—` | Активна ли торговая точка |
| `POIType` | `str | None` | Нет | `—` | Тип торговой точки (POI-код) |

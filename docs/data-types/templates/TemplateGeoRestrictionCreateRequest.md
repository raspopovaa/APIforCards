# `TemplateGeoRestrictionCreateRequest`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | `—` | Идентификатор договора |
| `country` | `str` | Да | `—` | Код страны (например, 'RUS') |
| `region` | `str | None` | Нет | `—` | Код региона (например, '45') |
| `partner` | `str | None` | Нет | `—` | Код партнера (АЗС) |
| `service_center` | `str | None` | Нет | `—` | Код сервисного центра |
| `restriction_type` | `int` | Да | `—` | Тип геоограничителя (1 — разрешение, 2 — запрет) |

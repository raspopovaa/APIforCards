# `TemplateRestrictionCreateRequest`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | `—` | Идентификатор договора |
| `product_type` | `str` | Да | `—` | Тип продукта (например, '1-276PF01') |
| `product_group` | `str | None` | Нет | `—` | Группа продукта (например, '1-276PF0E') |
| `restriction_type` | `int` | Да | `—` | Тип ограничителя (1 — разрешение, 2 — запрет) |

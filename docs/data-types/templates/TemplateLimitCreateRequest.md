# `TemplateLimitCreateRequest`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | `—` | Идентификатор договора |
| `product_type` | `str` | Да | `—` | Тип продукта (например, '1-276PF01') |
| `product_group` | `str | None` | Нет | `—` | Группа продукта (например, '1-276PF0E') |
| `sum` | `LimitSum | None` | Нет | `—` | Суммовой лимит |
| `amount` | `LimitAmount | None` | Нет | `—` | Объемный лимит |
| `time` | `LimitTime` | Да | `—` | Период лимита |
| `term` | `LimitTerm | None` | Нет | `—` | Дополнительные временные ограничения |
| `create_restriction` | `bool | None` | Нет | `—` | Создать ограничитель автоматически |

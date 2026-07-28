# `ContractData`

Основные данные договора

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `contract_id` | `str` | Да | `—` | ID договора |
| `way_id` | `str` | Да | `—` | ID договора в процессинге |
| `contract_number` | `str` | Да | `—` | Номер договора |
| `unique_payment_id` | `str` | Да | `—` | Уникальный идентификатор платежа (УИП) |
| `client` | `str` | Да | `—` | ID клиента |
| `client_category` | `str` | Да | `—` | Категория клиента |
| `contract_category` | `str` | Да | `—` | Категория договора |
| `country` | `str` | Да | `—` | Страна заключения |
| `region` | `str` | Да | `—` | Регион заключения |
| `fin_institution` | `str` | Да | `—` | Финансовый институт |
| `invoice_scheme` | `str` | Да | `—` | Подключение инвойсирования |
| `invoice_period` | `str | None` | Нет | `—` | Дни выставления счетов |
| `invoice_pmt_delay` | `str | None` | Нет | `—` | Количество дней на оплату инвойса |
| `contract_status` | `str` | Да | `—` | ID статуса договора |
| `contract_status_name` | `str` | Да | `—` | Значение статуса договора |
| `pay_scheme` | `str` | Да | `—` | Условия оплаты |
| `discount_scheme` | `str` | Да | `—` | Схема расчета скидки (код из справочника DiscountScheme) |
| `auto_pay` | `str` | Да | `—` | Признак разрешения для подключения автосписания с р/с |
| `auto_pay_type` | `str` | Да | `—` | Тип подключения автоматического платежа |
| `credit_limit` | `str | None` | Нет | `—` | Кредитный лимит |
| `current_amount_limiter` | `str` | Да | `—` | Накопленная сумма по контракту |
| `balance_amount_limiter` | `str | None` | Нет | `—` | Доступная сумма по контракту (max – current) |
| `max_amount_limiter` | `str | None` | Нет | `—` | Ограничение лимита на сумму договора |
| `date_open` | `str` | Да | `—` | Дата заключения договора |
| `effective_date` | `str` | Да | `—` | Дата вступления в силу |
| `end_date` | `str` | Да | `—` | Дата окончания |
| `date_expire` | `str` | Да | `—` | Дата закрытия |
| `product_type` | `bool` | Да | `—` | Признак универсального топливного продукта (false – старый продукт, true – УТП) |
| `type_code` | `str` | Да | `—` | Тип договора |
| `supplier_name` | `str` | Да | `—` | Имя поставщика |

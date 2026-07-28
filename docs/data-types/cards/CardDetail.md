# `CardDetail`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `id` | `str` | Да | `—` | Идентификатор карты |
| `contract_id` | `str` | Да | `—` | ID договора |
| `number` | `str` | Да | `—` | Номер карты |
| `status` | `str` | Да | `—` | Статус карты |
| `can_work_offline` | `bool | None` | Нет | `—` | Может работать офлайн |
| `card_auth_type` | `str | None` | Нет | `—` | Тип аутентификации карты |
| `comment` | `str | None` | Нет | `—` | Комментарий к карте |
| `date_last_usage` | `datetime | str | None` | Нет | `—` | Дата последнего использования (может быть пустой строкой) |
| `date_released` | `datetime | str | None` | Нет | `—` | Дата выпуска карты |
| `servicecenter_last_usage_name` | `str | None` | Нет | `—` | Название АЗС последнего использования |
| `transaction_timeout` | `TransactionTimeout | None` | Нет | `—` | Таймаут транзакции |
| `product` | `str | None` | Нет | `—` | Тип продукта (limit/wallet) |
| `carrier` | `str | None` | Нет | `—` | Тип карты (Plastic/Virtual) |
| `available` | `str | None` | Нет | `—` | Доступный лимит или баланс |
| `currency` | `str | None` | Нет | `—` | Валюта |
| `payment_of_tolls` | `str | None` | Нет | `—` | Признак оплаты дорожных сборов |
| `previous` | `str | None` | Нет | `—` | ID предыдущей карты |
| `next` | `str | None` | Нет | `—` | ID следующей карты |

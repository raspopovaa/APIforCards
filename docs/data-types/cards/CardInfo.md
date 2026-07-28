# `CardInfo`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `id` | `str` | Да | `—` | Уникальный идентификатор карты |
| `contract_id` | `str` | Да | `—` | Идентификатор договора |
| `number` | `str` | Да | `—` | Номер топливной карты |
| `status` | `str` | Да | `—` | Статус карты (например, Active, Locked(Client)) |
| `can_work_offline` | `bool | None` | Нет | `—` | Может ли карта работать офлайн |
| `card_auth_type` | `str | None` | Нет | `—` | Тип авторизации карты (например, PIN) |
| `comment` | `str | None` | Нет | `—` | Комментарий к карте |
| `date_expired` | `datetime | None` | Нет | `—` | Дата истечения срока действия карты |
| `date_last_usage` | `datetime | None` | Нет | `—` | Дата последнего использования карты |
| `date_released` | `datetime | None` | Нет | `—` | Дата выпуска карты |
| `servicecenter_last_usage_name` | `str | None` | Нет | `—` | Название последней АЗС, где использовалась карта |
| `transaction_last_detail` | `str | None` | Нет | `—` | Информация о последней транзакции |
| `transaction_timeout` | `TransactionTimeout | None` | Нет | `—` | Таймаут последней транзакции |
| `product` | `str | None` | Нет | `—` | Тип продукта (limit/wallet) |
| `payment_of_tolls` | `str | None` | Нет | `—` | Оплата платных дорог ('Y' или 'N') |

# `CardGroupInfo`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `id` | `str` | Да | `—` | ID карты |
| `group` | `str` | Да | `—` | ID группы карт |
| `contract_id` | `str` | Да | `—` | ID договора |
| `number` | `str` | Да | `—` | Номер карты |
| `status` | `str` | Да | `—` | Статус карты |
| `comment` | `str | None` | Нет | `—` | Комментарий |
| `product` | `str | None` | Нет | `—` | Тип продукта |
| `payment_of_tolls` | `str | None` | Нет | `—` | Оплата платных дорог ('Y' или 'N') |
| `sync_group_state` | `str | None` | Нет | `—` | Статус синхронизации группы |

# `VirtualCardData`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `id` | `str` | Да | `—` | ID виртуальной карты |
| `number` | `str` | Да | `—` | Номер виртуальной карты |
| `carrier` | `str` | Да | `—` | Тип носителя, обычно 'Virtual Card' |
| `product` | `str` | Да | `—` | Тип продукта карты ('wallet' или 'limit') |
| `status` | `str` | Да | `—` | Статус карты (например, 'Active', 'Blocked', 'Pending') |

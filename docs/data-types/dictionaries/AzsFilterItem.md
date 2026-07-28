# `AzsFilterItem`

Описание фильтра торговых точек

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `filter` | `str | None` | Нет | `—` | Ключ фильтра (например: services_with_card, countries и т.д.) |
| `name` | `str | None` | Нет | `—` | Название фильтра (человекочитаемое) |
| `values` | `dict[str, AzsFilterValue] | None` | Нет | `—` | Список значений для данного фильтра |

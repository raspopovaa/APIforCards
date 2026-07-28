# `WorkingTimeV2`

Расписание работы торговой точки

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `Weekday` | `str | None` | Нет | `—` | День недели или режим работы (Monday, Everyday, Round-The-Clock) |
| `StartWorkTime` | `str | None` | Нет | `—` | Время открытия, формат HH:MM |
| `FinishWorkTime` | `str | None` | Нет | `—` | Время закрытия, формат HH:MM |
| `Everyday` | `bool | None` | Нет | `—` | Признак работы ежедневно |
| `Round_The_Clock` | `bool | None` | Нет | `Round-The-Clock` | Признак круглосуточного режима |

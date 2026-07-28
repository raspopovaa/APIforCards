# `AuthUserData`

Модель данных SDK.

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `client_id` | `str` | Да | `—` | ID клиента в системе |
| `client_status` | `str` | Да | `—` | Статус клиента (Active, Blocked, и т.п.) |
| `org_name` | `str | None` | Нет | `—` | Наименование организации |
| `session_id` | `str` | Да | `—` | JWT токен активной сессии |
| `user_id` | `str` | Да | `—` | ID пользователя |
| `contracts` | `list[ContractInfo]` | Нет | `—` | Список доступных договоров |
| `role_id` | `str | None` | Нет | `—` | Код роли (например, Supervisor) |
| `role_name` | `str | None` | Нет | `—` | Название роли (например, Администратор) |
| `read_only` | `bool` | Нет | `—` | Флаг режима только чтение |
| `user_name` | `str | None` | Нет | `—` | Имя пользователя |
| `user_patronymic` | `str | None` | Нет | `—` | Отчество пользователя |
| `user_surname` | `str | None` | Нет | `—` | Фамилия пользователя |
| `last_contract` | `str | None` | Нет | `—` | SID последнего договора |
| `access` | `AccessRights | None` | Нет | `—` | Права доступа (web/api/mobile) |
| `email` | `str | None` | Нет | `—` | Электронная почта |
| `phone` | `str | None` | Нет | `—` | Телефон |

# `ContractResponse`

Полный ответ API по договору

| Поле | Python-тип | Обязательное | Alias | Описание |
|---|---|:---:|---|---|
| `mpc` | `bool` | Да | `—` | Разрешен ли выпуск виртуальных карт |
| `template_id` | `str` | Да | `—` | ID шаблона виртуальных карт |
| `status` | `str` | Да | `—` | Статус Way4 |
| `status_crm` | `str` | Да | `—` | Статус CRM |
| `payment_term_id` | `str | None` | Нет | `—` | ID справочника условия оплаты |
| `payment_scheme_id` | `str | None` | Нет | `—` | ID справочника схема оплаты |
| `is_dealer` | `bool` | Да | `—` | Признак дилерский |
| `balanceData` | `BalanceData` | Да | `—` | Данные по расходу и балансу договора |
| `contractData` | `ContractData` | Да | `—` | Данные договора |
| `managerData` | `ManagerData | None` | Нет | `—` | Данные по менеджеру договора |
| `cardsData` | `CardsData` | Да | `—` | Данные по количеству карт и групп карт на договоре |

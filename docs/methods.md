# Методы API

Каталог генерируется из runtime registry и сверяется с независимым `specifications/api-methods.yaml`.

!!! info "Покрытие"
    SDK содержит **89 операций** и **91 внешних маршрутов**.
    DEMO-доступность и тарификация отражают предоставленную сводную спецификацию, но фактический доступ также зависит от роли и договора.

## Обозначения

- **DEMO** — метод отмечен как доступный на демонстрационном стенде.
- **Тарифицируется** — вызов отмечен как платный во внешней спецификации.
- **Route** — относительный путь после базового `/vip/`.

## `client.auth`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.auth.auth_user()` | `authuser` | POST | v1 | `authUser` | Да | Нет |
| `client.auth.get_info()` | `info` | GET | v1 | `info` | Да | Нет |
| `client.auth.logoff()` | `logoff` | GET | v1 | `logoff` | Да | Нет |

## `client.card_groups`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.card_groups.get_card_groups()` | `cardgroups` | GET | v1 | `cardGroups` | Да | Нет |
| `client.card_groups.remove_card_group()` | `removecardgroup` | POST | v1 | `removeCardGroup` | Да | Да |
| `client.card_groups.set_card_group()` | `setcardgroup` | POST | v1 | `setCardGroup` | Да | Да |
| `client.card_groups.set_cards_to_group()` | `setcardstogroup` | POST | v1 | `setCardsToGroup` | Да | Да |

## `client.cards`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.cards.block_card()` | `blockcard` | POST | v1 | `blockCard` | Да | Да |
| `client.cards.get_card_detail()` | `cards_detail` | GET | v1 | `cards` | Да | Да |
| `client.cards.get_card_drivers()` | `cards_drivers` | GET | v2 | `cards/{card_id}/drivers` | Да | Да |
| `client.cards.get_cards_by_group()` | `cards_group` | GET | v1 | `cards` | Нет | Нет |
| `client.cards.get_cards_v1()` | `cards` | GET | v1 | `cards` | Да | Да |
| `client.cards.get_cards_v2()` | `cards_cache` | GET | v2 | `cards` | Да | Нет |
| `client.cards.reset_pin()` | `cards_reset_pin` | POST | v2 | `cards/{card_id}/resetPIN` | Нет | Да |
| `client.cards.set_card_comment()` | `setcardcomment` | POST | v1 | `setCardComment` | Да | Да |
| `client.cards.verify_pin()` | `cards_verify_pin` | POST | v2 | `cards/{card_id}/verifyPIN` | Да | Нет |

## `client.contracts`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.contracts.get_contract_data()` | `getpartcontractdata` | GET | v1 | `getPartContractData` | Да | Да |
| `client.contracts.get_documents()` | `documents_get` | GET | v2 | `documents` | Нет | Нет |
| `client.contracts.get_invoices()` | `invoices` | GET | v2 | `invoices` | Да | Нет |
| `client.contracts.get_payments()` | `getpayments` | GET | v1 | `getPayments` | Да | Да |
| `client.contracts.order_cards()` | `order_cards` | POST | v2 | `orderCards` | Нет | Да |
| `client.contracts.order_documents_email()` | `documents_post` | POST | v2 | `documents` | Нет | Да |
| `client.contracts.order_invoice()` | `invoice` | POST | v2 | `invoice` | Нет | Нет |

## `client.dictionaries`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.dictionaries.get_azs_filters()` | `filters` | GET | v2 | `azs/filters` | Нет | Нет |
| `client.dictionaries.get_azs_list_v1()` | `azs` | GET | v1 | `AZS` | Да | Нет |
| `client.dictionaries.get_azs_list_v2()` | `poi` | GET | v2 | `azs` | Нет | Нет |
| `client.dictionaries.get_dictionary()` | `getdictionary` | GET | v1 | `getDictionary` | Да | Нет |

## `client.ewallet`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.ewallet.move_to_card()` | `movetocard` | POST | v1 | `moveToCard` | Да | Да |
| `client.ewallet.move_to_contract()` | `movetocontract` | POST | v1 | `moveToContract` | Да | Да |
| `client.ewallet.set_card_product()` | `setcardproduct` | POST | v1 | `setCardProduct` | Да | Да |

## `client.final_prices`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.final_prices.check_purchase()` | `check_purchase` | POST | v2 | `cards/{card_id}/checkPurchase` | Нет | Нет |
| `client.final_prices.get_final_prices()` | `calculate_prices` | POST | v2 | `cards/{card_id}/calculatePrices` | Нет | Нет |

## `client.invites`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.invites.create_invite()` | `invites_post` | POST | v2 | `invites` | Нет | Да |
| `client.invites.create_invite()` | `invites_post_free` | POST | v2 | `invites_free` | Да | Нет |
| `client.invites.delete_invite()` | `invites_delete` | DELETE | v2 | `invites/{invite_id}` | Да | Нет |
| `client.invites.get_invites()` | `invites_get` | GET | v2 | `invites` | Да | Нет |
| `client.invites.prolong_invite()` | `invites_prolong` | POST | v2 | `invites/{invite_id}/prolong` | Нет | Да |
| `client.invites.prolong_invite()` | `invites_prolong_free` | POST | v2 | `invites/{invite_id}/prolong_free` | Да | Нет |
| `client.invites.resend_invite()` | `invites_send` | GET | v2 | `invites/{invite_id}/send` | Нет | Да |

## `client.limits`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.limits.get_limits()` | `limit` | GET | v1 | `limit` | Да | Нет |
| `client.limits.remove_limit()` | `removelimit` | POST | v1 | `removeLimit` | Да | Да |
| `client.limits.set_limit()` | `setlimit` | POST | v1 | `setLimit` | Да | Да |

## `client.region_limits`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.region_limits.get_region_limits()` | `regionlimit` | GET | v1 | `regionLimit` | Да | Да |
| `client.region_limits.remove_region_limit()` | `removeregionlimit` | POST | v1 | `removeRegionLimit` | Да | Да |
| `client.region_limits.set_region_limit()` | `setregionlimit` | POST | v1 | `setRegionLimit` | Да | Да |

## `client.reports`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.reports.download_report_file()` | `reports_jobs_file` | GET | v2 | `reports/jobs/{job_id}` | Нет | Да |
| `client.reports.download_report_file_v1()` | `getreportfile` | GET | v1 | `getReportFile` | Нет | Да |
| `client.reports.get_report_job_list_v1()` | `getreportjoblist` | GET | v1 | `getReportJobList` | Да | Нет |
| `client.reports.get_report_jobs()` | `reports_jobs` | GET | v2 | `reports/jobs` | Да | Нет |
| `client.reports.get_reports()` | `reports_get` | GET | v2 | `reports` | Да | Нет |
| `client.reports.order_report()` | `reports_post` | POST | v2 | `reports` | Да | Да |
| `client.reports.order_report_v1()` | `reports` | GET | v1 | `reports` | Нет | Да |

## `client.restrictions`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.restrictions.get_restrictions()` | `restriction` | GET | v1 | `restriction` | Да | Да |
| `client.restrictions.remove_restriction()` | `removerestriction` | POST | v1 | `removeRestriction` | Да | Да |
| `client.restrictions.set_restriction()` | `setrestriction` | POST | v1 | `setRestriction` | Нет | Да |

## `client.templates`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.templates.create_template()` | `vc_templates_post` | POST | v2 | `vc/templates` | Да | Да |
| `client.templates.create_template_georestriction()` | `vc_templates_georestrictions_post` | POST | v2 | `vc/templates/{template_id}/georestrictions` | Да | Да |
| `client.templates.create_template_limit()` | `vc_templates_limits_post` | POST | v2 | `vc/templates/{template_id}/limits` | Да | Да |
| `client.templates.create_template_restriction()` | `vc_templates_restrictions_post` | POST | v2 | `vc/templates/{template_id}/restrictions` | Да | Да |
| `client.templates.delete_template()` | `vc_templates_delete` | DELETE | v2 | `vc/templates/{template_id}` | Да | Да |
| `client.templates.delete_template_georestriction()` | `vc_templates_georestrictions_delete` | DELETE | v2 | `vc/templates/{template_id}/georestrictions/{georestrictions_id}` | Да | Да |
| `client.templates.delete_template_limit()` | `vc_templates_limits_delete` | DELETE | v2 | `vc/templates/{template_id}/limits/{limit_id}` | Да | Да |
| `client.templates.delete_template_restriction()` | `vc_templates_restrictions_delete` | DELETE | v2 | `vc/templates/{template_id}/restrictions/{restrictions_id}` | Да | Да |
| `client.templates.get_template_georestrictions()` | `vc_templates_georestrictions_get` | GET | v2 | `vc/templates/{template_id}/georestrictions` | Да | Нет |
| `client.templates.get_template_limits()` | `vc_templates_limits_get` | GET | v2 | `vc/templates/{template_id}/limits` | Да | Нет |
| `client.templates.get_template_restrictions()` | `vc_templates_restrictions_get` | GET | v2 | `vc/templates/{template_id}/restrictions` | Да | Нет |
| `client.templates.get_templates()` | `vc_templates_get` | GET | v2 | `vc/templates` | Да | Нет |
| `client.templates.update_template()` | `vc_templates_put` | PUT | v2 | `vc/templates/{template_id}` | Да | Да |
| `client.templates.update_template_georestriction()` | `vc_templates_georestrictions_put` | PUT | v2 | `vc/templates/{template_id}/georestrictions/{georestrictions_id}` | Да | Да |
| `client.templates.update_template_limit()` | `vc_templates_limits_put` | PUT | v2 | `vc/templates/{template_id}/limits/{limit_id}` | Да | Да |
| `client.templates.update_template_restriction()` | `vc_templates_restrictions_put` | PUT | v2 | `vc/templates/{template_id}/restrictions/{restrictions_id}` | Да | Да |

## `client.transactions`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.transactions.get_card_transactions_v2()` | `card_transactions` | GET | v2 | `cards/{card_id}/transactions` | Да | Да |
| `client.transactions.get_transaction_detail()` | `transaction_detail` | GET | v2 | `transactions/{transaction_id}` | Да | Нет |
| `client.transactions.get_transactions_v1()` | `transactions` | GET | v1 | `transactions` | Нет | Да |
| `client.transactions.get_transactions_v2()` | `contract_transactions` | GET | v2 | `transactions` | Да | Да |

## `client.users`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.users.attach_card()` | `users_attach_card` | POST | v2 | `users/{user_id}/attachCard` | Да | Да |
| `client.users.attach_contracts()` | `users_attach_contracts` | POST | v2 | `users/{user_id}/attachContracts` | Да | Да |
| `client.users.create_user()` | `users_post` | POST | v2 | `users` | Да | Да |
| `client.users.delete_user()` | `users_delete` | DELETE | v2 | `users/{user_id}` | Да | Да |
| `client.users.detach_card()` | `users_detach_card` | POST | v2 | `users/{user_id}/detachCard` | Да | Да |
| `client.users.detach_contracts()` | `users_detach_contracts` | POST | v2 | `users/{user_id}/detachContracts` | Да | Да |
| `client.users.get_users()` | `users_get` | GET | v2 | `users` | Да | Нет |

## `client.virtual_cards`

| Вызов SDK | External code | HTTP | Версия | Route | DEMO | Тарифицируется |
|---|---|---:|---:|---|:---:|:---:|
| `client.virtual_cards.confirm_mpc()` | `confirm_mpc` | POST | v2 | `cards/{card_id}/confirmMPC` | Нет | Нет |
| `client.virtual_cards.create_virtual_card()` | `cards_post` | POST | v2 | `cards` | Нет | Да |
| `client.virtual_cards.delete_mpc()` | `delete_mpc` | POST | v2 | `cards/{card_id}/deleteMPC` | Нет | Нет |
| `client.virtual_cards.generate_payment_qr()` | `pay` | POST | v2 | `cards/{card_id}/pay` | Нет | Нет |
| `client.virtual_cards.get_mpc_qr_list()` | `mpc` | GET | v2 | `MPC` | Нет | Нет |
| `client.virtual_cards.init_mpc()` | `init_mpc` | POST | v2 | `cards/{card_id}/initMPC` | Нет | Нет |
| `client.virtual_cards.release_virtual_card()` | `release` | POST | v2 | `cards/release` | Нет | Да |
| `client.virtual_cards.reset_mpc()` | `reset_mpc` | POST | v2 | `cards/{card_id}/resetMPC` | Нет | Нет |
| `client.virtual_cards.update_mpc()` | `update_mpc` | POST | v2 | `cards/{card_id}/updateMPC` | Нет | Нет |

## Дополнительные варианты маршрутов

Эти варианты поддерживаются SDK для совместимости или POST-fallback, но не имеют отдельного external code в сводной спецификации.

| Операция | Variant | HTTP | Версия | Route |
|---|---|---:|---:|---|
| `delete_invite` | `post_override` | POST | v2 | `invites/{invite_id}` |
| `delete_template` | `post_override` | POST | v2 | `vc/templates/{template_id}` |
| `delete_template_georestriction` | `post_override` | POST | v2 | `vc/templates/{template_id}/georestrictions/{georestriction_id}` |
| `delete_template_limit` | `post_override` | POST | v2 | `vc/templates/{template_id}/limits/{limit_id}` |
| `delete_template_restriction` | `post_override` | POST | v2 | `vc/templates/{template_id}/restrictions/{restriction_id}` |
| `delete_user` | `post_override` | POST | v2 | `users/{user_id}` |
| `update_template_georestriction` | `put` | PUT | v2 | `vc/templates/{template_id}/georestrictions/{georestriction_id}` |
| `update_template_restriction` | `put` | PUT | v2 | `vc/templates/{template_id}/restrictions/{restriction_id}` |

## Известные расхождения

- `calculate_prices`: сводная таблица указывает `GET`, SDK использует `POST`. The summary table specifies GET, while the detailed API specification requires a request body and POST.
- `check_purchase`: сводная таблица указывает `GET`, SDK использует `POST`. The summary table specifies GET, while the detailed API specification requires a request body and POST.

# Типовые сценарии

Примеры используют условные идентификаторы и не содержат credentials. Перед
вызовом изменяющего метода проверьте его тарификацию и DEMO-доступность в
[каталоге методов](methods.md).

## Авторизация и получение карт

```python
await client.auth.auth_user(contract_number="TEST-001")

cards = await client.cards.get_cards_v2(
    contract_id=client.contract_id,
    status="Active",
    page=1,
    onpage=20,
)
```

Единственный договор выбирается автоматически. При нескольких договорах передайте
`contract_id` или `contract_number`; SDK не выбирает первый договор по порядку.
Session ID SDK хранит самостоятельно. Не выводите его в терминал и не передавайте
в telemetry.

## Защита утраченной карты

```python
await client.cards.block_card(
    contract_id="contract-id",
    card_ids=["card-id"],
    block=True,
)
```

Блокировка изменяет состояние карты. Если соединение оборвалось после отправки
запроса, сначала проверьте состояние карты, а не повторяйте операцию безусловно.

## Лимит и товарное ограничение

```python
await client.limits.set_limit(
    limits=[{
        "contract_id": "contract-id",
        "card_id": "card-id",
        "sum": {"currency": "810", "value": 5000.0},
        "time": {"number": 1, "type": 1},
    }]
)

await client.restrictions.set_restriction(
    restrictions=[{
        "contract_id": "contract-id",
        "card_id": "card-id",
        "productType": "product-type-id",
        "restriction_type": 1,
    }]
)
```

Для изменения существующего лимита или ограничителя передавайте его `id`. Перед
созданием новой записи полезно запросить текущее состояние соответствующим GET-
методом.

## Заказ и получение отчёта

```python
available = await client.reports.get_reports()

job = await client.reports.order_report(
    report_id="report-id",
    format="xlsx",
    params={
        "contract_id": "contract-id",
        "date_from": "2026-01-01",
        "date_to": "2026-01-31",
    },
)

jobs = await client.reports.get_report_jobs()
report_file = await client.reports.download_report_file(job_id="job-id")
```

Формирование файла выполняется асинхронно на стороне API. Не запускайте частый
polling: учитывайте rate limit и ожидаемое время подготовки отчёта. Binary download
использует ту же retry-политику, что и JSON, но только для безопасных и
идемпотентных операций.

## Приглашение и виртуальная карта

```python
invite = await client.invites.create_invite(
    data={
        "role": "Driver",
        "mobile": "79990000000",
        "contracts": [{"sid": "contract-id"}],
    },
    with_send=False,
)

card = await client.virtual_cards.release_virtual_card(
    type_="wallet",
    template_id="template-id",
    user_id="user-id",
)
```

Сначала настройте шаблон лимитов и ограничений. В журналирование не должны
попадать телефон, ссылка приглашения и идентификаторы пользователя.

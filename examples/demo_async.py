import asyncio
import os
import sys
import time
from pathlib import Path
from typing import Any, Awaitable, Callable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from api_client_opti24 import APIClient
from api_client_opti24.env import load_env_file


DATE_FROM = "2023-04-01"
DATE_TO = "2023-04-30"

USE_COLOR = os.getenv("NO_COLOR") is None
DEMO_MIN_REQUEST_INTERVAL = float(os.getenv("DEMO_MIN_REQUEST_INTERVAL", "0.25"))


class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"


class DemoRateLimiter:
    def __init__(self, min_interval_seconds: float) -> None:
        self._min_interval_seconds = min_interval_seconds
        self._lock = asyncio.Lock()
        self._last_request_started_at = 0.0

    async def wait_turn(self) -> None:
        async with self._lock:
            now = time.monotonic()
            delay = self._min_interval_seconds - (now - self._last_request_started_at)
            if delay > 0:
                await asyncio.sleep(delay)
            self._last_request_started_at = time.monotonic()


def paint(text: str, *styles: str) -> str:
    if not USE_COLOR or not styles:
        return text
    return f"{''.join(styles)}{text}{Color.RESET}"

METHODS = {
    "auth_user": {
        "name": "Авторизация пользователя",
        "http": "POST",
        "url": "/vip/v1/authUser",
        "description": "Авторизация в API и получение активной сессии.",
    },
    "get_info": {
        "name": "Статистика",
        "http": "GET",
        "url": "/vip/v1/info",
        "description": "Получение статистических данных по вызовам всех методов.",
    },
    "get_contract_data": {
        "name": "Данные по договору",
        "http": "GET",
        "url": "/vip/v1/getPartContractData",
        "description": "Получение статуса договора, менеджера, баланса и числа карт.",
    },
    "get_payments": {
        "name": "Платежи по договору",
        "http": "GET",
        "url": "/vip/v1/getPayments",
        "description": "Получение данных о платежах по выбранному договору.",
    },
    "get_invoices": {
        "name": "Счета на оплату",
        "http": "GET",
        "url": "/vip/v2/invoices",
        "description": "Получение списка счетов на оплату.",
    },
    "get_cards_v2": {
        "name": "Список карт договора (v2)",
        "http": "GET",
        "url": "/vip/v2/cards",
        "description": "Получение списка карт с группой, статусом, комментарием и наличием МПК.",
    },
    "get_cards_v1": {
        "name": "Список топливных карт (Процессинг)",
        "http": "GET",
        "url": "/vip/v1/cards",
        "description": "Получение списка карт из процессинга.",
    },
    "get_card_detail": {
        "name": "Детальная информация по карте",
        "http": "GET",
        "url": "/vip/v1/cards",
        "description": "Получение детальной информации по конкретной карте.",
    },
    "get_card_drivers": {
        "name": "Список водителей по карте",
        "http": "GET",
        "url": "/vip/v2/cards/{card_id}/drivers",
        "description": "Получение списка водителей, связанных с картой.",
    },
    "get_transactions_v2": {
        "name": "Список транзакций по договору (v2)",
        "http": "GET",
        "url": "/vip/v2/transactions",
        "description": "Получение списка транзакций по договору за выбранный период.",
    },
    "get_card_transactions_v2": {
        "name": "Список транзакций по карте (v2)",
        "http": "GET",
        "url": "/vip/v2/cards/{card_id}/transactions",
        "description": "Получение списка транзакций по конкретной карте.",
    },
    "get_transaction_detail": {
        "name": "Данные по транзакции",
        "http": "GET",
        "url": "/vip/v2/transactions/{transaction_id}",
        "description": "Получение детальной информации по одной транзакции.",
    },
    "get_limits": {
        "name": "Список продуктовых лимитов",
        "http": "GET",
        "url": "/vip/v1/limit",
        "description": "Получение списка продуктовых лимитов по договору, карте или группе.",
    },
    "get_restrictions": {
        "name": "Список товарных ограничителей",
        "http": "GET",
        "url": "/vip/v1/restriction",
        "description": "Получение списка товарных ограничителей по договору, карте или группе.",
    },
    "get_region_limits": {
        "name": "Список региональных лимитов",
        "http": "GET",
        "url": "/vip/v1/regionLimit",
        "description": "Получение списка региональных лимитов по договору, карте или группе.",
    },
    "get_card_groups": {
        "name": "Список групп карт",
        "http": "GET",
        "url": "/vip/v1/cardGroups",
        "description": "Получение списка групп карт по договору.",
    },
    "get_reports": {
        "name": "Список доступных отчетов (v2)",
        "http": "GET",
        "url": "/vip/v2/reports",
        "description": "Получение списка доступных отчетов.",
    },
    "get_report_jobs": {
        "name": "Список заказанных отчетов (v2)",
        "http": "GET",
        "url": "/vip/v2/reports/jobs",
        "description": "Получение списка ранее заказанных отчетов по ссылке.",
    },
    "get_report_job_list_v1": {
        "name": "Список заказанных отчетов (v1)",
        "http": "GET",
        "url": "/vip/v1/getReportJobList",
        "description": "Получение списка ранее заказанных отчетов по ссылке.",
    },
    "get_invites": {
        "name": "Список приглашений",
        "http": "GET",
        "url": "/vip/v2/invites",
        "description": "Получение списка приглашений пользователей.",
    },
    "get_users": {
        "name": "Список пользователей",
        "http": "GET",
        "url": "/vip/v2/users",
        "description": "Получение списка пользователей.",
    },
    "get_templates": {
        "name": "Список шаблонов ВК",
        "http": "GET",
        "url": "/vip/v2/vc/templates",
        "description": "Получение списка шаблонов виртуальных карт.",
    },
    "get_template_limits": {
        "name": "Список лимитов шаблона ВК",
        "http": "GET",
        "url": "/vip/v2/vc/templates/{template_id}/limits",
        "description": "Получение списка лимитов шаблона виртуальной карты.",
    },
    "get_template_restrictions": {
        "name": "Список ограничителей шаблона ВК",
        "http": "GET",
        "url": "/vip/v2/vc/templates/{template_id}/restrictions",
        "description": "Получение списка ограничителей шаблона виртуальной карты.",
    },
    "get_template_georestrictions": {
        "name": "Список геоограничителей шаблона ВК",
        "http": "GET",
        "url": "/vip/v2/vc/templates/{template_id}/georestrictions",
        "description": "Получение списка геоограничителей шаблона виртуальной карты.",
    },
    "get_azs_list_v1": {
        "name": "Список торговых точек",
        "http": "GET",
        "url": "/vip/v1/AZS",
        "description": "Получение списка торговых точек.",
    },
    "get_dictionary": {
        "name": "Общие справочники",
        "http": "GET",
        "url": "/vip/v1/getDictionary",
        "description": "Получение общего справочника по имени.",
    },
    "logoff": {
        "name": "Деавторизация пользователя",
        "http": "GET",
        "url": "/vip/v1/logoff",
        "description": "Деактивация ранее полученной сессии.",
    },
}


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Environment variable {name} is required. Copy .env.example to .env and fill it."
        )
    return value


def print_block(title: str) -> None:
    print()
    line = "=" * 88
    print(paint(line, Color.DIM, Color.CYAN))
    print(paint(title, Color.BOLD, Color.CYAN))
    print(paint(line, Color.DIM, Color.CYAN))


def print_method_header(key: str) -> None:
    meta = METHODS[key]
    print_block(f"[{meta['http']}] {meta['url']}")
    print(f"{paint('Метод:', Color.BOLD, Color.BLUE)} {paint(meta['name'], Color.BOLD)}")
    print(f"{paint('Описание:', Color.BOLD, Color.MAGENTA)} {meta['description']}")


def format_contract(contract: Any) -> str:
    if contract is None:
        return "не указан"
    return f"{safe_getattr(contract, 'number')} ({safe_getattr(contract, 'id')})"


def choose_contract(contracts: list[Any]) -> Any:
    if not contracts:
        raise RuntimeError("После авторизации не найдено ни одного договора.")

    if len(contracts) == 1:
        contract = contracts[0]
        print(paint("Выбран единственный доступный договор.", Color.BOLD, Color.GREEN))
        print(paint(f"Договор: {format_contract(contract)}", Color.BOLD, Color.YELLOW))
        return contract

    print_block("Выбор договора")
    print("После авторизации найдено несколько договоров.")
    print("Укажите номер договора, по которому нужно сформировать demo-вызовы.")
    print()
    for index, contract in enumerate(contracts, start=1):
        print(f"{paint(str(index) + '.', Color.BOLD, Color.CYAN)} {format_contract(contract)}")

    while True:
        raw_value = input(paint("Введите номер договора: ", Color.BOLD, Color.YELLOW)).strip()
        try:
            selected_index = int(raw_value)
        except ValueError:
            print(paint("Нужно ввести целое число из списка.", Color.RED))
            continue

        if 1 <= selected_index <= len(contracts):
            selected_contract = contracts[selected_index - 1]
            print(paint(f"Выбран договор: {format_contract(selected_contract)}", Color.BOLD, Color.GREEN))
            return selected_contract

        print(paint("Номер вне диапазона списка договоров.", Color.RED))


def shorten_token(token: str, start: int = 24, end: int = 16) -> str:
    if len(token) <= start + end + 3:
        return token
    return f"{token[:start]}...{token[-end:]}"


def safe_getattr(obj: Any, *path: str) -> Any:
    current = obj
    for part in path:
        if current is None:
            return None
        if isinstance(current, dict):
            current = current.get(part)
        else:
            current = getattr(current, part, None)
    return current


def summarize_result(key: str, result: Any) -> None:
    if key == "auth_user":
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} авторизация успешна")
        print(f"{paint('Session:', Color.BOLD, Color.YELLOW)} {shorten_token(safe_getattr(result, 'data', 'session_id') or '')}")
        print(f"{paint('Договоры:', Color.BOLD, Color.YELLOW)} {[item.number for item in safe_getattr(result, 'data', 'contracts') or []]}")
        return

    if key == "get_info":
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} статистика получена")
        print(f"{paint('Период:', Color.BOLD, Color.YELLOW)} {safe_getattr(result, 'data', 'from_')} - {safe_getattr(result, 'data', 'to')}")
        print(f"{paint('Клиент:', Color.BOLD, Color.YELLOW)} {safe_getattr(result, 'data', 'client_info', 'Client')}")
        return

    if key == "get_contract_data":
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} данные договора получены")
        print(f"{paint('Статус договора:', Color.BOLD, Color.YELLOW)} {safe_getattr(result, 'contractData', 'contract_status_name')}")
        manager_last_name = safe_getattr(result, "managerData", "last_name")
        manager_first_name = safe_getattr(result, "managerData", "first_name")
        manager_display = "не указан"
        if manager_last_name or manager_first_name:
            manager_display = f"{manager_last_name or ''} {manager_first_name or ''}".strip()
        print(f"{paint('Менеджер:', Color.BOLD, Color.YELLOW)} {manager_display}")
        print(f"{paint('Доступный остаток:', Color.BOLD, Color.YELLOW)} {safe_getattr(result, 'balanceData', 'available_amount')}")
        return

    if key in {"get_payments", "get_invoices", "get_cards_v2", "get_cards_v1", "get_transactions_v2", "get_card_transactions_v2", "get_limits", "get_restrictions", "get_region_limits", "get_card_groups", "get_users", "get_templates", "get_azs_list_v1"}:
        total = safe_getattr(result, "data", "total_count")
        items = safe_getattr(result, "data", "result") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} данные получены")
        if total is not None:
            print(f"{paint('Всего записей:', Color.BOLD, Color.YELLOW)} {total}")
        preview = []
        for item in items[:3]:
            value = (
                safe_getattr(item, "number")
                or safe_getattr(item, "id")
                or safe_getattr(item, "name")
                or safe_getattr(item, "card_number")
            )
            if value is not None:
                preview.append(str(value))
        if preview:
            print(f"{paint('Примеры:', Color.BOLD, Color.YELLOW)} {preview}")
        return

    if key == "get_card_detail":
        items = safe_getattr(result, "data", "result") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} детали карты получены")
        if items:
            item = items[0]
            print(f"{paint('Карта:', Color.BOLD, Color.YELLOW)} {safe_getattr(item, 'number')}")
            print(f"{paint('Статус:', Color.BOLD, Color.YELLOW)} {safe_getattr(item, 'status')}")
            print(f"{paint('Продукт:', Color.BOLD, Color.YELLOW)} {safe_getattr(item, 'product')}")
        return

    if key == "get_card_drivers":
        total = safe_getattr(result, "data", "total_count")
        items = safe_getattr(result, "data", "result") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} список водителей получен")
        print(f"{paint('Всего водителей:', Color.BOLD, Color.YELLOW)} {total}")
        for item in items[:3]:
            print(paint("-", Color.DIM), safe_getattr(item, "last_name"), safe_getattr(item, "first_name"))
        return

    if key == "get_transaction_detail":
        items = safe_getattr(result, "data", "result") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} детализация транзакции получена")
        if items:
            item = items[0]
            print(f"{paint('Transaction ID:', Color.BOLD, Color.YELLOW)} {safe_getattr(item, 'id')}")
            print(f"{paint('Card ID:', Color.BOLD, Color.YELLOW)} {safe_getattr(item, 'card_id')}")
            print(f"{paint('Payment type:', Color.BOLD, Color.YELLOW)} {safe_getattr(item, 'payment_type')}")
        return

    if key in {"get_reports", "get_report_jobs", "get_invites", "get_template_limits", "get_template_restrictions", "get_template_georestrictions"}:
        total = safe_getattr(result, "total_count") or safe_getattr(result, "data", "total_count")
        items = safe_getattr(result, "result") or safe_getattr(result, "data", "result") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} данные получены")
        if total is not None:
            print(f"{paint('Всего записей:', Color.BOLD, Color.YELLOW)} {total}")
        if items:
            print(f"{paint('Примеры:', Color.BOLD, Color.YELLOW)} {[safe_getattr(item, 'id') or safe_getattr(item, 'name') for item in items[:3]]}")
        return

    if key == "get_report_job_list_v1":
        jobs = safe_getattr(result, "jobs") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} список отчетов получен")
        print(f"{paint('Всего job:', Color.BOLD, Color.YELLOW)} {len(jobs)}")
        return

    if key == "get_dictionary":
        data = safe_getattr(result, "data") or []
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} справочник получен")
        print(f"{paint('Количество элементов:', Color.BOLD, Color.YELLOW)} {len(data) if isinstance(data, list) else 'n/a'}")
        return

    if key == "logoff":
        print(f"{paint('Результат:', Color.BOLD, Color.GREEN)} выход выполнен")
        return

    print(paint("Результат получен", Color.BOLD, Color.GREEN))


async def run_method(
    key: str,
    action: Callable[[], Awaitable[Any]],
    context: list[str] | None = None,
    *,
    limiter: DemoRateLimiter | None = None,
) -> Any:
    print_method_header(key)
    if context:
        for line in context:
            print(paint(line, Color.DIM, Color.YELLOW))
    if limiter is not None:
        await limiter.wait_turn()
    try:
        result = await action()
    except Exception as exc:
        print(f"{paint('Статус:', Color.BOLD, Color.RED)} {paint('ERROR', Color.BOLD, Color.RED)}")
        print(f"{paint('Ошибка:', Color.BOLD, Color.RED)} {exc.__class__.__name__}: {exc}")
        return None

    print(f"{paint('Статус:', Color.BOLD, Color.GREEN)} {paint('OK', Color.BOLD, Color.GREEN)}")
    summarize_result(key, result)
    return result


async def main() -> None:
    load_env_file(PROJECT_ROOT / ".env")
    limiter = DemoRateLimiter(DEMO_MIN_REQUEST_INTERVAL)

    async with APIClient(
        base_url=require_env("API_BASE_URL"),
        api_key=require_env("API_KEY"),
        login=require_env("API_LOGIN"),
        password=require_env("API_PASSWORD"),
    ) as client:
        auth = await run_method("auth_user", lambda: client.auth_user(), limiter=limiter)
        if auth is None:
            return

        contracts = list(auth.data.contracts)
        selected_contract = choose_contract(contracts)
        client.contract_id = selected_contract.id

        await run_method("get_info", lambda: client.get_info(), limiter=limiter)

        contract_data = None
        payments = None
        invoices = None
        cards_v2 = None
        cards_v1 = None
        card_detail = None
        card_drivers = None
        transactions = None
        card_transactions = None
        limits = None
        restrictions = None
        region_limits = None
        card_groups = None
        reports = None
        report_jobs = None
        report_jobs_v1 = None
        invites = None
        users = None
        templates = None
        azs = None
        dictionary = None
        transaction_detail = None
        template_limits = None
        template_restrictions = None
        template_georestrictions = None
        if contracts:
            contract_data = await run_method(
                "get_contract_data",
                lambda: client.get_contract_data(selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            payments = await run_method(
                "get_payments",
                lambda: client.get_payments(selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            invoices = await run_method(
                "get_invoices",
                lambda: client.get_invoices(),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            cards_v2 = await run_method(
                "get_cards_v2",
                lambda: client.get_cards_v2(contract_id=selected_contract.id, page=1, onpage=5),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            cards_v1 = await run_method(
                "get_cards_v1",
                lambda: client.get_cards_v1(contract_id=selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            limits = await run_method(
                "get_limits",
                lambda: client.get_limits(contract_id=selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            restrictions = await run_method(
                "get_restrictions",
                lambda: client.get_restrictions(contract_id=selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            region_limits = await run_method(
                "get_region_limits",
                lambda: client.get_region_limits(contract_id=selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            card_groups = await run_method(
                "get_card_groups",
                lambda: client.get_card_groups(contract_id=selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            reports = await run_method(
                "get_reports",
                lambda: client.get_reports(),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            report_jobs = await run_method(
                "get_report_jobs",
                lambda: client.get_report_jobs(),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            report_jobs_v1 = await run_method(
                "get_report_job_list_v1",
                lambda: client.get_report_job_list_v1(),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            invites = await run_method(
                "get_invites",
                lambda: client.get_invites(),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            users = await run_method(
                "get_users",
                lambda: client.get_users(page=1, on_page=5),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            templates = await run_method(
                "get_templates",
                lambda: client.get_templates(selected_contract.id),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            azs = await run_method(
                "get_azs_list_v1",
                lambda: client.get_azs_list_v1(page=1, onpage=3),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            dictionary = await run_method(
                "get_dictionary",
                lambda: client.get_dictionary(name="CardStatus"),
                context=[f"Активный договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )
            transactions = await run_method(
                "get_transactions_v2",
                lambda: client.get_transactions_v2(
                    contract_id=selected_contract.id,
                    date_from=DATE_FROM,
                    date_to=DATE_TO,
                    page_limit=10,
                    page_offset=0,
                ),
                context=[f"Договор: {format_contract(selected_contract)}"],
                limiter=limiter,
            )

        first_card_id = None
        if cards_v2 and cards_v2.data.result:
            first_card_id = cards_v2.data.result[0].id

        if first_card_id:
            card_detail = await run_method(
                "get_card_detail",
                lambda: client.get_card_detail(contract_id=selected_contract.id, card_id=first_card_id),
                context=[
                    f"Договор: {format_contract(selected_contract)}",
                    f"Карта: {first_card_id}",
                ],
                limiter=limiter,
            )
            card_drivers = await run_method(
                "get_card_drivers",
                lambda: client.get_card_drivers(card_id=first_card_id, contract_id=selected_contract.id),
                context=[
                    f"Договор: {format_contract(selected_contract)}",
                    f"Карта: {first_card_id}",
                ],
                limiter=limiter,
            )
            card_transactions = await run_method(
                "get_card_transactions_v2",
                lambda: client.get_card_transactions_v2(
                    card_id=first_card_id,
                    contract_id=selected_contract.id,
                    date_from=DATE_FROM,
                    date_to=DATE_TO,
                    page_limit=10,
                    page_offset=0,
                ),
                context=[
                    f"Договор: {format_contract(selected_contract)}",
                    f"Карта: {first_card_id}",
                ],
                limiter=limiter,
            )

        transaction_id = None
        if transactions and transactions.data.result:
            transaction_id = str(transactions.data.result[0].id)

        if transaction_id:
            transaction_detail = await run_method(
                "get_transaction_detail",
                lambda: client.get_transaction_detail(
                    transaction_id=transaction_id,
                    contract_id=selected_contract.id,
                ),
                context=[
                    f"Договор: {format_contract(selected_contract)}",
                    f"Транзакция: {transaction_id}",
                ],
                limiter=limiter,
            )

        template_id = None
        if selected_contract:
            template_id = safe_getattr(selected_contract, "template_id")
        if not template_id and templates:
            template_items = safe_getattr(templates, "data", "result") or []
            if template_items:
                template_id = safe_getattr(template_items[0], "id")

        if template_id:
            template_limits = await run_method(
                "get_template_limits",
                lambda: client.get_template_limits(template_id),
                context=[
                    f"Договор: {format_contract(selected_contract)}",
                    f"Шаблон ВК: {template_id}",
                ],
                limiter=limiter,
            )
            if template_limits is not None:
                template_restrictions = await run_method(
                    "get_template_restrictions",
                    lambda: client.get_template_restrictions(template_id),
                    context=[
                        f"Договор: {format_contract(selected_contract)}",
                        f"Шаблон ВК: {template_id}",
                    ],
                    limiter=limiter,
                )
                template_georestrictions = await run_method(
                    "get_template_georestrictions",
                    lambda: client.get_template_georestrictions(template_id),
                    context=[
                        f"Договор: {format_contract(selected_contract)}",
                        f"Шаблон ВК: {template_id}",
                    ],
                    limiter=limiter,
                )

        await run_method("logoff", lambda: client.logoff(), limiter=limiter)


if __name__ == "__main__":
    asyncio.run(main())

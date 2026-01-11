from typing import Any, Iterator

def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Возвращает итератор по транзакциям с заданной валютой."""

    for t in transactions:
        code = t.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency:
            yield t







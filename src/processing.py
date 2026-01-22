from typing import Any
from .decorators import log

@log(filename="mylog.txt")
def filter_by_state(transactions: list[dict[str, Any]], state_value: str = "EXECUTED") -> list[dict[str, Any]]:
    """Фунция принимает список и фильтрует по ключу state"""
    filtered_transactions = []
    for transaction in transactions:
        if transaction["state"] == state_value:
            filtered_transactions.append(transaction)
    return filtered_transactions

@log(filename="mylog.txt")
def sort_by_date(transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """функция принимает список и сортирует по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)

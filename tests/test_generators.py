from typing import Any, Iterator
from src.generators import filter_by_currency

def test_filter_by_currency_usd():
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}}
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_no_matches():
    transactions = [{"id": 1, "operationAmount": {"currency": {"code": "EUR"}}}]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_missing_fields():
    transactions = [
        {"id": 1},
        {"id": 2, "operationAmount": {}},
        {"id": 3, "operationAmount": {"currency": {}}},
        {"id": 4, "operationAmount": {"currency": {"code": "USD"}}}
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 4


def test_filter_by_currency_case_sensitive():
    transactions = [{"id": 1, "operationAmount": {"currency": {"code": "usd"}}}]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []



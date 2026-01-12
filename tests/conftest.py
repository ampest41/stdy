from typing import Any
import pytest



@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T09:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02T10:30:00"},
        {"id": 4, "state": "PENDING", "date": "2023-01-04T14:20:00"},
    ]
@pytest.fixture
def empty_transactions() -> list:
    return []

@pytest.fixture
def currency_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет"
        },
        {
            "id": 123456789,
            "state": "CANCELED",
            "date": "2020-01-01T12:00:00.000000",
            "operationAmount": {
                "currency": {"code": "EUR"}
            },
            "description": "Покупка в Европе"
        }
    ]
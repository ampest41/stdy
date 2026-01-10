from typing import Any

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_default(sample_transactions: list[dict[str, Any]]) -> None:
    """Проверка фильтрации по умолчанию"""
    result = filter_by_state(sample_transactions)
    assert len(result) == 3
    assert all(t["state"] == "EXECUTED" for t in result)


@pytest.mark.parametrize(
    "state_value, expected_count",
    [
        ("EXECUTED", 3),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_parametrized(
    sample_transactions: list[dict[str, Any]], state_value: str, expected_count: int
) -> None:
    """Тесты для разных значений state"""
    result = filter_by_state(sample_transactions, state_value)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(t["state"] == state_value for t in result)


def test_filter_by_state_empty_list(empty_transactions: list[Any]) -> None:
    """Проверка фильтрации пустого списка"""
    result = filter_by_state(empty_transactions, "EXECUTED")
    assert result == []


def test_sort_by_date_stable(sample_transactions: list[dict[str, Any]]) -> None:
    """проверка на одинаковые даты"""
    result = sort_by_date(sample_transactions)
    same_date_ids = [t["id"] for t in result if t["date"] == "2023-01-01T12:00:00"]
    assert same_date_ids == [1, 5]

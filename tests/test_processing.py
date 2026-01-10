import pytest
from src.processing import filter_by_state


def test_filter_by_state_default(sample_transactions):
    """Проверка фильтрации по умолчанию"""
    result = filter_by_state(sample_transactions)
    assert len(result) == 3
    assert all(t["state"] == "EXECUTED" for t in result)


@pytest.mark.parametrize("state_value, expected_count", [
    ("EXECUTED", 3),
    ("CANCELED", 1),
    ("PENDING", 1),
    ("UNKNOWN", 0),
])
def test_filter_by_state_parametrized(sample_transactions, state_value, expected_count):
    """Тесты для разных значений state"""
    result = filter_by_state(sample_transactions, state_value)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(t["state"] == state_value for t in result)


def test_filter_by_state_empty_list(empty_transactions):
    """Проверка фильтрации пустого списка"""
    result = filter_by_state(empty_transactions, "EXECUTED")
    assert result == []


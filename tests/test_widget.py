import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "value_input, expected_output",
    [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Карта 1234567890", "Карта 1234 56** **** 7890"),
        ("Карта 1234567890123456789", "Карта 1234 56** **** 6789"),
    ],
)
def test_mask_account_card(value_input: str, expected_output: str) -> None:
    assert mask_account_card(value_input) == expected_output


def test_mask_account_card_empty_string() -> None:
    with pytest.raises(ValueError, match="Пустая строка"):
        mask_account_card("")


def test_mask_account_card_no_number() -> None:
    with pytest.raises(ValueError, match="Не найден номер"):
        mask_account_card("Visa")


def test_mask_account_card_short_card_number() -> None:
    with pytest.raises(ValueError, match="Номер карты должен содержать минимум 10 цифр"):
        mask_account_card("Карта 12345")


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("2023-01-01T12:00:00", "01.01.2023"),
        ("", ""),
        ("2023-01-01", ""),
        ("invalid", ""),
        ("2023-ab-cdT10:30:00", ""),
    ],
)
def test_get_date(input_str: str, expected: str) -> None:
    assert get_date(input_str) == expected

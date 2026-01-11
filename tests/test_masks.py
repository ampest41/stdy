import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "value_input, expected_output",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234567890", "1234 56** **** 7890"),
        ("12345678901", "1234 56** **** 8901"),
        ("1234567890123456789", "1234 56** **** 6789"),
        ("", "**** **"),
        ("1", "1*** ***1"),
        ("123", "123* **** *123"),
    ],
)
def test_get_mask_card_number(value_input: str, expected_output: str) -> None:
    assert get_mask_card_number(value_input) == expected_output


@pytest.mark.parametrize(
    "value_input, expected_output",
    [
        ("12345678901234567890", "**7890"),
        ("123", "**123"),
        ("", "**"),
        ("1", "**1"),
        (" ", "** "),
    ],
)
def test_get_account(value_input: str, expected_output: str) -> None:
    assert get_mask_account(value_input) == expected_output

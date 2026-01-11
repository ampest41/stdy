from typing import Any, Iterator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator

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


def test_transaction_descriptions_normal():
    """Тест: корректные описания для обычных транзакций."""
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Пополнение счета"},
        {"id": 3, "description": "Оплата услуг"}
    ]

    result = list(transaction_descriptions(transactions))
    expected = ["Перевод организации", "Пополнение счета", "Оплата услуг"]
    assert result == expected


def test_transaction_descriptions_missing_description():
    """Тест: транзакции без 'description' возвращают пустую строку."""
    transactions = [
        {"id": 1, "description": "Есть описание"},
        {"id": 2},  # нет description
        {"id": 3, "amount": 100}  # тоже нет
    ]

    result = list(transaction_descriptions(transactions))
    expected = ["Есть описание", "", ""]
    assert result == expected


def test_transaction_descriptions_empty_list():
    """Тест: пустой список → пустой итератор (без ошибок)."""
    result = list(transaction_descriptions([]))
    assert result == []


def test_transaction_descriptions_one_transaction():
    """Тест: одна транзакция."""
    transactions = [{"description": "Один элемент"}]
    result = list(transaction_descriptions(transactions))
    assert result == ["Один элемент"]


def test_transaction_descriptions_all_empty_descriptions():
    """Тест: все транзакции без описаний."""
    transactions = [{}, {"id": 1}, {"amount": 50}]
    result = list(transaction_descriptions(transactions))
    assert result == ["", "", ""]

def test_card_number_generator_basic():
    """Тест: базовая генерация — правильный формат и последовательность."""
    result = list(card_number_generator(1, 3))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]
    assert result == expected


def test_card_number_generator_format():
    """Тест: формат всегда 'XXXX XXXX XXXX XXXX' (ровно 19 символов, 3 пробела)."""
    gen = card_number_generator(1234567890123456, 1234567890123456)
    card = next(gen)
    assert len(card) == 19
    assert card.count(" ") == 3
    blocks = card.split()
    assert len(blocks) == 4
    assert all(len(block) == 4 for block in blocks)
    assert all(block.isdigit() for block in blocks)


def test_card_number_generator_edge_values():
    """Тест: корректная работа с минимальным и максимальным значениями."""
    # Минимальное значение по условию — 1
    result_min = list(card_number_generator(1, 1))
    assert result_min == ["0000 0000 0000 0001"]

    # Максимальное значение — 9999999999999999
    result_max = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result_max == ["9999 9999 9999 9999"]


def test_card_number_generator_single_value():
    """Тест: один номер в диапазоне."""
    result = list(card_number_generator(42, 42))
    assert result == ["0000 0000 0000 0042"]


def test_card_number_generator_empty_range():
    """Тест: start > end → пустой результат (но без ошибки)."""
    result = list(card_number_generator(5, 3))
    assert result == []


def test_card_number_generator_large_range():
    """Тест: генерация нескольких значений — проверка последовательности."""
    result = list(card_number_generator(9999999999999997, 9999999999999999))
    expected = [
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]
    assert result == expected


def test_card_number_generator_no_premature_stop():
    """Тест: генератор выдаёт ровно (end - start + 1) элементов."""
    start, end = 100, 200
    result = list(card_number_generator(start, end))
    assert len(result) == end - start + 1
    # Проверим первый и последний
    assert result[0] == "0000 0000 0000 0100"
    assert result[-1] == "0000 0000 0000 0200"

from typing import Any, Iterator

def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Возвращает итератор по транзакциям с заданной валютой."""

    for t in transactions:
        code = t.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency:
            yield t



def transaction_descriptions(transactions):
    descriptions = map(lambda t: t.get("description", ""), transactions)
    for desc in descriptions:
        yield desc


def card_number_generator(start:int, end:int) -> Iterator[str]:
    for number in range(start, end+1):
        card = str(number)
        if len(card) < 16:
            card = "0" * (16 - len(card)) + card
        yield f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:]}"


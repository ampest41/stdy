def get_mask_card_number(card_number: str) -> str:
    """функция маскирует номер карты"""

    masked = card_number[0:6] + "******" + card_number[-4:]

    blocks = []

    for i in range(0, len(masked), 4):
        block = masked[i : i + 4]
        blocks.append(block)
    return " ".join(blocks)


def get_mask_account(account: str) -> str:
    """функция маскирует номер счета"""

    return "**" + account[-4:]

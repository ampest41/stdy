from src.masks import get_mask_account
from src.masks import get_mask_card_number

card_number: str = input()

card_number = get_mask_card_number(card_number)
print(card_number)


account: str = input()

account_number = get_mask_account(account)
print(account_number)

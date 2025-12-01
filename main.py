from src.widget import get_date
from src.widget import mask_account_card

card_info: str = input()
date_time: str = input()

print(mask_account_card(card_info))
print(get_date(date_time))

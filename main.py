# from src.widget import get_date
# from src.widget import mask_account_card
from src.processing import filter_by_state
from src.processing import sort_by_date

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


executed_transactions = filter_by_state(transactions)

sorted_by_date_transaction = sort_by_date(transactions)

print(executed_transactions)
print(sorted_by_date_transaction)

# card_info: str = input()
# date_time: str = input()

# print(mask_account_card(card_info))
# print(get_date(date_time))

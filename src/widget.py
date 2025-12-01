def mask_account_card(card_info: str) -> str:
    '''функция принимает тип и номер карты или счета и возвращает маску'''



    parts = card_info.rsplit(' ',1)
    type_name = parts[0]
    number = parts[1]


    if type_name == "Счет":
        return type_name + " " + "**" + number[-4:]
    else:
        masked = f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"
        return type_name + " " + masked





def get_date(date_time: str) -> str:
    '''функция принимает дату и возвращает ее в удобном формате'''



    date_part = date_time.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"




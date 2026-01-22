from .decorators import log



@log(filename="mylog.txt")
def mask_account_card(card_info: str) -> str:
    """функция принимает тип и номер карты или счета и возвращает маску"""

    if not card_info.strip():
        raise ValueError("Пустая строка")

    if card_info.strip().isdigit():
        number = card_info.strip()
        if len(number) < 10:
            raise ValueError("Номер карты должен содержать минимум 10 цифр")
        masked = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        return masked

    parts = card_info.rsplit(" ", 1)
    if len(parts) < 2:
        raise ValueError("Не найден номер")
    type_name = parts[0]
    number = parts[1]

    if not number.isdigit():
        raise ValueError("Номер должен содержать только цифры")
    if len(number) < 10:
        raise ValueError("Номер карты должен содержать минимум 10 цифр")

    if type_name == "Счет":
        return type_name + " " + "**" + number[-4:]
    else:
        masked = f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"
        return type_name + " " + masked

@log(filename="mylog.txt")

def get_date(date_time: str) -> str:
    """функция принимает дату и возвращает ее в удобном формате"""

    if not date_time or "T" not in date_time:
        return ""  # или raise ValueError("Некорректный формат даты")

    date_part = date_time.split("T")[0]
    parts = date_part.split("-")

    if len(parts) != 3:
        return ""

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return ""

    return f"{day}.{month}.{year}"

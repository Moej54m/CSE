def valid_card_number(num: str):
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print(" NOT EVERY NUMBER IS 16 DIGITS")
        return False


def validate(num: str):
    if not all_16_digits(num):
        return False


print(validate("8248714205534850"))


def drop_last_num(num: str):
    list_num = list(num)
    for index in range(len(list_num)):

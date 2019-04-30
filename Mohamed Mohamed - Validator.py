def valid_card_number(num: str):
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print(" NOT EVERY NUMBER IS 16 DIGITS")
        return False


list_num = list(number)
for index in range(len(list_num)):
    list_num[index] = int(list_num[index])

print(valid_card_number("6854429810265090"))

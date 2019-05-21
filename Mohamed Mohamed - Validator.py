import csv


def sixteen_digits(number16: str):
    if(len(number16)) == 16:
        if len(number16) == 16:
            return True
        else:
            return False


def divisible_by_2(number16: str):
    if number % 2 == 0:
        return True
    return False


def valid_card_number(num: str):
    if not sixteen_digits(num):
        return False
    valid_card_number_list = list(num)
    valid_card_number_list.pop(15)
    for number in range(len(valid_card_number_list)):
        valid_card_number_list[number] = int(valid_card_number_list[number])
    reversed_num = num[::-1]
    reversed_num_list = []
    for i in range(len(reversed_num)):
        reversed_num_list.append(int(reversed_num[i]))
        for index in range(len(reversed_num_list)):
            if divisible_by_2(index):
                if int(reversed_num_list[index]) * 2






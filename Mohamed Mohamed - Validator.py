import csv


def sixteen_numbers(number16: str):
    if(len(number16)) == 16:
        if len(number16) == 16:
            return True
        else:
            print("Not every Number is 16  digits.")
            return False


def divisible(number: int):
    if number % 2 == 0:
        return True
    return False


def valid_card_digits(num: str):
    if not sixteen_numbers(num):
        return False
    valid_card_digits_list = list(num)
    valid_card_digits_list.pop(15)
    for number in range(len(valid_card_digits_list)):
        valid_card_digits_list[number] = int(valid_card_digits_list[number])
    reversed_num = valid_card_digits_list[::-1]
    reversed_num_list = []
    for i in range(len(reversed_num)):
        reversed_num_list.append(int(reversed_num[i]))
        for index in range(len(reversed_num_list)):
            if divisible(index):
                if int(reversed_num_list[index]) * 2 > 9:
                    reversed_num_list[index] = int(reversed_num_list[index]) * 2 - 9
                else:
                    reversed_num_list[index] *= 2
                    sum_numbers = sum(reversed_num_list)
                    if{sum_numbers % 10} == 0:
                        return True

                return False


with open("Book1 2.csv", 'r') as old_csv:
    with open("ValidatorCheck.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            num = row[0]
            if valid_card_digits(num):
                writer.writerow(row)
                print("Done")




import csv
def reverse_it(string):

    with open("Book1.csv") as old_csv:
        with open("MyNewFile.csv", 'w', newline='') as new_CSV:
            print("Writing file.... ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num % 3 == 0:
                writer.writerow(row)
        # old_number = int(row[0]) + 1
        # print(old_number)
print("OK")


def validate(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def divisible_by _3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


    def all_16_digits(num: str):
        if len(num) == 16:
            return True
        else:
            print(" NOT EVERY NUMBER IS 16 DIGITS")
            return False
# import csv# #
# with open("Book1.csv") as old_csv:

#     with open("MyNewFile.csv", 'w', newline='') as new_CSV:
#         print("Writing file.... ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num % 2 == 0:
#         writer.writerow(row)
#         # old_number = int(row[0]) + 1
#         # print(old_number)
# print("OK")
#

def reverse_it(string):
    print(string[0:9:2])

def valid_card_number(num: str):
    ?????????

print(valid_card_number("6854429810265090"))
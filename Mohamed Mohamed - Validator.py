# The Luhn Formula:
#
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10 (Modulo 10)

def all_16_digits(num: str):
    if len(num) == 16:
        print("Every card has 16 digits.")


def drop_num(num: str):
    list_num = list(num)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
        list_num.pop(15)
        print("The last digit of the card was removed.")
        print(list_num)
        return list_num

    def reverse(num: str):
        list_num = list(num)
        print(list_num(::-1))


    def validate (num: str):
    if not all_16_digits(num):
        drop_num("3785162546340070")
        reverse("3785162546340070")




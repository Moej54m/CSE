import random
import string
words = ["LeBron James", "Kyrie Irving", "National Basketball Association.", "Doofenshmirtz.",
            "Wakanda Forever.", "High School", "Hamburger", "Russell Westbrook", "Games"]
output = []
guesses = 8

list_of_letters = string.ascii_letters

word_selection = random.choice(words)
length = len(word_selection)
word_list = list(word_selection)

for i in range(length):
    output.append("* ")
print("".join(output))

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter")
    print('\n' * 10)
    if user_guess in word_selection:
        print("You are correct!")
        for i in range (len(word_selection)):
            if user_guess in word_list:
                word_list.pop(i)
    for i in range(len(word_selection)):
        if word_selection[i] == user_guess:
            output.pop(i)
            output.insert(i, user_guess)
        print("".join(output))
    else:
        print("WRONG")
        guesses = (guesses - 1)
        print(guesses)
    if guesses <= 0:
        print("You are CORRRRRECT!")
        print("The word was %s" % word_selection)

import random
import string
words = ["LeBron James", "Kyrie Irving", "National Basketball Association.", "Doofenshmirtz.",
            "Wakanda Forever.", "High School", "Hamburger", "Russell Westbrook", "Games"]
output = []
guesses = 8
guess_word = []

list_of_letters = string.ascii_letters

word_selection = random.choice(words)
length = len(word_selection)
word_list = list(word_selection)
print(word_list)

for i in range(length):
    output.append("* ")
print("".join(output))

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter:")
    print('\n' * 10)
    print(output)
    if user_guess.lower() in word_list or user_guess.upper() in word_list:
        print("You are correct!")
        for i in range(len(word_selection)):
            if word_selection[i].lower() == user_guess.lower():
                output.pop(i)
                output.insert(i, user_guess)
        print("".join(output))

    else:
        print("NOOPE")
        guesses = (guesses - 1)
        print(guesses)
        print("You are CORRRRRECT!")

    if guesses == words:
        print("The word was %s" % word_selection)

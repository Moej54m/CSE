import random
import string
words = ["LeBron James", "Kyrie Irving", "NBA.", "Doofenshmirtz.",
            "Wakanda Forever.", "High School", "Hamburger", "Russell Westbrook", "Games"]
output = []
guesses = 8
guess_word = []

list_of_letters = string.ascii_letters

word_selection = random.choice(words)
length = len(word_selection)
word_list = list(word_selection)
punctuation = string.punctuation
list_of_punctuation = list(punctuation)

for i in range(length):
    output.append("* ")

for i in range(length):
    for j in range(len(list_of_punctuation)):
        if list_of_punctuation[j] in word_selection[i]:
            output.pop(i)
            output.insert(i, list_of_punctuation[j])

print("".join(output))

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter:")
    print('\n' * 10)
    if user_guess.lower() in word_selection or user_guess.upper() in word_selection:
        print("You are correct!")
        for i in range(len(word_selection)):
            if word_selection[i].lower() == user_guess.lower():
                output.pop(i)
                output.insert(i, user_guess)
        print("".join(output))
    else:
        print("You got it wrong!")
        guesses = (guesses - 1)
        print(guesses)
    if guesses <= 0:
        print("You don't have any guesses. GAME OVER")
        break
    if output == word_list:
        print("You won!!!")
        print("THe word was %s" % word_selection)
        break

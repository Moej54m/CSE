import random

r = random.randint(1, 10)
guesses_left = 5
playing = True
print("Think of a number from 1 to 10")

while guesses_left > 0 and playing:
    guess = int(input("Guess="))
    if guess > r:
        print("Lower")
        guesses_left = guesses_left -1
    elif guess < r:
        print("Greater")
        guesses_left = guesses_left -1
    else:
        print("Correct")
        playing = Falsea
    if guesses_left == 0:
        print("You Lose")


import random
import string
athletes = ["LeBron James", "Kyrie Irving", "National Basketball Association.", "Doofenshmirtz Evil Incorporated.",
            "Wakanda Forever.", "High School", "Hamburger", "Russell Westbrook", "Games"]
print("I'm thinking of a word, what is it?")

word = random.choice(athletes)
print(word)
print(list(string.punctuation))
print(string.whitespace)

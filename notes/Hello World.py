"""
print("Hello World!")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself.
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space")
print()
print()
print("There should be a couple blank lines here.")

#Math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # Modulus (Remainder)

# Powers
# What is 2^20?
print(2 ** 100)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name= "Mowdi"
car_type= "Yoinkers"
car_cylinders= 18
car_miles_per_gallon= 4

# Make it print "I have a car called Mowdi. It is a Yoinkers."
print("I have a car called %s. It is a %s" % (car_name, car_type)

# Reacasting
real_age = int(input("How old are you again?"))

























f(1)
f(5)
f(5000)


# Distance formula
def distance(x1, x2, y1, y2)
    dist= ((x2-x1) **2 + (y2-y1)**2)**(1/2)
print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12))

# Loops
for i in range(5); # This gives the numbers 0 through 4
 say_it()




while a < 10
    print(a)
a *=0 # This is the same as saying a = a + 1


""
For loops - Use when you know exactly how many iterations
While loops - Use when you don't know how many iterations
"""


# Control Structures (If statements)
sunny = False 
if sunny:
  print("Go Outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage>= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
      return "F"


your_grade = grade_calc(82)
print(your_grade)

# "RANDOM" Notes
import random # thIS should be line 1
print(random.randint(0,100))
# Equality Statements
print(5 > 3)
print (5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3 # A is set to 3
a == 3 # Is equal to 3?
"""

colors = ["blue", "turquoise", "pink", "orange", "black", "red"]
print(colors)
print(colors[1])
print(colors[0])

# Length of the list
print("There are %d things on the list." % len(colors))

# Changing Elements in a list
colors[1] = "Green"
print(colors)

# Looping through lists 
for item in colors:
    print(item) 

NBA_Teams = ["Boston Celtics", "Golden State Warriors", "Houston Rockets", "Toronto Raptors", "Cleveland Cavaliers"]
NBA_Teams[2] = "Utah Jazz"
print(NBA_Teams)
print("The last thing in the list is")

# Slicing a list
print(NBA_Teams[1:3])

food_list = ["pizza", "tamales", "pie", "burrito", "flan", "salad", "turkey", "fried ice cream", "rice", "chicken"             "lasagna"]
food_list.append("rice")
food_list.append("chicken")
print(food_list)
food_list.insert(1, "pie")
print(food_list)
food_list.remove("salad")
print(food_list)

# Tuples
brands = ("apple", "samsung", "HTC")  # Notice the parentheses

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index(chicken))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Function Notes
# a**2 + b**2 = c**2
def pythagorean(a, b):
    return (a**2 + b**2)**(1/2)

print(pythagorean(3, 4))

for i in range(len(list1)): # i goes through all indicies
    if list1[i] =="u":  # if we find a U
        list1.pop(i)  # remove the i-th index
        list.insert(i, "*") # Put a * there instead


# Turn a list into a string
print("".join(list1))














































































































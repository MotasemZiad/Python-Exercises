from datetime import datetime
print("Practice Python")


# Exercise 1:
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# name = input("Enter your name:\n")
# age = int(input(f"Hello {name}, How old are you?:\n"))

# year_to_be_hundred = 2022 + (100 - age)
# print(f"On {year_to_be_hundred} you will be 100 years old.")


# Exercise 2:
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

number = int(input("Enter a number:\n"))

if(number % 2 == 0):
    if(number % 4 == 0):
        print(f"{number} is a multiple of 4")
    else:
        print(f"{number} is Even")
else:
    print(f"{number} is Odd")

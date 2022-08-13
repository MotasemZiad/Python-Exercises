from datetime import datetime
print("Practice Python")


# Exercise 1:
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name:\n")
age = int(input(f"Hello {name}, How old are you?:\n"))

year_to_be_hundred = 2022 + (100 - age)
print(f"On {year_to_be_hundred} you will be 100 years old.")

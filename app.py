# import os
# OS module

# name = input("Enter a folder name:\n")
# os.system(f"mkdir {name}")

# os.system("cd ahmed")

# os.system('lsd')

# os.system('git --version')
# os.system('flutter --version')
# os.system('dart --version')
# os.system('python --version')
# os.system('php --version')
# os.system('docker --version')
# os.system('java --version')

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

# number = int(input("Enter a number:\n"))

# if(number % 2 == 0):
#     if(number % 4 == 0):
#         print(f"{number} is a multiple of 4")
#     else:
#         print(f"{number} is Even")
# else:
#     print(f"{number} is Odd")

# Exercise 3:
# Take a list and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# def print_smaller_numbers(list_input, endpoint):
#     new_list = [i for i in list_input if i < endpoint]
#     # for i in list_input:
#     #     if(i < 5):
#     #         new_list.append(i)
#     print(new_list)


# random_list = [1, 1, 2, 3, 5, 8, 13, 21, 12, 17, 23, 47, 9, 15, 28, 34, 55, 89]

# while True:
#     great_number = int(input("Enter a number (-1 to exit): \n"))
#     if(great_number == -1):
#         break
#     print_smaller_numbers(random_list, great_number)

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

# Exercise 4:
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

# def get_divisors(num_input):
#     list_of_divisors = [i for i in range(
#         1, num_input + 1) if num_input % i == 0]
#     # for i in range(1, num_input + 1):
#     #     if num_input % i == 0:
#     #         list_of_divisors.append(i)
#     return list_of_divisors


# while True:
#     num_input = int(input("Enter a number: (-1 to exit)\n"))
#     if(num_input == -1):
#         break
#     print(get_divisors(num_input))

# Exercise 5:
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# import random


# def find_common(list1, list2):
#     return list(set([i for i in list1 for j in list2 if i == j]))
#     # list_common = set()
#     # for i in list1:
#     #     for j in list2:
#     #         if(i == j):
#     #             list_common.add(i)
#     # return list(list_common)


# a = []
# b = []


# for i in range(20):
#     a.append(random.randint(0, 100))
#     b.append(random.randint(0, 100))

# print(find_common(a, b))

# Exercise 6:
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# def is_palindrome(sentence):
#     lower_case_sentence = sentence.lower()
#     reversed_sentence = lower_case_sentence[::-1]
#     if(lower_case_sentence == reversed_sentence):
#         return True
#     return False


# while True:
#     str_input = input("Enter a word:\n")
#     if(str_input == "exit"):
#         break
#     if(is_palindrome(str_input)):
#         print("This is a palindrome")
#     else:
#         print("This is NOT a palindrome")

# Exercise 7:
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# def get_even_numbers(list_input):
#     return [i for i in list_input if i % 2 == 0]


# print(get_even_numbers([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))

# Exercise 8:
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# print("Rock Paper Scissors Game\t (Enter exit to end the game)")
# first_player_score = 0
# second_player_score = 0
# while True:
#     first_player_choice = input("Player 1: Enter your choice:\n")
#     if(first_player_choice.lower() == "exit"):
#         print(
#             f"Final Score: Player 1: {first_player_score} VS. Player 2: {second_player_score}")
#         break
#     second_player_choice = input("Player 2: Enter your choice:\n")

#     if (first_player_choice.lower() == "rock" and second_player_choice.lower() == "scissors") or (first_player_choice.lower() == "scissors" and second_player_choice.lower() == "paper") or (first_player_choice.lower() == "paper" and second_player_choice.lower() == "rock"):
#         first_player_score += 1
#         print("Player 1 win")
#     elif (second_player_choice.lower() == "rock" and first_player_choice.lower() == "scissors") or (second_player_choice.lower() == "scissors" and first_player_choice.lower() == "paper") or (second_player_choice.lower() == "paper" and first_player_choice.lower() == "rock"):
#         second_player_score += 1
#         print("Player 2 win")
#     elif first_player_choice.lower() == second_player_choice.lower():
#         print("Draw!")
#     else:
#         print("Enter rock, paper, or scissors!")

# Exercise 9:

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# import random

# tries = 0
# print("Guessing Game\nWe are generating a number between 1 to 9:")
# generated_number = random.randint(1, 9)

# while True:
#     user_input = input("Try to guess the number: (type exit to end)\n")

#     if user_input == 'exit':
#         break

#     tries += 1
#     if int(user_input) < 1 or int(user_input) > 9:
#         print("Invalid input, please enter a number between 1 and 9")
#     else:
#         if int(user_input) == generated_number:
#             print(f"Your guess is right, You took {tries} tries to get it!")
#             break
#         elif int(user_input) > generated_number:
#             print("Your guess is greater than the right one.")
#         elif int(user_input) < generated_number:
#             print("Your guess is less than the right one.")

# Exercise 10:
# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:
# Randomly generate two lists to test this
import random


def find_in_common(list1, list2):
    return list(set([i for i in list1 if i in list2]))
    # return list(set([i for i in list1 for j in list2 if i == j]))


first_list = random.sample(range(0, 100), k=random.randint(1, 20))
second_list = random.sample(range(0, 100), k=random.randint(1, 20))

print(first_list)
print(second_list)

print("Element in common with two generated lists:",
      find_in_common(first_list, second_list))

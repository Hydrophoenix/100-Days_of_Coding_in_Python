'''A rock, paper and scissors game. The rule states that Rock beats Scissors, Scissors beat Paper and Paper beat Rock'''
import random
# Welcome the use to the game
print("Welcome to the Rock, Paper and Scissors game")
# Equate R, P, S to a number
R = 1
P = 2
S = 3
#game_options = ["R", "P", "S"]
user_name = input("Type in your name: ")
# Ask the user to make a choice betwwem 1 and 3
user_choice = int(input("What would you choose? (Type in 0 for Rock, 1 for Paper or 2 for Scissors) "))
# Using the random module, get a random number
comp_choice = random.randint(0, 2)
print(f"Computer chose {comp_choice}")
print(f"You chose {user_choice}")
# Check using the rock, paper and scissors rule to check who wins
if user_choice >= 1 or user_choice <= 3:
    if user_choice == comp_choice:
        print("It's a Draw!!")
    elif user_choice == R and comp_choice == S:
        print("You Win!")
    elif user_choice == S and comp_choice == R:
        print("CPU Win!")
    elif user_choice == S and comp_choice == P:
        print("You Win!")
    elif user_choice == P and comp_choice == S:
        print("CPU Win!")
    elif user_choice == P and comp_choice == R:
        print("You Win!")
    elif user_choice == R and comp_choice == P:
        print("CPU Win!")
    else:
        print("Wrong input, Please try again!")

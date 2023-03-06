'''A virtual coin toss program that randomly tells the user "Heads" or "Tails"'''
# imprort the random module
import random
# using the randint fnc assign a random number from 0 and 1 to variable 'ranum'
ranum = random.randint(0, 1)
# using if statement show the user Heads or Tail depending on 'ranum'
if ranum == 1:
    print("Heads")
else:
    print("Tails")

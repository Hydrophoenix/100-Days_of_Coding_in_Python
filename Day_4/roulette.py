'''A program that selects a random name from a list'''
import random
# ask the user to input names of friends seperated by commas and assign to variable 'friends'
# using the split function, turn the string to a list
friends = input("Type the names of your friends seperated by commas \n").split(',')
# using the len() fnc, get the length of list items
COUNT = len(friends) - 1
# use the randint fnc to generate a random number and use it to display a random name
ranum = random.randint(0, COUNT)
print(f"{friends[ranum]} is going to buy the meal today!")

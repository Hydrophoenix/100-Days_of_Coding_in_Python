'''This program tells you if an inputed number is even or odd'''
# Ask for the number to be checked and convert the str to int
user_num = int(input("Type your number here: "))
# Using the modulus, check if number is even or odd and display result
if user_num % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

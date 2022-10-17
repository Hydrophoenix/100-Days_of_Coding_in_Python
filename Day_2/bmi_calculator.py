'''Write s program that calculates the Body Mass Index
from a user's weight and height.
The BMI is calculated by dividing the weight (in Kg)
by the square of the height (in m) of the user
NB Final result should be in whole number'''

# Ask the user to imput their:
# name
username = input("Type in your name please: ")
# weight
user_weight = float(input("Type in your weight in kilogram (Kg): "))
# height
user_height = float(input("Type in your height in meters (m): "))

# Calculate the BMI
user_BMI = user_weight / user_height**2

# Display the result to the user using the round function
print(f"{username} your BMI is {round(user_BMI, 2)}")

# // is used to give the whole number of a division
# % is used to give the remainder of a division exercise

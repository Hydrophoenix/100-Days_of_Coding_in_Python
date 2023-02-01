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
user_BMI = round(user_BMI)
# Display the result to the user using the round function and the interpretation of their BMI
if user_BMI < 18.5:
    print(f"{username}, your BMI is {user_BMI}, you are underweight")
elif user_BMI <= 24.99:
    print(f"{username}, your BMI is {user_BMI}, you have a normal weight")
elif user_BMI <= 29.99:
    print(f"{username}, your BMI is {user_BMI}, you are sligthly overweight")
elif user_BMI <= 34.99:
    print(f"{username}, your BMI is {user_BMI}, you are obese")
else:
    print(f"{username}, your BMI is {user_BMI}, you are clinically obese")

# // is used to give the whole number of a division
# % is used to give the remainder of a division exercise
# The round fnc is used to round up a decimal

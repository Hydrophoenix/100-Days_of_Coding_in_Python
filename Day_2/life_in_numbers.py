'''Create a program using maths and f-strings thatb tells
us how many days, weeks, months we have left if we live
until 100years'''

# Get the users current age
cur_age = int(input("Please input your current age (please ensure it is whole number): "))
# Subtract the currect age from 100
age_remaining = 100 - cur_age
# Calculate how many days is left to get to 100years
days_left = age_remaining * 365
# Calculate how many weeks is left to get to 100years
weeks_left = age_remaining * 52
# Calculate how many months is left to get to 100years
months_left = age_remaining * 12
# Display the days, weeks and months left
message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left."
print(message)

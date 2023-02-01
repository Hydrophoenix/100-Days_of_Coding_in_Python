'''Create a program that calculates the total bill
including a predetermined tip and splits it amongst
the number of participants'''

# Welcome the user
print("Welcome to the Tip Calculator")
# ask for the total bill
bill = float(input("Please type in the total bill:N"))
# ask for the % tip which should be either 10, 12 or 15
percent_tip = int(input("How much tip would you like to give (10, 12 or 15)?: "))
# ask for the total number of participants
members = int(input("How many people would be splitting the bill?: "))
# Do the calculation each participant would pay from the total bill
tip = percent_tip / 100 * bill # determining the actual tip
total_bill = tip + bill # getting the total bill
members_bill = total_bill / members # getting each participant bill
MEMBERS_BILL = "{:0.2f}".format(members_bill) # rounding the bill to 2 d.p

# Display the result
message = f"Each person would pay {MEMBERS_BILL}"
print(message)

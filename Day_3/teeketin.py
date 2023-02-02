'''This program is to give a ticket to a custiomer after some conditions has been met'''
# Welcome msg
BILL = 0
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm: "))
if height >= 120:
    print("You can ride in the rollercoaster")
    age = int(input("Type in your age: "))
    if age < 12:
        BILL = 5
    elif age <= 18:
        BILL = 7
    elif age >= 45 and age <= 55:
        BILL = 0
    else:
        BILL = 12
    want_photo = input("Do you want a poto taken? Y or N: ")
    if want_photo == "Y" or want_photo == "y":
    # add #3 to their bill
        BILL += 3
        print(f"Your final bill is #{BILL}")
    else:
        print(BILL)
else:
    print("Sorry you have to grow taller to ride")

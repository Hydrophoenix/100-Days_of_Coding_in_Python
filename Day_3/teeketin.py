'''This program is to give a ticket to a custiomer after some conditions has been met'''
# Welcome msg
BILL = 0
print("Welcome to the rollercoaster")
height = int(print("What is your height in cm: "))
if height >= 120:
    print("You can ride in the rollercoaster")
    age = int(print("Type in your age: "))
    if age < 12:
        BILL = 5
        print("Please pay #5")
    elif age <= 18:
        BILL = 7
        print("Please pay #7")
    else:
        BILL = 12
        print("Please pay #12")
    want_photo = input("Do you want a poto taken? Y or N: ")
    if want_photo == "Y":
        # add #3 to their bill
        BILL += 3
    print(f"Your final bill is #{BILL}")
else:
    print("Sorry you have to grow taller to ride")

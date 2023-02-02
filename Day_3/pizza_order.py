'''Build an automatic pizza order program. Based on the user's order, work out their final bill
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: +$1'''
BILL = 0
print("Welcome to FUN Pizza Place")
customer_name = input("Kindly type in your name: ")
customer_choice = input("What size of pizza do you want (Type S, M or L): ")
if customer_choice == "s" or customer_choice == "S":
    BILL += 15
    pepperoni = input("Would you love pepperoni? (Y or N) ")
    if pepperoni == "y" or pepperoni == "Y":
        BILL += 2
elif customer_choice == "m" or customer_choice == "M":
    BILL += 20
    pepperoni = input("Would you love pepperoni? (Y or N) ")
    if pepperoni == "y" or pepperoni == "Y":
        BILL += 3
elif customer_choice == "l" or customer_choice == "L":
    BILL += 25
    pepperoni = input("Would you love pepperoni? (Y or N) ")
    if pepperoni == "y" or pepperoni == "Y":
        BILL += 3
else:
    print("Kindly type in the correct response")
want_cheese = input("Would you love extra cheese? Y or N: ")
if want_cheese == "y" or want_cheese == "Y":
    BILL += 1
    print(f"Your total bill is {BILL}")
else:
    print(f"Your total bill is {BILL}")

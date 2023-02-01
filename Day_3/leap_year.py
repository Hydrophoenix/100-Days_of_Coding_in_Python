'''This program tells you if a given year is a leap year or not
To know a leap year, it must meet the following conditions
1. Must be evenly divisible by 4
2. If it is also evenly divisible by 100, it must also be evenly divisible by 400.'''
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")

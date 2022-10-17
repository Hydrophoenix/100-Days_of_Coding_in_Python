'''
Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 8
'''
two_digit_number = input("Type a two digit number: ")

# Using string slicing, pick out each digit and add
result = int(two_digit_number[0]) + int(two_digit_number[1])
print(result)

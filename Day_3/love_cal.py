'''
This program tests the compatibility between two people. It takes both peoples's name and check for the number of times the letters in the word TRUE occurs, then check for the number of times the letters in the word LOVE occurs and finally combine the numbers to make a 2 digit number.
for love scores less than 10 or greater than 90, the message should be "Your score is **x**, you go together like coke and mentos"
For love score between 40 and 50, the message should be "Your score is **y** you are alright together"
Otherwise the message will just be their score "Your score is **z**"
'''
# send out a welcome message
print("Welcome to the Love Calculator")
# Ask user for the full names of the people to be checked & change to lowercase
name_1 = input("Enter your full name: ").lower()
name_2 = input("Enter your partner's full name: ").lower()
name_3 = name_1 + name_2
# Check names, for letters in 'TRUE' and 'LOVE'
T = name_3.count('t')
R = name_3.count('r')
U = name_3.count('u')
L = name_3.count('l')
O = name_3.count('o')
V = name_3.count('v')
E = name_3.count('e')
X = str(T + R + U + E)
Y = str(L + O + V + E)
# Convert numbers found to string and combine both
love_score = int(X + Y)
# Print out the appropriate final message to the user
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")

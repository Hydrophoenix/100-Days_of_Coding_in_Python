'''A program that generates a band name based on some informations you provide it'''

# Create a greating for your program
print("Welcome to the BAND NAME GENERATOR")
print("I can help you with a band name if you provide me some information")
print("If you are ready, lets get started")

# Ask the user for the city that they grew in
user_city = input("Tell me the city you were born in: ")

# Ask the user for the name of a pet
user_pet = input("Tell me your favorite pet's name: ")

# Combine the name of their city and the name of the pet and show them their band name
print(f"Your band name could be {user_city} {user_pet}")

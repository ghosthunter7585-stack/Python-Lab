# This program takes a user's name, age, and city and creates a greeting.

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# The f-string combines all three inputs into one sentence.
print(f"Hello {name}, you are {age} years old and you live in {city}.")
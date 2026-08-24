# This program is a number guessing game.
# The user gets a maximum of 7 attempts to guess a random number from 1 to 100.

import random


secret_number = random.randint(1, 100)
maximum_attempts = 7
attempts = 0
guessed_correctly = False

print("========== NUMBER GUESSING GAME ==========")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.")

while attempts < maximum_attempts:
    guess = int(input("\nEnter your guess: "))

    # Make sure the guess is inside the allowed range.
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess == secret_number:
        guessed_correctly = True
        print("Correct! You guessed the number!")
        print("Number of attempts:", attempts)
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    print("Attempts remaining:", maximum_attempts - attempts)


if not guessed_correctly:
    print("\nYou ran out of attempts.")
    print("The correct number was:", secret_number)
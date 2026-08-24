# This program combines the previous programs into one menu-driven application.
# The user can select an option and continue using the program until choosing Exit.


def is_armstrong(number):
    digits = len(str(number))
    original_number = number
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    return total == original_number


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def is_perfect(number):
    if number <= 1:
        return False

    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    return divisor_sum == number


def is_number_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original_number == reversed_number


def fibonacci(n):
    first = 0
    second = 1

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second


def print_patterns(n):
    print("\nRight-Aligned Triangle:")

    for row in range(1, n + 1):
        # Spaces are used to move the stars to the right.
        for space in range(n - row):
            print(" ", end="")

        for star in range(row):
            print("*", end="")

        print()

    print("\nNumber Pattern:")

    for row in range(1, n + 1):
        for number in range(1, row + 1):
            print(number, end="")
        print()

    print("\nSimple Pyramid:")

    for row in range(1, n + 1):
        for space in range(n - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


while True:
    print("\n========== MENU ==========")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a positive number: "))

        if number < 0:
            print("Invalid input. Number must be positive.")
        elif is_armstrong(number):
            print(number, "is an Armstrong number.")
        else:
            print(number, "is not an Armstrong number.")

    elif choice == "2":
        number = int(input("Enter a positive number: "))

        if number < 1:
            print("Invalid input. Number must be positive.")
        elif is_prime(number):
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")

    elif choice == "3":
        number = int(input("Enter a positive number: "))

        if number < 1:
            print("Invalid input. Number must be positive.")
        elif is_perfect(number):
            print(number, "is a perfect number.")
        else:
            print(number, "is not a perfect number.")

    elif choice == "4":
        number = int(input("Enter a positive number: "))

        if number < 1:
            print("Invalid input. Number must be positive.")
        elif is_number_palindrome(number):
            print(number, "is a palindrome.")
        else:
            print(number, "is not a palindrome.")

    elif choice == "5":
        n = int(input("Enter the number of Fibonacci terms: "))

        if n < 1:
            print("Invalid input. Number must be positive.")
        else:
            print("Fibonacci series:")
            fibonacci(n)
            print()

    elif choice == "6":
        n = int(input("Enter the number of rows: "))

        if n < 1:
            print("Invalid input. Number must be positive.")
        else:
            print_patterns(n)

    elif choice == "7":
        print("Program ended. Goodbye!")
        break

    else:
        # Invalid choices are handled without crashing the program.
        print("Invalid menu choice. Please select a number from 1 to 7.")
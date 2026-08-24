# This program checks whether a number is a palindrome using arithmetic.
# It also provides a second version that checks a string palindrome.


def is_number_palindrome(number):
    original_number = number
    reversed_number = 0

    # Reverse the number using arithmetic operations only.
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original_number == reversed_number


number = int(input("Enter a positive number: "))

while number < 1:
    print("Please enter a positive number.")
    number = int(input("Enter a positive number: "))

if is_number_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")


def is_string_palindrome(text):
    # Compare the string with its reversed version.
    return text == text[::-1]


text = input("\nEnter a string: ")

if is_string_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# This program checks whether a number is an Armstrong number.
# It also prints all Armstrong numbers within a user-given range.


def is_armstrong(number):
    digits = len(str(number))
    original_number = number
    total = 0

    while number > 0:
        digit = number % 10

        # Raise each digit to the power of the number of digits.
        total += digit ** digits
        number //= 10

    return total == original_number


number = int(input("Enter a positive number: "))

while number < 0:
    print("Please enter a positive number.")
    number = int(input("Enter a positive number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


start = int(input("\nEnter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))

while start < 0 or end < 0 or start > end:
    print("Invalid range.")
    start = int(input("Enter the starting value: "))
    end = int(input("Enter the ending value: "))

print("Armstrong numbers in the range:")

for value in range(start, end + 1):
    if is_armstrong(value):
        print(value, end=" ")
# This program checks whether a number is a perfect number.
# It also prints all perfect numbers up to a user-given limit.


def is_perfect(number):
    if number <= 1:
        return False

    divisor_sum = 0

    # Add all proper divisors of the number.
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    return divisor_sum == number


number = int(input("Enter a positive number: "))

while number < 1:
    print("Please enter a positive number.")
    number = int(input("Enter a positive number: "))

if is_perfect(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")


limit = int(input("\nEnter the limit: "))

while limit < 1:
    print("Please enter a positive limit.")
    limit = int(input("Enter the limit: "))

print("Perfect numbers up to", limit, ":")

for value in range(1, limit + 1):
    if is_perfect(value):
        print(value, end=" ")
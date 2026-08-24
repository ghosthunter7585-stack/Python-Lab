# This program checks whether a number is prime.
# It also prints all prime numbers up to a user-given limit.


def is_prime(number):
    if number < 2:
        return False

    # Only divisors up to the square root need to be checked.
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


number = int(input("Enter a positive number: "))

while number < 1:
    print("Please enter a positive number.")
    number = int(input("Enter a positive number: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


limit = int(input("\nEnter the limit: "))

while limit < 1:
    print("Please enter a positive limit.")
    limit = int(input("Enter the limit: "))

print("Prime numbers up to", limit, ":")

for value in range(2, limit + 1):
    if is_prime(value):
        print(value, end=" ")
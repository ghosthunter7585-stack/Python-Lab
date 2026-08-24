# This program prints three different star and number patterns.
# Nested loops are used to control rows, stars, numbers, and spaces.


n = int(input("Enter the number of rows: "))

while n < 1:
    print("Please enter a positive number.")
    n = int(input("Enter the number of rows: "))


# Pattern 1: Right-aligned triangle of stars
print("\n1. Right-Aligned Triangle")

for row in range(1, n + 1):
    # Print spaces before the stars to align the triangle to the right.
    for space in range(n - row):
        print(" ", end="")

    for star in range(row):
        print("*", end="")

    print()


# Pattern 2: Number pattern
print("\n2. Number Pattern")

for row in range(1, n + 1):
    for number in range(1, row + 1):
        print(number, end="")

    print()


# Pattern 3: Simple pyramid with centered spaces
print("\n3. Simple Pyramid")

for row in range(1, n + 1):
    # Print spaces before the stars to center the pyramid.
    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
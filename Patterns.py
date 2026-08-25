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


# Pattern 4: Hollow Diamond 
n = int(input("Enter an odd number: "))

mid = n // 2

for i in range(n):
    if i <= mid:
        stars = i
    else:
        stars = n - i - 1

    spaces = mid - stars

    print(" " * spaces, end="")

    if stars == 0:
        print("*")
    else:
        print("*" + " " * (2 * stars - 1) + "*")


#Pattern 5: Butterfly Pattern
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    spaces = 2 * (n - i)

    print("*" * i, end="")
    print(" " * spaces, end="")
    print("*" * i)

for i in range(n - 1, 0, -1):
    spaces = 2 * (n - i)

    print("*" * i, end="")
    print(" " * spaces, end="")
    print("*" * i)

#Pattern 6: Star Pattern
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

#Pattern 7: Matrix Operations 
matrix = []

print("Enter the elements of the 3 x 3 matrix:")

for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# Display the matrix
print("\nMatrix:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# Sum of all elements
total_sum = 0

for i in range(3):
    for j in range(3):
        total_sum += matrix[i][j]

print("\nSum of all elements:", total_sum)

# Sum of main diagonal
diagonal_sum = 0

for i in range(3):
    diagonal_sum += matrix[i][i]

print("Sum of main diagonal:", diagonal_sum)

# Largest and smallest element
largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest element:", largest)
print("Smallest element:", smallest)

# Transpose
print("\nTranspose:")
for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print() 
# This program prints the Fibonacci series using a loop.
# It also prints the series using recursion and compares function calls.


def fibonacci_loop(n):
    series = []
    first = 0
    second = 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series


recursive_calls = 0


def fibonacci_recursive(n):
    global recursive_calls
    recursive_calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def recursive_series(n):
    series = []

    for i in range(n):
        series.append(fibonacci_recursive(i))

    return series


n = int(input("Enter the number of terms: "))

while n < 1:
    print("Please enter a positive number.")
    n = int(input("Enter the number of terms: "))


loop_series = fibonacci_loop(n)

print("\nFibonacci series using loop:")
print(*loop_series)


recursive_calls = 0
recursive_result = recursive_series(n)

print("\nFibonacci series using recursion:")
print(*recursive_result)

print("\nNumber of recursive function calls:", recursive_calls)
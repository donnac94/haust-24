# Get the number of Fibonacci numbers to generate
n = int(input("How many Fibonacci numbers: "))

# Initialize the first two Fibonacci numbers
fib_0 = 0
fib_1 = 1

# Print the first number
print(f"0: {fib_0}")

# Handle case when n is more than 1
if n > 1:
    print(f"1: {fib_1}")

# Generate and print the rest of the Fibonacci sequence
for i in range(2, n):
    fib_next = fib_0 + fib_1
    print(f"{i}: {fib_next}")
    fib_0 = fib_1  # Move to the next number in the sequence
    fib_1 = fib_next
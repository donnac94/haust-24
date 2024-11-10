number = int(input("Input a number: "))

# We only need to check number//2 + 1, because there is no number higher than half the number that could possibly divide the number
for i in range(2, number//2 + 1):
    # If it divides, we print
    if number%i == 0:
        print(i)
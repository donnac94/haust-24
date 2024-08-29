
n = int(input("Enter a positive integer: "))

# Leid 1
i = 2 # Start at 2 because multiplying by 1 is not neccesary
factorial = 1 # This stores our result
while i <= n:
    factorial = factorial * i # 1 * 2 * 3 * 4 * 5
    i += 1 # Iterate the loop, increment i
print(factorial)

# Leid 2
i = 5 # Lets start from the other end
factorial = 1
while i > 1: # Notice how the guard is different here!
    factorial = factorial * i # 5 * 4 * 3 * 2 
    i -= 1 # Iterate the loop, decrement i

print(factorial)
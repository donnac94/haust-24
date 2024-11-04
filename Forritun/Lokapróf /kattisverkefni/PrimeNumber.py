# Read the input number
n = int(input(""))

# Check if n is prime
if n <= 1: # 0 and 1 are not prime numbers
    print("not prime") 
else: # Check if n is divisible by any number from 2 to sqrt(n)
    is_prime = True  # Assume n is prime unless proven otherwise
    for i in range(2, int(n ** 0.5) + 1): # Check all numbers from 2 to sqrt(n)
        if n % i == 0: # If n is divisible by i
            is_prime = False  # Found a divisor, n is not prime 
            break # No need to check further

    # Print the result based on the is_prime flag
    if is_prime: # If n is prime
        print("prime") 
    else:
        print("not prime")
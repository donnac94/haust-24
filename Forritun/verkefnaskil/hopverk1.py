def digit_sum(x):
    """Returns the digit sum of a number x."""
    return sum(int(d) for d in str(x))

def main():
    # Part 1: Check divisors
    while True:
        inp = input().strip()
        if inp.lower() == 'q':
            break
        num = int(inp)
        divisors = sum(1 for i in range(1, num + 1) if num % i == 0)
        print("yes" if divisors >= 10 else "no")
    
    # Part 2: Digit sum conditions
    n = int(input().strip())
    
    results = []
    
    # Check two-digit numbers up to and including n
    for x in range(10, min(n + 1, 100)):  # Only consider two-digit numbers
        if digit_sum(x) ** 2 == n:
            results.append(x)
    
    # Check three-digit numbers up to and including n
    for x in range(100, min(n + 1, 1000)):  # Only consider three-digit numbers
        if digit_sum(x) ** 3 == n:
            results.append(x)
    
    # Print results in ascending order
    if results:
        for number in sorted(results):
            print(number)
    else:
        print("No numbers found matching the criteria")

if __name__ == "__main__":
    main()
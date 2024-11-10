n = int(input())  # Number of elements in the list
numer = list(map(int, input().split()))  # List of numbers

numer.sort()

third = n // 3

# Slice the list into three parts: center, first, and last
first_third = numer[:third]
center_third = numer[third:2*third]
last_third = numer[2*third:]

# Rearrange them: center + first + last
result = center_third + first_third + last_third

# Print the rearranged list
print(" ".join(map(str, result)))
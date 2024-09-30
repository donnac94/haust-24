n = int(input())  # Number of elements in the list
numer = [int(x) for x in input().split()]  # List of numbers without using map

third = n // 3

# Slice the list into three parts: center, first, and last
first_third = numer[:third]
center_third = numer[third:2*third]
last_third = numer[2*third:]

# Rearrange them: center + first + last
result = center_third + first_third + last_third

# Print the rearranged list without using map
print(" ".join(str(x) for x in result))
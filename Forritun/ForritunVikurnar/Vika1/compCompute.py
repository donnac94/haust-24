import math

# Input: Four lines of integers
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output the distance with precision up to 10^-9
print(f"{distance:.9f}")
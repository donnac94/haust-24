import math

# Input: the roof's angle in degrees
d = int(input())

# Length of the plywood
length = 50  # in cm

# Calculate the height of the second piece of wood
height = length * math.tan(math.radians(d))

# Output the height rounded to 1 decimal place
print(f"{height:.1f}")
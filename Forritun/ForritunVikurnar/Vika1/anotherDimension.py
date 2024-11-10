import math

# Input: the diameter of the sphere
d = float(input())

# Calculate the radius
r = d / 2

# Calculate the volume of the hemisphere
volume = (2/3) * math.pi * (r ** 3)

# Output the volume with precision to ensure an absolute or relative error of at most 10^-9
print(f"{volume:.9f}")
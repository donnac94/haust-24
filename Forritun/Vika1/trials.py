#trials 
import math

# Input: lengths of the sides of the triangle
a = int(input())
b = int(input())
c = int(input())

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Output the area with precision to handle an absolute or relative error of at most 10^-9
print(f"{area:.9f}")
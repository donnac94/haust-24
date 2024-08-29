# Input the values of a, b, c
a = int(input())
b = int(input())
c = int(input())

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Determine the number of real roots
if discriminant > 0:
    print(2)  # Two distinct real roots
elif discriminant == 0:
    print(1)  # One real root (repeated root)
else:
    print(0)  # No real roots
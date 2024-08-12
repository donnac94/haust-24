import math

x = float(input("Enter in side x: "))
y = float(input("Enter in side y: "))

# This is Pythagoras Theorem
z = math.sqrt((x**2) + (y**2))

# Round so we only display at most 2 extra decimal places
z = round(z, 2)

print(f"z = {z}")
print(f"{z = }")
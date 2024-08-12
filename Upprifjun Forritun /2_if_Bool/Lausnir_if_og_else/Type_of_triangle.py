# Solution

a = float(input("Enter in the one side of the triangle: "))
b = float(input("Enter in the second side of the triangle: "))
c = float(input("Enter in the third side of the triangle: "))

# remember, if a == b and b == c, then a == c
if ((a == b) and (b == c)):
    print("Jafnhliða þríhyrningur")
elif (a == b) or (a == c) or (b == c):
    # If any two sides of the triangles are equal
    print("Jafnarma þríhyrningur")
else:
    # The final case, where all are different
    print("Venjulegur þríhyrningur")
    
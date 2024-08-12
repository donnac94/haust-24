a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# We only need to calculate d for the number of roots
d = b**2 - 4 * a * c

if d > 0:
    print("The equation has 2 roots")
elif d == 0:
    print("The equation has 1 root")
else:
    print("The equation has 0 roots")

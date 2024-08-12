height = float(input("How tall are you in cm: "))

# Check if height is lower or equal to 0
if height <= 0:
    print("Invalid height!")
elif height < 140:
    # check if heigh is below 140 cm
    print("You are not tall enough for the rollercoaster")
else:
    # Catches all other cases, i.e. user is higher or equal to 140cm
    print("You are tall enough for the rollercoaster")



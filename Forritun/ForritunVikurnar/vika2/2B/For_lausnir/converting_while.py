start = int(input("Where to start the range?: ")) # Do not remove this line
end = int(input("Where to stop the range?: ")) # Do not remove this line
increment = int(input("Whats the increment?: ")) # Do not remove this line
# Rewrite the while loop below into a for loop
i = start
while i < end:
    print(i, end=", ")
    i += increment

print()

# Notice the simularities
for i in range(start, end, increment):
    print(i, end=", ")























def validate_name(name):
    return bool


def get_user_name():
    while True:
        # Input
        name = input("Enter in name")
        # Validation
        if validate_name(name):
            return name
        # Error handle
        print("Invalid input, try again")



user = get_user_name()
# username is valid

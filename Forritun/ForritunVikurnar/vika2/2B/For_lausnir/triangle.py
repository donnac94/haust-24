
# Leid 1
for i in range(1, 6): # i: [1-5]
    for j in range(0, i):
        print("*", end="")
    print() # This is so we print a new line, see what happens if you remove this

# Leid 2
for i in range(1, 6):
    print("*" * i) # Only one for loop!!
stop = int(input("Enter in a positive number: "))

i = 1
while i**2 <= stop: # Note how we have to check i**2
    print(i**2) # Prints 1**2 then 2**2 then 3**2 and so forth
    i += 1 # Increment
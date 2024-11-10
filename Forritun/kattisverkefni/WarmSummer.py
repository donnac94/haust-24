# This program  doubles a number given by the user, and asks if the user wants to double more numbers.


while True:
    # Ask if the user wants to start doubling
    answer = input("You need something doubled? (Y)es? ")
    if answer.lower() != 'y':
        break  # Exit if the answer is not 'Y' or 'y'
    
    # Ask for a number to double
    number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
    doubled = number * 2
    
    # Print the doubled value with precision up to 6 decimal places
    print(f"{doubled:.6f}")
    
    # Ask if the user wants to continue, without resetting the original loop
    while True: # Loop until the user doesn't want to double more
        answer = input("You need something else doubled? (Y)es? ")
        if answer.lower() == 'y':
            # If the user wants to double more, continue the original logic
            number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
            doubled = number * 2
            print(f"{doubled:.6f}")
        else: 
            # Exit the loop and program if the user doesn't want to continue
            exit()
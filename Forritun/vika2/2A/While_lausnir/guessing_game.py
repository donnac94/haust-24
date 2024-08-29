import random
random_number = random.randint(1, 100) # In the range 1-100

while True:
    number = int(input("Enter in a number: "))
    if number < random_number:
        # User needs to guess a higher number
        print("The number is higher")
    elif number > random_number:
        # User needs to guess a lwoer number
        print("The number is lower")
    else:
        # If it is not lower nor larger, it must be the same!
        print(f"You are correct, the number was {random_number}!")
        break # Because it's a while True loop



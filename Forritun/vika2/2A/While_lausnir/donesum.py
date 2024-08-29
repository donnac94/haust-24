summan = 0
user_number = input("Enter a number (or 'done'): ")

while user_number != 'done':    
    # Logic fyrir summu
    user_number = int(user_number)
    summan += user_number
    user_number = input("Enter a number (or 'done'): ")

print(f"The sum is {summan}")
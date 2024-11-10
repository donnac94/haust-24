while True:
    answer = input("You need something doubled? (Y)es? ")
    if answer != 'Y' and answer != 'Yes':
    
    number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
    doubled_number = number * 2
    print(f"{doubled_number:.6f}")
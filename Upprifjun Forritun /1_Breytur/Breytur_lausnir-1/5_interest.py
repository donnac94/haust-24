money = int(input("Enter in initial amount: "))
interest = float(input("Enter in interest in %: "))
years = int(input("Enter in years: "))


# Converting % interest to a float number

# i.e. 6% -> 1.06
interest = interest/100 + 1

# The equation
result = money*(interest**years)

print(f"Your investment in {years} years will be {result}kr")
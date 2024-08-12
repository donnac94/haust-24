import math

money = int(input("Enter initial amount: "))
interest = float(input("Enter in interest in % : "))
years = int(input("Enter in years: "))

interest = interest/100 + 1

result = money * (interest ** years)

print(f"Your investment in {years} years will be {result} kr")
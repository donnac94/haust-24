number = int(input("sláðu inn númer: "))

sum_of_digits = 0 

number_str = str(number)

for i in range(len(number_str)):
  sum_of_digits += int(number_str[i])
  
print(f"Summa talnanna er {sum_of_digits}")


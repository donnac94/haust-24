number = int(input("Enter in a number: "))

fizz_buzz_str = ""

if number % 2 == 0:
    fizz_buzz_str += "Fizz"
if number % 3 == 0:
    fizz_buzz_str += "Buzz"

if fizz_buzz_str == "":
    print(number)
else:
    print(fizz_buzz_str)

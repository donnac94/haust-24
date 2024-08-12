number = int(input("Enter in a number: "))

# Leið 1
# We will store the final result in this variable
fizz_buzz_str = ""

if number % 2 == 0:
    fizz_buzz_str += "Fizz"
if number % 3 == 0:
    fizz_buzz_str += "Buzz"

# This case is when the number is neither divisable by 2 nor 3
if fizz_buzz_str == "":
    print(number)
else:
    print(fizz_buzz_str)

    
# Leið 2
if number % 2 == 0:
    print("Fizz", end="") # end="" removes the newline at the end of print!
if number % 3 == 0:
    print("Buzz")

if number % 2 != 0 and number % 3 != 0:
    print(number)
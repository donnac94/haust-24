# Input = 12345
# Output = 15 (the sum of the integer) 


# Use: 
# 1. list comprehension
# 2. f-strings

# Additional tasks: 
# 1. take input form Users


number_input = int(input("Enter a number: "))

str_number = str(number_input) # Convert the number to a string

sum_of_digits = sum([int(digit) for digit in str_number]) # list comprehension 

print(f"The sum of the digits of the number {number_input} is {sum_of_digits}") # f-string


  


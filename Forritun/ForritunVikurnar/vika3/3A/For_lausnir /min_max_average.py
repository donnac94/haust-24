
num_of_numbers = int(input("How many numbers do you want to type in?: "))

# When the user has input no numbers, the min and max are nothing, so we assign them as None, which represents the absence of a value
min_num = None
max_num = None
sum_num = 0 # Lets store our sum, to later calculate the average
for i in range(num_of_numbers):
    number = int(input("Enter in a number: "))
    # If min_num is None, then max_num is also None and we can assume the user has not input any numbers, so the first number must be the max and the min!
    if min_num == None:
        min_num = number
        max_num = number
    # Else we have to check whether the number is the lowest/highest so far
    elif number < min_num:
        min_num = number
    elif number > max_num:
        max_num = number
        
    sum_num += number

# Average is the sum of values divided by the number of total input (which the user conveniently inputs in the begining)
avg = sum_num/num_of_numbers

print(f"The max number is {max_num}, the min number is {min_num} and the average is {avg}")

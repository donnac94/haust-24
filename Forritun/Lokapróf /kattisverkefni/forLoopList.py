# ask user for 5 number inputs 

numbers = [int(input("Enter a number: ")) for i in range(5)] # list comprehension

sum_of_numbers = sum(numbers) # sum the numbers

average = sum_of_numbers / len(numbers) # calculate the average of the numbers

print(numbers) # print the list of numbers
print(f"The sum of the numbers is {sum_of_numbers}") # print the sum of the numbers
print(f"The average of the numbers is {average}") # print the average of the numbersß
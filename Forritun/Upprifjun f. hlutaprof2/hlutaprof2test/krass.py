total = 0 # inital value of total

while True: # While this statement is true
    n = int(input()) # input a number
    if n == 10: # if the number is 10
        break # break the loop
    total += n # add the number to the total
    
print(total) # print the total

# The code reads numbers from the user until the number 10 is entered. The sum of all numbers entered before 10 is then printed.
"""
Write a program that implements 
multiplication by using addition and a loop

input: 
consists of two lines 
first line - contains the first integer x, where 0 <= x <= 10**6
second line - contains the second integer y, where 0 <= y <= 10**6
"""

# Step 1: Read the inputs
first = int(input(""))
second = int(input(""))

# Step 2: Initialize the result
result = 0 # inital value of result

# Step 3: Use a loop to add x to itself y times
for _ in range(second): # Loop y times
    result += first # Add x to the result y times

# Step 4: Print the result
print(result)
    
    
    

# Write a Python function divide_numbers(a, b) that takes two numbers and returns their division.
# Use exception handling to catch any ZeroDivisionError and print “Cannot divide by zero.”

# Function to divide two numbers
def divide_numbers(a, b): # Function to divide two numbers
    try: # Try to divide the numbers
        return a / b # Return the result
    except ZeroDivisionError: # Catch ZeroDivisionError
        return "Cannot divide by zero." # Return error message

# Example usage
a = float(input("Enter the numerator: ")) # Get the numerator
b = float(input("Enter the denominator: ")) # Get the denominator
print("Result:", divide_numbers(a, b)) #    Print the result

# Input: temperature in degrees Fahrenheit
f = int(input())

# Convert Fahrenheit to Celsius
c = (5 / 9) * (f - 32)

# Round the result to the nearest integer
c_rounded = round(c)

# Output the result
print(c_rounded)
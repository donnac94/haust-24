# Input: the number of improvements and improvements per year
n = int(input())
k = int(input())

# Calculate the number of years that have passed
years_passed = n // k

# Determine the current year
current_year = 2022 + years_passed

# Output the current year
print(current_year)
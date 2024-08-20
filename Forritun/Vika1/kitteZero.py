# Input: reproduction number R_0
R_0 = float(input())

# Calculate the total number of cases
total_cases = 1 + R_0 + (R_0 ** 2) + (R_0 ** 3)

# Round the result to the nearest integer
total_cases_rounded = round(total_cases)

# Output the total number of cases
print(total_cases_rounded)
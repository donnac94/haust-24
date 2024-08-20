# Input: the total number of seconds
s = int(input())

# Calculate the number of hours
hours = s // 3600

# Calculate the remaining seconds after converting to hours
remaining_seconds = s % 3600

# Calculate the number of minutes from the remaining seconds
minutes = remaining_seconds // 60

# Calculate the remaining seconds after converting to minutes
seconds = remaining_seconds % 60

# Output the result in the format "hours : minutes : seconds"
print(f"{hours} : {minutes} : {seconds}")
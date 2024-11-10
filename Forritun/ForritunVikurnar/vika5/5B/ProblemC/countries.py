# Open the file and read the lines
with open('/Users/donnac/Desktop/haust24/Forritun/vika5/5B/ProblemC/countries2.py', 'r') as file:
    countries = file.read().splitlines()

# Input the suffix from the user
suffix = input().strip()

# Find countries that end with the given suffix
matching_countries = [country for country in countries if country.endswith(suffix)]

# Output each matching country
for country in matching_countries:
    print(country)

# Output the total count of matching countries
print(f"{len(matching_countries)} countries with suffix {suffix} in total.")
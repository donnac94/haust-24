# Input: the length of the road in football fields
n = int(input())

# Conversion factor from football fields to kilometers
conversion_factor = 0.09144

# Calculate the length of the road in kilometers
kilometers = n * conversion_factor

# Output the length in kilometers with precision to ensure an absolute error less than 10^-5
print(f"{kilometers:.5f}")
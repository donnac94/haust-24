
# 1. list comprehension
# 2. f-strings

numbers = [10, 11, 12, 13 ,14, 15, 16, 17, 18, 19]

filtered_list = [num for num in numbers if num % 2 == 0] # list comprehension

print(f"Even numbers: {filtered_list}") # f-string

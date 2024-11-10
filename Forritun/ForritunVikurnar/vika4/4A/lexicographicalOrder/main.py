from alphabeticalOrder import precedes

first = input("Give me a string: ")
second = input("Give me another string: ")

result = precedes(first, second)

print(f"The string '{result}' has alphabetical precedence.")
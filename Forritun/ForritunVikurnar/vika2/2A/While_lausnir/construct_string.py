
result_str = "" # Lets store our result in this string
while True:
    character = input("Enter a character (or 'done' to exit): ")
    # First check if the user wants to exit
    if character == 'done':
        print(result_str)
        break
    # Only add to the string if it is a single character input
    if len(character) == 1:
        result_str += character
    else:
        # User input something that was not one character!
        print("Input must be one character") 
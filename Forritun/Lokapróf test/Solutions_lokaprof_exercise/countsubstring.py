
def count_substring(mainstring, substring): 
    """ Returns the number of times the substring occurs in the mainstring.
    The function compares the substring to the mainstring character by character.
    If the characters match, the function increments the inner_index.
    If the inner_index is equal to the length of the substring, the function increments the counter.
    The function returns the counter.
    
    param mainstring: str - the string to search in.
    param substring: str - the string to search for.
    return: int - the number of times the substring occurs in the mainstring.
    """
    
    counter = 0 # Initialize the counter to 0
    
    # Iterate through the mainstring
    for i in range(len(mainstring)): 
        inner_index = 0 # Initialize the inner_index to 0
        
        # While the inner_index is less than the length of the mainstring, the inner_index is less than the length of the substring,
        while (i + inner_index < len(mainstring) # the mainstring index is less than the length of the mainstring
               and inner_index < len(substring) # the inner_index is less than the length of the substring
               and mainstring[i + inner_index] == substring[inner_index]): # the mainstring index is equal to the substring index
            inner_index += 1 # Increment the inner_index
            
            # If the inner_index is equal to the length of the substring, increment the counter
            if inner_index == len(substring): 
                counter += 1
                
    return counter # Return the counter

"""
The function count_substring takes two strings as input, mainstring and substring.
The function initializes a counter to 0.
The function iterates through the mainstring.
The function initializes an inner_index to 0.
The function iterates through the mainstring and substring.
The function increments the inner_index if the characters match.
The function increments the counter if the inner_index is equal to the length of the substring.
The function returns the counter.

param mainstring: str - the string to search in.
param substring: str - the string to search for.
return: int - the number of times the substring occurs in the mainstring.
"""
if __name__ == "__main__":
    choice = "" # Initialize the choice to an empty string
    
    # While the choice is not equal to 'q', prompt the user to enter 's' to count substrings or 'q' to quit.
    while choice != "q": # While the choice is not equal to 'q'
        choice = input("Enter 's' to count substrings or 'q' to quit: ") # Prompt the user to enter 's' to count substrings or 'q' to quit
        # If the choice is equal to 's', prompt the user to enter the mainstring and substring.
        if choice == "s": 
            mainstring = input("Enter main string: ")
            substring = input("Enter substring: ")
            
            # Print the number of times the substring occurs in the mainstring.
            print("The string", substring, "occurs", count_substring(mainstring, substring), "times in the string", mainstring) 
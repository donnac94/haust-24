from storednumbers import StoredNumber

# Create a class called ManyStoredNumbers. This class should have
# an attribute called number_list which is a list. The class should
# have a method called add_stored_number which takes a StoredNumber
# object as a parameter and appends it to the number_list. The class
# should also have a __str__ method which returns a string representation
# of the ManyStoredNumbers object. The string should contain the string
# representation of each StoredNumber object in the number_list, separated
# by a newline character. The string should start with the text "These are the numbers:".
class ManyStoredNumbers:
    def __init__(self): # Initialize the number_list to an empty list
        self.number_list = [] 

    def add_stored_number(self, st_num): # Append the StoredNumber object to the number_list
        self.number_list.append(st_num) 

    def __str__(self): # Return a string representation of the ManyStoredNumbers object
        ret_val = "These are the numbers:\n" # Initialize the return value to "These are the numbers:\n"
        for number in self.number_list: # Iterate through the number_list
            ret_val += str(number) + "\n" # Append the string representation of the StoredNumber object to the return value
        return ret_val # Return the return value

# Create an instance of the ManyStoredNumbers class and add some StoredNumber objects to it.
# Print the ManyStoredNumbers object to see the string representation of the object.
# Add another StoredNumber object to the ManyStoredNumbers object and print it again to see the updated string representation.
# The output should look like this:
# These are the numbers:
# the_number: 4.6
# the_number: -3
if __name__ == "__main__":
    many_stored = ManyStoredNumbers() # Create an instance of the ManyStoredNumbers class
    many_stored.add_stored_number(StoredNumber(4.6)) # Add a StoredNumber object to the ManyStoredNumbers object
    many_stored.add_stored_number(StoredNumber(-3)) # Add a StoredNumber object to the ManyStoredNumbers object
    print(many_stored) # Print the ManyStoredNumbers object
    many_stored.add_stored_number(StoredNumber(9.0)) # Add a StoredNumber object to the ManyStoredNumbers object
    print(many_stored) # Print the ManyStoredNumbers object

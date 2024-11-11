""""
The class StoredNumber is a class that stores a number. The class has the following methods:
- __init__(self, the_number): Initializes the StoredNumber object with the given number.
- set_number(self, num): Sets the number of the StoredNumber object to the given number.
- get_number(self): Returns the number stored in the StoredNumber object.
- __str__(self): Returns a string representation of the StoredNumber object.
"""
class StoredNumber:
    def __init__(self, the_number): # Initialize the StoredNumber object with the given number
        self.__the_number = the_number

    def set_number(self, num): # Set the number of the StoredNumber object to the given number
        self.__the_number = num

    def get_number(self): # Return the number stored in the StoredNumber object
        return self.__the_number

    def __str__(self): # Return a string representation of the StoredNumber object
        return f"the_number: {self.__the_number}"

if __name__ == "__main__":
    st_num = StoredNumber(5.0) # Create an instance of the StoredNumber class with the number 5.0
    print(st_num) 
    st_num2 = StoredNumber(1) # Create another instance of the StoredNumber class with the number 1
    print(st_num2)
    st_num2.set_number(3.4) # Set the number of the second StoredNumber object to 3.4
    print(st_num2)
    print(st_num2.get_number()) # Print the number stored in the second StoredNumber object

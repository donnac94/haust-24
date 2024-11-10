
# 1. Create a class called StoredNumber that stores a number in a private variable. The class should have
class StoredNumber: # class to store a number
    def __init__(self, the_number): # constructor for the class
        self.__the_number = the_number # store the number in a private variable

# function to set the number
    def set_number(self, num): # function to set the number
        self.__the_number = num # set the number to the new number

# function to get the number
    def get_number(self): # function to get the number
        return self.__the_number # return the number

# function to return the string representation of the class
    def __str__(self): #    function to return the string representation of the class
        return f"the_number: {self.__the_number}" # return the string representation of the class

# if the script is run
if __name__ == "__main__":
    st_num = StoredNumber(5.0) # create an instance of the class
    print(st_num) # print the string representation of the class

    st_num2 = StoredNumber(1) # create an instance of the class
    print(st_num2) # print the string representation of the class
    
    st_num2.set_number(3.4) # set the number of the instance
    print(st_num2) # print the string representation of the class
    print(st_num2.get_number()) # print the number of the instance

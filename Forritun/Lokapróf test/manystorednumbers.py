from storednumbers import StoredNumber 

# class that stores many stored numbers
class ManyStoredNumbers: # class that stores many stored numbers
    def __init__(self): # constructor for the class
        self.number_list = [] # list to store the stored numbers

# function to add a stored number to the list
    def add_stored_number(self, st_num): # function to add a stored number to the list
        self.number_list.append(st_num) #   add the stored number to the list

# function to return the string representation of the class
    def __str__(self): # function to return the string representation of the class
        ret_val = "These are the numbers:\n" # string to store the return value
        for number in self.number_list: # loop through the list of stored numbers
            ret_val += str(number) + "\n" # add the string representation of the stored number to the return value
        return ret_val # return the return value


# if the script is run
if __name__ == "__main__": # if the script is run
    many_stored = ManyStoredNumbers() # create an instance of the class
    many_stored.add_stored_number(StoredNumber(4.6)) # add a stored number to the list
    many_stored.add_stored_number(StoredNumber(-3)) # add a stored number to the list
    print(many_stored) # print the string representation of the class
    many_stored.add_stored_number(StoredNumber(9.0)) # add a stored number to the list
    print(many_stored) # print the string representation of the class

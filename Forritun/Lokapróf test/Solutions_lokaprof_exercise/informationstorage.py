
length = 0.0
width = 0.0
height = 0.0
mass = 0.0
volume = 0.0


try: # Try to read the values from the file
    file_reader = open("info_file.txt", "r") # Open the file for reading
    file_string = file_reader.readline() # Read the first line of the file
    file_values = file_string.split() # Split the line into a list of values
    length = float(file_values[0]) # Convert the first value to a float and assign it to the length variable
    width = float(file_values[1]) # Convert the second value to a float and assign it to the width variable
    height = float(file_values[2]) # Convert the third value to a float and assign it to the height variable
    mass = float(file_values[3]) # Convert the fourth value to a float and assign it to the mass variable
    volume = float(file_values[4]) # Convert the fifth value to a float and assign it to the volume variable

except: # If an error occurs, do nothing
    pass # Do nothing

choice = "" # Initialize the choice variable to an empty string

# While the choice is not 'exit', print the values and prompt the user to enter a code and a new value or 'exit'.
while choice != "exit": 
    print("length", length) #   Print the value of the length variable
    print("width", width) # Print the value of the width variable
    print("height", height) # Print the value of the height variable
    print("mass", mass) # Print the value of the mass variable
    print("volume", volume) #   Print the value of the volume variable
    
    # Prompt the user to enter a code and a new value or 'exit
    choice = input("enter code and new value or exit: ") 
    split_choice = choice.split() # Split the choice into a list of values
    # If the length of the split_choice list is greater than 1, check the first value of the list and 
    # assign the second value to the corresponding variable.
    
    if len(split_choice) > 1: # If the length of the split_choice list is greater than 1
        # Check the first value of the list and assign the second value to the corresponding variable
        if split_choice[0] == "length": # If the first value is 'length'
            length = float(split_choice[1]) # Convert the second value to a float and assign it to the length variable
        # If the first value is 'width'
        if split_choice[0] == "width":
            width = float(split_choice[1])
            
        if split_choice[0] == "height":
            height = float(split_choice[1])
        if split_choice[0] == "mass":
            mass = float(split_choice[1])
        if split_choice[0] == "volume":
            volume = float(split_choice[1])

file_reader = open("info_file.txt", "w+") # Open the file for writing
file_reader.write(f"{length} {width} {height} {mass} {volume}") # Write the values to the file
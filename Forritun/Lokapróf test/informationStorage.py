
length = 0.0
width = 0.0
height = 0.0
mass = 0.0
volume = 0.0

try: # Here we try to open the file and read the values
    file_reader = open("info_file.txt", "r") # Open the file
    file_string = file_reader.readline() # Read the first line
    file_values = file_string.split() # Split the line into a list
    length = float(file_values[0]) # Assign the values to the variables
    width = float(file_values[1]) # Assign the values to the variables
    height = float(file_values[2]) #  Assign the values to the variables
    mass = float(file_values[3]) # Assign the values to the variables    
    volume = float(file_values[4]) # Assign the values to the variables

except: # If the file does not exist we pass
    pass 

choice = "" # We create a variable to store the user input

while choice != "exit": # We loop until the user inputs exit
    print("length", length) # We print the length values
    print("width", width) # We print the mass values
    print("height", height) # We print the height values
    print("mass", mass) # We print the mass values
    print("volume", volume) # We print the volume alues
    
    choice = input("enter code and new value or exit: ") # We ask the user for input
    split_choice = choice.split() # We split the input into a list
    if len(split_choice) > 1: # If the list has more than one element
        if split_choice[0] == "length": #  If the first element is length
            length = float(split_choice[1]) # We assign the second element to the length variable
            
        if split_choice[0] == "width": # If the first element is width
            width = float(split_choice[1]) # We assign the second element to the width variable
            
        if split_choice[0] == "height": # If the first element is height
            height = float(split_choice[1]) # We assign the second element to the height variable
            
        if split_choice[0] == "mass": # If the first element is mass
            mass = float(split_choice[1]) # We assign the second element to the mass variable
            
        if split_choice[0] == "volume": # If the first element is volume
            volume = float(split_choice[1]) # We assign the second element to the volume variable

file_reader = open("info_file.txt", "w+") # We open the file in write mode
file_reader.write(f"{length} {width} {height} {mass} {volume}") # We write the values to the file
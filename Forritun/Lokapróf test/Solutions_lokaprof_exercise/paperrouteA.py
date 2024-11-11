# Here we use a list because the doors are numbered like the index + 1,
# 1, 2, 3, ..., n

paper_list = [] # Initialize the paper_list to an empty list

# Function to add a door to the paper_list
def add_door():
    paper_count = int(input("Enter number of papers for new door: ")) # Prompt the user to enter the number of papers for the new door
    paper_list.append(paper_count) # Append the paper_count to the paper_list

# Function to edit the paper_list
def edit_menu(): # Define the edit_menu function
    quitting = False # Initialize the quitting variable to False
    
    # While not quitting, iterate through the paper_list and print the door number and the number of papers for each door.
    while not quitting:
        for i in range(len(paper_list)): # Iterate through the paper_list
            print(i + 1, ": ", paper_list[i]) # Print the door number and the number of papers for each door
        door_num = int(input("Enter door number (0 to exit to main menu): ")) # Prompt the user to enter the door number
        # If the door number is 0, set quitting to True.
        if door_num == 0:
            quitting = True
        # If the door number is greater than the length of the paper_list, print an error message.
        elif 0 < door_num <= len(paper_list): # If the door number is greater than 0 and less than or equal to the length of the paper_list
            paper_list[door_num - 1] = int(input(f"Number of papers for door {door_num}: ")) # Prompt the user to enter the number of papers for the door

# Function to display the main menu
def main_menu():
    quitting = False # Initialize the quitting variable to False
    # While not quitting, display the main menu options.
    while not quitting:
        print("Welcome to the paper route program!")
        print("Options:")
        print("D: Add door")
        print("E: View and edit")
        print("Q: Exit the program")
        
        # Prompt the user to enter their choice.
        choice = input("Enter your choice: ")
        # If the choice is 'D' or 'd', call the add_door function.
        if choice == "D" or choice == "d":
            add_door()
        # If the choice is 'E' or 'e', call the edit_menu function.    
        if choice == "E" or choice == "e":
            edit_menu()
        # If the choice is 'Q' or 'q', set quitting to True.
        if choice == "Q" or choice == "q":
            quitting = True

if __name__ == "__main__":
    main_menu()
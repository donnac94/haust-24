# Here we use a list because the doors are numbered like the index + 1,
# 1, 2, 3, ..., n

paper_list = [] # Here we use a list because the doors are numbered like the index + 1, 1, 2, 3, ..., n

def add_door(): # Here we add a door to the list
    paper_count = int(input("Enter number of papers for new door: ")) # Here we ask the user to input the number of papers for the new door
    paper_list.append(paper_count) #  Here we append the number of papers for the new door to the list

def edit_menu(): #  Here we edit the menu
    quitting = False #  Here we set quitting to False
    while not quitting: # Here we use a while loop to loop through the list of papers
        for i in range(len(paper_list)): #  Here we use a for loop to loop through the list of papers
            print(i + 1, ": ", paper_list[i]) #  Here we print the index + 1 and the number of papers for each door
        door_num = int(input("Enter door number (0 to exit to main menu): ")) #  Here we ask the user to input the door number
        if door_num == 0: # Here we check if the door number is 0
            quitting = True #  Here we set quitting to True
        elif 0 < door_num <= len(paper_list): #  Here we check if the door number is greater than 0 and less than or equal to the length of the list of papers
            paper_list[door_num - 1] = int(input(f"Number of papers for door {door_num}: ")) #  Here we ask the user to input the number of papers for the door

def main_menu(): #  Here we create the main menu
    quitting = False #  Here we set quitting to False
    while not quitting: # Here we use a while loop to loop through the main menu
        print("Welcome to the paper route program!") #  Here we print a welcome message
        print('************************************')
        print("Options:") # Here we print the options
        print("D: Add door") #  Here we print the option to add a door
        print("E: View and edit") # Here we print the option to view and edit
        print("Q: Exit the program") #  Here we print the option to exit the program
        print('************************************')
        choice = input("Enter your choice: ") #  Here we ask the user to input their choice
        if choice == "D" or choice == "d": #  Here we check if the user's choice is to add a door
            add_door() #  Here we call the add_door function
        if choice == "E" or choice == "e": #  Here we check if the user's choice is to view and edit
            edit_menu() #  Here we call the edit_menu function
        if choice == "Q" or choice == "q": #  Here we check if the user's choice is to exit the program
            quitting = True #  Here we set quitting to True

if __name__ == "__main__": #  Here we check if the script is being run as the main program
    main_menu() #  Here we call the main_menu function
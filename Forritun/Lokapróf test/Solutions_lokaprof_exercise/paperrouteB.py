# Here we use a dictionary instead of a list
# so we can have actual house numbers as the key

paper_dict = {}

def add_door():
    address_num = int(input("Enter address number for new door: "))
    paper_count = int(input("Enter number of papers for new door: "))
    paper_dict[address_num] = paper_count

def edit_menu():
    quitting = False
    while not quitting:
        for addr in paper_dict:
            print(addr, ": ", paper_dict[addr])
        door_num = int(input("Enter door number (0 to exit to main menu): "))
        if door_num == 0:
            quitting = True
        elif door_num in paper_dict:
            paper_dict[door_num] = int(input(f"Number of papers for door {door_num}: "))

def main_menu():
    quitting = False
    while not quitting:
        print("Welcome to the paper route program!")
        print("Options:")
        print("D: Add door")
        print("E: View and edit")
        print("Q: Exit the program")
        choice = input("Enter your choice: ")
        if choice == "D" or choice == "d":
            add_door()
        if choice == "E" or choice == "e":
            edit_menu()
        if choice == "Q" or choice == "q":
            quitting = True

if __name__ == "__main__":
    main_menu()
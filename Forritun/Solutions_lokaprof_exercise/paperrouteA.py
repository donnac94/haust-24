# Here we use a list because the doors are numbered like the index + 1,
# 1, 2, 3, ..., n

paper_list = []

def add_door():
    paper_count = int(input("Enter number of papers for new door: "))
    paper_list.append(paper_count)

def edit_menu():
    quitting = False
    while not quitting:
        for i in range(len(paper_list)):
            print(i + 1, ": ", paper_list[i])
        door_num = int(input("Enter door number (0 to exit to main menu): "))
        if door_num == 0:
            quitting = True
        elif 0 < door_num <= len(paper_list):
            paper_list[door_num - 1] = int(input(f"Number of papers for door {door_num}: "))

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
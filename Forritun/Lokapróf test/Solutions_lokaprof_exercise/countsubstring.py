def count_substring(mainstring, substring):
    counter = 0
    for i in range(len(mainstring)):
        inner_index = 0
        while (i + inner_index < len(mainstring)
               and inner_index < len(substring)
               and mainstring[i + inner_index] == substring[inner_index]):
            inner_index += 1
            if inner_index == len(substring):
                counter += 1
    return counter

if __name__ == "__main__":
    choice = ""
    while choice != "q":
        choice = input("Enter 's' to count substrings or 'q' to quit: ")
        if choice == "s":
            mainstring = input("Enter main string: ")
            substring = input("Enter substring: ")
            print("The string", substring, "occurs", count_substring(mainstring, substring), "times in the string", mainstring)
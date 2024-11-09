
length = 0.0
width = 0.0
height = 0.0
mass = 0.0
volume = 0.0

try:
    file_reader = open("info_file.txt", "r")
    file_string = file_reader.readline()
    file_values = file_string.split()
    length = float(file_values[0])
    width = float(file_values[1])
    height = float(file_values[2])
    mass = float(file_values[3])
    volume = float(file_values[4])

except:
    pass

choice = ""

while choice != "exit":
    print("length", length)
    print("width", width)
    print("height", height)
    print("mass", mass)
    print("volume", volume)
    choice = input("enter code and new value or exit: ")
    split_choice = choice.split()
    if len(split_choice) > 1:
        if split_choice[0] == "length":
            length = float(split_choice[1])
        if split_choice[0] == "width":
            width = float(split_choice[1])
        if split_choice[0] == "height":
            height = float(split_choice[1])
        if split_choice[0] == "mass":
            mass = float(split_choice[1])
        if split_choice[0] == "volume":
            volume = float(split_choice[1])

file_reader = open("info_file.txt", "w+")
file_reader.write(f"{length} {width} {height} {mass} {volume}")
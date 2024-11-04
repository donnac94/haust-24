def main():
    # Step 1: Ask for the number of pairs and store them in a dictionary
    num_pairs = int(input("How many pairs? "))
    id_name_dict = {}
    
    for _ in range(num_pairs):
        id_input = input("What is the ID? ")  # Accept as string since it can be any format
        name_input = input("What is the name? ")
        id_name_dict[id_input] = name_input  # Store ID and name in the dictionary

    # Step 2: Enter lookup mode until the user quits
    while True:
        lookup_id = input("What id to look up (q to quit)? ")
        if lookup_id == 'q':
            print("Quitting...")
            break
        elif lookup_id in id_name_dict:
            print(f"The name for {lookup_id} is {id_name_dict[lookup_id]}")
        else:
            print("The ID is not in the collection")

main()
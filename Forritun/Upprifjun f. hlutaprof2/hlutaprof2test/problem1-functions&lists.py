
# FUNCTION get_input_list HERE
def get_input_list(n):
    if n <= 0:
        return None
    input_list = []
    for _ in range(n):
        num = int(input("Please enter the next number: "))
        input_list.append(num)
    return input_list
  
# FUNCTION average_of_list HERE
def average_of_list(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

# FUNCTION triple_values HERE
def triple_values(lst):
    for i in range(len(lst)):
        lst[i] *= 3
    

def main():
    number_of_inputs = int(input("How many numbers will you input? "))
    input_list = get_input_list(number_of_inputs)
    
    if input_list is None:
        print("Not valid!")
    else:
        print("The list: ", input_list)
        average = average_of_list(input_list)
        print(f"The average of the values is: {average}")
        triple_values(input_list)
        print("Now the list is: ", input_list)

# Run the program
main()
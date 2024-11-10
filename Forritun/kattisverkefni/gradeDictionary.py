#   1. Create a dictionary called student_grades.
#   2. Inside the student_grades dictionary, create a key for each student whose name is the key and whose grade is the value.
#   3. Assign the value 85 to the key "Alice".
#   4. Assign the value 92 to the key "Bob".
#   5. Assign the value 78 to the key "Charlie".

# Create dictionary
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

def print_grades(grades_dict): # Function to print grades
    for student, grade in grades_dict.items(): #  Loop through the dictionary
        print(f"{student}: {grade}") # Print the student and grade

# Example usage
print_grades(student_grades)
from typing import List

# Function to return a new list with only even numbers (does not modify the original list)
def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""
    return [num for num in int_list if num % 2 == 0]

# Function to remove all odd numbers from the list (modifies the original list)
def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""
    int_list[:] = [num for num in int_list if num % 2 == 0]
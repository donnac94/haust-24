"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 
print(EXPECTED_BAKE_TIME)

def bake_time_remaining(elapsed_bake_time):
  """Calculate the bake time remaining.

  :param elapsed_bake_time: int - baking time already elapsed.
  :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

  Function that takes the actual minutes the lasagna has been in the oven as
  an argument and returns how many minutes the lasagna still needs to bake
  based on the `EXPECTED_BAKE_TIME`.
  """
  return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
  """ Calculates the preperation time.

  Args:
      number_of_layers (int): takes the number of layers as an argument.

  Returns:
      preparation_time_in_minutes (int): returns the preparation time in minutes.
  """
  return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  """Calculates the elapsed time in minutes.

  Args:
      number_of_layers (int): takes the number of layers as an argument.
      elapsed_bake_time (int): takes the elapsed time in minutes as an argument.

  Returns:
      elapsed_time_in_minutes (int): returns the elapsed time in minutes.
  """
  return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time 

number_of_layers = int(input())
elapsed_bake_time = int(input())
print(elapsed_time_in_minutes(number_of_layers, elapsed_bake_time))

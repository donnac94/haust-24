MIN_POSITION = 1
MAX_POSITION = 10

def display_pos(position):
  """
  Displays the current position of the character on the x-axis.
  The character's current position is marked as 'o' and other 
  positions are marked as 'x'.

  Args:
      position (int): The current position of the character on the x-axis.
  """
  for i in range(MIN_POSITION, MAX_POSITION + 1):
      if i == position:
        print('o', end='')
      else:
        print('x', end='')
  print()
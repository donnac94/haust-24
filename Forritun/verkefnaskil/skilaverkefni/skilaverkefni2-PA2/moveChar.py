from displayPos import display_pos

MIN_POSITION = 1
MAX_POSITION = 10
MOVE_LEFT = 'l'
MOVE_RIGHT = 'r'

def move(position):
  """
  Moves the character on the x-axis based on user input. The user can 
  move the character left ('l') or right ('r'). If an invalid input 
  is provided, the program exits.

  Args:
      position (int): The initial position of the character.
  """
  while True:
      display_pos(position)
      print(f"{MOVE_LEFT}: left\n{MOVE_RIGHT}: right")
      move = input("Move: ").strip().lower()

      if move == MOVE_LEFT and position > MIN_POSITION:
          position -= 1
      elif move == MOVE_RIGHT and position < MAX_POSITION:
          position += 1
      elif move not in [MOVE_LEFT, MOVE_RIGHT]:
          print("")
          break
  return position
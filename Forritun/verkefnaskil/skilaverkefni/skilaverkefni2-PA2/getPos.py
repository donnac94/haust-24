MIN_POSITION = 1
MAX_POSITION = 10

def get_initial_pos():
    """
  Repeatedly prompts the user to input a valid initial position for the 
  character on the x-axis. 
  The position must be between MIN_POSITION and 
  MAX_POSITION (inclusive).

  Returns:
      int: The valid initial position provided by the user.
  """
    while True:
        try:
            position = int(input(f"Position in [{MIN_POSITION}..{MAX_POSITION}]: "))
            if MIN_POSITION <= position <= MAX_POSITION:
                return position
            else:
                print("")
        except ValueError:
            print("")
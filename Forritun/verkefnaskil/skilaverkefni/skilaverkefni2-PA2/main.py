from getPos import get_initial_pos
from moveChar import move

def main():
  """
  The main function that gets the initial position of the character 
  and then handles its movement.
  """
  position = get_initial_pos()
  move(position)

if __name__ == "__main__":
  main()
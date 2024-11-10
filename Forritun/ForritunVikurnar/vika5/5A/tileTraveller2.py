def print_directions(available_directions):
   """Prints the available directions to the player."""
   directions = {
       'N': "(N)orth",
       'S': "(S)outh",
       'E': "(E)ast",
       'W': "(W)est"
   }
   print("You can travel:", ' or '.join([directions[dir] for dir in available_directions]) + ".")


def move(position, direction):
   """Moves the player to a new position based on the direction."""
   x, y = position
   if direction == 'N':
       return x, y + 1
   elif direction == 'S':
       return x, y - 1
   elif direction == 'E':
       return x + 1, y
   elif direction == 'W':
       return x - 1, y
   return position


def get_available_directions(position):
   """Returns the available directions based on the player's current position."""
   x, y = position
   if (x, y) == (1, 1):
       return 'N'
   elif (x, y) == (1, 2):
       return 'NES'
   elif (x, y) == (1, 3):
       return 'ES'
   elif (x, y) == (2, 1):
       return 'N'
   elif (x, y) == (2, 2):
       return 'SW'
   elif (x, y) == (2, 3):
       return 'EW'
   elif (x, y) == (3, 1):
       return ''
   elif (x, y) == (3, 2):
       return 'NS'
   elif (x, y) == (3, 3):
       return 'SW'
   return ''


def main():
   position = (1, 1)  # Start at position (1, 1)
  
   while position != (3, 1):  # The goal is to reach (3, 1)
       available_directions = get_available_directions(position)
       print_directions(available_directions)
#        print(position)
      
       move_direction = input("Direction: ").upper()
      
       if move_direction in available_directions:
           position = move(position, move_direction)
       else:
           print("Not a valid direction!")


   print("Victory!")


if __name__ == "__main__":
   main()

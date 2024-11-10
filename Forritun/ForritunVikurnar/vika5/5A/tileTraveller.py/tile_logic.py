# tile_logic.py

from constants import VALID_DIRECTIONS, VICTORY_TILE

def get_available_directions(x, y):
    """Returns a string of valid directions for the given tile coordinates."""
    return VALID_DIRECTIONS.get((x, y), "")

def move_player(x, y, direction):
    """Moves the player in the given direction if valid."""
    if direction == "n":
        return x, y + 1
    elif direction == "s":
        return x, y - 1
    elif direction == "e":
        return x + 1, y
    elif direction == "w":
        return x - 1, y
    else:
        return x, y  # No movement if invalid direction

def check_victory(x, y):
    """Checks if the player has reached the victory tile (3, 1)."""
    return (x, y) == VICTORY_TILE
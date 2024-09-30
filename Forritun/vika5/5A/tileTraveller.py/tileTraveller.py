# TileTraveller.py
from game import Game

def main():
    game = Game()

    while not game.check_victory():
        current_tile = game.get_current_tile()  # Get the current tile based on player position
        available_directions = current_tile.get_available_directions()
        print(f"You can travel: {format_directions(available_directions)}.")  # Format the available directions correctly

        direction = input("Direction: ").lower()  # Take user input for direction
        game.move_player(direction)  # Move the player according to input

    print("Victory!")  # Victory message once the player reaches the end

def format_directions(directions):
    """Formats the available directions into the required format."""
    direction_map = {
        "n": "(N)orth",
        "s": "(S)outh",
        "e": "(E)ast",
        "w": "(W)est"
    }
    formatted = [direction_map[d] for d in directions]  # Format each direction using direction_map
    return " or ".join(formatted)  # Join the directions with "or"

if __name__ == "__main__":
    main()
# constants.py

# Dictionary for storing valid directions for each tile
VALID_DIRECTIONS = {
    (1, 1): "n",
    (1, 2): "nse",
    (1, 3): "es",
    (2, 1): "n",
    (2, 2): "sw",
    (2, 3): "we",
    (3, 1): "",
    (3, 2): "ns",
    (3, 3): "sw"
}

# Victory tile coordinates
VICTORY_TILE = (3, 1)
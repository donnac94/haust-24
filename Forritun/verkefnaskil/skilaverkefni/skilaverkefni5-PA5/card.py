class Card:
    def __init__(self, rank, suit):
        # Check if rank is a numeric string and convert to integer if so
        if isinstance(rank, str):
            if rank.isdigit():
                self.rank = int(rank)
            else:
                # Map face cards ('J', 'Q', 'K', 'A') to their integer values
                rank_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
                self.rank = rank_map.get(rank)
        else:
            # If rank is already an integer, assign it directly
            self.rank = rank

        # Store the suit
        self.suit = suit  # 'H', 'S', 'D', or 'C'

    def __str__(self):
        # Convert rank back to string representation for face cards if needed
        if self.rank in [11, 12, 13, 14]:
            rank_str = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}[self.rank]
        else:
            # For numbers less than 11, just convert to string
            rank_str = str(self.rank)

        # Right justify the rank in a field of width 2
        return f"{rank_str:>2}{self.suit}"
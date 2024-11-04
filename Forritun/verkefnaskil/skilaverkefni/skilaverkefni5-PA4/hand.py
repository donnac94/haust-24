class Hand:
    NUMBER_OF_CARDS = 13  # Define the constant for max cards

    def __init__(self):
        # Initialize an empty list to hold cards
        self.cards = []

    def __str__(self):
        # If hand is empty, return "Empty"
        if not self.cards:
            return "Empty"
        # Otherwise, return a single line of cards with space-separated values
        return " ".join(str(card) for card in self.cards)

    def add_card(self, card):
        # Only add card if hand has space
        if len(self.cards) < Hand.NUMBER_OF_CARDS:
            self.cards.append(card)
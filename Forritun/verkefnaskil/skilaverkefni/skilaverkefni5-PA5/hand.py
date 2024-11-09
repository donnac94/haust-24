class Hand:
    NUMBER_OF_CARDS = 13

    def __init__(self):
        self.cards = []

    def __str__(self):
        # If empty, return "Empty"
        if not self.cards:
            return "Empty"
        # Otherwise, join cards with single spaces
        return " ".join(str(card) for card in self.cards)

    def add_card(self, card):
        if len(self.cards) < Hand.NUMBER_OF_CARDS:
            self.cards.append(card)
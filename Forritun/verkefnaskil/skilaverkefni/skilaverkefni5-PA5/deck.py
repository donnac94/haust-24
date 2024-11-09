import random
from card import Card

class Deck:
    def __init__(self):
        # Define suits and ranks in the order specified (HSDC)
        suits = ['H', 'S', 'D', 'C']
        ranks = list(range(2, 15))  # 2 through 14 (where 11-14 are J, Q, K, A)
        # Generate deck in sorted order by suit and then by rank
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    def __str__(self):
        # Format the deck as a string with 13 cards per line
        lines = []
        for i in range(0, len(self.deck), 13):
            line = " ".join(str(card) for card in self.deck[i:i+13])
            lines.append(line)
        return "\n".join(lines)

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffle using random.shuffle

    def deal(self):
        # Deal the top card by popping it from the list
        return self.deck.pop(0) if self.deck else None
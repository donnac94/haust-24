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
        # Return the deck as a string with 13 cards per line
        deck_str = ""
        for i, card in enumerate(self.deck):
            deck_str += str(card) + " "
            if (i + 1) % 13 == 0:
                deck_str += "\n"
        return deck_str.strip()

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffle using random.shuffle

    def deal(self):
        # Deal the top card by popping it from the list
        return self.deck.pop(0) if self.deck else None
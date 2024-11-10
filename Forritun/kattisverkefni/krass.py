def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    # Define the value of each card in a dictionary
    card_values = {
        'J': 10, 'Q': 10, 'K': 10,
        'A': 11,  # Note: we're assuming that an ace is worth 11 here
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10
    }

    # If either card is an ace, the value of an additional ace should be 1 to avoid busting
    if card_one == 'A' or card_two == 'A': # If either card is an ace
        return 1 # Return 1
    else: 
        return 11 

print(value_of_ace('7', '3'))  
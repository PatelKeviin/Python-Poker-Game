CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITS = ['D', 'H', 'S', 'C']
COMBINATIONS = ['High card', 'Pair', 'Two pairs', 'Three of a kind', 'Straight',
                'Flush', 'Full house', 'Four of a kind', 'Straight flush', 'Royal flush']


def order_cards(player_cards):
    """
    A helper function used for ordering cards.
    returns: ordered cards in the player hand
    """
    card_indices = []
    for value, suit in player_cards:
        card_indices.append(CARDS.index(value))

    ordered_card_indices = sorted(card_indices)
    ordered_cards = []
    for card_index in ordered_card_indices:
        ordered_cards.append(CARDS[card_index])

    return ordered_cards    # contains only values, and not suits information


def remove_card_from_hand(player_cards, card):
    """
    A helper function used in 'round_result' function
    """
    for value, suit in player_cards:
        if value == card:
            player_cards.remove((value, suit))


def get_high_card(player_cards):
    """
    params: A list of tuples containing card value and suit, for e.g, [('3', 'S'), ('3', 'S'), ('J', 'C'), ('T', 'H'), ('7', 'C')]
    return: ["High card", "Value"]
    """
    high_card = None
    card_index = -1
    for value, suit in player_cards:
        if CARDS.index(value) > card_index:
            card_index = CARDS.index(value)

    return ['High card', CARDS[card_index]]


def is_pair(player_cards, cards_to_exclude=None):
    """
    params: 
    player_cards: A list of tuples containing card value and suit, for e.g, [('3', 'S'), ('3', 'S'), ('J', 'C'), ('T', 'H'), ('7', 'C')]
    cards_to_exclude: A list of cards not to count as they have previously been counted already
    return: False if not, otherwise ["Pair", "Value"]

    Conditions:
    - two cards of the same value
    """
    player_hand_cards = ''
    for value, suit in player_cards:
        player_hand_cards += value

    for card in player_hand_cards:
        if (cards_to_exclude is None) or (card not in cards_to_exclude):
            if player_hand_cards.count(card) == 2:
                return ['Pair', card]
    return False


def is_two_pairs(player_cards):
    """
    return: False if not, otherwise ["Two pairs", "Value"]

    Conditions:
    - two different pairs
    """
    if is_pair(player_cards):
        first_pair = is_pair(player_cards)[1]

        if is_pair(player_cards, [first_pair]):
            second_pair = is_pair(player_cards, [first_pair])[1]

            if CARDS.index(first_pair) > CARDS.index(second_pair):
                return ['Two pairs', first_pair]
            else:
                return ['Two pairs', second_pair]

    return False


def is_three_of_a_kind(player_cards):
    """
    params: A list of tuples containing card value and suit, for e.g, [('3', 'S'), ('3', 'S'), ('J', 'C'), ('T', 'H'), ('7', 'C')]
    return: False if not, otherwise ["Three of a kind", "Value"]

    Conditions:
    - three cards of the same value
    """
    player_hand_cards = ''
    for value, suit in player_cards:
        player_hand_cards += value

    for card in player_hand_cards:
        if player_hand_cards.count(card) == 3:
            return ['Three of a kind', card]
    return False


def is_straight(player_cards):
    """
    params: A list of tuples containing card value and suit, for e.g, [('3', 'S'), ('3', 'S'), ('J', 'C'), ('T', 'H'), ('7', 'C')]
    return: False if not, otherwise ["Straight", "Value"]

    Conditions:
    - all cards in consecutive value order
    """
    ordered_cards = order_cards(player_cards)

    if ''.join(ordered_cards) in '23456789TJQKA':
        return ['Straight', get_high_card(player_cards)[1]]
    else:
        return False


def is_flush(player_cards):
    """
    params: A list of tuples containing card value and suit, for e.g, [('3', 'S'), ('3', 'S'), ('J', 'C'), ('T', 'H'), ('7', 'C')]
    return: False if not, otherwise ["Flush", "Value"]

    Conditions:
    - same suit
    """
    player_hand_suits = []
    for card in player_cards:
        player_hand_suits.append(card[1])

    concatenate_player_hand_suits = ''.join(player_hand_suits)

    if concatenate_player_hand_suits == 'DDDDD' or concatenate_player_hand_suits == 'HHHHH' or concatenate_player_hand_suits == 'SSSSS' or concatenate_player_hand_suits == 'CCCCC':
        return ['Flush', get_high_card(player_cards)[1]]
    else:
        return False


def is_full_house(player_cards):
    """
    return: False, otherwise ["Full house", "Value"]

    Conditions:
    - three of a kind
    - a pair
    """
    if is_three_of_a_kind(player_cards) and is_pair(player_cards):
        return ['Full house', is_three_of_a_kind(player_cards)[1]]
    return False


def is_four_of_a_kind(player_cards):
    """
    return: False, otherwise ["Four of a kind", "Value"]

    Conditions:
    - four cards of the same value
    """
    player_hand_cards = ''
    for value, suit in player_cards:
        player_hand_cards += value

    for card in player_hand_cards:
        if player_hand_cards.count(card) == 4:
            return ['Four of a kind', card]
    return False


def is_straight_flush(player_cards):
    """
    return: False if not, otherwise ["Straight flush", "Value"]

    Conditions:
    - same suit (flush)
    - consecutive cards (straight)
    """
    if is_straight(player_cards) and is_flush(player_cards):
        return ['Straight flush', get_high_card(player_cards)[1]]
    else:
        return False


def is_royal_flush(player_cards):
    """
    return: False if not, otherwise ["Royal flush", "Value"]

    Conditions:
    - same suit
    - Ten, Jack, Queen, King and Ace cards
    """
    if is_flush(player_cards):
        ordered_cards = order_cards(player_cards)
        if ''.join(ordered_cards) == 'TJQKA':
            return ['Royal flush', 'A']

    return False


def get_combination(player_cards):
    """
    return: ["Combination", "Value"]
    """
    if is_royal_flush(player_cards):
        return is_royal_flush(player_cards)
    elif is_straight_flush(player_cards):
        return is_straight_flush(player_cards)
    elif is_four_of_a_kind(player_cards):
        return is_four_of_a_kind(player_cards)
    elif is_full_house(player_cards):
        return is_full_house(player_cards)
    elif is_flush(player_cards):
        return is_flush(player_cards)
    elif is_straight(player_cards):
        return is_straight(player_cards)
    elif is_three_of_a_kind(player_cards):
        return is_three_of_a_kind(player_cards)
    elif is_two_pairs(player_cards):
        return is_two_pairs(player_cards)
    elif is_pair(player_cards):
        return is_pair(player_cards)
    else:
        return get_high_card(player_cards)


def round_result(player1_cards, player2_cards, player1_points, player2_points):
    """
    if ranks tie (same combination + value), then get high cards until tie is broken
    """
    player1_hand_combination = get_combination(player1_cards)
    player2_hand_combination = get_combination(player2_cards)

    # player1 has a higher level combination than player2
    if COMBINATIONS.index(player1_hand_combination[0]) > COMBINATIONS.index(player2_hand_combination[0]):
        return player1_points + 1, player2_points
    # player1 has a lower level combination than player2
    elif COMBINATIONS.index(player1_hand_combination[0]) < COMBINATIONS.index(player2_hand_combination[0]):
        return player1_points, player2_points + 1
    else:
        # if combinations are same for both, values of the combinations is used to break the tie
        if CARDS.index(player1_hand_combination[1]) > CARDS.index(player2_hand_combination[1]):
            return player1_points + 1, player2_points
        elif CARDS.index(player1_hand_combination[1]) < CARDS.index(player2_hand_combination[1]):
            return player1_points, player2_points + 1
        else:
            # if two ranks are same, then highest cards are used until the tie is broken
            while True:
                player1_highest_card = get_high_card(player1_cards)[1]
                player2_highest_card = get_high_card(player2_cards)[1]

                if CARDS.index(player1_highest_card) > CARDS.index(player2_highest_card):
                    return player1_points + 1, player2_points
                elif CARDS.index(player1_highest_card) < CARDS.index(player2_highest_card):
                    return player1_points, player2_points + 1
                else:
                    remove_card_from_hand(player1_cards, player1_highest_card)
                    remove_card_from_hand(player2_cards, player2_highest_card)


# deal cards to player1 and player2
def distribute_cards(cards):
    player1_cards, player2_cards = [], []
    player1_cards_temp, player2_cards_temp = cards.split(
        ' ')[:5], cards.split(' ')[5:]

    for player1_card_temp, player2_card_temp in zip(player1_cards_temp, player2_cards_temp):
        player1_cards.append((player1_card_temp[0], player1_card_temp[1]))
        player2_cards.append((player2_card_temp[0], player2_card_temp[1]))

    return player1_cards, player2_cards


# game loop
def main():
    player1_points, player2_points = 0, 0

    # input
    with open('poker-hands.txt', 'r') as file:
        for line in file.readlines():
            player1_cards, player2_cards = distribute_cards(line)
            player1_points, player2_points = round_result(
                player1_cards, player2_cards, player1_points, player2_points)

    # output
    print('Player 1: {} hands'.format(player1_points))
    print('Player 2: {} hands'.format(player2_points))


# main function
main()

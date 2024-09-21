
import random

# Define the deck and card values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

deck = [(rank, suit) for rank in ranks for suit in suits]

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Example usage
hand = [deal_card(deck), deal_card(deck)]
print(hand)
print(calculate_hand_value(hand))

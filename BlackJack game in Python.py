# Blackjack game implementation in Python
import random

# Card class represents a single playing card with a suit and value
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
# Deck class represents a standard deck of 52 playing cards
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
# Hand class represents a player's hand in the game, which can hold multiple cards and calculate the total value of the hand    
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
                value += 11
            else:
                value += int(card.value)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Main function to play the blackjack game
def play_blackjack():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # Initial deal: two cards for player and dealer
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print("Dealer's hand: ", dealer_hand.cards[0], "and [Hidden]")
    print("Player's hand: ", player_hand)

    # Player's turn
    while True:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.add_card(deck.deal_card())
            print("Player's hand: ", player_hand)
            if player_hand.get_value() > 21:
                print("Player busts! Dealer wins.")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    # Dealer's turn
    print("Dealer's hand: ", dealer_hand)
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        print("Dealer's hand: ", dealer_hand)

    # Determine the winner
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()

    if dealer_value > 21:
        print("Dealer busts! Player wins.")
    elif player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_blackjack()
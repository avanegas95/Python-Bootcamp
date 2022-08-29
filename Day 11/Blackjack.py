from art import logo

############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def hand_total(hand):
    '''Returns the total value of the cards in a hand'''
    #Needs more logic to take into account 
    for card in hand:
        total = hand[card]
        return total

def draw_card(new_card):
    '''Adds a card to someone's hand'''


cards = [11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []

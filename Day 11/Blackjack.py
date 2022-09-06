from art import logo
import random

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
    total = 0 
    for index, card in enumerate(hand):
        total += card
        # Sets the value of the Ace depending on whether the player goes over 21 or not
        if card == 11:
            if total > 21:
                hand[index] = 1
                total = total - 10
    return total

def draw_card(hand):
    '''Adds a card to someone's hand'''
    hand.append(random.choice(cards))

def starting_hands():
    '''Sets up up the player and the dealer with 2 cards each.'''
    for i in range(2):
        draw_card(user_hand)
        draw_card(dealer_hand)

def print_hands():
    '''Displays the player's hand and the computer's first card'''
    print(f"    Your cards: {user_hand}, current score: {hand_total(user_hand)}")
    print(f"    Computer's first card: {dealer_hand[0]}")

def restart_game():
    global user_hand
    global dealer_hand
    global draw_again
    global dealer_draw_again
    global play_again
    user_hand = []
    dealer_hand = []
    draw_again = 'y'
    dealer_draw_again = 'y'
    play_again = 'y'
    

def check_winner():
    if hand_total(dealer_hand) == 21:
        print("Dealer has a blackjack. You lose!")
    elif hand_total(user_hand) == 21:
        print("You got a blackjack! You win!")
    elif hand_total(user_hand) == hand_total(dealer_hand):
        print("It's a draw!")
    elif hand_total(user_hand) > 21 and hand_total(dealer_hand) < 21:
        print("You went over. You lose!")
    elif hand_total(dealer_hand) > 21: 
        if hand_total(user_hand) < 21:
            print("Dealer bust! You win!")
        else:
            print("You both bust")
    else:
        if hand_total(dealer_hand) < 21 and hand_total(dealer_hand) > hand_total(user_hand):
            print("Dealer has a higher score. Dealer wins!")
        else:
            print("You have a higher score. You win!")


print(logo)
cards = [11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []
draw_again = 'y'
dealer_draw_again = 'y'
play_again = 'y'


while play_again == 'y':    
    starting_hands()
    while draw_again == 'y':
        print_hands()
        draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_again == 'y':
            draw_card(user_hand)
            if hand_total(user_hand) > 21 and hand_total(dealer_hand) < 21:
                break
    while dealer_draw_again == 'y':
        if hand_total(dealer_hand) < 16:
            draw_card(dealer_hand)
        else:
            dealer_draw_again = 'n'
    print(f"    Your cards: {user_hand}, final score: {hand_total(user_hand)}")
    print(f"    Computer's cards: {dealer_hand}, final score: {hand_total(dealer_hand)}")
    check_winner()
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'y':
        restart_game()
        print("___________________________________________________")
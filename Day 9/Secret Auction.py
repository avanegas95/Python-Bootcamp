import os
from art import logo

clear = lambda:os.system('cls')
repeat = True
list_of_bidders = []

def add_new_bidder(name, amount):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = amount

    list_of_bidders.append(new_bidder)

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ''
    for bidder in list_of_bidders:
        if bidder['bid'] > highest_bid:
            highest_bid = bidder['bid']
            winner = bidder['name']
    print(f"The winner is {winner} with a bid of {highest_bid}." )


print(logo)
print("Welcome to the secret auction program.")

while repeat:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    add_new_bidder(name, bid)
    again = input("Are there any other bidder? Type 'yes' or 'no'. ")

    if again == 'yes':
        repeat == True
        clear()
    else:
        find_highest_bidder(list_of_bidders)
        repeat = False


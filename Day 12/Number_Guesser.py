from glob import glob
from pickle import GLOBAL
from random import randint
from typing import Set
from art import logo


HARD = 5
EASY = 10


def check_guess(guess, answer, guesses):
    '''Takes in the guess which is given by the user and determines whether it is higher or lower than the actual number'''
    if guess > answer:
        print("Too high.")
        return guesses - 1
    elif guess < answer:
        print("Too low.")
        return guesses - 1            
    elif guess == answer:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    global guesses
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'hard':
        return HARD
    else:
        return EASY

def game():
    actual_number = randint(1,100)
    guess = 0
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # For debugging purposes the next line is commented out and reveals the answer
    print(f"Pssst, the correct answer is {actual_number}")
    guesses = set_difficulty()
    
    # Keep guessing the number until they get it. Check in the loop for attempts left
    while guess != actual_number:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        guesses = check_guess(guess, actual_number, guesses)
        if guesses == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != actual_number:
            print("Guess again.")
        
game()



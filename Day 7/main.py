import random
import hangman_art
import hangman_words


lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
print(hangman_art.logo)

#Testing code
#print(f'Psst, the solution is {chosen_word}.')

#Create Blank Display
display = []
for x in chosen_word:
    display += '_'

#Check the guessed letter
while '_' in display:
    guess = input("Guess a letter: ").lower()
    #Replace blank with the letter if it is correct. Subtract a life it is incorrect
    if guess not in display:
        for position in range(word_length):
            letter = display[position]
            if guess == chosen_word[position]:
                display[position] = guess
     
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}. That's not in the word. You lose a life.")

        
        print(display)
        print(hangman_art.stages[lives])
        if not '_' in display:
            print('You win!')
        elif lives == 0:
            print('You lose')
            print(f'The word was {chosen_word}')
            break
    else:
        print(f"You've already guessed {guess}.")
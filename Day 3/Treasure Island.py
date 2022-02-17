print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_branch = input('You come along to a fork in the road. Where do you want to go? Type "left" or "right"\n')

if first_branch.lower() == 'left':
    #Go on
    second_branch = input('You come across a river. It is very calm. There is a house on the other side. Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if second_branch.lower() == 'wait':
        #go on
        third_branch = input("An old man takes you across on his boat. You approach the house and it has 3 doors; red, yellow, and blue. Which do you choose?\n")

        if third_branch.lower() == 'yellow':
            print("You found the treasue! You win!")
        elif third_branch.lower() == 'red':
            print("The whole place blows up.")
            print("Game over!") 
        elif third_branch.lower() == 'blue':
            print("A bear eats your face.")
            print("Game over!") 
        else:
            print("That hard to pick a door huh? You turn around and go home.")
            print("Game over!") 
    else:
        print("You attempt to swim across the river. However you get a cramp and drown.")
        print("Game over!") 
else:
    print("You fall into a hole covered by some leaves.")
    print("Game over!") 
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n")
computer  = random.randint(0,2)
images = [rock, paper, scissors]

results = [["tie", "win", "lose"], ["lose", "tie", "win"], ["win", "lose", "tie"]]
#outcome = 

print(images[int(player)])
print("Computer chose:\n" + images[computer])
print(f"You {results[computer - 1][int(player) - 1]}")



# if player == computer:
#     print(images[player])
#     print("Computer chose:")
#     print(images[computer])
#     print("It's a tie!")

# if player = 0 and computer  == 1:
#     print(images[player])
#     print("Computer chose:")
#     print(images[computer])
#     print("You lose")

# if player == 1 and computer == 2:
#     print(images[player])
#     print("Computer chose:")
#     print(images[computer])
#     print("You lose")

# if player == 2 and computer == 0:
#     print(images[player])
#     print("Computer chose:")
#     print(images[computer])
#     print("You lose")


import random

# coin = random.randint(0,1)

# if coin == 1:
#     print("Heads")
# else:
#     print("Tails")



# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# payee = random.randint(0, len(names) - 1)
# print(f"{names[payee]} is going to buy the meal today!")





# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

map[int(position[1]) -1][int(position[0]) -1] = "x"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
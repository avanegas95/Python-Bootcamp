# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# BMI = round(weight/height ** 2)

# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you are normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

#Leap Year Determination
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")






# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == 'S':
#     bill +=15
#     if add_pepperoni == 'Y':
#         bill += 2
# elif size == 'M':
#     bill +=20
#     if add_pepperoni == 'Y':
#         bill += 3
# else:
#     bill +=25
#     if add_pepperoni == 'Y':
#         bill += 3

# if extra_cheese == 'Y':
#     bill += 1

# print(f"Your final bill is: ${bill}.")




print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

true_count = 0
love_count = 0

if name1.count('t') > 0 or name2.count('t') > 0:
    true_count += name1.count('t') + name2.count('t')
if name1.count('r') > 0 or name2.count('r') > 0:
    true_count += name1.count('r') + name2.count('r')
if name1.count('u') > 0 or name2.count('u') > 0:
    true_count += name1.count('u') + name2.count('u')
if name1.count('e') > 0 or name2.count('e') > 0:
    true_count += name1.count('e') + name2.count('e')


if name1.count('l') > 0 or name2.count('l') > 0:
    love_count += name1.count('l') + name2.count('l')
if name1.count('o') > 0 or name2.count('o') > 0:
    love_count += name1.count('o') + name2.count('o')
if name1.count('v') > 0 or name2.count('v') > 0:
    love_count += name1.count('v') + name2.count('v')
if name1.count('e') > 0 or name2.count('e') > 0:
    love_count += name1.count('e') + name2.count('e')

final_score = int(str(true_count) + str(love_count))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
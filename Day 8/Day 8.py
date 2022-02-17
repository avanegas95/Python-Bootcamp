import math
# def greet():
#     print("Hello there.")
#     print("How are you?")
#     print("I'm doing good")

# greet())

# def greet_with(name, location):
#     print(f"Hello there {name}.")
#     print(f"I see you are in {location}")

# def paint_calc(height, width, cover):
#     total_area = height * width
#     cans = total_area/cover
#     print(f"You'll need {math.ceil(cans)} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# def prime_checker(number):
#     if number == 1 or number == 2 or number == 3:
#         print("It is a prime number.")
#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#         print("It is not a prime number.")
#     else:
#         print("It is a prime number.")

def prime_checker(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
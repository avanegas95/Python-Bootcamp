# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# count = 0
# total = 0
# for student in student_heights:
#     total += student
#     count += 1

# print(round(total/count))








# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# high_score = 0

# for score in student_scores:
#     if score > high_score:
#         high_score = score

# print("The highest score in the class is: " + str(high_score))

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)








for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}") 

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades= {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for name in student_scores:
#     if student_scores[name] <= 70:
#         student_grades[name] = "Fail"
#     elif student_scores[name] <= 80:
#         student_grades[name] = "Acceptable"
#     elif student_scores[name] <= 90:
#         student_grades[name] = "Exceeds Expectations"
#     else:
#          student_grades[name] = "Outstanding"
# # 🚨 Don't change the code below 👇
# print(student_grades)





#Nesting Dictionaries Inside Dictionaries
# travel_log = {
#     "France": 
#         {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
#     "Germany":
#         {"cities_visited": ["Paris", "Lille", "Dijon"], "total_vsists": 5},
# }

#Nesting Dictinary in a List
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
  new_country = {}
  new_country["country"] = country
  new_country["cities"] = cities
  new_country["total_vists"] = visits
  
  travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# #Function with Outputs

# def format_name(f_name, l_name):
#     title_f_name = f_name.title()
#     title_l_name = l_name.title()
#     return f"{title_f_name} {title_l_name}"

# formated_string = format_name("ANDersOn", "VAnEgAs")
# print(formated_string)  



#Modify leap year code to return the month. February has an extra day on a leap year
def is_leap(year):
  """This function will return true or false depending on whether or not the year is a leap"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
    

def days_in_month(year, month):
    """Returns how many days are in a given month, in a certain year. Takes into account leap years."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month-1]
  
# Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

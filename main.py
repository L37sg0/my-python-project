# print('200 is great number') # string
# print("200 is great number") # string
# print(2) # integer
# print(-22) # - integer
# print(2.99) # float
# print(2 * 8) # math operations
from re import match

# print("20 days are " + str(50) +" minutes") # concatenating str and int
# print(20*60*24) # math operations

# print(f"20 days are {20*24*60} minutes") # concatenating str and int the right way - will not work in python version 2

# to_minutes = 24 * 60
# to_seconds = to_minutes * 60
# calculation_to_units =  to_seconds
# unit = "seconds"
#
# print(f"20 days are {20 * calculation_to_units} {unit}")
# print(f"30 days are {30 * calculation_to_units} {unit}")
# print(f"40 days are {40 * calculation_to_units} {unit}")

# calculation_to_units =  to_minutes
# unit = "minutes"
#
# print(f"20 days are {20 * calculation_to_units} {unit}")
# print(f"30 days are {30 * calculation_to_units} {unit}")
# print(f"40 days are {40 * calculation_to_units} {unit}")

# calculation_to_units =  to_minutes/24
# unit = "hours"
#
# print(f"20 days are {20 * calculation_to_units} {unit}")
# print(f"30 days are {30 * calculation_to_units} {unit}")
# print(f"40 days are {40 * calculation_to_units} {unit}")

# to_minutes = 24 * 60
# to_seconds = to_minutes * 60
# to_hours = to_minutes/60
# # calculation_to_units =  to_hours
# units = "hours"
#
# def days_to_units(days, units):
#     # calculation_to_units =
#     print(f"{days} days are {days * calculation_to_units} {units}")
#     print("All fine")
#
# days_to_units(35,"hours")
# days_to_units(40,"hours")
# days_to_units(50,"hours")
# days_to_units(5,"hours")

# Scopes
# A variable is only available from inside the region it is created
#
# def scope_check(num_of_days):
#     my_var = "Random var inside function"
#     print(my_var) # internal variable defined inside function
#     print(num_of_days) # internal variable passed as a parameter
#     print(units) # global scope variable
#
# scope_check(20)

# User inputs
calculation_to_units =  24
units = "hours"
def days_to_units(days, units):
    print(f"{days} days are {days * calculation_to_units} {units}")
    print("All fine")

user_input = input("Enter number of days and will convert it to hours:\n")
print(user_input)
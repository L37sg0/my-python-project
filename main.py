# print('200 is great number') # string
# print("200 is great number") # string
# print(2) # integer
# print(-22) # - integer
# print(2.99) # float
# print(2 * 8) # math operations

# print("20 days are " + str(50) +" minutes") # concatenating str and int
# print(20*60*24) # math operations

# print(f"20 days are {20*24*60} minutes") # concatenating str and int the right way - will not work in python version 2

to_minutes = 24 * 60
to_seconds = to_minutes * 60
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

calculation_to_units =  to_minutes/24
unit = "hours"

print(f"20 days are {20 * calculation_to_units} {unit}")
print(f"30 days are {30 * calculation_to_units} {unit}")
print(f"40 days are {40 * calculation_to_units} {unit}")
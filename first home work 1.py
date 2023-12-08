


# Task1
#  1
#

import this



# everything is understandable, but have some questions
# why Anton has import datetime in his 1st task?
# what is namespaces?

#  2
#
a = 1
b = 5
c = 4
x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
print(x1)
print(x2)

#  3
#
name = input("Please enter your name: ")
print("Hello " + name)

#  4
#
UAH_amount = input("Please enter money amount in UAH: ")
print("By the 12.08.2034 rate your {UAH_amount} UAH will equal = " + str(float(UAH_amount) / 28) + "USD")

# Task2
#
input_snake_case = input("Put in your creds here (divided by underscore): ")
case_conversion = input_snake_case.split("_")
case_conversion_next = "".join([text.title() for text in case_conversion])
print(case_conversion_next)

# Task3
#
from datetime import date
input_name_age = input("Put in your data here (in this format - Name Surname*1888-01-01*1999-01-01): ")
splitting_input = input_name_age.split("*")
d0 = date.fromisoformat(splitting_input[1])
d1 = date.fromisoformat(splitting_input[2])
delta = (d1 - d0)
age_var = int(delta.days)/365

print("Full name: " + splitting_input[1] + "\n" + "Age: " + str(age_var))


#end of homework

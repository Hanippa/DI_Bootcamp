# 🌟 Exercise 1: Import
# Instructions

#     In a file named func.py create a function that adds 2 number, and prints the result
#     In a file namedexercise_one.py import and the function

# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn






############### DONE IN SEPERATE FILES ################









# 🌟 Exercise 2: Random Module
# Instructions

#     Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
#         if it’s the same number, display a success message to the user, else don’t.




import random
def randran(num):
    rand = random.randint(0, 100)
    if rand == num:
        print("success its the same number ",rand)
randran(22)







# 🌟 Exercise 3: String module
# Instructions

#     Generate random String of length 5
#     Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
#     Hint: use the string module

import string
print(random.choice(string.ascii_letters) , end="") 
print(random.choice(string.ascii_letters) , end="") 
print(random.choice(string.ascii_letters) , end="") 
print(random.choice(string.ascii_letters) , end="") 
print(random.choice(string.ascii_letters)) 


# datetime module



# 🌟 Exercise 4 : Current Date
# Instructions

#     Create a function that displays the current date.
#     Hint : Use the datetime module.


import datetime
def curdate():
    return datetime.date.today()
print(curdate())



# Exercise 5 : Amount of time left until January 1st
# Instructions

#     Create a function that displays the amount of time left from now until January 1st.
#     (Example: the 1st of January is in 10 days and 10:34:01hours).

def newyear():
    return (datetime.date(2024,1,1) - curdate()).days
print(newyear())

# Exercise 6 : Birthday and minutes
# Instructions

#     Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def birthday(birthdate):
    return (curdate() - birthdate).days*1440
print(birthday(datetime.date(2003,10,14)))
# Exercise 7 : Upcoming Holiday
# Instructions

#     Write a function that displays today’s date.
#     The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
#     Hint: Start by hardcoding the datetime and name of the upcoming holiday.

def holiday():
    passover = (datetime.date(2023,4,5) - curdate()).days
    purim =( datetime.date(2024,3,25) - curdate()).days
    hanuka = (datetime.date(2023,12,7) - curdate()).days
    roshhashana =(datetime.date(2023,9,15) - curdate()).days
    hlist = [purim,passover,hanuka,roshhashana]
    print(sorted(hlist)[0], "days until closest holiday")
holiday()
# Exercise 8 : How Old Are You On Jupiter?
# Instructions

#     Given an age in seconds, calculate how old someone would be on:
#         Earth: orbital period 365.25 Earth days, or 31557600 seconds
#         Mercury: orbital period 0.2408467 Earth years
#         Venus: orbital period 0.61519726 Earth years
#         Mars: orbital period 1.8808158 Earth years
#         Jupiter: orbital period 11.862615 Earth years
#         Saturn: orbital period 29.447498 Earth years
#         Uranus: orbital period 84.016846 Earth years
#         Neptune: orbital period 164.79132 Earth years

# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.


def age(date):
    return f"""
Eearth : {(curdate() - date).days/365.25}
Mercury : {(curdate() - date).days/(365.25*0.2408467)}
Venus : {(curdate() - date).days/(365.25*0.61519726)}
Mars : {(curdate() - date).days/(365.25*1.8808158)}
Jupiter : {(curdate() - date).days/(365.25*11.862615)}
Saturn : {(curdate() - date).days/(365.25*29.447498)}
Uranus : {(curdate() - date).days/(365.25*84.016846)}
Neptune : {(curdate() - date).days/(365.25*164.79132)}  
    """
print(age(datetime.date(2000,1,1)))

# Exercise 9 : Faker Module
# Instructions

#     Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
#     Create an empty list called users. Tip: It should be a list of dictionaries.
#     Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker
dictex = {"name" : "" , "address": "", "language_code":"",}
users = []

def adddict():
    fake = Faker()
    users.append({ "name":fake.name() , "address":fake.address() , "language_code":fake.user_agent()})

adddict()
adddict()
adddict()
adddict()
print(users)

# Exercise 7 : Odd or Even
# Instructions

#     Write code that asks the user for a number and determines whether this number is odd or even.

user_number = int(input("Enter a number and I will tell you if its even or not"))
if not(user_number % 2):
    print("Your number is Even!")
else:
    print("Your number is Odd!")
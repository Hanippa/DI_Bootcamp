# Exercise 2 : What is the Season ?
# Instructions

#     Ask the user to input a month (1 to 12).
#     Display the season of the month received :
#         Spring runs from March (3) to May (5)
#         Summer runs from June (6) to August (8)
#         Autumn runs from September (9) to November (11)
#         Winter runs from December (12) to February (2)

month = int(input("Enter a month number: "))
if month == 12 or month in range(1 , 3):
    print("Winter")
if month in range(3 , 6):
    print("Spring")
if month in range(6 , 9):
    print("Summer")
if month in range(9 , 12):
    print("Autumn")

# Instructions

#     Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#     Display a little cake as seen below:

#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !


birthday_cake = """       ___________
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~"""

date_of_birth = input("What is your date of birth? (DD/MM/YYYY) : ")
age = int(str(2023 - int(date_of_birth[6:]))[-1]) 
birthday_cake = birthday_cake[:((4-age//2)+8)] + ("i" * age) +birthday_cake[((4-age//2)+8)+age:]
print(birthday_cake)

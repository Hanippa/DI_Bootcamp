# 🌟 Exercise 9 : Tall enough to ride a roller coaster
# Instructions

#     Write code that will ask the user for their height in inches.
#     If they are over 145cm print a message that states they are tall enough to ride.
#     If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("What is your height in cm? "))
if height > 145:
    print("Nice, You are tall enough, Enjoy ")
elif height <= 145:
    print("You are not tall enough for this ride, come back next year when you grow a little taller!") 
#Exercise 1
# Place a comment next to each variable. The comments will:

#     Explain what each variable does
#     Find out the type of each
#     Format each variable into a print statement


cars = 100 #this line creates a cars variable type: Interger
space_in_a_car = 4.0 #this line creates a space_in_car variable type: Float
drivers = 30 #this line creates a drivers variable type: Interger
passengers = 90 #this line creates a passenger variable type: Interger
cars_not_driven = cars - drivers #this line creates a cars_not_driven that is a subtruction of two interger variables. variable type: Interger
cars_driven = drivers #this line creates a cars_driven which takes the value from the drivers interger variable. variable type: Interger
carpool_capacity = cars_driven * space_in_a_car #this line creates a carpool_capacity that is a multipication of an interger and a float. variable type: float
average_passengers_per_car = passengers / cars_driven #this line creates a average_passengers_per_car that is a devistion of two interger variables. variable type: Interger


print(f"There are {cars} cars available.")
print(f"There are only {drivers }drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")

#Exercise 2
# Analyze the code below and predict what the outcome will be. Check the results in your python shell.
age = input("How old are you? ")
print("You are {} years old".format(age))

#predicted result = You are 19 years old
#result = You are 19 years old
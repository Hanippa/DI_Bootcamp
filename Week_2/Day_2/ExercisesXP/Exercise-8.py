# Exercise 8: Who ordered a pizza ?
# Instructions

#     Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#     As they enter each topping, print a message saying you’ll add that topping to their pizza.
#     Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

total_price = 10
toppingslist = []
topping = ""
while True:
    topping = input("Nice, you are almost there, what toppings do you want on your pizza?")
    toppingslist.append(topping)
    if topping == "quit":
        break
    total_price += 1
    print(toppingslist)

print(f"The toppings you chose are {tppingslist} and the total price for your pizza is : {total_price}")
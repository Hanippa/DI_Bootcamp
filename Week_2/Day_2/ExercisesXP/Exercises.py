# 🌟 Exercise 1 : Set
# Instructions

#     Create a set called my_fav_numbers with all your favorites numbers.
#     Add two new numbers to the set.
#     Remove the last number.
#     Create a set called friend_fav_numbers with your friend’s favorites numbers.
#     Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {2 , 6 , 7 , 8}
my_fav_numbers = my_fav_numbers.union({3 , 0})
my_fav_numberslist = list(my_fav_numbers)
my_fav_numberslist.pop(-1)
print(set(my_fav_numberslist))




# 🌟 Exercise 2: Tuple
# Instructions

#     Given a tuple which value is integers, is it possible to add more integers to the tuple?
#No


# 🌟 Exercise 3: List
# Instructions

# Using this list 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#     Remove “Banana” from the list.
#     Remove “Blueberries” from the list.
#     Add “Kiwi” to the end of the list.
#     Add “Apples” to the beginning of the list.
#     Count how many apples are in the basket.
#     Empty the basket.
#     Print(basket)

basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(0, "Apple")
basket.append("Kiwi")
print(basket.count("Apple"))
basket.clear()
print(basket)

# 🌟 Exercise 4: Floats
# Instructions

#     Recap – What is a float? What is the difference between an integer and a float?
#     Can you think of another way to generate a sequence of floats?
#     Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
 
float_list = []
for i in range(0 , 8):
    float_list.append((i+3 )/2)
print(float_list)

# 🌟 Exercise 5: For Loop
# Instructions

#     Use a for loop to print all numbers from 1 to 20, inclusive.
#     Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(0 , 20):
    print("index: ",i+1)
    if ((i+1) % 2) == 0:
        print(i+1 , "is an Even number")


# 🌟 Exercise 6 : While Loop
# Instructions

#     Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
while True:
    if input("What is your name? : ") == "Dekel":
        break


# 🌟 Exercise 7: Favorite fruits
# Instructions

#     Ask the user to input their favorite fruit(s) (one or several fruits).
#     Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
#     Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#     Now that we have a list of fruits, ask the user to input a name of any fruit.
#         If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#         If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.


favorite_fruits = input("Pick your favorite fruits! (sperate them with a space) : ").split()
if favorite_fruits.index(input("Pick a fruit! : ")):
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("Your chose a new fruit. I hope you enjoy")
    
    
# Exercise 8: Who ordered a pizza ?
# Instructions

#     Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#     As they enter each topping, print a message saying you’ll add that topping to their pizza.
#     Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).



total_price = 10
toppingslist = []
while True:
    topping = input("Nice, you are almost there, what toppings do you want on your pizza?")
    if topping == "quit":
        break
    else:
        print(f"Added {topping} to your toppings!")
        total_price += 2.5
        toppingslist.append(topping)
print(f"\n \n The toppings you chose are {toppingslist} and the total price for your pizza is : {total_price}")


# Exercise 1 : What are you learning ?
# Instructions

#     Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
#     Call the function, and make sure the message displays correctly.


def display_message(name):
    return f"Hi i'm {name} what i am learning in this section of the course is how to use functions!"
print(display_message("Dekel"))

# 🌟 Exercise 2: What’s your favorite book ?
# Instructions

#     Write a function called favorite_book() that accepts one parameter called title.
#     The function should print a message, such as "One of my favorite books is <title>".
#     For example: “One of my favorite books is Alice in Wonderland”
#     Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title:str):
    return f"Hi one of my favorite books is {title}"
print(favorite_book("Life and suffering"))

# 🌟 Exercise 3 : Some Geography
# Instructions

#     Write a function called describe_city() that accepts the name of a city and its country as parameters.
#     The function should print a simple sentence, such as "<city> is in <country>".
#     For example “Reykjavik is in Iceland”
#     Give the country parameter a default value.
#     Call your function.

def describe_city(city_name, country_name="USA"):
    return f"{city_name} is one of the best cities in the world and it is located in the country of {country_name}"
print(describe_city("beijing","china"))

# Exercise 4 : Random
# Instructions

#     Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
#     Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random
def random_compare(num:int) -> str:
    random_num = random.randint(0, 5)
    print("Nice! both numbers are the same! ") if  random_num==num else print(f"The number does not match :( your number: {num} The random number {random_num}")
random_compare(input("Write a number between 0 and 100 : "))


# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Instructions

#     Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#     The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
#     Call the function make_shirt().

#     Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
#     Make a large shirt with the default message
#     Make medium shirt with the default message
#     Make a shirt of any size with a different message.

#     Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(msg:str="I love python", size:str="large"):
    print(f"The size of the shirt is {size} and the text is {msg}")
make_shirt()
make_shirt(size="medium")
make_shirt("Paint it Black", "small")

# 🌟 Exercise 6 : Magicians …
# Instructions

#     Using this list of magician’s names.magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#     Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
#     Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
#     Call the function make_great().
#     Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magincians() -> None:
    print([name for name in magician_names])
show_magincians()
def make_great():
    for i,value in enumerate(magician_names):
        magician_names[i] += " The Great"
    return magician_names
make_great()
show_magincians()

# 🌟 Exercise 7 : Temperature Advice
# Instructions

#     Create a function called get_random_temp().
#         This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#         Test your function to make sure it generates expected results.

#     Create a function called main().
#         Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#         Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

#     Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#         below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#         between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#         between 16 and 23
#         between 24 and 32
#         between 32 and 40

#     Change the get_random_temp() function:
#         Add a parameter to the function, named ‘season’.
#         Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#         Now that we’ve changed get_random_temp(), let’s change the main() function:
#             Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#             Use the season as an argument when calling get_random_temp().

#     Bonus: Give the temperature as a floating-point number instead of an integer.
#     Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

import random
def get_random_temp(season:str):
    if season == "winter":
        return random.uniform(-10.0, 16.0)
    if season == "spring":
        return random.uniform(0, 23)
    if season == "fall":
        return random.uniform(15, 27)
    if season == "summer":
        return random.uniform(23, 40)
def main():
    user_season = input("What is the season : ")
    temperature = get_random_temp(user_season)
    print(f"Hello!, the temrature is {temperature} degrees celcius. I hope you'll have lovely day!")
    if temperature < 0:
        print("brrr its freezing cloth yourself properly!")
    elif temperature < 16:
        print("Its pretty cold, get something warm!")
    elif temperature < 23:
        print("Its a little cold, chose your clothes wisely!")
    elif temperature < 32:
        print("Its a little warm, you should go outside and enjoy the weather!")
    elif temperature <= 40:
        print("Its way too hot, I suggest you stay indoors and if you do go outside wear sunskin!")
main()
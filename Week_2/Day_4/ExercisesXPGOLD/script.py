# Exercise 1 : When will I retire ?
# Instructions

# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

#     Create a function get_age(year, month, day)
#     Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
#     After calculating the age of a person, the function should return the age (the age is an integer).
#     Create a function can_retire(gender, date_of_birth).
#     It should call the get_age function (with what arguments?) in order to receive an age.
#     Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
#     Calculate. You may need to do a little more hard-coding here.
#     Return True if the person can retire, and False if he/she can’t.

# Some Hints

#     Ask for the user’s gender as “m” or “f”.
#     Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
#     Call can_retire to get a definite value for whether the person can or can’t retire.
#     Display a message informing the user whether they can retire or not.
#     As always, test your code to ensure it works.

date = {"year":2023 , "month":3 , "day":29}
def get_age(year, month, day):
    return date["year"] - year - ((date["month"], date["day"]) < (month, day))
print(get_age(2000, 10, 10))

def can_retire(gender, year , month , day):
    if gender == "female" and get_age(year, month , day) > 61:
        return "Can retire"
    elif gender == "female":
        return "Can't retire"
    if gender == "male" and get_age(year, month, day) >66:
        return "Can retire"
    elif gender == "male":
        return "Can't retire"
gender = input("Hello welcome to the retirment checking system! Please type your gender to start! : ")
dob = input("What is your date of birth?(dd/mm/yyyy) : ")
print(f"we got the results for you, you {can_retire(gender, int(dob[6:10]),int(dob[3:5]), int(dob[0:2]))}...")

# Exercise 2 : Sum
# Instructions

#     Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.

# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

def ducplicator(x:int , limit:int):
    result = 0
    x_str = ""
    for i in range(limit):
        x_str += str(x)
        result += int(x_str)
    return result
print(ducplicator(3 , 4))


# Exercise 3 : Double Dice
# Instructions

#     Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
#     Create a function called throw_until_doubles.
#         It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
#         For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
#         This function should return the number of times it threw the dice in total. In the example above, it should return 3.

#     Create a main function.
#     It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).

#     After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
#     Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.

#     For example:
#         If the results of the throws were as follows (your code would do 100 doubles, not just 3):
#             (1, 2), (3, 1), (5, 5)
#             (3, 3)
#             (2, 4), (1, 2), (3, 4), (2, 2)

#         Then my output would show something like this:
#             Total throws: 8
#             Average throws to reach doubles: 2.67.

import random
def throw_dice():
    return random.randint(1,6)

def throw_until_doubles():
    count = 0
    dice1 = throw_dice()
    dice2 = throw_dice()
    while dice1 != dice2:
        dice1 = throw_dice()
        dice2 = throw_dice()
        print("|",dice1,"|   |",dice2,"|")
        count += 1
    print(f"You got double! with {count} tries")
    return count
def main():
    total_tries = 0
    for i in range(100):
        total_tries += throw_until_doubles()
    print(f"total dice throws {total_tries} \n average throws to reach double {total_tries/100}")
main()
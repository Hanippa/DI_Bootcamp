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
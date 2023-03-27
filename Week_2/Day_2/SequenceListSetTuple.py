# Exercise 1


# Given this list:

list1 = [5, 10, 15, 20, 25, 50, 20]

# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# Hint : Look at the index method

if 20 in list1:
    list1[list1.index(20)] = 200
    print(list1)

# Exercise 2


# Unpack the following tuple into 4 variables

a_tuple = (10, 20, 30, 40)

(a , b , c , d) = a_tuple
print(a , b , c ,d)
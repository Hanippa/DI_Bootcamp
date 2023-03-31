# Exercise 1
# Instructions

#     Draw the following pattern using for loops:

#   *
#  ***
# *****


#     Draw the following pattern using for loops:

#     *
#    **
#   ***
#  ****
# *****


#     Draw the following pattern using for loops:

# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
print("\n")
print("pattern #1")
print("\n")
for i in range(3):
    print(" "*(4-i),"*"*(i+1*i+1))

print("\n")
print("pattern #2")
print("\n")

for i in range(5):
    print(" "*(4-i),"*"*(i+1))

print("\n")
print("pattern #3")
print("\n")

for i in range(5):
    print("*"*(i+1))
for i in range(5):
    print(" "*(i),"*"*(5-i))

print("\n")


# Exercise 2
# Instructions

#     Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233]                                               #// Initlizes a list with a simingly random set of numbers. 
for i in range(len(my_list) - 1):                                             #// Starts a for loop with a range of 0 to the langth of the array (5) minus 1 (4).
    minimum = i                                                               #// sets a new variable that will take the value of i each loop iteration.
    for j in range( i + 1, len(my_list)):                                     #// Starts another for loop in range of the i value plus 1 (2 ++) to the length of the array (5)
        if(my_list[j] < my_list[minimum]):                                    #// If statement, if the array in the j position is smaller then the array in the position of j(index of second loop)
            minimum = j                                                       #// sets the minimum variable as the j index value
            if(minimum != i):                                                 #// If statement, if the minimum variable is not equal to the main index i 
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]   #// Sets the array at index i as the array in index minimum, and sets the array at index minimum to the array at index i. what this does is moves the new found minimum number to the first spot and the old one to the left spot.
print(my_list)                                                                #// What this program does is sort a list from the lowest number to the highest.

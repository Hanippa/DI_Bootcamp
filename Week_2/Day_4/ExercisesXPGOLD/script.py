# Exercise 2 : Sum
# Instructions

#     Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.

# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

def  ducplicator(x:int , limit:int):
    result = 0
    x_str = ""
    for i in range(limit):
        x_str += str(x)
        result += int(x_str)
    return result
print(ducplicator(3 , 4))
    
# Exercise 1
# Instructions

#     Write a script that inserts an item at a defined index in a list.


word_list = ["one","two","three"]
word_list.insert(3, "four")
print("Exercise 1 : ",word_list)

# Exercise 2
# Instructions

#     Write a script that counts the number of spaces in a string.

string = "notice the contradiction"
print("Exercise 2 : ",string.count(" "))

# Exercise 3
# Instructions

#     Write a script that calculates the number of upper case letters and lower case letters in a string.

string = "Capital Owners Love This"
string_cap = [x for x in string if x.isupper()]
print("Exercise 3 : ",len(string_cap) , len(string) - len(string_cap))

# Exercise 4
# Instructions

# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12

def my_sum(array):
    array[0] = array[0]+array[1]
    del array[1]
    if len(array) >= 2:
        my_sum(array)
    return array
print("Exercise 4 : ",my_sum([1,5,4,5])[0])

# Exercise 5
# Instructions

# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50

def my_max(array):
    if array[0] > array[1]:
        del array[1]
    else:
        del array[0]
    if len(array) >= 2:
        my_max(array)
    return array
print("Exercise 5 : ",my_max([5, 10, 15, 20, 25, 30, 35, 40, 45])[0])

# Exercise 6
# Instructions

# Write a function that returns factorial of a number

#     >>>factorial(4)
#     >>>24

def factorial(number):
    final = 1
    for i in range(1, number):
        final += final * i
    return final
print("Exercise 6 : ",factorial(5))


# Exercise 7
# Instructions

# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2


def count_char(array , char):
    count = 0
    for i in range(len(array)):
        if array[i] == char:
            count += 1
    return count
print("Exercise 7 : ",count_char("All it takes to know what being free means is to look at the sky" , 'o'))


# Exercise 8
# Instructions

# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3

def l2norm(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]**2
    return sum**0.5
print("Exercise 8 : ",l2norm([1,2,2]))

# Exercise 9
# Instructions

# Write a function to find if an array is monotonic (sorted either ascending of descending)

#     >>>is_mono([7,6,5,5,2,0])
#     >>>True

#     >>>is_mono([2,3,3,3])
#     >>>True

#     >>>is_mono([1,2,0,4])
#     >>>False

def is_mono(array):
    if array[0] > array[1]:
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                return False
    elif array[0] < array[1]:
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return False
    return True
print("Exercise 9 : ",is_mono([2,3,3,3]))

# Exercise 10
# Instructions

#     Write a function that prints the longest word in a list.

def longstring(array):
    if len(array[0]) > len(array[1]):
        del array[1]
    else:
        del array[0]
    if len(array) >= 2:
        longstring(array)
    return array
print("Exercise 10 : ",longstring(["Thors", "Thorkel", "Thorfin", "Helga", "Iceland", "Norway","TheKingOfWales"])[0])

# Exercise 11
# Instructions

#     Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

people_array = ["a","b",1,"f",9,20]
num_list = []
word_list = []
for i in range(len(people_array)):
    if type(people_array[i]) == str:
        word_list.append(people_array[i])
    elif type(people_array[i]) == int:
        num_list.append(people_array[i])
print("Exercise 11 : ",num_list , word_list)

# Exercise 12
# Instructions

# Write a function to check if a string is a palindrome:

#     >>>is_palindrome('radar')
#     >>>True

#     >>>is_palindrome('John)
#     >>>False

def palindrome(string):
    if string == string[::-1]:
        return True
    return False
print("Exercise 11 : ", palindrome("radar"))


# Exercise 13
# Instructions

# Write a function that returns the amount of words in a sentence with length > k:

#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3

def count_long(string , k):
    count = 0
    string_array = string.split(" ")
    for i in range(len(string_array)):
        if len(string_array[i]) > k:
            count += 1
    return count
print("Exercise 13 : ",count_long("Do or do not there is no try" , 2))

# Exercise 14
# Instructions

# Write a function that returns the average value in a dictionary (assume the values are numeric):

#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3

def dict_avg(dictionary:dict()):
    sum = 0
    for i in dictionary.values():
        sum += i
    return sum/len(dictionary)
print("Exercise 14 : ",dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

# Exercise 15
# Instructions

# Write a function that returns common divisors of 2 numbers:

#     >>>common_div(10,20)
#     >>>[2,5,10]


def common_div(num1 , num2):
    num1_set = set()
    num2_set = set()
    for i in range(2, num1+1):
        if not(num1%i):
            num1_set.add(i)
    for i in range(2, num2+1):
        if not(num2%i):
            num2_set.add(i)
    return list(num1_set.intersection(num2_set))
print("Exercise 15 : ",common_div(40,60))

# Exercise 16
# Instructions

# Write a function that test if a number is prime:

#     >>>is_prime(11)
#     >>>True

def is_prime(number):
    if number == 1:
        return False
    for i in range(2,number):
        if not(number%i):
            return False
    return True
print("Exercise 16 : ",is_prime(1))


# Exercise 17
# Instructions

# Write a function that prints elements of a list if the index and the value are even:

#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]

def weird_print(array):
    return [a for i , a in enumerate(array) if i%2 == 0 and a%2 == 0]

print("Exercise 17 : " , weird_print([1,2,2,3,4,5]))


# Exercise 18
# Instructions

# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2


def type_count(**kwargs):
    type_dict = {int:0,str:0,float:0,bool:0}
    for i in kwargs.values():
        type_dict[type(i)] += 1 
    return type_dict
print("Exercise 18 : ",type_count(a=1,b='string',c=1.0,d=True,e=False,f=False))


# Exercise 19
# Instructions

#     Write a function that mimics the builtin .split() method for strings.
#     By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.


def string_split(word ,char):
    word_list = []
    for i in range(word.count(char)):
        word_list.append(word[:word.index(char)])
        word = word[word.index(char)+len(char):]
    word_list.append(word)
    return word_list
print("Exercise 19 : ",string_split("welcomeabctoabctheabcjungle", "abc"))

# Exercise 20
# Instructions

#     Convert a string into password format.

# Example:
# input : "mypassword"
# output: "***********"

pass_input = "mypassword"
pass_input = list(pass_input)
for i in range(len(pass_input)):
    pass_input[i]='*'
print("Exercise 19 : ",''.join(pass_input))
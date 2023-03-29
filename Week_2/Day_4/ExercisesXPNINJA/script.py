# Exercise 1 : What’s your name ?
# Instructions

#     Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
#     middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.

# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(first_name , last_name , *middle_name):
    if middle_name:
        return first_name + " " + middle_name[0] + " " + last_name
    else:
         return first_name + " " + last_name
print(get_full_name("Luffy", "Monkey","D."))


# Exercise 2 : From English to Morse
# Instructions

#     Write a function that converts English text to morse code and another one that does the opposite.
#     Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.

morse_dict = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."," ":"/"}

def to_morse(string:str) -> str:
    morse = ""
    for i in string:
        morse += morse_dict[i] + " "
    return morse
def from_morse(string:str) -> str:
    text = ""
    seperated_string = string.split(" ")
    for i in range(len(seperated_string)):
        for j in morse_dict.keys():
            if morse_dict[j] == seperated_string[i]:
                text += j
    return text
user_choice = input("encrypt or decrypt? : ")
if user_choice == "encrypt":
    data = input("Text to encrypt : ").lower()
    print(to_morse(data))
elif user_choice == "decrypt":
    data = input("Text to decrypt : ")
    print(from_morse(data))

# Exercise 3 : Box of stars
# Instructions

#     Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
#     For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

def box_printer(*string):
    word = ""
    longest =  len(max(string, key=len))
    print("*"*(longest+4))
    for word in string:
        word = "* " + word + " "*(longest - len(word)) + " *"
        print(word)
    print("*"*(longest+4))  

box_printer("Brook","Luffy","Nami","Franky","Usopp","Robin","Sanji","Zoro","Chopper","iiiiiiiiiiiiiiiiiiii")


# Exercise 4

#     Analyse this code before executing it. What is the purpose of this code?

# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

############# ANSWER ###############

# The purpose of the function is to sort the number by value, it checks the value of the number before index each iteration and sorts 2 by 2.

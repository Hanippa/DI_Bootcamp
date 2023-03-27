# Instructions
# Challenge 1

#     Ask the user for a number and a length.
#     Create a program that prints a list of multiples of the number until the list length reaches length.

# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number_list = []
user_number = int(input("Please enter a number : "))
user_length = int(input("Please enter length : "))
for i in range(0 , user_length):
    number_list.append(user_number * i)
print(number_list)


# Challenge 2

#     Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
final_string = ""
user_string = input("Plese enter a string : ")
for i in range(0 , len(user_string)):
    if not(user_string[i] == user_string[i-1]):
        final_string += user_string[i]
print(final_string)

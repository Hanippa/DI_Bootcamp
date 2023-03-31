# Instructions

#     Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#     Use List Comprehension

# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world



user_string = input("Enter a comma seperated list of words : ")
user_string_array = user_string.split(",")
user_string_array.sort()
print(''.join([word + "," for word in user_string_array])[:-1])
# for word in user_string_array:
#     print(word + ",",end="")

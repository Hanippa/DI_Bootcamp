# Instructions

# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

result = ""
user_choice = input("Do you want to encrypt or decrypt? : ")
if user_choice == "encrypt":
    data = input("data to ecrypt : ")
    offset = input("encryption offset : ")
    for i in data:
        if i == ' ':
            result += ' '
        else:
            result += chr(ord(i) + int(offset))
elif user_choice == "decrypt":
    data = input("data to decrypt : ")
    offset = input("encryption offset : ")
    for i in data:
        if i == ' ':
            result += ' '
        else:
            result += chr(ord(i) - int(offset))
print(result)
# 🌟 Exercise 1 – Random Sentence Generator
# Instructions

# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

#     Download this word list

#     Save it in your development directory.

#     Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

#     Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
#         use the words list to get your random words.
#         the amount of words should be the value of the length parameter.

#     Take the random words and create a sentence (using a python method), the sentence should be lower case.

#     Create a function called main which will:
#         Print a message explaining what the program does.

#         Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
#             If the user inputs incorrect data, print an error message and end the program.
#             If the user inputs correct data, run your code.

import random
import re

wordlist = "Week_3\Day_4\ExercisesXP\sowpods.txt"
# with open(wordlist,'r') as wordlist:
#     wordlist.read()
def get_words_from_file():
    with open(wordlist,'r') as wlist:
        f = wlist.read()
    return f.split("\n")
def get_random_sentence(length):
    sentence = ""
    random_word_list = get_words_from_file()
    for i in range(length):
        sentence += random.choice(random_word_list) + " "
    return sentence
def main():
    print("This program !@  \n")
    user_in = int(input("How long do you want the sentence to be? : "))
    if isinstance(user_in, int) and  20 >= user_in > 1:
        print(get_random_sentence(user_in))
    else:
        raise ValueError("Value does not meet the requirements (2-20)")

print(get_random_sentence(4))
main()


# 🌟 Exercise 2: Working with JSON
# Instructions

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


#     Access the nested “salary” key from the JSON-string above.
#     Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
#     Save the dictionary as JSON to a file.
 
loaded_json = json.loads(sampleJson)
print(loaded_json["company"]["employee"]["payable"]["salary"])
loaded_json["company"]["employee"]["birthdate"] = ""
with open("company", 'w') as file_obj:
    json.dump(loaded_json, file_obj)

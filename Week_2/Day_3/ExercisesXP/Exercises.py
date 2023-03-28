# 🌟 Exercise 1 : Convert lists into dictionaries
# Instructions

#     Convert the two following lists, into dictionaries.
#     Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# # Expected output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


dictionary = list(zip(keys , values))
print(dict(dictionary))



# 🌟 Exercise 2 : Cinemax
# Instructions

#     A movie theater charges different ticket prices depending on a person’s age.
#         if a person is under the age of 3, the ticket is free.
#         if they are between 3 and 12, the ticket is $10.
#         if they are over the age of 12, the ticket is $15.

#     Given the following object:

#     How much does each family member have to pay ?
#     Print out the family’s total cost for the movies.
#     Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


family = {}
user_name = input("What is your name?(type quit to complete) : ")
if user_name != "quit":
    user_age = input("What is your age? : ")
while user_name != "quit":
    if True:
        break
    family[user_name] = int(user_age)
    user_name = input("What is your name?(type quit to complete) : ")
    if user_name != "quit":
        user_age = input("What is your age : ")
for key,value in family.items():
    if value > 3:
        print(f"{key} you have to pay 10$ ") if value > 3 and value <= 12 else print(f"{key} you have to pay 15$")
    else:
        print(f"{key} you have to pay 0$ ")

# 🌟 Exercise 3: Zara
# Instructions

#     Here is some information about a brand.

#     name: Zara 
#     creation_date: 1975 
#     creator_name: Amancio Ortega Gaona 
#     type_of_clothes: men, women, children, home 
#     international_competitors: Gap, H&M, Benetton 
#     number_stores: 7000 
#     major_color: 
#         France: blue, 
#         Spain: red, 
#         US: pink, green


#     2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
#     3. Change the number of stores to 2.
#     4. Print a sentence that explains who Zaras clients are.
#     5. Add a key called country_creation with a value of Spain.
#     6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
#     7. Delete the information about the date of creation.
#     8. Print the last international competitor.
#     9. Print the major clothes colors in the US.
#     10. Print the amount of key value pairs (ie. length of the dictionary).
#     11. Print the keys of the dictionary.
#     12. Create another dictionary called more_on_zara with the following details:

#     creation_date: 1975 
#     number_stores: 10 000



#     13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
#     14. Print the value of the key number_stores. What just happened ?



brand = {
    "name" : "Zara",
    "creation_date" : "1975",
    "creator_name" : "Amancio Ortega Gaona",
    "type_of_clothes" : "men, women, children, home",
    "international_competitors" : ("Gap" , "H&M" , "Benetton"),
    "number_of_stores" : "7000",
    "major_color" : {"France" : "blue","Spain" : "red" , "US" : "pink, green"}
}

brand["number_of_stores"] = "2"
print(f"{brand['name']}'s Clients are {brand['type_of_clothes']}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand.keys():
    brand["international_competitors"] += ("Desigual",)
brand["creation_date"] = ""
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

more_on_zara = {"creation_date" : "1975" , "number_of_stores" : "10000"}
brand.update(more_on_zara)
print(brand["number_of_stores"])







# Exercise 4 : Disney characters
# Instructions

# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


#     Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
#     Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
#     Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
#     Only recreate the 1st result for:
#         The characters, which names contain the letter “i”.
#         The characters, which names start with the letter “m” or “p”.
users_dict = {}
for i in range(len(users)):
    users_dict[i] = users[i]
print(users_dict)

users_dict = {}
for i in range(len(users)):
    users_dict[users[i]] = i
print(users_dict)

users.sort()
users_dict = {}
for i in range(len(users)):
    users_dict[users[i]] = i
print(users_dict)


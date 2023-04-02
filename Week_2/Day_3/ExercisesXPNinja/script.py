# Exercise 1 : Cars
# Instructions

#     Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
#     Convert it into a list using Python (don’t do it by hand!).
#     Print out a message saying how many manufacturers/companies are in the list.
#     Print the list of manufacturers in reverse/descending order (Z-A).
#     Using loops or list comprehension:
#         Find out how many manufacturers’ names have the letter ‘o’ in them.
#         Find out how many manufacturers’ names do not have the letter ‘i’ in them.

#     Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
#         Remove these programmatically. (Hint: you can use set to help you).
#         Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

#     Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.


list_string = list("Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(","))
print(f"There are {len(list_string)} companies!")
list_string.reverse()
print(list_string)
print(f"There are {len([x for x in list_string if 'o' in x])} companies with the letter o")
print(f"There are {len([x for x in list_string if 'i' not in x])} companies without the letter i")
list_string_dup = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
for inx , i in enumerate(list_string_dup):
    if list_string_dup.count(i) > 1:
        del list_string_dup[inx]
print(list_string_dup)

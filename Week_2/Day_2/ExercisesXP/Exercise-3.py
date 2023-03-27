# 🌟 Exercise 3: List
# Instructions

# Using this list 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#     Remove “Banana” from the list.
#     Remove “Blueberries” from the list.
#     Add “Kiwi” to the end of the list.
#     Add “Apples” to the beginning of the list.
#     Count how many apples are in the basket.
#     Empty the basket.
#     Print(basket)

basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(0, "Apple")
basket.append("Kiwi")
print(basket.count("Apple"))
basket.clear()
print(basket)

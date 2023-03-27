# 🌟 Exercise 5: For Loop
# Instructions

#     Use a for loop to print all numbers from 1 to 20, inclusive.
#     Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(0 , 20):
    print("index: ",i+1)
    if ((i+1) % 2) == 0:
        print(i+1 , "is an Even number")
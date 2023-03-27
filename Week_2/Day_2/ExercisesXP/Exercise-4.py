# 🌟 Exercise 4: Floats
# Instructions

#     Recap – What is a float? What is the difference between an integer and a float?
#     Can you think of another way to generate a sequence of floats?
#     Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
 
float_list = []
for i in range(0 , 8):
    float_list.append((i+3 )/2)
print(float_list)
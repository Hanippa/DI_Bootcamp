import re
# Instructions

# Given a “Matrix” string:

#     7i3
#     Tsi
#     h%x
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!


# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns, like here:
# 7 	i 	3
# T 	s 	i
# h 	% 	x
# i 		#
# s 	M 	
# $ 	a 	
# # 	t 	%
# ^ 	r 	!


# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if/else statements to check the data
# ● String for the output of the secret message



#String to enter (same string given but without new lines(it breaks the terminal))
# 7i3Tsih%xi #sM $a #t%^r!

def string_to_matrix(string : str) -> list():
    string_list = list(string)
    list_1 = []
    for i in range(0, len(string_list)-2 , 3):
        list_1.append([string_list[i] , string_list[i+1] , string_list[i+2]])
    return list_1

def matrix_decode(list:list()) -> str:
    for j in range(3):
        for i in list:
            if re.search("([A-Za-z ])" , i[j]):
                print(i[j] , end='')
matrix = string_to_matrix(input("string : "))
matrix_decode(matrix)
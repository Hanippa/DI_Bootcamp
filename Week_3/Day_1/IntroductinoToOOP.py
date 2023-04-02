# Exercise

# Analyse the code below. What will be the ouput ?

# Explain the goal of the `__init__()` method // The goal of the init method is to initialize the object, gives it memory locations. and thus constructs the intial object.

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x) //3
# print("p.y is:", p.y) //4

print(Point.__dir__(int()))
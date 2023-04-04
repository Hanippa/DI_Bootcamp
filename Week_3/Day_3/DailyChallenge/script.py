# Instructions :

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

#     Compute the circle’s area
#     Print the circle and get something nice
#     Be able to add two circles together
#     Be able to compare two circles to see which is bigger
#     Be able to compare two circles and see if there are equal
#     Be able to put them in a list and sort them
class Circle:
    def __init__(self,radius=0.0,diameter=0.0):
        if diameter == 0.0:
            self.radius = radius
            self.diameter = radius*2
        if radius == 0.0:
            self.diameter = diameter
            self.radius = diameter/2
    def area(self):
        return 3.14*self.radius*self.radius
    def __str__(self):
        string = ""
        for i in range(1,4+1):
            string += "\n"
            string += "  "*(4-i)
            for j in range(4):
                string += "*"*i
        for i in range(4,0,-1):
            string += "\n"
            string += "  "*(4-i)
            for j in range(4):
                string += "*"*i
        return string + f"A circle with a radius of {self.radius}"
    def __repr__(self):
        return str(self.radius)
    def __add__(self,circle):
        return Circle(circle.radius+self.radius)
    def __eq__(self, o):
        return o.radius == self.radius
    def __gt__(self,o):
        return self.radius > o.radius
    def __lt__(self,o):
        return self.radius < o.radius

circle = Circle(radius=4)
circle2 = Circle(diameter=10)
print(circle>circle2)   
cirlist = [circle,circle2]
print(cirlist)
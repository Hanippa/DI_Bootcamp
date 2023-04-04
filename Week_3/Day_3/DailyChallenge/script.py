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

circle = Circle(radius=10)

print(circle.area())
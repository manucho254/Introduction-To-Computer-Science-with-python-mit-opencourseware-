"""
    Object oriented programming
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) **2
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    def __str__(self):
        """ Helps in representation of an object
        """
        return "<" + str(self.x) + ","+str(self.y)+">"

c = Coordinate(10, 20)
val = Coordinate(0, 0)
print(c.distance(val))
print(val)

print(type(c)) # checks the type of object
print(isinstance(c, Coordinate))
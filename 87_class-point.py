import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point(1, 2)
p2 = Point(4, 6)
print(f"Distance: {p1.distance(p2)}")  
















# The Point class represents a 2D point and includes a method
#  to calculate the distance to another point.


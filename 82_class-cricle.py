import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(4)
print(f"Area: {circle.area()}") 
print(f"Circumference: {circle.circumference()}")   
























# The Circle class calculates the area and circumference based on the radius attribute.
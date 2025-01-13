class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")  
print(f"Perimeter: {rect.perimeter()}")  



















# The Rectangle class has two attributes, length and width.
# The methods area() and perimeter() calculate the area and perimeter of the rectangle.

# The __init__ method in Python is a special method that is 
# automatically called when a new object of a class is created. 
# It's known as the constructor of the class.

# Purpose:
# The __init__ method is used to initialize the attributes 
# (or properties) of the newly created object.
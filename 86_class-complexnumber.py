class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)
print(c1 + c2)  
print(c1 - c2)  





















# The ComplexNumber class represents complex numbers and 
# overloads the + and - operators to allow addition and subtraction.

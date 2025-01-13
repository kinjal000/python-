class MyClass:
    def __init__(self, name):
        self.name = name
    
    def instance_method(self):
        return f"Instance method: {self.name}"
    
    @classmethod
    def class_method(cls):
        return "Class method"
    
    @staticmethod
    def static_method():
        return "Static method"

# Example usage
obj = MyClass("John")
print(obj.instance_method())  # Output: Instance method: John
print(MyClass.class_method())  # Output: Class method
print(MyClass.static_method())  # Output: Static method


















# The class_method() operates on the class, while static_method() operates without 
# needing the class or instance.

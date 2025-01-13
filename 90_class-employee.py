class Employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary
    
    def display_info(self):
        return f"Employee: {self.name}, ID: {self.ID}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, ID, salary, department):
        super().__init__(name, ID, salary)
        self.department = department
    
    def display_info(self):
        return f"Manager: {self.name}, ID: {self.ID},
          Salary: {self.salary}, Department: {self.department}"

emp = Manager("Alice", "M001", 50000, "Sales")
print(emp.display_info())



















# The Manager class inherits from Employee and adds an additional
#  attribute department. The display_info() method is overridden in the Manager class.

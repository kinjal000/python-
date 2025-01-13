class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Alice", "S001", [90, 80, 85])
print(f"Average grade: {student.average_grade()}") 




















# The Student class stores a student's name, ID, and grades. 
# The method average_grade() calculates the average of the grades.

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

name = input("Enter student name: ")

if name in grades:
    print(name, "grade:", grades[name])
else:
    print(name, "not found.")

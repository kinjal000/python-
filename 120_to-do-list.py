def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        print("Your tasks:")
        for task in tasks:
            print(task.strip())

while True:
    choice = input("1. Add Task 2. View Tasks 3. Exit: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break













    
# Explanation:

# This program allows the user to add tasks to a text file and view them later.
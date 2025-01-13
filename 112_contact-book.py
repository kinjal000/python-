def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")
    
    with open("contacts.txt", "a") as file:
        file.write(f"{name}, {number}, {email}\n")
    print("Contact added!")

def search_contact(name):
    with open("contacts.txt", "r") as file:
        for line in file:
            if name.lower() in line.lower():
                print(line)

while True:
    choice = input("Choose: 1. Add Contact 2. Search Contact 3. Exit: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        break





















    
# Explanation:

# The program allows users to add contacts to a file and search for them.
# add_contact() stores the contact in contacts.txt, and search_contact()
# looks for the contact by name in the file.
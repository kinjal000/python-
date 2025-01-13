
names = {"Alice", "Bob", "Charlie"}

name = input("Enter a name: ")
if name in names:
    print(name, "is in the set.")
else:
    print(name, "is not in the set.")

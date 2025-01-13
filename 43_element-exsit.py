
my_tuple = ('apple', 'banana', 'cherry')

element = input("Enter element to check: ")

if element in my_tuple:
    print(element, "exists in the tuple.")
else:
    print(element, "does not exist in the tuple.")

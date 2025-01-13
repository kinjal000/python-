
list1 = [int(x) for x in input("Enter first list of numbers: ").split()]
list2 = [int(x) for x in input("Enter second list of numbers: ").split()]

common_elements = list(set(list1) & set(list2))

print("Common elements:", common_elements)

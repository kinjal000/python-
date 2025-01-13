
list1 = [int(x) for x in input("Enter first list of numbers: ").split()]
list2 = [int(x) for x in input("Enter second list of numbers: ").split()]

elementwise_sum = [a + b for a, b in zip(list1, list2)]

print("Element-wise sum:", elementwise_sum)

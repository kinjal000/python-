
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

unique_numbers = list(set(numbers))

print("List without duplicates:", unique_numbers)

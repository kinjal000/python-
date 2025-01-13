
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)

print("Sum:", sum_numbers)
print("Average:", average)


numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

positive = sum(1 for x in numbers if x > 0)
negative = sum(1 for x in numbers if x < 0)
zero = sum(1 for x in numbers if x == 0)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

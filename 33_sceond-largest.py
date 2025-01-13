
numbers = [int(x) for x in input("Enter unique numbers separated by space: ").split()]

numbers.sort()
second_largest = numbers[-2]

print("Second largest:", second_largest)

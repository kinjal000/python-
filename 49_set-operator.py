
set1 = set(map(int, input("Enter first list of numbers: ").split()))
set2 = set(map(int, input("Enter second list of numbers: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

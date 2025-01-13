def count_occurrences(lst, x):
    return lst.count(x)

lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
x = int(input("Enter the number to count: "))
print(f"{x} appears {count_occurrences(lst, x)} times in the list.")

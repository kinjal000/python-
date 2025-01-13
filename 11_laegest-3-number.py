# Input three distinct numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Determine the largest number
if a > b and a > c:
    print(f"The largest number is {a}")
elif b > a and b > c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")





















# Compare each number with the others using if-elif conditions to find the largest.
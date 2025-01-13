
num = int(input("Enter a positive integer: "))

count = 0
while num > 0:
    num //= 10
    count += 1

print(f"The number has {count} digits.")

























# Use a loop to divide the number by 10 until it becomes 0, counting each step.
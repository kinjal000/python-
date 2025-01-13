
num = int(input("Enter a positive integer: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"The reversed number is {reversed_num}.")























# Extract digits using modulo, build the reversed number, 
# and remove digits using integer division.
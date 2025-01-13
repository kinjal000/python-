def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    total = sum([digit ** power for digit in digits])
    return total == n

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")






















# Explanation:

# We convert the number to a list of digits.
# We calculate the sum of each digit raised to the power of the number of digits.
# If this sum equals the original number, it's an Armstrong number.

#  Armstrong number is a number where the sum of its digits raised to the power
# of the number of digits equals the number itself.

# Example:
# Consider the number 153:

# It has 3 digits: 1, 5, and 3.
# Calculate the sum of each digit raised to the power of 3
# (since the number has 3 digits):1^3 +5^3 +3^3=1+125+27=153
# Since the sum equals the original number, 153 is an Armstrong number.
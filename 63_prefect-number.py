def perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

num = int(input("Enter a number: "))
if perfect_number(num):
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")


























# Explanation:

# We find all divisors of the number (excluding the number itself).
# If the sum of the divisors equals the number, it's a Perfect number.
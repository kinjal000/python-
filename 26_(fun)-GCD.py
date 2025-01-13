def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("GCD:", gcd(a, b))


























# Explanation: The gcd function uses the Euclidean algorithm to f
# ind the greatest common divisor.
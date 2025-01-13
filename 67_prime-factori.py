def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

num = int(input("Enter a number: "))
print(f"Prime factors: {prime_factors(num)}")























# Explanation:

# We iterate over possible factors and divide the number by each factor 
# repeatedly to find prime factors.
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print("Result:", power(base, exponent))
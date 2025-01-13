def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
x
number = int(input("Enter a number: "))
if prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

















# Explanation: The function checks divisibility up to the square root 
# of the number to determine if it’s prime.
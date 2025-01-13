def fibonacci(n):
    sequence = [0, 1]
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci(n))
























# Explanation: The function generates Fibonacci numbers by summing
# the last two numbers in the sequence.
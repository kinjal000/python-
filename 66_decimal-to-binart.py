def decimal_to_binary(n):
    return bin(n)[2:]

num = int(input("Enter a decimal number: "))
print(f"Binary equivalent: {decimal_to_binary(num)}")



























# Explanation:

# We use Python's built-in bin() function to convert a decimal to binary, t
# hen remove the "0b" prefix.
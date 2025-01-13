def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_str = input("Enter a binary number: ")
print(f"Decimal equivalent: {binary_to_decimal(binary_str)}")





























# Explanation:

# The int function can convert a binary string to a decimal number by specifying base 2.


# Example 1:

# If the user enters the binary number 1101:

# The function binary_to_decimal("1101") is called.
# It converts 1101 from binary to decimal.
# The binary number 1101 can be expanded as:
# 1^2 * 2^2 + 1^2 * 2^2 + 0^2 * 2^2 + 1^2 * 2^2 =8+4+0+1=13
# The result 13 is printed.

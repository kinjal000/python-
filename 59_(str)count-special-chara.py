string = input("Enter a string: ")

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
count = 0

for char in string:
    if char in special_chars:
        count += 1

print("Number of special characters:", count)






















# Explanation:

# We define a string of special characters.
# We loop through the input string and count how many characters are special.
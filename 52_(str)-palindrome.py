
string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
























# Explanation:

# string[::-1] reverses the string.
# We compare the original string with its reverse. If they match, it's a palindrome.
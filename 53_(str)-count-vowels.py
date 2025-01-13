
string = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)






















# Explanation:

# We define a string vowels containing both uppercase and lowercase vowels.
# We loop through the string and check each character. If it is a vowel,
# we increase the count.
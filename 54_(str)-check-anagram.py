
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
























# Explanation:

# sorted() sorts the characters of a string.
# If the sorted versions of both strings match, they are anagrams.
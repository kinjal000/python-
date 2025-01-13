string = input("Enter a string: ")

char_freq = {}

for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character frequency:", char_freq)




















# Explanation:

# We use a dictionary to store the frequency of each character.
# For each character in the string, if it is already in the dictionary,
#  we increment its count; otherwise, we add it to the dictionary.
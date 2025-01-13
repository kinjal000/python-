def number_to_words(n):
    words = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
             6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return ' '.join([words[int(digit)] for digit in str(n)])

num = int(input("Enter a number: "))
print(f"Number in words: {number_to_words(num)}")




























# Explanation:

# We map each digit to its word form and join them into a string.



# Input:
# n is a number (e.g., 123).
# str(n):
# Converts the number n into a string (e.g., 123 → "123").
# [int(digit) for digit in str(n)]:
# Loops through each character in the string, converts it back to an integer (e.g., "1" → 1).
# words[int(digit)]:
# Accesses the corresponding word for each digit from the predefined words list (e.g., 1 → "one").
# ' '.join([...]):
# Joins the words with spaces in between to form a single string.
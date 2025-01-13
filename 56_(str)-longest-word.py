
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print("The longest word is:", longest_word)
























# Explanation:

# split() breaks the sentence into words.
# max() finds the word with the maximum length using key=len.
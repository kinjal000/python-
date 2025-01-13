
sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = {word: words.count(word) for word in words}

print("Word count dictionary:", word_count)

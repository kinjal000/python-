letter = input("Enter a letter: ").lower()

if letter in 'aeiou':
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")



























# lower() ensures case insensitivity.
# in checks if the letter is one of the vowels.
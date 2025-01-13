import random

def hangman(word):
    guessed = "_" * len(word)
    attempts = 10
    guessed_letters = []
    
    while attempts > 0 and "_" in guessed:
        print(f"Word: {guessed}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            guessed = "".join([c if c == guess or c in guessed_letters else "_" for c in word])
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        
    if "_" not in guessed:
        print(f"You won! The word is: {word}")
    else:
        print(f"You lost! The word was: {word}")

word = random.choice(["python", "hangman", "programming"])
hangman(word)

















# Explanation:

# The user tries to guess letters of a hidden word.
# Incorrect guesses reduce the number of attempts.
# The game ends when the word is guessed or the attempts run out.

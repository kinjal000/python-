import random
secret_number = random.randint(1, 100)

guess = 0
while guess != secret_number:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")





















# Randomly generate a number and keep prompting the user until they guess it right.
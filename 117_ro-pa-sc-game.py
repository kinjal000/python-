import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

print(play_game())





















# Explanation:

# The user plays against the computer in a simple Rock-Paper-Scissors game.
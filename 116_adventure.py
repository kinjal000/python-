def start_adventure():
    print("Welcome to the Adventure!")
    while True:
        choice = input("You are in a dark room. Do you want to go left or right? ").lower()
        if choice == "left":
            print("You entered a library. There's a book on the table.")
        elif choice == "right":
            print("You entered a forest. It's getting dark.")
        else:
            print("Invalid choice, try again.")
        continue_game = input("Do you want to keep exploring? (yes/no): ").lower()
        if continue_game != "yes":
            break
    print("Game Over")

start_adventure()

















# Explanation:

# The user makes choices to navigate through different rooms. 
# The adventure continues until the user decides to stop.
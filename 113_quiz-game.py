def ask_question(question, options, answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Enter your choice: "))
    return choice == answer

score = 0
questions = [
    ("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1),
    ("What is 2 + 2?", ["3", "4", "5", "6"], 2),
]

for question, options, answer in questions:
    if ask_question(question, options, answer):
        score += 1

print(f"Your score: {score}/{len(questions)}")



















# Explanation:

# The program asks multiple-choice questions and checks if the answer is correct.
# The score is tracked, and the final score is displayed at the end.

# enumerate() is a built-in Python function that is used to iterate over a sequence
# (like a list, tuple, or string) while keeping track of the index of each element
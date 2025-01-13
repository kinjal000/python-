text_to_append = input("Enter text to append: ")

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")

print("Text appended to output.txt")


























# Explanation:

# open("output.txt", "a") opens the file in append mode, 
# new content is added without overwriting.
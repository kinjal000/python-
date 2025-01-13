word_to_search = input("Enter the word to search for: ")

try:
    with open("output.txt", "r") as file:
        lines = file.readlines()
    
    found_lines = [index + 1 for index, line in enumerate(lines) if word_to_search in line]
    
    if found_lines:
        print(f"Word found on line(s): {found_lines}")
    else:
        print("Word not found.")
except FileNotFoundError:
    print("File not found!")






















# Explanation:

# enumerate() loops over the lines with an index.
# A list comprehension is used to find the line numbers where the word appears.
try:
    with open("output.txt", "r") as file:
        content = file.read()
    
    total_chars = len(content)
    total_lines = content.count('\n') + 1
    total_words = len(content.split())

    print(f"Total characters: {total_chars}")
    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
except FileNotFoundError:
    print("File not found!")






















    
# Explanation:

# len(content) counts the total number of characters.
# content.count('\n') + 1 counts the total number of lines (since each line ends with \n).
# .split() splits the content into words, and len() counts them.
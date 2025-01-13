try:
    with open("output.txt", "r") as file:
        content = file.read()
    words = content.split()
    print("Number of words:", len(words))
except FileNotFoundError:
    print("File not found!")


























    
# Explanation:

# file.read() reads the entire content of the file.
# .split() splits the content into words.
# len() counts the number of words.
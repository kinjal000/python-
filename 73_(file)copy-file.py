import shutil

try:
    shutil.copy("output.txt", "input.txt")
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found!")



























# Explanation:

# shutil.copy() is used to copy the content of one file to another.
# A try-except block is used to handle cases where the source file doesn’t exist.
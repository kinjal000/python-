
try:
    with open("output.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")

























# Explanation:

# open("output.txt", "r") opens the file in read mode.
# file.read() reads the entire content of the file.
# A try-except block handles the case where the file might not exist.

# try:
# It begins a try block, where the code attempts to open and read the file.

# with open("output.txt", "r") as file:
# It tries to open output.txt in read mode ("r").
# The with keyword ensures the file is automatically closed after reading

# print("File not found!")
# In case of an error (file not found), it prints the message "File not found!".
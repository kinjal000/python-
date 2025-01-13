user_input = input("Enter a string to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input)

print("Content written to output.txt")


























# Explanation:

# input() is used to get a string from the user.
# open("output.txt", "w") opens the file in write mode.
# If the file doesn’t exist, it creates it.
# file.write() writes the user input to the file.


# The with keyword ensures that the file is properly closed after 
# the block of code is executed, even if an error occurs within the block.
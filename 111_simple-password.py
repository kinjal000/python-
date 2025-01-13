import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the password length: "))
print("Generated Password:", generate_password(length))

























# Explanation:

# We use the random and string modules.
# The generate_password function generates a password by randomly 
# electing characters from letters, digits, and special characters.
# The user inputs the desired length for the password, and the program
#    prints the generated password.
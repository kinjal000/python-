import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        print(f"Definition of {word}: {definition}")
    else:
        print("Word not found.")

word = input("Enter a word to look up: ")
get_definition(word)


















# Explanation:

# The program fetches the definition of a word from an online API and displays it.
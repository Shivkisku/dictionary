import json
from difflib import get_close_matches

# Load the dictionary data from a JSON file
with open("data.json") as file:
    data = json.load(file)

def translate(word):
    # Normalize the input word to lowercase
    word = word.lower()

    # Check if the word is in the dictionary
    if word in data:
        return data[word]

    # Check if the titlecased version of the word is in the dictionary
    if word.title() in data:
        return data[word.title()] 

    # Check if the uppercase version of the word is in the dictionary
    if word.upper() in data:
        return data[word.upper()]

    # If the word is not found, suggest similar words
    close_matches = get_close_matches(word, data.keys(), n=3, cutoff=0.6)
    if close_matches:
        suggestion = close_matches[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % suggestion)
        if yn == "Y":
            return data[suggestion]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Prompt the user to enter a word to look up
word = input("Enter a word: ")

# Get the definition of the word or a suggestion for a similar word
output = translate(word)

# Print the output
if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)

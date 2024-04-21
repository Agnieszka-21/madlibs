# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import all available stories for mad libs
from madlibs_stories import madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8

# Python library to choose a random story from the provided ones
import random 


# Two Python libraries used to access dictionary API & the file with the api key
import json
import requests
import dictionary_api
# Access the dictionary API key
app_key = dictionary_api.API_KEY_SERVICE
# A variable to get the user's inputs (words) for the stories, one by one
users_word = "cat"
# Code figured out based on the following tutorial: https://www.youtube.com/watch?v=hpc5jyVpUpw
# Aiming to access 'fl', functional label of the given word (e.g. adjective, verb, etc.)
response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{users_word}?key={app_key}")
word_checked = response.json()
print(word_checked[0]['fl'])


# Welcome screen
welcome = "Welcome to MAD LIBS! \n \nHow to play: \nYou will be asked to provide certain words \
(a noun, an adjective etc.) that are then inserted into a randomly selected story. \
To provide your words, simply type them as prompted and confirm the submission of \
each word by pressing Enter. Afterwards, simply read the complete story. Have fun!\n"

print(welcome)


# Choose a random mad lib story to complete and print
if __name__ == "__main__":
    madlib_story = random.choice([madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8])
    madlib_story.madlib()


# Would you like to play again (Y/N)? 
play_again_question = input("\nWould you like to play again (Y/N)? ").upper()

if play_again_question == "Y":
    madlib_story = random.choice([madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8])
    madlib_story.madlib()
elif play_again_question == "N":
    end_game = "Okay, thanks for playing!"
    print(end_game)    
else:
    input("Type Y if you'd like to play again or N to finish your game, then press Enter: ")
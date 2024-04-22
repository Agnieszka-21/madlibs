# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import all available stories for mad libs
#from madlibs_stories import madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8

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
print(word_checked)
print(word_checked[0]['fl'])


# Welcome screen
welcome = "Welcome to MAD LIBS! \n \nHow to play: \nYou will be asked to provide certain words \
(a noun, an adjective etc.) that are then inserted into a randomly selected story. \
To provide your words, simply type them as prompted and confirm the submission of \
each word by pressing Enter. Afterwards, simply read the complete story. Have fun!\n"
print(welcome)


#Mad lib stories as a class - trying something
# Required user's inputs
noun1 = input("Noun: ")
noun2 = input("Another noun: ")
noun_pl = input("Plural noun: ")
adj1 = input("Adjective: ")
adj2 = input("Another adjective: ")
adv = input("Adverb: ")
verb = input("Verb: ")


#Class
class Story:
    """
    A mad lib story with blanks
    """
    def __init__(self, title, story):
        self.title = title
        self.story = story
    def madlib_story(self):
        """
        Add a story
        """
        return (self.title)
        #print(self.title)
        #print(self.story)

madlib1 = Story("\nStrange Science", f"\nScience is full of {adv} strange facts and stories. Did you know that \
rats can laugh when they are being tickled? Another fun {noun1} about rats is that \
their teeth never stop growing. Babies may be {adj1} but they have 100 more {noun_pl} \
than adults. When babies are born, they have the ability to {verb}. Newborn rats have \
{adj2} stomachs. They are approximately the size of a(n) {noun2}.")

madlib2 = Story("\nFall Fun", f"\nThe weather is starting to turn crisp. \
The wind is blowing through the {noun_pl}. I am excited to go \
{noun1} picking this weekend. Each autumn, my family drives out to my \
uncle’s orchard. We pick as many apples as our {noun2} can hold. \
This year we are also going to {verb} a scarecrow contest. I can’t decide \
if I want the face to be {adj1} or {adv} {adj2}.")

madlib3 = Story("\nSpace Adventure", f"\nOnce upon a time, in a galaxy far, far away, \
there was an adventurous {noun1} named Anakin. One day, Anakin hopped \
aboard their {adj1} spaceship - his mission was to {verb} \
a new {noun2}. As the spaceship soared through the {adj2} galaxy, \
Anakin marvelled at the twinkling {noun_pl} he passed. {adv}, \
an asteroid appeared out of nowhere and shot across their path.")


#print(madlib1.title, madlib1.story)

all_stories = [madlib1, madlib2, madlib3]

# Choose a random mad lib story to complete and print
#if __name__ == "__main__":
    #madlib_story = random.choice([madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8])
    #madlib_story = madlib1
    #madlib_story.madlib_story()
random_story = random.choice(all_stories)
print(random_story)

# Would you like to play again (Y/N)? 
play_again_question = input("\nWould you like to play again (Y/N)? ").upper()

if play_again_question == "Y":
    #madlib_story = random.choice([madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8])
    madlib_story.madlib()
elif play_again_question == "N":
    end_game = "Okay, thanks for playing!"
    print(end_game)    
else:
    input("Type Y if you'd like to play again or N to finish your game, then press Enter: ")
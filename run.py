# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Python library to choose a random story from the provided ones
import random 

# Two Python libraries used to access dictionary API & the file with the api key
import json
import requests
import dictionary_api


# Welcome screen
def welcome():
    welcome = "Welcome to MAD LIBS! \n \nHow to play: \nYou will be asked to provide certain words \
(a noun, an adjective etc.) that are then inserted into a randomly selected story. \
To provide your words, simply type them as prompted and confirm the submission of \
each word by pressing Enter. Afterwards, simply read the complete story. Have fun!\n"
    print(welcome)
welcome()


noun1 = "noun"
noun2 = "noun"
nouns = noun1 or noun2
word_type = nouns

words_needed = [noun1, noun2] # A list of all required word inputs
words_accepted = []

# Required user's inputs - words to fill any blanks in a mad lib
def word_input():
    if len(words_accepted) == 0:
        global noun1
        noun1 = input("Noun: ").upper()
        global current_word
        current_word = noun1
    elif len(words_accepted) == 1:
        global noun2
        noun2 = input("Another noun: ").upper()
        current_word = noun2
    #noun_pl = input("Plural noun: ").upper()
    #adj1 = input("Adjective: ").upper()
    #adj2 = input("Another adjective: ").upper()
    #adv = input("Adverb: ").upper()
    #verb = input("Verb: ").upper()
#word_input()


# Access the dictionary API key
def look_up_word():
    global users_word
    users_word = current_word
    app_key = dictionary_api.API_KEY_SERVICE
    
    # Code figured out based on the following tutorial: https://www.youtube.com/watch?v=hpc5jyVpUpw
    # Aiming to access 'fl', functional label of the given word (e.g. adjective, verb, etc.)
    response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{users_word}?key={app_key}")
    global word_checked
    word_checked = response.json()
    print(word_checked)
#look_up_word()


# Validate input - check if the provided word was found in the dictionary and if it is a correct type (adj, adv etc)
def validate_word():
    # Check if the word can be found in the dictionary
    try: 
        word_checked[0]['fl']
        print("Validation successful.")
        print(word_checked[0]['fl'])
        #global current_word
        global word_type
        match word_type:
            case nouns:
                if (word_checked[0]['fl'] == "noun"):
                    print("Great, your word is a noun.")
                    words_accepted.append(users_word)
                    print(words_accepted)
                # In case the given word is not a noun
                else:
                    noun1 = input("It looks like your word is not a noun. Try again: ").upper()
                    global current_word
                    current_word = noun1
                    look_up_word()
                    validate_word()

    # Word not found in the dictionary - likely misspelled
    except TypeError: 
        print("This is not a valid word.")
        noun1 = input("Please check for typos and try again - enter a noun here: ").upper()
        current_word = noun1
        look_up_word()
        validate_word()
    #except ConnectionError (can't connect to API)
#validate_word()


for word in words_needed:
    word_input()
    look_up_word()
    validate_word()


""" Trying something

#Class Story for all available mad libs
class Story:
    """
    #A mad lib story with blanks
"""
    def __init__(self, title, text):
        self.title = title
        self.text = text

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

madlib4 = Story("\nAre we alone?", f"\nAfter many {adj1} days and nights, Buzz {adv} \
arrived at the mysterious planet. He stepped out of the {noun1} and \
was greeted by {adj2} {noun_pl} and other curious creatures. \
He wanted to {verb} the {noun2} and become friends with the locals. \
But his intuition was telling him that he couldn’t trust his hosts...")

madlib5 = Story("\nSummer Camp Mystery", f"\nIt was a(n) {adv} {adj1} summer day - the first day of camp! \
The camp counsellor told us to {verb} for the {noun1} \
- a local legend with sharp teeth, bushy {noun2}, and \
a very {adj2} smell. That night as other campers and I were \
going to sleep, we heard a noise. It sounded like someone \
chewing on {noun_pl}...")

madlib6 = Story("\nFirst Day at Wizard School", f"\nHermione jumped out of <noun> as she opened her eyes. \
Today was her first day at wizard school! She dressed {adv}, \
grabbing a pointy hat to {verb} on her head. Arriving at school, \
she took her seat in class and prepared her first potion. The ingredients \
included a(n) {adj1} bezoar and {adj2} {noun_pl}. \
It would be worth it when she could turn a spider into a(n) {noun2}.")

madlib7 = Story("\nAmazon Explorers", f"\nThe {adj1} explorer flew his plane over the Amazon jungle. \
Below, he could {verb} tall trees growing along the edge of \
a(n) {noun1}. Behind him, he could hear his co-pilot, Emma, muttering. \
\“We're not going to make it. When the {adj2} eagle flew into the wing, \
it damaged it too much. We need to find somewhere clear to land.\” \
{adv}, Marcus spotted a clearing - a perfect landing spot. \
They got out of the plane to check the damaged {noun2}. Suddenly, a loud roar made them jump. \
From out of the jungle came a pair of {noun_pl}...")

madlib8 = Story("Dino Danger", f"\nDinosaurs were a diverse group of {noun_pl} \
that lived on Earth until about 66 million years ago. Some \
dinosaurs were carnivores - they ate {noun1}. Other \
dinosaurs were herbivores and ate {noun2}. One of the most {adj1} \
dinosaurs had a(n) {adj2} armour along its back. It walked \
{adv} due to its large size. Imagine how amazing it would \
have been to see dinosaurs {verb} through cities \
and fly in the sky…")


# Lists of titles and texts for all available stories
all_titles = [madlib1.title, madlib2.title, madlib3.title, madlib4.title, madlib5.title, madlib6.title, madlib7.title, madlib8.title]
all_texts = [madlib1.text, madlib2.text, madlib3.text, madlib4.text, madlib5.text, madlib6.text, madlib7.text, madlib8.text]

# Choose a random mad lib story to complete and print
#if __name__ == "__main__":
    #madlib_story = random.choice([madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8])
    #madlib_story = madlib1
    #madlib_story.madlib_story()

def choose_story_randomly():
    # Get an index of each title from the available list
    for title in all_titles:
        title_indices = [all_titles.index(title)]
    # Choose a random title index
    randomly_chosen_title = random.choice(title_indices)
    # Choose a text that matches the title (same index)
    matching_text = all_texts[randomly_chosen_title]
    # Print the full story (randomly chosen title with its text)
    print(all_titles[randomly_chosen_title])
    print(matching_text)

choose_story_randomly()



# Would you like to play again (Y/N)? 
play_again_question = input("\nWould you like to play again (Y/N)? ").upper()

if play_again_question == "Y":
    new_game_how = input("If you would like to re-use your words with a different story, type A and press Enter. \
If you'd like to start a new game, type B and press Enter: ").upper()
    if new_game_how == "A":
        random_or_not = input("If you want to choose your next story from a list of titles, type A and press Enter. \
If you'd rather use a random story, type B and press Enter: ").upper()
        if random_or_not == "A":
            print(all_titles)
        elif random_or_not == "B":
            choose_story_randomly() #needs to be adjusted so that the list of possible stories excludes the previously used story

elif play_again_question == "N":
    end_game = "Okay, thanks for playing!"
    print(end_game)    
else:
    input("Type Y if you'd like to play again or N to finish your game, then press Enter: ")

"""
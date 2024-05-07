# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Python library used to clear terminal
import os

# Python library to choose a random story from the provided ones
import random 

# Two Python libraries used to access dictionary API & the file containing the API key
import json
import requests
import dictionary_api



# Clears the terminal window prior to new content. For Windows and macOS/Linux
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def restart_program(): # Does it work for macOS/Linux?
    os.system('cls' if os.name == 'nt' else 'clear')
    script_name = os.path.basename(__file__)
    os.system(script_name)


# Welcome screen - prints a welcome message and a short description of how to play the game
def welcome():
    welcome = "Welcome to MAD LIBS! \n \nHow to play: \nYou will be asked to provide certain words \
(a noun, an adjective etc.) that are then inserted into a randomly selected story. \
To provide your words, simply type them as prompted and confirm the submission of \
each word by pressing Enter. Afterwards, simply read the complete story. Have fun!\n"
    print(welcome)


class Words:
    """
    Required word inputs from the user and their grammatical types
    """
    def __init__(self, word_required, word_type):
        self.word_required = word_required
        self.word_type = word_type

noun1 = Words("noun", "noun")
noun2 = Words("noun", "noun")
noun_pl = Words("noun", "noun")
adj1 = Words("adjective", "adjective")
adj2 = Words("adjective", "adjective")
adv = Words("adverb", "adverb")
verb = Words("verb", "verb")


# A list of all required word inputs
WORDS_NEEDED = (noun1, noun2, noun_pl, adj1, adj2, adv, verb)

# A list that grows with each valid word input from user
words_accepted = []

# Current word input being looked up and validated
current_word = None


# Required user's inputs - ask for words that will be used to fill any blanks in a mad lib
def get_word_input():
    if len(words_accepted) == 0:
        noun1.word_required = input("Noun:\n").upper()
        global current_word
        current_word = noun1
    elif len(words_accepted) == 1:
        noun2.word_required = input("Another noun:\n").upper()
        current_word = noun2
    elif len(words_accepted) == 2:
        noun_pl.word_required = input("Plural noun:\n").upper()
        current_word = noun_pl
    elif len(words_accepted) == 3:
        adj1.word_required = input("Adjective:\n").upper()
        current_word = adj1
    elif len(words_accepted) == 4:
        adj2.word_required = input("Another adjective:\n").upper()
        current_word = adj2
    elif len(words_accepted) == 5:
        adv.word_required = input("Adverb:\n").upper()
        current_word = adv
    elif len(words_accepted) == 6:
        verb.word_required = input("Verb:\n").upper()
        current_word = verb
#word_input()



# Access the dictionary API key
def look_up_word():
    app_key = dictionary_api.API_KEY_SERVICE
    try:
        # Code figured out based on the following tutorial: https://www.youtube.com/watch?v=hpc5jyVpUpw
        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{current_word.word_required}?key={app_key}")
        word_checked = response.json()
        #print(word_checked)

        def validate_word():
            try: 
                # Check if the word can be found in the dictionary
                current_word.word_required in word_checked[0]['meta']['id']
                #print("Validation successful.")
                #print(word_checked[0]['meta']['id'])
                #print(current_word.word_required)

                # Aiming to access 'fl', functional label of the given word (e.g. adjective, verb, etc.)
                if 'fl' in word_checked[0]:
                    fl_available = [word_checked[0]['fl']]
                # If such a label is not found (usually for plural nouns)
                elif 'plural of' in word_checked[0]['cxs'][0]['cxl']:
                    fl_available = ["noun"]

                # Check for homographs - a word has multiple meanings/grammatic functions
                if len(word_checked) > 1 and 'hom' in word_checked[1] and 'fl' in word_checked[1]:
                    #print("This word has multiple meanings and functions")
                    fl_available.append(word_checked[1]['fl'])
                    
                    if len(word_checked) > 2 and 'hom' in word_checked[2] and 'fl' in word_checked[2]: #double check if working correctly
                        fl_available.append(word_checked[2]['fl'])
                print(fl_available)

                # Check if the valid word has the correct grammatical type (function label)
                def valid_words_type():
                    global current_word
                    if current_word.word_type == "noun": 
                        if "noun" in fl_available:
                            print("Great, your word is a noun.")
                            words_accepted.append(current_word.word_required)
                            print(words_accepted)
                        else:
                            current_word.word_required = input("It looks like your word is not a noun. Try again:\n")
                            look_up_word()
                    elif current_word.word_type == "adjective":
                        if "adjective" or "adverb or adjective" in fl_available:
                            print("Great, your word is an adjective.")
                            words_accepted.append(current_word.word_required)
                            print(words_accepted)
                        else:
                            current_word.word_required = input("It looks like your word is not an adjective. Try again:\n")
                            look_up_word()
                    elif current_word.word_type == "adverb":
                        if "adverb" in fl_available or ("adjective" in fl_available and current_word.word_required[-2:] == 'ly'):
                            print("Great, your word is an adverb.")
                            print(current_word.word_required[-2:])
                            words_accepted.append(current_word.word_required)
                            print(words_accepted)  
                        else: 
                            current_word.word_required = input("It looks like your word is not an adverb. Try again:\n")
                            look_up_word()
                    elif current_word.word_type == "verb":
                        if "verb" in fl_available:
                            print("Great, your word is a verb.")
                            words_accepted.append(current_word.word_required)
                            print(words_accepted)  
                        else: 
                            current_word.word_required = input("It looks like your word is not a verb. Try again:\n")
                            look_up_word()
                    else:
                        input(f"It looks like your word is not a {current_word.word_type}. Please try again:\n")
                valid_words_type() 
                

            # Word not found in the dictionary - likely misspelled, a typo, or not a word
            except TypeError: 
                current_word.word_required = input(f"Please check for typos and try again. Enter your {current_word.word_type} here:\n")
                look_up_word()

            except IndexError: 
                current_word.word_required = input(f"Your word could not be validated. Please try again - enter your {current_word.word_type} here:\n")
                look_up_word()

        validate_word()

    except ConnectionError:
        print("Sorry, there was a connection issue.")
        restart = input("Type R and press Enter to restart the game:\n")  
        if restart == "R":
            clear_terminal()
            restart_program()
        else:
            restart_ask_again = input("Invalid input. Please type R and press Enter to restart the game:\n")
            if restart_ask_again == "R":
                clear_terminal()
                restart_program()
            else:
                print("Thanks for playing MAD LIBS!")



# Start game by printing the welcome message and asking for word inputs
def start_game(WORDS_NEEDED):
    welcome()
    for word in WORDS_NEEDED:
        get_word_input()
        look_up_word()
start_game(WORDS_NEEDED)


      
#Class Story for all available mad libs
class Story:
    """
    A mad lib story with blanks
    """
    def __init__(self, title, text):
        self.title = title
        self.text = text

madlib1 = Story("\nStrange Science", f"\nScience is full of {adv.word_required} strange facts and stories. Did you know that \
rats can laugh when they are being tickled? Another fun {noun1.word_required} about rats is that \
their teeth never stop growing. Babies may be {adj1.word_required} but they have 100 more {noun_pl.word_required} \
than adults. When babies are born, they have the ability to {verb.word_required}. Newborn rats have \
{adj2.word_required} stomachs. They are approximately the size of a(n) {noun2.word_required}.")

madlib2 = Story("\nFall Fun", f"\nThe weather is starting to turn crisp. \
The wind is blowing through the {noun_pl.word_required}. I am excited to go \
{noun1.word_required} picking this weekend. Each autumn, my family drives out to my \
uncle's orchard. We pick as many apples as our {noun2.word_required} can hold. \
This year we are also going to {verb.word_required} a scarecrow contest. I can't decide \
if I want the face to be {adj1.word_required} or {adv.word_required} {adj2.word_required}.")

madlib3 = Story("\nSpace Adventure", f"\nOnce upon a time, in a galaxy far, far away, \
there was an adventurous {noun1.word_required} named Anakin. One day, Anakin hopped \
aboard their {adj1.word_required} spaceship - his mission was to {verb.word_required} \
a new {noun2.word_required}. As the spaceship soared through the {adj2.word_required} galaxy, \
Anakin marvelled at the twinkling {noun_pl.word_required} he passed. {adv.word_required}, \
an asteroid appeared out of nowhere and shot across their path.")

madlib4 = Story("\nAre we alone?", f"\nAfter many {adj1.word_required} days and nights, Buzz {adv.word_required} \
arrived at the mysterious planet. He stepped out of the {noun1.word_required} and \
was greeted by {adj2.word_required} {noun_pl.word_required} and other curious creatures. \
He wanted to {verb.word_required} the {noun2.word_required} and become friends with the locals. \
But his intuition was telling him that he couldn't trust his hosts...")

madlib5 = Story("\nSummer Camp Mystery", f"\nIt was a(n) {adv.word_required} {adj1.word_required} summer day - the first day of camp! \
The camp counsellor told us to {verb.word_required} for the {noun1.word_required} \
- a local legend with sharp teeth, bushy {noun2.word_required}, and \
a very {adj2.word_required} smell. That night as other campers and I were \
going to sleep, we heard a noise. It sounded like someone \
chewing on {noun_pl.word_required}...")

madlib6 = Story("\nFirst Day at Wizard School", f"\nHermione jumped out of {noun1.word_required} as she opened her eyes. \
Today was her first day at wizard school! She dressed {adv.word_required}, \
grabbing a pointy hat to {verb.word_required} on her head. Arriving at school, \
she took her seat in class and prepared her first potion. The ingredients \
included a(n) {adj1.word_required} bezoar and {adj2.word_required} {noun_pl.word_required}. \
It would be worth it when she could turn a spider into a(n) {noun2.word_required}.")

madlib7 = Story("\nAmazon Explorers", f"\nThe {adj1.word_required} explorer flew his plane over the Amazon jungle. \
Below, he could {verb.word_required} tall trees growing along the edge of \
a(n) {noun1.word_required}. Behind him, he could hear his co-pilot, Emma, muttering. \
\“We're not going to make it. When the {adj2.word_required} eagle flew into the wing, \
it damaged it too much. We need to find somewhere clear to land.\” \
{adv.word_required}, Marcus spotted a clearing - a perfect landing spot. \
They got out of the plane to check the damaged {noun2.word_required}. Suddenly, a loud roar made them jump. \
From out of the jungle came a pair of {noun_pl.word_required}...")

madlib8 = Story("\nDino Danger", f"\nDinosaurs were a diverse group of {noun_pl.word_required} \
that lived on Earth until about 66 million years ago. Some \
dinosaurs were carnivores - they ate {noun1.word_required}. Other \
dinosaurs were herbivores and ate {noun2.word_required}. One of the most {adj1.word_required} \
dinosaurs had a(n) {adj2.word_required} armour along its back. It walked \
{adv.word_required} due to its large size. Imagine how amazing it would \
have been to see dinosaurs {verb.word_required} through cities \
and fly in the sky…")


# Lists of titles and texts for all available stories
ALL_TITLES = [madlib1.title, madlib2.title, madlib3.title, madlib4.title, madlib5.title, madlib6.title, madlib7.title, madlib8.title]
ALL_TEXTS = [madlib1.text, madlib2.text, madlib3.text, madlib4.text, madlib5.text, madlib6.text, madlib7.text, madlib8.text]
available_titles = ALL_TITLES
available_texts = ALL_TEXTS

# Randomly choose a title and a matching text from currently available titles and texts
def choose_story_randomly(list_of_titles, list_of_texts):

    # Choose a title randomly
    randomly_chosen_title = random.choice(list_of_titles)
    get_index_of_randomly_chosen_title = list_of_titles.index(randomly_chosen_title)

    # Get matching text (same index as the randomly chosen title's)
    matching_text = list_of_texts[get_index_of_randomly_chosen_title]

    # Print the randomly chosen mad lib to the terminal
    print(randomly_chosen_title, matching_text)

    # Update the list of available titles and texts (in case user wants to play again using the same words with a different story)
    available_titles = list_of_titles.remove(randomly_chosen_title)
    available_texts = list_of_texts.remove(matching_text)

choose_story_randomly(available_titles, available_texts)



# Ask the user whether they would like to play again and give them options
def play_again_or_not():
    play_again_question = input("\nWould you like to play again (Y/N)?\n").upper()
    if play_again_question == "Y":
        new_game_how = input("If you would like to re-use your words with a different story, type A and press Enter. \
If you'd like to start a new game, type B and press Enter:\n").upper()
        if new_game_how == "A":
            try:
                choose_story_randomly(available_titles, available_texts)
                play_again_or_not()
            except IndexError:
                all_stories_used = input("You have seen all available stories. If you would like to start a new game, type B and press Enter:\n").upper()
                if all_stories_used == "B":
                    clear_terminal()
                    restart_program()
                else:
                    print("Invalid input. Thanks for playing MAD LIBS!")
        elif new_game_how == "B":
            clear_terminal()
            restart_program()
        else:
            input("Please choose A or B and press Enter:\n").upper()
    elif play_again_question == "N":
        end_game = "Okay, thanks for playing!"
        print(end_game)    
    else:
        print("Invalid input. Thanks for playing MAD LIBS!")
play_again_or_not()

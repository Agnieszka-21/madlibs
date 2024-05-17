# Python libraries used to clear terminal & restart program
import os
import sys

# To delay clearing the terminal after getting all word inputs
from time import sleep

# Python library to choose a random story from the provided ones
import random

# Libraries needed to access dictionary API & the .env file with API key
import json
import requests
from dotenv import load_dotenv

# Rich library
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding
from rich.style import Style
from rich.text import Text
#from rich import print


def clear_terminal():
    """
    Clears the terminal window prior to new content.
    For Windows and macOS/Linux
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def restart_program():
    """
    Restarts the program when user wants to play again with new words
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)


# From Rich library, used for printing rich text
console = Console()

def welcome():
    """
    Prints a welcome message and a short description of how to play the game
    """
    game_title = Text("WELCOME TO MAD LIBS", style="bold orange_red1")
    #game_title.stylize("dark_orange3", 0, 19)
    welcome_text = Text()
    welcome_text.append("\nHow to play: You will be asked "
                        "to provide certain words (a noun, adjective "
                        "etc.) that are then inserted into a randomly "
                        "selected story. Simply type each word "
                        "as prompted and press Enter to "
                        "submit it. Afterwards, read the "
                        "complete story. Have fun!\n")
    # welcome_text.stylize("dark_orange3", 0, 13)
    console.print(game_title)
    console.print(welcome_text)


class Words:
    """
    Required word inputs from the user and their grammatical types
    """
    def __init__(self, word_required, word_type, examples):
        self.word_required = word_required
        self.word_type = word_type
        self.examples = examples


noun1 = Words("input", "noun", "(e.g. tree, car, dog)")
noun2 = Words("input", "noun", "(e.g. tree, car, dog)")
noun_pl = Words("input", "plural noun", "(e.g. cats, mice)")
adj1 = Words("input", "adjective", "(e.g. sad, beautiful)")
adj2 = Words("input", "adjective", "(e.g. sad, beautiful)")
adv = Words("input", "adverb", "(e.g. gladly, tomorrow)")
verb = Words("input", "verb", "(e.g. walk, swim)")


# A list of all required word inputs
WORDS_NEEDED = (noun1, noun2, noun_pl, adj1, adj2, adv, verb)

# A list that grows with each valid word input from user
words_accepted = []

# Current word input being looked up and validated
current_word = None


def get_word_input():
    """
    Asks for required user's inputs - words that will be used
    to fill any blanks in a mad lib
    """
    if len(words_accepted) == 0:
        noun1.word_required = input("Noun: ").upper()
        global current_word
        current_word = noun1
    elif len(words_accepted) == 1:
        noun2.word_required = input("Another noun: ").upper()
        current_word = noun2
    elif len(words_accepted) == 2:
        noun_pl.word_required = input("Plural noun: ").upper()
        current_word = noun_pl
    elif len(words_accepted) == 3:
        adj1.word_required = input("Adjective: ").upper()
        current_word = adj1
    elif len(words_accepted) == 4:
        adj2.word_required = input("Another adjective: ").upper()
        current_word = adj2
    elif len(words_accepted) == 5:
        adv.word_required = input("Adverb: ").upper()
        current_word = adv
    elif len(words_accepted) == 6:
        verb.word_required = input("Verb: ").upper()
        current_word = verb


def look_up_word():
    """
    Looks up each word input in the dictionary
    """
    # Access the dictionary API key
    load_dotenv()
    APP_KEY = os.getenv('API_KEY_SERVICE')
    try:
        response = requests.get(
            "https://www.dictionaryapi.com/api/v3/references/"
            f"collegiate/json/{current_word.word_required}?key={APP_KEY}")
        word_checked = response.json()

        def validate_word():
            """
            Makes sure the user input is a valid word and add
            the word's 'fl', functional labels, to the list fl_avail
            (available labels)
            """
            try:
                # Check if the exact word can be found in the dictionary
                # current_word.word_required.lower() in word_checked[0]['meta']['id']
                print(word_checked[0]['meta']['id'])

                # Aiming to access 'fl' of the given word (e.g. noun, verb)
                if 'fl' in word_checked[0]:
                    fl_avail = [word_checked[0]['fl']]
                    
                    # Check for homographs
                    if len(word_checked) > 1 and (
                        'hom' in word_checked[1]) and (
                            'fl' in word_checked[1]):
                        fl_avail.append(word_checked[1]['fl'])

                        if len(word_checked) > 2 and (
                            'hom' in word_checked[2]) and (
                                'fl' in word_checked[2]):
                            fl_avail.append(word_checked[2]['fl'])
                
                # If such a label is not found (usually for plural nouns)
                elif 'plural of' in word_checked[0]['cxs'][0]['cxl']:
                    fl_avail = ["plural noun"]
                
                # If British spelling rather than American
                elif 'British spelling' in word_checked[0]['cxs'][0]['cxl']:
                    fl_avail = []
                    amer = word_checked[0]['cxs'][0]['cxtis'][0]['cxt'].upper()
                    switch_to_amer = input(
                        "We weren't able to check your word but there seems "
                        "to be a similar word with US spelling. Would you "
                        f"like to try {amer} instead? (Y/N) ").upper()
                    if switch_to_amer == 'Y':
                        current_word.word_required = amer
                        look_up_word()
                    elif switch_to_amer == 'N':
                        current_word.word_required = input(
                            "Okay, please try a different word: ").upper()
                        look_up_word()
                    else:
                        current_word.word_required = input(
                            "Your input was invalid. Please submit "
                            "a different word: ").upper()
                        look_up_word()
                    return
                
                # None of the above requirements was met when checking
                # the word - invalid word
                else:
                    current_word.word_required = input(
                        "Oops, something went wrong. Please submit "
                        f"a different {current_word.word_type} "
                        f"{current_word.examples}: ").upper()
                    look_up_word()
                    return

        
                def valid_words_type():
                    """
                    Checks if the valid word has the correct grammatical
                    type (function label)
                    """
                    global current_word
                    if current_word.word_type == "noun":
                        if "noun" in fl_avail:
                            valid_noun = Text(
                                "Great, your noun has been accepted.", 
                                style="sea_green1")
                            console.print(valid_noun)
                            words_accepted.append(current_word.word_required)
                        else:
                            current_word.word_required = input(
                                "It looks like your word is not a noun. "
                                f"Try again {current_word.examples}: ").upper()
                            look_up_word()
                    elif current_word.word_type == "plural noun":
                        if ("plural noun" in fl_avail) or (
                            "noun" in fl_avail and current_word.word_required[-1:] 
                            == 'S') or ("noun" in fl_avail and 
                            current_word.word_required.lower() in 
                            word_checked[0]['meta']['stems']):
                            valid_noun_pl = Text(
                                "Great, your plural noun has been accepted.", 
                                style="sea_green1")
                            console.print(valid_noun_pl)
                            words_accepted.append(current_word.word_required)
                        else:
                            current_word.word_required = input(
                                "It looks like your word is not a plural "
                                f"noun. Try again {current_word.examples}: "
                            ).upper()
                            look_up_word()
                    elif current_word.word_type == "adjective":
                        if "adjective" in fl_avail:
                            valid_adj = Text(
                                "Great, your adjective has been accepted.", 
                                style="sea_green1")
                            console.print(valid_adj)                            
                            words_accepted.append(current_word.word_required)
                        else:
                            current_word.word_required = input(
                                "It looks like your word is not an adjective. "
                                f"Try again {current_word.examples}: ").upper()
                            look_up_word()
                    elif current_word.word_type == "adverb":
                        if "adverb" in fl_avail or (
                            "adjective" in fl_avail and
                                current_word.word_required[-2:] == 'LY'):
                            valid_adverb = Text(
                                "Great, your word adverb has been accepted.", 
                                style="sea_green1")
                            console.print(valid_adverb)
                            words_accepted.append(current_word.word_required)
                        else:
                            current_word.word_required = input(
                                "It looks like your word is not an adverb. "
                                f"Try again {current_word.examples}: ").upper()
                            look_up_word()
                    elif current_word.word_type == "verb":
                        if "verb" in fl_avail:
                            valid_verb = Text(
                                "Great, your verb has been accepted.", 
                                style="sea_green1")
                            console.print(valid_verb)
                            words_accepted.append(current_word.word_required)
                        else:
                            current_word.word_required = input(
                                "It looks like your word is not a verb. "
                                f"Try again {current_word.examples}: ").upper()
                            look_up_word()
                    else:
                        input("It looks like your word is "
                              f"not a {current_word.word_type}. "
                              "Please try again: ").upper()
                valid_words_type()

            # Word not found in the dictionary (misspelled/not a word)
            except TypeError:
                current_word.word_required = input(
                    "Please check for typos and try again. Enter "
                    f"your {current_word.word_type} "
                    f"{current_word.examples} here: ").upper()
                look_up_word()

            # Word could not be validated (none of the required
            # details regarding its 'fl' could be accessed)
            except IndexError:
                current_word.word_required = input(
                    "Your word could not be validated. Please try "
                    f"again - enter your {current_word.word_type} "
                    "here: ").upper()
                look_up_word()
        validate_word()


    # Problem with connecting to the dictionary API
    except ConnectionError:
        print("Sorry, there was a connection issue.")
        restart = input("Type R and press Enter to restart the game: ")
        if restart == "R":
            clear_terminal()
            restart_program()
        else:
            restart_ask_again = input(
                "Invalid input. Please type R "
                "and press Enter to restart the game: ")
            if restart_ask_again == "R":
                clear_terminal()
                restart_program()
            else:
                print("Thanks for playing MAD LIBS!")

    #except:
        #current_word.word_required = input(
            #"Something went wrong... Please submit a "
            #f"different {current_word.word_type} "
            #f"{current_word.examples}: ").upper()
        #look_up_word()
        #return

                
def start_game(WORDS_NEEDED):
    """
    Starts a game by printing the welcome message
    and asking for word inputs
    """
    welcome()
    for word in WORDS_NEEDED:
        get_word_input()
        look_up_word()


start_game(WORDS_NEEDED)


class Story:
    """
    A mad lib story with blanks
    """
    def __init__(self, title, text):
        self.title = title
        self.text = text


madlib1 = Story("\nStrange Science", "\nScience is full of "
                f"{adv.word_required} strange facts and stories. "
                "Did you know that rats can laugh when they are being "
                f"tickled? Another fun {noun1.word_required} about "
                "rats is that their teeth never stop growing. Babies "
                f"may be {adj1.word_required} but they have 100 more "
                f"{noun_pl.word_required} than adults. When babies "
                f"are born, they have the ability to {verb.word_required}. "
                f"Newborn rats have {adj2.word_required} stomachs. They are "
                f"approximately the size of a(n) {noun2.word_required}.")

madlib2 = Story("\nFall Fun", "\nThe weather is starting to turn crisp. "
                f"The wind is blowing through the {noun_pl.word_required}. "
                f"I am excited to go {noun1.word_required} picking "
                "this weekend. Each autumn, my family drives out to my "
                "uncle's orchard. We pick as many apples as our "
                f"{noun2.word_required} can hold. This year we are also "
                f"going to {verb.word_required} a scarecrow contest. I "
                f"can't decide if I want the face to be {adj1.word_required} "
                f"or {adv.word_required} {adj2.word_required}.")

madlib3 = Story("\nSpace Adventure", "\nOnce upon a time, in a galaxy "
                "far, far away, there was an adventurous "
                f"{noun1.word_required} named Anakin. One day, Anakin hopped "
                f"aboard their {adj1.word_required} spaceship - his mission "
                f"was to {verb.word_required} a new {noun2.word_required}. "
                f"As the spaceship soared through the {adj2.word_required} "
                "galaxy, Anakin marvelled at the twinkling "
                f"{noun_pl.word_required} he passed. {adv.word_required}, "
                "an asteroid appeared out of nowhere and shot across their "
                "path.")

madlib4 = Story("\nAre we alone?", f"\nAfter many {adj1.word_required} days "
                f"and nights, Buzz {adv.word_required} arrived at the "
                "mysterious planet. He stepped out of the "
                f"{noun1.word_required} and was greeted by "
                f"{adj2.word_required} {noun_pl.word_required} "
                "and other curious creatures. He wanted to "
                f"{verb.word_required} the {noun2.word_required} and become "
                "friends with the locals. But his intuition was telling him "
                "that he couldn't trust his hosts...")

madlib5 = Story("\nSummer Camp Mystery", f"\nIt was a(n) {adv.word_required} "
                f"{adj1.word_required} summer day - the first day of camp! "
                f"The camp counsellor told us to {verb.word_required} for "
                f"the {noun1.word_required} - a local legend with sharp "
                f"teeth, bushy {noun2.word_required}, and a very "
                f"{adj2.word_required} smell. That night as other campers "
                "and I were going to sleep, we heard a noise. It sounded "
                f"like someone chewing on {noun_pl.word_required}...")

madlib6 = Story("\nFirst Day at Wizard School", "\nHermione jumped out "
                f"of {noun1.word_required} as she opened her eyes. "
                "Today was her first day at wizard school! "
                f"She dressed {adv.word_required}, grabbing a "
                f"pointy hat to {verb.word_required} on her head. Arriving "
                "at school, she took her seat in class and prepared her "
                "first potion. The ingredients included a(n) "
                f"{adj1.word_required} bezoar and {adj2.word_required} "
                f"{noun_pl.word_required}. It would be worth it when "
                f"she could turn a spider into a(n) {noun2.word_required}.")

madlib7 = Story("\nAmazon Explorers", f"\nThe {adj1.word_required} "
                "explorer flew his plane over the Amazon jungle. "
                f"Below, he could {verb.word_required} tall trees "
                f"growing along the edge of a(n) {noun1.word_required}. "
                "Behind him, he could hear his co-pilot, Emma, muttering. "
                f"'We are not going to make it. When the {adj2.word_required} "
                "eagle flew into the wing, it damaged it too much. We need "
                f"to find somewhere clear to land.' {adv.word_required}, "
                "Marcus noticed a clearing - a perfect landing spot. "
                "They got out of the plane to check the damaged "
                f"{noun2.word_required}. Suddenly, a loud roar made them "
                "jump. From out of the jungle emerged"
                f"a pair of {noun_pl.word_required}...")

madlib8 = Story("\nDino Danger", "\nDinosaurs were a diverse group of "
                f"{noun_pl.word_required} that lived on Earth until "
                "about 66 million years ago. Some dinosaurs were "
                f"carnivores - they ate {noun1.word_required}. Other "
                f"dinosaurs were herbivores and ate {noun2.word_required}. "
                f"One of the most {adj1.word_required} dinosaurs "
                f"had a(n) {adj2.word_required} armour along its back. "
                f"It walked {adv.word_required} due to its large size. "
                "Imagine how amazing it would have been to see dinosaurs "
                f"{verb.word_required} through cities and fly in the sky…")


# Lists of titles and texts for all available stories
ALL_TITLES = [madlib1.title, madlib2.title, madlib3.title, madlib4.title,
              madlib5.title, madlib6.title, madlib7.title, madlib8.title]
ALL_TEXTS = [madlib1.text, madlib2.text, madlib3.text, madlib4.text,
             madlib5.text, madlib6.text, madlib7.text, madlib8.text]
available_titles = ALL_TITLES
available_texts = ALL_TEXTS


def choose_story_randomly(list_of_titles, list_of_texts):
    """
    Randomly chooses a title and a matching text from
    currently available titles and texts
    """
    # Choose a title randomly
    randomly_chosen_title = random.choice(list_of_titles)
    index_of_chosen_title = list_of_titles.index(randomly_chosen_title)

    # Get matching text (same index as the randomly chosen title's)
    matching_text = list_of_texts[index_of_chosen_title]

    # Print the randomly chosen mad lib to the terminal
    print(randomly_chosen_title, matching_text)

    # Update the list of available titles and texts
    available_titles = list_of_titles.remove(randomly_chosen_title)
    available_texts = list_of_texts.remove(matching_text)


def play_again_or_not():
    """
    Asks the user whether they would like to play again
    and gives them options
    """
    options = ["Y", "N"]
    play_again_question = input(
        "\nWould you like to play again (Y/N)? ").upper()
    while play_again_question not in options:
        print("Invalid input. Let's try one more time...")
        play_again_or_not()
        return
    else:
        if play_again_question == "N":
            end_game = "Okay, thanks for playing!"
            print(end_game)
            return
   
    def how_to_play_again():
        """
        Works only when user chose Y (yes) - they
        would like to play again
        """
        if play_again_question == "Y":
            new_game_options = ["A", "B"]
            new_game_how = input(
                "If you would like to re-use your words with a "
                "different story, type A and press Enter. If you'd like "
                "to start a brand new game, type B and press Enter: ").upper()
            while new_game_how not in new_game_options:
                print("Invalid input. Let's try once again...")
                how_to_play_again()
                return
            else:
                if new_game_how == "B":
                    clear_terminal()
                    restart_program()

        def reuse_words():
            """
            Works only if user chose option A - play again
            and re-use the same words with another story
            """   
            if new_game_how == "A":
                try:
                    choose_story_randomly(available_titles, available_texts)
                    play_again_or_not()
                except IndexError:
                    all_stories_used = input(
                        "You have seen all available stories. "
                        "If you would like to start a new game, "
                        "type Y and press Enter: ").upper()
                    while all_stories_used != "Y":
                        print("Invalid input. Let's try again...")
                        reuse_words()
                        return
                    if all_stories_used == "Y":
                        clear_terminal()
                        restart_program()

        reuse_words()
    how_to_play_again()


sleep(0.5)
clear_terminal()
choose_story_randomly(available_titles, available_texts)
play_again_or_not()

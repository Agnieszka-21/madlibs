# Python libraries used to clear terminal & restart program
import os
import sys

# To delay clearing the terminal after getting all word inputs
from time import sleep

# Python library to choose a random story from the provided ones
import random

# Libraries needed to access dictionary API & the .env file with API key
import requests
from dotenv import load_dotenv

# Function adj_with_ly returns a list that helps validate adverbs correctly
from python_madlibs.adj_list_ly_ending import adj_with_ly

# Rich library used for styling printed text
from rich.console import Console
from rich.text import Text

# From Rich library, used for printing rich text
console = Console()

# A list that grows with each valid word input from user
words_accepted = []


# Code based on this article:
# https://www.geeksforgeeks.org/clear-screen-python/
def clear_terminal():
    """
    Clears the terminal window prior to new content.
    For Windows and macOS/Linux
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Code has been copied from the following source:
# https://gist.github.com/jrosco/d01b28c2f37100bb5278
def restart_program():
    """
    Restarts the program when user wants to play again with new words
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)


def welcome():
    """
    Prints a welcome message and a short description of how to play the game
    """
    game_title = Text("\nWELCOME TO MAD LIBS GRAMMAR", style="bold sea_green1")
    welcome_text = Text()
    welcome_text.append("\nHow to play: You will be asked to provide "
                        "certain words (a noun, adjective etc.) that "
                        "are then inserted into a randomly selected story. "
                        "Simply type each word as prompted and press "
                        "Enter to submit it. Afterwards, read "
                        "the complete story. Have fun!")
    console.print(game_title)
    console.print(welcome_text)


class Words:
    """
    Required word inputs from the user, their grammatical types
    and examples
    """
    def __init__(self, input, type, examples):
        self.input = input
        self.type = type
        self.examples = examples


noun1 = Words("input", "noun", "(e.g. tree, car, dog)")
noun2 = Words("input", "noun", "(e.g. tree, car, dog)")
noun_pl = Words("input", "plural noun", "(e.g. cats, mice)")
adj1 = Words("input", "adjective", "(e.g. sad, beautiful)")
adj2 = Words("input", "adjective", "(e.g. sad, beautiful)")
adv = Words("input", "adverb", "(e.g. gladly, finally)")
verb = Words("input", "verb", "(e.g. walk, swim)")


def get_word_input():
    """
    Asks for required user's inputs - words that will be used
    to fill any blanks in a mad lib
    """
    if len(words_accepted) == 0:
        noun1.input = input("\nNoun: ").upper().strip()
        global current_word
        current_word = noun1
    elif len(words_accepted) == 1:
        noun2.input = input("\nAnother noun: ").upper().strip()
        current_word = noun2
        exclude_repetitions()
    elif len(words_accepted) == 2:
        noun_pl.input = input("\nPlural noun: ").upper().strip()
        current_word = noun_pl
    elif len(words_accepted) == 3:
        adj1.input = input("\nAdjective: ").upper().strip()
        current_word = adj1
    elif len(words_accepted) == 4:
        adj2.input = input("\nAnother adjective: ").upper().strip()
        current_word = adj2
        exclude_repetitions()
    elif len(words_accepted) == 5:
        adv.input = input("\nAdverb: ").upper().strip()
        current_word = adv
    elif len(words_accepted) == 6:
        verb.input = input("\nVerb: ").upper().strip()
        current_word = verb


def exclude_repetitions():
    """
    Prevents from accepting the same input twice.
    Used for nouns and adjectives
    """
    if ((current_word == noun2) and (
        current_word.input == noun1.input)) or ((
            current_word == adj2) and (
                    current_word.input == adj1.input)):
        console.print(Text(
            f"You have already used this {current_word.type}. "
            "Please submit a different one."), style="orange3")
        get_word_input()


def exclude_numbers():
    """
    Checks if word input submitted by user is a number.
    If it is, user is asked for another input
    """
    try:
        int(current_word.input)
        console.print(Text(
            "Sorry, numbers are not allowed.", style="orange3"))
        current_word.input = input(
            f"Please submit a valid {current_word.type} "
            f"{current_word.examples}: ").upper().strip()
    except ValueError:
        pass


def word_found(dict_word, fl_avail):
    """
    Prints a sentence informing user their word has been found
    and confirms the entry's functional labels
    """
    console.print(Text(
        f"Your word has been found under {dict_word} "
        f"and identified as: {fl_avail}"))


def word_accepted():
    """
    Informs user that their word input has been accepted
    """
    correct_word_type = Text(
        f"Great, your {current_word.type} {current_word.input} "
        "has been accepted.", style="sea_green1")
    console.print(correct_word_type)
    words_accepted.append(current_word.input)


def incorrect_word_type():
    """
    Informs user that their word has not been accepted
    because of incorrect grammatical type
    """
    console.print(Text(
        f"It looks like your word is not a(n) {current_word.type}.",
        style="orange3"))


def request_another_word():
    """
    Asks user to submit another word input. Gives examples
    of the required word type
    """
    current_word.input = input(
        f"Try again - please submit your {current_word.type} "
        f"{current_word.examples} here: ").upper().strip()


def get_and_check_another_input():
    """
    Runs 4 functions that request and validate a new word input
    when user's previous input has been rejected
    """
    request_another_word()
    exclude_numbers()
    exclude_repetitions()
    look_up_word()


def validate_nouns(fl_avail, dict_word):
    """
    Check whether the word meets specific criteria to be accepted
    as a noun. If not, request another input
    """
    if "noun" in fl_avail and (current_word.input == dict_word):
        word_found(dict_word, fl_avail)
        word_accepted()
    elif "noun" in fl_avail and (current_word.input != dict_word):
        console.print(Text(
            "Your word is a noun but it seems to be slightly "
            f"different from the valid option {dict_word}. "
            "Therefore, we adjusted your word accordingly."
        ))
        current_word.input = dict_word
        word_accepted()
    elif "plural noun" in fl_avail:
        console.print(Text(
            f"Your word is a plural noun. However, a singular or "
            "uncountable noun is required here.", style="orange3"
        ))
        get_and_check_another_input()
    else:
        incorrect_word_type()
        get_and_check_another_input()


def validate_plural_nouns(fl_avail, dict_word, word_checked):
    """
    Check if the word meets specific criteria to be accepted
    as a plural noun. If not, request another input
    """
    if "plural noun" in fl_avail:
        word_found(dict_word, fl_avail)
        word_accepted()
    elif "noun" in fl_avail:
        # Get index of the "noun" (ni) from fl_avail
        ni = fl_avail.index("noun")
        if 'ins' in word_checked[ni]:
            # Get the value 'if' (inflection = plural)
            pl = word_checked[ni]['ins'][0]['if'].split('*')
            plural = ''.join([str(item) for item in pl])
            if current_word.input == plural.upper():
                console.print(Text(
                    f"Your word has been found under {dict_word} "
                    f"(plural {plural.upper()}) and "
                    f"identified as: {fl_avail}"))
                word_accepted()
            else:
                console.print(
                    Text("Your word seems to be a singular noun."),
                    style="orange3")
                get_and_check_another_input()
        elif (current_word.input != dict_word and
                current_word.input.lower() in
                word_checked[ni]['meta']['stems']):
            word_found(dict_word, fl_avail)
            word_accepted()
        else:
            incorrect_word_type()
            get_and_check_another_input()
    else:
        incorrect_word_type()
        get_and_check_another_input()


def validate_adjectives(fl_avail, dict_word):
    """
    Check if the word meets specific criteria to be accepted
    as an adjective. If not, request another input
    """
    if ("adjective" in fl_avail and (
        current_word.input[-2:] != 'LY')) or (
            "adjective" in fl_avail and (
                current_word.input[-2:] == 'LY') and (
                    current_word.input in adj_with_ly())):
        word_found(dict_word, fl_avail)
        word_accepted()
    else:
        incorrect_word_type()
        get_and_check_another_input()


def validate_adverbs(fl_avail, dict_word):
    """
    Check if the word meets specific criteria to be accepted
    as an adverb. If not, request another input
    """
    if "adverb" in fl_avail:
        word_found(dict_word, fl_avail)
        word_accepted()
    elif ("adjective" in fl_avail and (
        current_word.input[-2:] == 'LY') and (
            current_word.input not in adj_with_ly())):
        word_found(dict_word, fl_avail)
        console.print(Text(
            "However, by adding the suffix -ly, you "
            "turned the adjective into an adverb, so..."))
        word_accepted()
    else:
        incorrect_word_type()
        get_and_check_another_input()


def validate_verbs(fl_avail, dict_word):
    """
    Check if the word meets specific criteria to be accepted
    as a verb. If not, request another input
    """
    if "verb" in fl_avail:
        word_found(dict_word, fl_avail)
        word_accepted()
    else:
        incorrect_word_type()
        get_and_check_another_input()


def valid_words_type(word_checked, fl_avail):
    """
    Checks if the valid word has the correct grammatical type
    (part 3/3 of the word input validation process)
    """
    # Variable dict_word will be used to show which exact word
    # has been found and checked in the dictionary to validate
    # user input
    if word_checked[0]['meta']['id'][-2] == ':':
        dict_word = word_checked[0]['meta']['id'][:-2].upper()
    else:
        dict_word = word_checked[0]['meta']['id'].upper()

    # Check whether specific word type criteria have been met
    if current_word.type == "noun":
        validate_nouns(fl_avail, dict_word)
    elif current_word.type == "plural noun":
        validate_plural_nouns(fl_avail, dict_word, word_checked)
    elif current_word.type == "adjective":
        validate_adjectives(fl_avail, dict_word)
    elif current_word.type == "adverb":
        validate_adverbs(fl_avail, dict_word)
    elif current_word.type == "verb":
        validate_verbs(fl_avail, dict_word)


def get_fl(word_checked):
    """
    Gets all available functional labels for the current
    word and adds them to the list fl_avail
    """
    fl_avail = [word_checked[0]['fl']]

    # Check for homographs - words with multiple labels
    if len(word_checked) > 1 and (
        'hom' in word_checked[1]) and (
            'fl' in word_checked[1]):
        fl_avail.append(word_checked[1]['fl'])

        if len(word_checked) > 2 and (
            'hom' in word_checked[2]) and (
                'fl' in word_checked[2]):
            fl_avail.append(word_checked[2]['fl'])

            if len(word_checked) > 3 and (
                'hom' in word_checked[3]) and (
                    'fl' in word_checked[3]):
                fl_avail.append(word_checked[3]['fl'])
    valid_words_type(word_checked, fl_avail)


def alternative_spelling(word_checked):
    """
    Handles word inputs with British spelling and offers
    to swap the word for its American counterpart to enable
    validation
    """
    amer = word_checked[0]['cxs'][0]['cxtis'][0]['cxt'].upper()
    error_msg_uk = Text("We weren't able to check your word. "
                        "However...", style="orange3")
    console.print(error_msg_uk)
    switch_to_amer = input(
        "There seems to be a similar word with US spelling. "
        f"\nWould you like to try {amer} instead? "
        "(Y/N) ").upper().strip()
    if switch_to_amer == 'Y':
        current_word.input = amer
        look_up_word()
    elif switch_to_amer == 'N':
        get_and_check_another_input()
    else:
        invalid_input = Text(
            "Your input was invalid...", style="orange3")
        console.print(invalid_input)
        get_and_check_another_input()


def validate_word(word_checked):
    """
    Makes sure that user input is a valid word and adds
    the word's 'fl' (functional label like "noun" or "verb") to the
    list of available labels called fl_avail
    (part 2/3 of the word input validation process)
    """
    try:
        # Aiming to access 'fl' of the given word (e.g. noun, verb)
        if 'fl' in word_checked[0]:
            get_fl(word_checked)

        # If such a label is not found (usually for plural nouns)
        elif 'cxs' in word_checked[0] and \
                'plural of' in word_checked[0]['cxs'][0]['cxl']:
            fl_avail = ["plural noun"]
            valid_words_type(word_checked, fl_avail)

        # If British spelling rather than American
        elif 'cxs' in word_checked[0] and 'British spelling' \
                in word_checked[0]['cxs'][0]['cxl']:
            fl_avail = []
            alternative_spelling(word_checked)

        # None of the above requirements was met when checking
        # the word - invalid word
        else:
            console.print(Text(
                "Oops, something went wrong.", style="orange3"))
            get_and_check_another_input()

    # Word not found in the dictionary (misspelled)
    except TypeError:
        console.print(Text(
            "Please check for typos...", style="orange3"))
        get_and_check_another_input()

    # Word could not be validated (none of the required
    # details regarding its 'fl' could be accessed)
    except IndexError:
        console.print(Text(
            "Unfortunately, your input could not be validated "
            "(possibly not a word).", style="orange3"))
        get_and_check_another_input()


def look_up_word():
    """
    Looks up each word input in the dictionary
    (part 1/3 of the word input validation process)
    """
    # Access the dictionary API key
    load_dotenv()
    APP_KEY = os.getenv('API_KEY_SERVICE')

    try:
        response = requests.get(
            "https://www.dictionaryapi.com/api/v3/references/"
            f"collegiate/json/{current_word.input}?key={APP_KEY}")
        word_checked = response.json()
        validate_word(word_checked)

    # Problem with connecting to the dictionary API
    except ConnectionError:
        console.print(Text("Sorry, there was a connection issue and we "
                           "couldn't access the dictionary to check your "
                           "word input.", style="orange3"))
        restart = input("Type R and press Enter to restart the "
                        "game: ").upper().strip()
        if restart == "R":
            clear_terminal()
            restart_program()
        else:
            console.print(Text("Invalid input.", style="orange3"))
            restart_ask_again = input(
                "Please type R and press Enter to restart the game: "
                ).upper().strip()
            if restart_ask_again == "R":
                clear_terminal()
                restart_program()
            else:
                console.print(Text(
                    "Invalid input. We'll end the game now. "
                    "Please come back later or click the orange"
                    "RUN PROGRAM button above to play again."))
                console.print(Text(
                    "Thanks for playing MAD LIBS!", style="sea_green1"))

    # When user presses Enter without submitting any input
    except requests.exceptions.JSONDecodeError:
        console.print(Text("Something went wrong...", style="orange3"))
        get_and_check_another_input()


def start_game():
    """
    Starts a game by printing the welcome message
    and asking for and validating word inputs
    """
    welcome()
    # A list of all required word inputs
    words_needed = (noun1, noun2, noun_pl, adj1, adj2, adv, verb)
    for word in words_needed:
        get_word_input()
        exclude_numbers()
        look_up_word()


if __name__ == "__main__":
    start_game()


class Story:
    """
    A mad lib story with blanks
    """
    def __init__(self, title, text):
        self.title = title
        self.text = text


madlib1 = Story("\nStrange Science", "\nScience is full of "
                f"{adv.input} strange facts and stories. "
                "Did you know that rats can laugh when they are being "
                f"tickled? Another fun {noun1.input} about "
                "rats is that their teeth never stop growing. Babies "
                f"may be {adj1.input} but they have 100 more "
                f"{noun_pl.input} than adults. When babies "
                f"are born, they have the ability to {verb.input}. "
                f"Newborn rats have {adj2.input} stomachs. They are "
                f"approximately the size of a(n) {noun2.input}.")

madlib2 = Story("\nFall Fun", "\nThe weather is starting to turn crisp. "
                f"The wind is blowing through the {noun_pl.input}. "
                f"I am excited to go {noun1.input} picking "
                "this weekend. Each autumn, my family drives out to my "
                "uncle's orchard. We pick as many apples as our "
                f"{noun2.input} can hold. This year we are also "
                f"going to {verb.input} a scarecrow contest. I "
                f"can't decide if I want the face to be {adj1.input} "
                f"or {adv.input} {adj2.input}.")

madlib3 = Story("\nSpace Adventure", "\nOnce upon a time, in a galaxy "
                "far, far away, there was an adventurous "
                f"{noun1.input} named Anakin. One day, Anakin hopped "
                f"aboard their {adj1.input} spaceship - his mission "
                f"was to {verb.input} a new {noun2.input}. "
                f"As the spaceship soared through the {adj2.input} "
                "galaxy, Anakin marvelled at the twinkling "
                f"{noun_pl.input} he passed. {adv.input}, "
                "an asteroid appeared out of nowhere and shot across their "
                "path.")

madlib4 = Story("\nAre we alone?", f"\nAfter many {adj1.input} days "
                f"and nights, Buzz {adv.input} arrived at the "
                "mysterious planet. He stepped out of the "
                f"{noun1.input} and was greeted by "
                f"{adj2.input} {noun_pl.input} "
                "and other curious creatures. He wanted to "
                f"{verb.input} the {noun2.input} and become "
                "friends with the locals. But his intuition was telling him "
                "that he couldn't trust his hosts...")

madlib5 = Story("\nSummer Camp Mystery", f"\nIt was a(n) {adv.input} "
                f"{adj1.input} summer day - the first day of camp! "
                f"The camp counsellor told us to {verb.input} for "
                f"the {noun1.input} - a local legend with sharp "
                f"teeth, bushy {noun2.input}, and a very "
                f"{adj2.input} smell. That night as other campers "
                "and I were going to sleep, we heard a noise. It sounded "
                f"like someone chewing on {noun_pl.input}...")

madlib6 = Story("\nFirst Day at Wizard School", "\nHermione jumped out "
                f"of {noun1.input} as she opened her eyes. "
                "Today was her first day at wizard school! "
                f"She dressed {adv.input}, grabbing a "
                f"pointy hat to {verb.input} on her head. Arriving "
                "at school, she took her seat in class and prepared her "
                "first potion. The ingredients included a(n) "
                f"{adj1.input} bezoar and {adj2.input} "
                f"{noun_pl.input}. It would be worth it when "
                f"she could turn a spider into a(n) {noun2.input}.")

madlib7 = Story("\nAmazon Explorers", f"\nThe {adj1.input} "
                "explorer flew his plane over the Amazon jungle. "
                f"Below, he could {verb.input} tall trees "
                f"growing along the edge of a(n) {noun1.input}. "
                "Behind him, he could hear his co-pilot, Emma, muttering. "
                f"'We are not going to make it! When the {adj2.input} "
                "eagle flew into the wing, it damaged it too much. We need "
                f"to find somewhere clear to land.' {adv.input}, "
                "Marcus noticed a clearing - a perfect landing spot. "
                "They got out of the plane to check the damaged "
                f"{noun2.input}. Suddenly, a loud roar made them "
                "jump. From out of the jungle emerged "
                f"a pair of {noun_pl.input}...")

madlib8 = Story("\nDino Danger", "\nDinosaurs were a diverse group of "
                f"{noun_pl.input} that lived on Earth until "
                "about 66 million years ago. Some dinosaurs were "
                f"carnivores - they ate {noun1.input}. Other "
                f"dinosaurs were herbivores and ate {noun2.input}. "
                f"One of the most {adj1.input} dinosaurs "
                f"had a(n) {adj2.input} armour along its back. "
                f"It walked {adv.input} due to its large size. "
                "Imagine how amazing it would have been to see dinosaurs "
                f"{verb.input} through cities and fly in the sky…")


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
    console.print(Text(randomly_chosen_title, style="bold sea_green1"))
    console.print(Text(matching_text, style="sea_green1"))

    # Update the list of available titles and texts
    available_titles = list_of_titles.remove(randomly_chosen_title)
    available_texts = list_of_texts.remove(matching_text)


def reuse_words():
    """
    Prints another story to the terminal (as long as there is a story
    available) while re-using word inputs. Called when user chooses to
    play again and picks option A
    """
    try:
        clear_terminal()
        choose_story_randomly(available_titles, available_texts)
        play_again_or_not()
    except IndexError:
        console.print(Text(
            "\nYou have seen all available stories.", style="orange3"))
        all_stories_used = input(
            "If you would like to start a new game, "
            "type Y and press Enter. \nAny other input will end "
            "the game: ").upper().strip()
        if all_stories_used == "Y":
            clear_terminal()
            restart_program()
        else:
            end_game = "\nThanks for playing MAD LIBS!"
            console.print(Text(end_game, style="bold sea_green1"))


def how_to_play_again():
    """
    Works only if the user chooses to play again. Gives the user
    2 options regarding how to play a new game.
    """
    while True:
        try:
            new_game_options = ["A", "B"]
            new_game_input = input(
                "\nIf you would like to re-use your words with a "
                "different story, type A and press Enter. If you'd "
                "like to start a brand new game, type B and press "
                "Enter: "
                ).upper().strip()
            test_new = new_game_input.isalpha()
            if test_new is False:
                raise ValueError
            if new_game_input in new_game_options:
                break
            else:
                console.print(Text("Invalid input. Let's try one more "
                                   "time..."), style="orange3")
        except ValueError:
            console.print(Text("Your input is invalid. Let's try "
                               "again..."), style="orange3")
    if new_game_input == "B":
        clear_terminal()
        restart_program()
    else:
        reuse_words()


def play_again_or_not():
    """
    Asks the user whether they would like to play again
    and gives them options
    """
    while True:
        try:
            play_again_options = ["Y", "N"]
            play_again_input = input(
                "\nWould you like to play again (Y/N)? ").upper().strip()
            test_play_again = play_again_input.isalpha()
            if test_play_again is False:
                raise ValueError
            if play_again_input in play_again_options:
                break
            else:
                console.print(Text(
                    "Invalid input. Let's try one more time..."),
                    style="orange3")
        except ValueError:
            console.print(Text("Your input is invalid. Let's try "
                               "again..."), style="orange3")
    if play_again_input == "N":
        end_game = "\nOkay, thanks for playing MAD LIBS!"
        console.print(Text(end_game, style="bold sea_green1"))
    else:
        how_to_play_again()


def print_story():
    """
    Prints a mad lib story with user's inputs to the terminal
    and handles what happens next (end game or play again)
    """
    sleep(1.5)
    clear_terminal()
    choose_story_randomly(available_titles, available_texts)
    play_again_or_not()


if __name__ == "__main__":
    print_story()

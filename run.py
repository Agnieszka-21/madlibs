# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from madlibs_stories import madlib1, madlib2, madlib3, madlib4, madlib5, madlib6, madlib7, madlib8
import random 


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


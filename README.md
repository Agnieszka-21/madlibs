![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Mad Libs Grammar

## Introduction

Mad Libs Grammar is a web application developed in Python. It is based on the concept of Mad Libs - a simple game for both children and adults. Sometimes played purely for fun or as a party game, in this application the game clearly focuses on grammar, asking the user for word inputs that are specifically nouns, adjectives, adverbs and verbs. Therefore, this particular version of Mad Libs is aimed toward any users who understand the basics of the English grammar. Any provided word inputs are validated via API, one by one, using an online dictionary. Once all required word inputs are obtained and accepted as valid, one of available stories is printed to the terminal, with the user's inputs instead of any blanks, providing a quick fun read full of surprising twists. 

The game utilizes the Code Institute's template that generates a "terminal" onto the page, making it available within a web browser. 

## Table of Contents

## UX

### The Strategy Plane

Mad Libs Grammar is simple and fun game for both children (about 10+) and adults. It is based on the concept of Mad Libs - stories with words removed and replaced by blank spaces, where the user is asked for specific word/phrasal inputs to fill these blanks, without knowing the story. After obtaining all words that are needed, the full story is presented to the user, providing a quick, fun read full of unusual twists - sometimes weird and nonsensical, sometimes hilarious. 

In Mad Libs Grammar the user is asked specifically for nouns, adjectives, adverbs, and verbs. Each word input is looked up via API in an online dictionary and validated.

#### Site Goals
- To entertain users with a simple and quick game.
- To educate, test knowledge, and revisit the basics of the English grammar.
- To provide users with multiple short and engaging stories to read.

#### User Stories
- As a user, I want to enjoy a quick, simple online game on my own.
- As a user, I want a fun challenge that tests my knowledge and sharpens my cognitive skills.
- As a user, I want to enjoy reading short, funny stories with unexpected twists.

### The Scope Plane

Features planned include:
- Ensure the game is contained within the game terminal screen, taking into account its limitations.
- In spite of the confines of the terminal, the game should be easy to follow, visually clear, and easy on the eye.
- After finishing the game, the user should be able to play again easily and given 2 options:
  1) re-use the same words with a different story for a quick fun read, or
  2) start from scratch by submitting new word inputs.
  

### The Structure Plane

#### User Story 1
"I want to enjoy a quick, simple online game on my own."

#### Acceptance Criteria
It should be clear to the user that this is a game, and there should be a concise explanation regaridng how to play it (including how to provide required inputs).

#### Implementation
The user will be shown a "welcome screen" with a colorful game title, a how-to-play blurb, and the first required input to encourage quick and easy interaction.

#### User Story 2
"I want a fun challenge that tests my knowledge and sharpens my cognitive skills."

#### Acceptance Criteria
The game should have a clear challenge - in this case testing the user's grammar skills and requiring some creativity on the part of the user who has to come up with words that meet specific criteria (be a noun, adjective, adverb, or verb).

#### Implementation
The user will be asked to submit 7 words, one at a time: 2 nouns, 1 plural noun, 2 adjectives, 1 adverb, and 1 verb. Each of these inputs will be validated accordingly (see the chart below), making sure that the user submitted a word that can be found in an online dictionary (connected via API). This means that any empty inputs, special characters, numbers, made-up words and words with typos will not be accepted. 

The user will be informed with orange text (to catch their attention and convey that something is wrong - without the negative associations most users would have if the color was red rather than orange) what the issue was and asked for another input instead. 
Some examples will be given to the user to make sure that they clearly understand what is expected of them and do not get stuck or frustrated at any point.

If a word input is deemed valid, the user will be informed that their word was found in the dictionary and what the word's grammatical function (or functions, if the word has multiple meanings & functions) is to provide clarity. A sea green message will be printed to confirm that the user's word input has been accepted, and the user will be prompted to submit the next required word. This process will be repeated until all 7 valid inputs are obtained. 

#### User Story 3
"I want to enjoy reading short, funny stories with unexpected twists."

#### Acceptance Criteria
At least a few different short and engaging stories should be available so that the user can play the game multiple times, and maybe even re-use their words with various stories to have some extra fun without too much effort. 

#### Implementation
Eight stories will be provided, each with a different theme, some of them loosely based on well-known books and films to create some entertaining references. Once all word inputs are obtained from the user, one of the stories will be randomly chosen and printed to the terminal. The user will be also asked right away (underneath the story) if they would like to play again, and if they choose to do so, they will be given an option to re-use their words so that they can enjoy reading various fun stories without having to provide new words each time. Should they choose this option mutiple times and run out of available stories, they will be informed that they can restart the game.


### The Skeleton Plane

- __Game logic__
  
The following flowchart was created to depict the basic logic of the game. It illustrates the steps that are needed for a complete game of Mad Libs Grammar, without going into too much detail.

![Flowchart - game logic](link)

Since getting 7 valid word inputs from the user (2 nouns, 1 plural noun, 2 adjectives, an adverb, and a verb) is an essential part of this application, much thought went into creating and refining a reliable validation process for these inputs. To keep it clear and easy to follow, I split it into 3 parts:

- __Word input validation - part 1__
  
  - Request a word input from the user, specifying which grammatical type is needed (e.g. a noun). 
  - Make sure the input is not a number (integer) using the function exclude_numbers.
    - If the input is a number: inform the user that numbers are not allowed and request another input instead, adding examples of the required word type for clarity. Restart the valiation process.
    - If the input is not a number, simply move on to the next step.
  - Via API, try to establish a connection with the online dictionary (Merriam-Webster Collegiate Dictionary), and look up the word submitted by the user (function look_up_word).
    - Possible errors and how to handle them:
      - ConnectionError: the online dictionary could not be accessed. Apologize for the issue and ask the user if they would like to restart the game. Ask for input (R) - if R is submitted, clear the terminal and restart the program. If the user submits anything else, inform them that their input is invalid and ask more last time if they would like to restart the game, requesting input (R). If the input is invalid again, simply print the thank you message and end the game. Otherwise, clear the terminal and restart the program.
      - requests.exceptions.JSONDecodeError: the user pressed Enter without submitting anything. Inform them that something went wrong and request input once again, this time adding examples of the required word type for more clarity. Restart the validation process.
    - If there are no errors, move on to part 2 of word validation inside the nested function validate_word.

  ![Flowchart - validation part 1](link)

- __Word input validation - part 2__

  - Try to access specific details in the dictionary within the entry for the word that is being validated (nested function validate_word, inside the function look_up_word).
  - These specific details include:
    - A key called 'fl' (functional label). Its value defines the grammatical function of the word (e.g. "noun"). In case the word is a homograph and therefore has multiple meanings and functions (like "extract", for example, which is both a verb and a noun), check its further 'fl' keys (up to 2 more, if available) for a more accurate validation. If at least one 'fl' was found, add its value to the list called fl_avail, which gathers available functional labels of the current word. This prepares us for part 3 of word validation.
    - If the 'fl' key has not been found, look for another key called 'cxs', and if it is present, check whether it contains under 'cxl' (a nested key) the value "plural of". Irregular plural forms of nouns (such as "mice" or "men") can be identified this way. Add "plural noun" to the list called fl_avail and move on to part 3 of the validation process.
    - If "plural of" has not been found inside the 'cxl' key, check whether the 'cxs' key is present and whether the nested key 'cxl' contains the phrase "British spelling". This is the case for words that are spelled differently in US English and British English. Since the online dictionary prioritizes US spelling, the British version - while it still has its own entry - does not contain any of the information needed to identify the word type. Therefore, inform the user that their word could not be validated but there is a similar word with US spelling, and ask them if they would like to submit that word instead. If they agree, find the word's 'fl' by going back to look_up_word in order to restart the validation process (since the input is clearly not a number, we can skip the part of excluding numbers). If the user refuses to use the suggested word (input N) or submits an invalid input, request another word input from them, adding examples of the expected word type for more clarity, and restart the validation process.
    - If none of these details could be accessed (for example, the user submitted a bunch of random letters that are not even similar to any actual word), inform the user that something went wrong and request another input, specifying the expected word type and adding examples. Restart the validation process.
  - Possible errors and how to handle them: 
    - IndexError: occurs when the user submits a floating point number, an input containing special characters etc. Inform the user that their input could not be validated and is possibly not a word. Request another input, adding examples of the currently required word type for more clarity. Restart the validation process.
    - TypeError: the word submitted by the user was misspelled (in such a case the dictionary simply returns a list of similar words). Ask the user to check for typos and request another input, adding examples of the expected word type. Restart the validation process.
  
  ![Flowchart - validation part 2](link)

- __Word input validation - part 3__

  - This is the last part of the word validation process, and it is being taken care of by the function valid_words_type, nested inside validate_word, which is nested inside the look_up_word function. 
  - Once the list fl_avail contains a value or multiple values (like "noun", "adjective" etc.) after going through the validate_word function, check whether the 'fl' value for the current word is correct for the expected word type. If needed, other criteria might need to be met, too. Each word type has its own set of criteria.
  - Nouns simply need the value "noun" in fl_avail to be accepted. If this value is not present, the user is informed that their word is not a noun, and a new input is requested. The message includes examples of the expected word type. Once a new input is obtained, the entire validation process is restarted for the new word input.
  - Plural nouns are accepted if the value "plural noun" is found within fl_avail (for nouns with irregular plural form), or if the value "noun" is found in fl_avail and the submitted word was found under the key 'stems' in the dictionary (which lists all the entry's headwords, variants, inflections... including its plural form). 
  - Adjectives are acceped if the value "adjective" is found in fl_avail, as long as the word does not end in 'LY'. Otherwise, if an adjective ends in 'LY', an additional criterium must be met: the adjective needs to be found in the list adj_with_ly. This additional requirement resulted from the realization that while many adverbs end in 'LY' (basically, one can create an adverb by adding the suffix -ly to an adjective, e.g. "glad" - "gladly"), there are also multiple adjectives with this ending, and this additional criterium helps to avoid inaccurate classification. If these criteria are not met, the user is informed that their word is not an adjective, and is requested to submit another input (examples are given in order to make it clear and simple). The validation process starts from the beginning for that new input.
  - Adverbs are accepted if the value "adverb" is present in fl_avail. Since some adverbs that are derived from adjectives do not have separate entries in the dictionary, another option is to have the value "adjective" in fl_avail if the word ends in 'LY', and it is not found in the list of adj_with_ly. (SCREEENSHOT) If these criteria are not met, the user is informed that their word is not an adverb, and is requested to submit another input (examples of the expected word type are given for more clarity). The validation process starts from the beginning for that new input.
  - Verbs simply need the value "verb" in fl_avail to be accepted. If this value is not present, the user is informed that their word is not a verb, and is requested to submit another input (again, word examples are given). The validation process starts from the beginning for that new input.
  
  ![Flowchart - validation part 3](link)

This 3-part validation process runs in a loop until each of the 7 required word inputs is obained. Once all inputs are validated and accepted, one of the available mad lib stories is chosen randomly and printed to the terminal with the user's inputs in specified places. The user can then read the entire story and enjoy the unexpected twists and turns. 

- __End of game__
  
The user is also asked whether they would like to play again, and if they decide to do so, they are given 2 options: 
  - Option A is to simply re-use the same word inputs with another story, which allows for more entertainment, quickly and effortlessly. In order to ensure that stories are not repeated, the function choose_story_randomly removes each printed story from the list of available options. When the user repeats option A multiple times and all stories are printed to the terminal, a message pops up in the terminal to inform that there are no other stories left; the user is offergiven the option to restart the game with new word inputs. Alternatively, they can finish the game.
  - Option B is to start from the beginning, with new word inputs. If the user chooses this option, the terminal is cleared, and the program starts again from the beginning.
Whenever the user decides to end the game, a thank you message is printed to the terminal. The flowchart below illustrates the process of ending the game in more detail.

![Flowchart - end of game](link)

- __The use of classes__
  
In order to not only deepen my understanding of Python classes, but also to keep the number of variables with global scope to a minimum, I decided to create two classes for this program. 
  - Class Words is initiated with 3 instance variables: input, word_type, and examples. There are 7 instances of that class, one for each required word input. While the value of the variable "input" will be replaced by user's word input, the other two variables stay unchanged and are used during the word validation process (e.g. in printed statements).
  - Class Story is initiated with 2 instance variables: title and text. There are 8 instances of that class, one for each mad lib. 

The use of these two classes allows for adding further word inputs and stories in a simple way and makes the code easily readable. 


### The Surface Plane



## Future Enhancements

- A more accurate process for validating plural and singular nouns would be helpful in maintaining the educational aspect of the game. Nouns with irregular plural form are always validated correctly, which is great. However, ensuring that nouns with a regular plural form (e.g. "dog" - "dogs") are correctly classified as singular or plural is rather challenging. The online dictionary does not seem to offer a way of making that distinction unambiguously. While there is a key containing inflections ('ins') with a nested key 'if' and its value being a fully spelled-out inflection, this particular value contains the asterisk sign (*) if the word has more than one syllable. Therefore, a simple comparison of the submitted word to this value does not suffice to provide accurate validation and a more refined solution would need to be applied.
- More stories could be added as further instances of the class Story to provide a wider range of topics and to keep users entertained for longer, also encouraging them to return to the application multiple times.


## Testing

### Testing Overview

### Validator Testing

### Notable Bugs

## Libraries Utilized

## Deployment

The application has been deployed via Heroku.

This program was developed using a [template from the Code Institute](https://github.com/Code-Institute-Org/p3-template). Since the provided README.md in the template clearly states that the code should be contained within the run.py file, I decided not to split it into smaller files. The only exception is a separate Python file (inside the directory python_madlibs) with a long list of adjectives ending in 'ly' and a function that adjusts that list accordingly. This ensures that the code stays clear and easily readable. Moreover, the template requests not to make any changes to other files (e.g. the html files) to make sure that the project deploys correctly. Therefore, I did not add any further styling for the page and the only styling is done inside the terminal (Rich library).

In order to deploy the application to Heroku I followed the following steps:
- Sign up or log in to Heroku.
- On the main Heroku dashboard page select "Create new app".
- Give the project a unique name (mad-libs-grammar), select a suitable region, and click "Create app". This will create the app in Heroku and bring you to the Deploy tab.
- Switch to the Settings tab. 
- In the "Config Vars" section click the "reveal config vars" button.
- In the KEY input field enter "PORT" (all capitals), in the VALUE field next to it enter "8000", and then click the "Add" button to the right. This config var is required because we are using the Code Institute's template.
- Add one more config var, with the KEY "API_KEY_SERVICE" and the VALUE that is the API key used to access the dictionary. Click "Add".
- In the section "Buildpacks" click the "Add buildpack" button and select "python". Confirm by clicking the button "Add buildpack". Then click the button "Add buildpack" once again and select "nodejs". Confirm ("Add buildpack").
-  The order of these buildpacks is important. If you added nodejs before python, you can easily rearrange this with a drag-and-drop.
-  Scroll up to the top of the page and switch to the Deploy tab. 
-  In the "Deployment Method" section choose the "GitHub" button. Follow the next steps (if any) as prompted to connect your GitHub account. In the "Connect to GitHub" section that appears, choose your account, enter the name of your repository, and select "Search".
-  Once your GitHub repo is connected to the Heroku app, scroll down to the section "Automatic deploys".
-  Confirm that the correct branch of the repo is selected in the drop-down box, and select "Enable Automatic Deploys". Whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app.
-  Alternatively, you can use the option "Manual deploys" (for this projects, I used the "automatic deploys" option that allowed me to see changes I made to the app as I developed it).
-  Heroku will now build the app for you. Once the process is completed, you will see the message "Your app was successfully deployed", and a link to the app where you can visit the live site.


## Credits

The following tutorials, articles, documentation and media were used to create this website...

### Code

- The function clear_terminal is based on the code from an article on the forum [geeksforgeeks.org](https://www.geeksforgeeks.org/clear-screen-python/). Link included also in the run.py file.
- Code for the function restart_program has been copied from [jrosco's GitHub account](https://gist.github.com/jrosco/d01b28c2f37100bb5278). Link included also in the run.py file.
- [This YouTube tutorial](https://www.youtube.com/watch?v=hpc5jyVpUpw) from VideoLab proved extremely helpful in understanding API and how to access and use the online dictionary in my program.
- [This documentation](https://rich.readthedocs.io/en/stable/index.html) proved indespensible when working with the Rich library (text styling).
- [The following article by Jake Witcher](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) helped me understand how to use an .env file to safely store my API key for the online dictionary.
- 

### Content

- [The Dictionary API Merriam-Webster](https://dictionaryapi.com/products/api-collegiate-dictionary) has been used to validate word inputs from the user. [Related documentation](https://dictionaryapi.com/products/json) was particularly helpful in developing accurate word validation.
- Short texts (stories) used in this application have been adapted from mad libs on [twinkle.ie](https://www.twinkl.ie/) - a website with numerous resources for teachers.
- [This website](https://word-lists.com/word-lists/list-of-adjectives-ending-in-ly/) is the source of a comprehensive list of adjectives ending in 'ly' (directory python_madlibs, file adj_list_ly_ending.py). The list has allowed for a much more accurate validation of adjectives and adverbs, ensuring at the same time that these word types can be clearly distinguished from one another.


## Acknowledgements

I would like to express my sincere gratitude to my mentor, Matt Bodden, whose suggestions and practical advice helped me ensure that this project not only takes my understanding of Python to a higher level, but also encourages best practices that result in a positive experience for the user of this web application.

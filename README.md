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
  
![Flow chart - initial game logic](link)

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

### The Surface Plane



## Future Enhancements

## Testing

### Testing Overview

### Validator Testing

### Notable Bugs

## Deployment

## Credits

The following tutorials, articles, documentation and media were used to create this website.

### Code

### Content

- The API Dictionary Merriam-Webster (https://dictionaryapi.com/products/api-collegiate-dictionary) has been used to validate word inputs from the user.

### Media?

## Acknowledgements

I would like to express my sincere gratitude to my mentor, Matt Bodden, whose suggestions and practical advice helped me ensure that this project not only takes my understanding of JavaScript to a higher level, but also encourages best practices that result in a positive experience for the user of this web application.

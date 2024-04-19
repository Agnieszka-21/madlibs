# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Required user's inputs
noun1 = input("Noun: ")
noun2 = input("Another noun: ")
noun_pl = input("Plural noun: ")
adj1 = input("Adjective: ")
adj2 = input("Another adjective: ")
adv = input("Adverb: ")
verb = input("Verb: ")

# First mad lib
madlib = f"Science is full of {adv} strange facts and stories. Did you know that \
rats can laugh when they are being tickled? Another fun {noun1} about rats is that \
their teeth never stop growing. Babies may be {adj1} but they have 100 more {noun_pl} \
than adults. When babies are born, they have the ability to {verb}. Newborn rats have \
{adj2} stomachs. They are approximately the size of a(n) {noun2}."

# Print the mad lib to the terminal once all inputs have been gathered
print(madlib)

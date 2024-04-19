def madlib():

    # Required user's inputs
    noun1 = input("Noun: ")
    noun2 = input("Another noun: ")
    noun_pl = input("Plural noun: ")
    adj1 = input("Adjective: ")
    adj2 = input("Another adjective: ")
    adv = input("Adverb: ")
    verb = input("Verb: ")

    # Mad lib number 4
    madlib = f"Are we alone? \nAfter many {adj1} days and nights, Buzz {adv} \
    arrived at the mysterious planet. He stepped out of the {noun1} and \
    was greeted by {adj2} {noun_pl} and other curious creatures. \
    He wanted to {verb} the {noun2} and become friends with the locals. \
    But his intuition was telling him that he couldn’t trust his hosts..."

    print(madlib)
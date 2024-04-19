def madlib():

    # Required user's inputs
    noun1 = input("Noun: ")
    noun2 = input("Another noun: ")
    noun_pl = input("Plural noun: ")
    adj1 = input("Adjective: ")
    adj2 = input("Another adjective: ")
    adv = input("Adverb: ")
    verb = input("Verb: ")

    # Mad lib number 5
    madlib = f"\nSummer Camp Mystery \nIt was a(n) {adv} {adj1} summer day - the first day of camp! \
The camp counsellor told us to {verb} for the {noun1} \
- a local legend with sharp teeth, bushy {noun2}, and \
a very {adj2} smell. That night as other campers and I were \
going to sleep, we heard a noise. It sounded like someone \
chewing on {noun_pl}..."

    print(madlib)
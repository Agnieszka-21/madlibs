def madlib():   
    
    # Required user's inputs
    noun1 = input("Noun: ")
    noun2 = input("Another noun: ")
    noun_pl = input("Plural noun: ")
    adj1 = input("Adjective: ")
    adj2 = input("Another adjective: ")
    adv = input("Adverb: ")
    verb = input("Verb: ")

    # Mad lib number 2
    madlib = f"\nFall Fun \nThe weather is starting to turn crisp. \
The wind is blowing through the {noun_pl}. I am excited to go \
{noun1} picking this weekend. Each autumn, my family drives out to my \
uncle’s orchard. We pick as many apples as our {noun2} can hold. \
This year we are also going to {verb} a scarecrow contest. I can’t decide \
if I want the face to be {adj1} or {adv} {adj2}."

    print(madlib)
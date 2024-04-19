def madlib():

    # Required user's inputs
    noun1 = input("Noun: ")
    noun2 = input("Another noun: ")
    noun_pl = input("Plural noun: ")
    adj1 = input("Adjective: ")
    adj2 = input("Another adjective: ")
    adv = input("Adverb: ")
    verb = input("Verb: ")

    # Mad lib number 8
    madlib = f"Dino Danger \nDinosaurs were a diverse group of {noun_pl} \
that lived on Earth until about 66 million years ago. Some \
dinosaurs were carnivores - they ate {noun1}. Other \
dinosaurs were herbivores and ate {noun2}. One of the most {adj1} \
dinosaurs had a(n) {adj2} armour along its back. It walked \
{adv} due to its large size. Imagine how amazing it would \
have been to see dinosaurs {verb} through cities \
and fly in the sky…"

    print(madlib)
from random import shuffle

phrase = input("Veuillez entrer une liste de mots séparés par '/' : ").split("/")
shuffle(phrase)

if len(phrase) <= 10:
    print("Les deux premiers mots de la liste sont", phrase[:2])
else:
    print("Les trois derniers mots de la liste sont", phrase[len(phrase)-3:])
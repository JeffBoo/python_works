from random import shuffle

liste_mots_raw = input("Ecrire de mots selon cette syntaxe mot1/mot2/mot3... : ")
liste_mots = liste_mots_raw.split("/")
shuffle(liste_mots)

if len(liste_mots) < 10:
    print(liste_mots[0], liste_mots[1])
else:
    print(liste_mots[len(liste_mots)-3], liste_mots[len(liste_mots)-2], liste_mots[len(liste_mots)-1])
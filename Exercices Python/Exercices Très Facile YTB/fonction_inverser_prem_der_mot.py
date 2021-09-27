
def intervertir_mot(phrase):
    phrase_list = phrase.split()
    n = len(phrase_list) # longueur de phrase_list
    premier_mot = phrase_list[0]
    dernier_mot = phrase_list[n-1]
    phrase_list.pop(0)
    phrase_list.pop()
    phrase_intermediaire = " ".join(phrase_list)
    phrase_intervertie = dernier_mot + " " + phrase_intermediaire + " " + premier_mot
    print(phrase_intervertie)


texte = input("Ecrire une phrase : ")
intervertir_mot(texte)
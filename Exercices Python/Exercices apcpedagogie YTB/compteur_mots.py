


def compteur_mot(phrase):
    nbre_mots = 0
    prec_car = " "
    for char in phrase:
        nbre_mots += int(prec_car == " " and char != " ")
        prec_car = char
    return nbre_mots

texte = input("Ecrire une phrase : ")
print("Il y a", compteur_mot(texte), "mot(s) dans la phrase :", texte)



"""Consigne : Vérifier si un entier positif composé de 5 chiffres distincts"""

entier = int(input("Saisir un nombre entier positif : "))
entier_trouve = True

if len(str(entier)) == 5 and entier > 0:
    nombre = str(entier)
    for chiffre in nombre:
        if nombre.count(chiffre)>1:
            entier_trouve = False
            break
    if entier_trouve == True:
        print(entier, "est distinct")
    else:
        print(entier, "n'est pas distinct")
else:
    print("Saisir un nombre positif composé de 5 chiffres !")

def supp_doublon(liste):
    nouvelle_liste = []
    for element in liste:
        if element not in nouvelle_liste:
            nouvelle_liste.append(element)
    return nouvelle_liste


print("Entrez des valeurs. Appuyez sur Entrée pour terminer")

liste_valeurs = []
nb_elements = 0

while True:
    valeur = input("Saisir une valeur : ")
    if valeur:
        try:
            liste_valeurs.append(int(valeur))
            nb_elements += 1
        except:
            continue
    else:
        break
print("Valeurs entrées : ", liste_valeurs)
print("Nombre d'éléments de la liste : ", nb_elements)
print("La nouvelle liste est : ", supp_doublon(liste_valeurs))

def freq_mot_fichier(nom_fichier):
    file = open(nom_fichier, "r")
    content = file.read()
    liste_mots = content.split()
    file.close()

    list_mot_unique = []
    for mot in liste_mots:
        if mot not in list_mot_unique:
            list_mot_unique.append(mot)
            print("Le mot", mot, "apparaît", liste_mots.count(mot))

fichier = input("Entrez le nom du fichier : ")
freq_mot_fichier(fichier)
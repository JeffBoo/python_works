
def un_mot_par_ligne(nom_fichier):
    file = open(nom_fichier, "r")
    content = file.read()
    liste_mots = content.split()
    file.close()
    file = open(nom_fichier, "w")
    for mot in liste_mots:
        file.write(mot + "\n")
    file.close()

fichier = input("Quel fichier voulez-vous modifier ? ")
un_mot_par_ligne(fichier)
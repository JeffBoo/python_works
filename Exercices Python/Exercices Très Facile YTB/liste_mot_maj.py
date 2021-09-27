
def liste_mot_maj(texte):
    liste_texte = texte.split()
    liste_maj = []

    for mot in liste_texte:
        if mot[0].isupper():
            liste_maj.append(mot)
    print("La liste des mots débutant par une majuscule sont : ", liste_maj)


message = input("Entrez votre message : ")
liste_mot_maj(message)

def commom_word_two_files(nom_fichier1, nom_fichier2):
    file1 = open(nom_fichier1, "r")
    file2 = open(nom_fichier2, "r")
    content1 = file1.read()
    content2 = file2.read()
    list_content1 = content1.split()
    list_content2 = content2.split()
    file1.close()
    file2.close()

    mots_communs_liste = []

    for mot in list_content1:
        if mot in list_content2 and mot not in mots_communs_liste:
            mots_communs_liste.append(mot)
    print("La liste des mots communs aux deux fichiers sont :", mots_communs_liste)

fichier1 = input("Nom du premier fichier : ")
fichier2 = input("Nom du second fichier : ")
commom_word_two_files(fichier1, fichier2)
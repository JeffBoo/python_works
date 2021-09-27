
def inserer_ligne_fichier(nom_fichier, message, no_ligne):
    file = open(nom_fichier, "r")
    liste_lignes = file.readlines()
    file.close()
    contenu_ligne_ajoutee = message + "\n"
    liste_lignes.insert(no_ligne-1, contenu_ligne_ajoutee)
    file = open(nom_fichier, "w")
    file.writelines(liste_lignes)
    file.close()

fichier = input("Nom du fichier à modifier : ")
texte = input("Texte de la ligne ajoutée : ")
num_ligne = int(input("Numéro de la ligne ajoutée : "))
inserer_ligne_fichier(fichier, texte, num_ligne)
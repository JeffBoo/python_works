
def modif_ligne_fichier(nom_fichier, message, ligne_modifiée):
    file = open(nom_fichier, "r")
    ligne = file.readlines()
    file.close()
    ligne[ligne_modifiée] = message + "\n"
    file = open(nom_fichier, "w")
    file.writelines(ligne)
    file.close()

fichier = input("Quel fichier voulez-vous modifier : ")
texte = input("Quel texte voulez-vous écrire : ")
no_ligne = int(input("Ligne où se trouve la modification : "))
modif_ligne_fichier(fichier, texte, no_ligne)

def invert_lines(nom_fichier, first_line, second_line):
    file = open(nom_fichier, "r")
    liste_lignes = file.readlines()
    file.close()
    ligne_a_remplir = ""
    ligne_a_remplir = liste_lignes[first_line-1]
    liste_lignes[first_line-1] = liste_lignes[second_line-1]
    liste_lignes[second_line-1] = ligne_a_remplir
    file = open(nom_fichier, "w")
    file.writelines(liste_lignes)
    file.close()

fichier = input("Nom du fichier à modifier : ")
line_un = int(input("Première ligne à intervertir : "))
line_deux = int(input("Deuxième ligne à intervertir : "))
invert_lines(fichier, line_un, line_deux)
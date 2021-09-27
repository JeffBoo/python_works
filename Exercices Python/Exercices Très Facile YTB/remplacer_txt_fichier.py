
def remplacement_texte_fichier(fichier, texte):
    file = open(fichier, "r")
    content = file.read()
    content_modified = texte + content[24:]
    file.close()
    file = open(fichier, "w")
    file.write(content_modified)
    file.close()

nom_fichier = input("Quel fichier voulez-vous modifier : ")
message = input("Quel texte voulez-vous mettre : ")
remplacement_texte_fichier(nom_fichier, message)

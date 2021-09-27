
def supp_mot_fichier(nom_fichier, num_mot):
    file = open(nom_fichier, "r")
    content = file.read()
    list_content = content.split()
    list_content.pop(num_mot-1)
    new_content = ""
    new_content = " ".join(list_content)
    file.close()
    file = open(nom_fichier, "w")
    file.write(new_content)
    file.close()

fichier = input("Quel fichier voulez-vous modifier : ")
numero_mot = int(input("Quelle est la place de ce mot : "))
supp_mot_fichier(fichier, numero_mot)
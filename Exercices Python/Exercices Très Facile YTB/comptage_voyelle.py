
def compte_voyelles(texte):
    compteur = 0
    voyelle_list = "aeiouy"
    for char in texte:
        if char in voyelle_list:
            compteur += 1
    return compteur

mot = input("Entrez un mot : ")
print("Il y a", compte_voyelles(mot), " voyelle(s) dans ce mot")

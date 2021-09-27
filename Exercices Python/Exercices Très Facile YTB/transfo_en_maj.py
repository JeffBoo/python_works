
def dev_maju(liste):
    list = liste.split()
    liste_maju = []
    for char in list:
        char_maj = char.upper()
        liste_maju.append(char_maj)
    return liste_maju

liste_mot = input("Entrez une liste de mots : ")
print("La liste des mots en majuscules est : ", dev_maju(liste_mot))
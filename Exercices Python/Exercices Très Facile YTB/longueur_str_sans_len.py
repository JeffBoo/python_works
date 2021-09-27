
def string_length(texte):
    longeur_mot = 0
    for char in texte:
        longeur_mot += 1
    return longeur_mot

mot = input("Entrez une chaine de caractère : ")
string_length(mot)
print("La longueur de la chaine de caractère est de : ", string_length(mot))
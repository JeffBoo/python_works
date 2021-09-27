
def position_a(texte):
    longueur_texte = len(texte)
    for i in range(longueur_texte):
        if texte[i] == "a":
            print("le caractère 'a' se trouve à la position : ", i+1)

mot = input("Entrez votre texte : ")
position_a(mot)

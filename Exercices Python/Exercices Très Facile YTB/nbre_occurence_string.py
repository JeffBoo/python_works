
def nbre_occu_dans_str(texte):
    longueur_txt = len(texte)
    apparition = ""
    for char in range(longueur_txt):
        if texte[char] not in apparition:
            print("Le caractère", texte[char], "apparaît", texte.count(texte[char]), "fois")
            apparition += texte[char]

mot = input("Entrez un texte : ")
nbre_occu_dans_str(mot)
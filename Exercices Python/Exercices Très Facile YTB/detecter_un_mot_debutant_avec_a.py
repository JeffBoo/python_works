
texte = input("Entrez votre texte : ")
list_texte = texte.split()
a_liste = []
for mot in list_texte:
    if mot[0] == "a":
        print(mot, "commence par le caractère 'a'")
        a_liste.append(mot)
print("La liste des mots commençant par le caractère 'a' dans le texte sont : ", a_liste)
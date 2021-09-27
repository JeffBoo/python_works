
def triangle_nb (n_lignes, n):
    hauteur = n_lignes
    espace_vide = hauteur - 1
    nb_etoile = n
    for n in range(1,hauteur+1):
        print(espace_vide*" " + nb_etoile*str(n))
        nb_etoile += 2
        espace_vide -= 1

lignes = int(input("Combien de lignes possède votre triangle ? "))
nb_init = int(input("Combien de chiffres au sommet de votre triangle ? "))

triangle_nb(lignes, nb_init)
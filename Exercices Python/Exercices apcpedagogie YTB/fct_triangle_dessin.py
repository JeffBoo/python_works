
def triangle(n_lignes, n):
    hauteur = n_lignes
    espace_vide = hauteur - 1
    nb_etoile = n
    for n in range(hauteur):
        print(espace_vide*" " + nb_etoile*"*")
        nb_etoile += 2
        espace_vide -= 1

lignes = int(input("Combien de lignes possède votre triangle ? "))
star_init = int(input("Combien d'étoiles au sommet de votre triangle ? "))

triangle(lignes, star_init)

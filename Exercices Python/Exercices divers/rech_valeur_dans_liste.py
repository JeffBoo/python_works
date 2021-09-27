def position(valeur, liste):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i
    return -1

# un appel de la fonction, pour la tester:
uneValeur = int(input("Entrez une valeur: "))
uneListe = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

p = position(uneValeur, uneListe)
if p >= 0:
    print("la valeur est a la position", p)
else:
    print("la valeur n’est pas presente")

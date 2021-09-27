
def som_chiffres(nombre):
    somme_pair = 0
    somme_impair = 0
    if nombre % 2 == 0:
        for num in range(0, nombre+1, 2):
            somme_pair += num
        print("La somme des nombres pairs jusqu'à", nombre, "est : ", somme_pair)
    else:
        for num in range(1, nombre+1, 2):
            somme_impair += num
        print("La somme des nombres impairs jusqu'à", nombre, "est : ", somme_impair)

numero = int(input("Entrez un nombre entier : "))
som_chiffres(numero)


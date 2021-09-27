
print("Entrez des valeurs. Appuyez sur entrée une fois terminé.")

liste_valeurs = []

while True:
    valeur = input("Saisir une valeur : ")
    if valeur:
        try:
            liste_valeurs.append(int(valeur))
        except ValueError:
            continue
    else:
        break

print("Valeurs entrées : ", liste_valeurs)

for i in range(len(liste_valeurs)):
    print("L'index", i, "contient la valeur", liste_valeurs[i])

somme = 0
for i in range(len(liste_valeurs)):
    somme += liste_valeurs[i]

print("La somme des valeurs vaut", somme)

liste_multiple = []
for x in liste_valeurs:
    liste_multiple.append(x*3)

print("Liste des multiples", liste_multiple)

max = 0
for a in liste_valeurs:
    if a > max:
        max = a
print("La valeur max est : ", max)

min = max
for a in liste_valeurs:
    if a < min:
        min = a
print("La valeur min est : ", min)

liste_pair = []

for x in liste_valeurs:
    if x%2 == 0:
        liste_pair.append(x)
print("La liste des nombres pairs est : ", liste_pair)

somme_impair = 0
for x in liste_valeurs:
    if x%2 != 0:
        somme_impair += x
print("La somme des nombres impairs est : ", somme_impair)
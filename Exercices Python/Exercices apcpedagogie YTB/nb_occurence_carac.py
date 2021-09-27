
chaine_cara = input("Entrez une chaine de caractère : ")

ensemble_unique = set({})

for cara in chaine_cara:
    if cara not in ensemble_unique:
        ensemble_unique.add(cara)
        print("Le nombre d'occurence(s) de :", cara, "est", chaine_cara.count(cara))
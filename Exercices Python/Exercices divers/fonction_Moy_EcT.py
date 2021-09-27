from math import sqrt

def moyenneEcartType(listeVal):
    nombre = 0
    sommeValeurs = 0.0
    sommeCarres = 0.0
    for x in listeVal:
        nombre += 1
        sommeValeurs += x
        sommeCarres += x * x
    moyenne = sommeValeurs / nombre
    ecartt = sqrt(sommeCarres / nombre - moyenne * moyenne)
    return (moyenne, ecartt)

# un appel de la fonction, pour la tester:
valeurs = [2, 2, 2, 8, 8, 8]
resultat = moyenneEcartType(valeurs)
print(resultat)

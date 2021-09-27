
liste_donnee = input("Insérer une liste : ")
diviseur = int(input("Donner un diviseur : "))

def nombre_div(liste, nombre):
    liste = liste.split()
    multiple = 0
    for num in liste:
        if int(num) % nombre == 0:
            multiple += 1
    return multiple

print("Le nombre de multiples de", diviseur, "dans la liste est", nombre_div(liste_donnee, diviseur))


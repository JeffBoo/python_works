from random import randint

juste_prix = randint(1,1000)
print(juste_prix)
choix = int(input("Quel est le juste prix ? : "))
while choix != juste_prix:
    if choix < juste_prix:
        print("C'est plus !")
        choix = int(input("Quel est le juste prix ? : "))
    else:
        print("C'est moins !")
        choix = int(input("Quel est le juste prix ? : "))
print("Vous avez trouvé le juste prix !")
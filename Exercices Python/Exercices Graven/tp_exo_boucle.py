from random import randint

# Jeu du Juste Prix

nb_tentatives = 0

nb_secret = randint(1,4)


while nb_tentatives < 5:

    nb_tente = int(input("Choisir un nombre entre 1 et 4 : "))
    if nb_tentatives < 5:
        nb_tentatives += 1
        if nb_tente is not nb_secret:
            print("Mauvaise réponse !!")
            if nb_secret < nb_tente:
                print("c'est plus petit !!")
            elif nb_secret > nb_tente:
                print("c'est plus grand !!")
        elif nb_tente == nb_secret:
            print("Bonne reponse !! Tu as gagné")
            break

if nb_tentatives >= 5:
    print("Perdu !! Nombre max de tentatives dépassé !!")

print("Nombre de tentatives {}, partie terminée".format(nb_tentatives))


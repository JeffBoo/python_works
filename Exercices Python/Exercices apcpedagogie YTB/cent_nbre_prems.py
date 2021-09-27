
print("Les 100 premiers nombrees premiers : ")
compteur_nbre_prems = 1
nbre = 2
somme = 0
while(compteur_nbre_prems <= 100):
    nbre_test = 2
    nbre_trouve = 1
    while(nbre_test <= nbre//2 and nbre_trouve == 1):
        if nbre % nbre_test == 0:
            nbre_trouve = 0
        else:
            nbre_test += 1
    if nbre_trouve == 1:
        print(compteur_nbre_prems, nbre)
        compteur_nbre_prems += 1
        somme += nbre
    nbre += 1
print("La somme des 100 premiers nombres premiers est :", somme)
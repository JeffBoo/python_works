"""Somme des 100 premiers nombres premiers via le critère sqrt"""
from math import*
compteur_nb_prems = 1
nbre_test = 2
somme = 0

while(compteur_nb_prems < 101):
    nbre = 2
    nbre_trouve = 0
    while(nbre < int(sqrt(nbre_test)) + 1 and nbre_trouve == 0):
        if(nbre_test % nbre == 0):
            nbre_trouve = 1
        else:
            nbre += 1
    if(nbre_trouve == 0):
        print(compteur_nb_prems, nbre_test)
        somme = int(somme) + nbre_test
        compteur_nb_prems += 1
    nbre_test += 1
print("La somme des 100 premiers nombres premiers est :", somme)



texte = """Maitre Corbeau, sur un arbre perche
Tenait en son bec un fromage
Maitre Renard, par l’odeur alleche
lui tint a peu pres ce langage"""

from array import array

compteurs = array("i")
compteurs.extend( [ 0 ] * 256 )

for c in texte:
    compteurs[ord(c)] = compteurs[ord(c)] + 1
for i in range(256):
    if compteurs[i] != 0:
        print(chr(i), ":", compteurs[i], "occurrence(s)")
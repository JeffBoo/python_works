texte = """Maitre Corbeau, sur un arbre perche
Tenait en son bec un fromage
Maitre Renard, par l’odeur alleche
lui tint a peu pres ce langage"""
dico = { }
for car in texte:
    if dico.has_key(car):
        dico[car] = dico[car] + 1
    else:
        dico[car] = 1
for car in dico.keys():
    print(car, ":", dico[car], "occurrence(s)")

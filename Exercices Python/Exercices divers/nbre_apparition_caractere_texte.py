texte = """Maitre Corbeau, sur un arbre perche
Tenait en son bec un fromage
Maitre Renard, par l’odeur alleche
lui tint a peu pres ce langage"""
auMoinsUneFois = set()
auMoinsDeuxFois = set()
for caract in texte:
    if caract in auMoinsUneFois:
        auMoinsDeuxFois.add(caract)
    else:
        auMoinsUneFois.add(caract)
print(auMoinsUneFois.difference(auMoinsDeuxFois))
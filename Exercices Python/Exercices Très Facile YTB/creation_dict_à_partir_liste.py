
cles = ["rapide", "lent", "bolide"]
valeurs = ["cheval", "escargot", "Flash"]

dico = dict(zip(cles, valeurs))
print("première version du dico", dico)

dicto = dict({})
for i in range(len(cles)):
    dicto[cles[i]] = valeurs[i]

print("deuxième version du dico", dicto)
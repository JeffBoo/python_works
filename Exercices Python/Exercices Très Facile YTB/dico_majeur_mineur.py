
dico = {"Albert" : 12, "Nicolas" : 19, "Marie" : 14, "Clément" : 21, "Gareth" : 23}

majeur = dict({})
mineur = dict({})

for key, value in dico.items():
    if value < 18:
        mineur[key] = value
    else:
        majeur[key] = value

print("Les personnes majeures sont : ", majeur)
print("Les personnes mineures sont : ", mineur)

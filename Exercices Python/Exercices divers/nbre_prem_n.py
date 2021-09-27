borne = int(input("Choisir la borne : "))
premiers = []
for candidat in range(3, borne + 1, 2):
    EstPremier = True
    for premier in premiers:
        if candidat % premier == 0:
            EstPremier = False
            break
    if EstPremier:
        premiers.append(candidat)
print("Les nombres premiers inferieurs ou egal à ", borne, "sont :", premiers)

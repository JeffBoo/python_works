
nombre_donne = int(input("Saisissez un nombre : "))

for i in range(2, nombre_donne + 1):
    nombre_trouve = 0
    for j in range(2, i):
        if i%j == 0:
            nombre_trouve = 1
    if nombre_trouve == 0:
        print(i)
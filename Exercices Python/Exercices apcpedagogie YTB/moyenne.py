
tab = []

note, nb_note, somme_note, moyenne = 0, 0, 0, 0

while note >= 0 and note <= 20:
    note = float(input("Saississez un nombre " + str(int(nb_note+1)) + " : "))
    if note >=0 and note <= 20:
        nb_note += 1
        somme_note += note
        tab.append(note)
print("Nombre de notes saisies : ", nb_note)
for j in tab:
    print("%0.2f" % j, end = " ") # Affichage de chaque valeur du tableau

print()
moyenne = (somme_note/nb_note)
print("La moyenne est de : ", "%0.2f" % moyenne)
if moyenne < 10:
    print("Non admis ! ")
elif moyenne >= 10 and moyenne <= 12:
    print("Passable")
elif moyenne > 12 and moyenne < 14:
    print("Mention Bien")
elif moyenne >= 14:
    print("Mention Très Bien")
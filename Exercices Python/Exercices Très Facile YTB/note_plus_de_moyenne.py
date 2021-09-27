
def liste_au_dessus_moyenne(liste_notes):
    liste_moyenne_plus = []
    notes = liste_notes.split()
    for note in notes:
        if int(note) >= 10:
            liste_moyenne_plus.append(int(note))
    print("Les notes au-dessus de la moyenne sont : ", liste_moyenne_plus)

liste = input("Entrez les notes : ")
liste_au_dessus_moyenne(liste)

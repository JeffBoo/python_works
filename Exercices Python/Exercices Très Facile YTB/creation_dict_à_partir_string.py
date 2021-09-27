
def creation_dico_string(chaine_cara):
    liste_mots = chaine_cara.split()
    dico = dict({})

    for mot in liste_mots:
        dico[mot] = len(mot)
    return dico

ch_cara = input("Insérer une chaine de caractères : ")
print("Le dico issu de la chaine de caractères est : ", creation_dico_string(ch_cara))
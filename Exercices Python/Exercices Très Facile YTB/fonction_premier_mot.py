
def prems_mot(message):
    longueur = 0
    premier_mot = ""
    while message[longueur] != " ":
        premier_mot += message[longueur]
        longueur += 1
    print("Le premier mot est :", premier_mot, "et il fait", longueur, "lettres")

phrase = input("Ecrire une phrase : ")
prems_mot(phrase)
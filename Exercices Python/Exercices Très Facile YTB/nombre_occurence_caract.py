
def occurence_number(sentence, letter):
    compteur = 0
    for x in sentence:
        if x == letter:
            compteur += 1
    print("Le  nombre de", letter, "dans", sentence, "est :", compteur)

phrase = input("Insérez une phrase : ")
lettre = input("Quelle letttre voulez-vous compter ? ")
occurence_number(phrase, lettre)
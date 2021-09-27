
def invert_cara(phrase):
    longueur_phrase = len(phrase)
    print("La phrase contient", longueur_phrase, "caractères")
    prem_car = phrase[0]
    dern_car = phrase[longueur_phrase - 1]
    phrase_interm = phrase[1:longueur_phrase - 1]
    phrase_finale = dern_car + phrase_interm + prem_car
    print("La nouvelle phrase est :", phrase_finale)

sentence = input("Saisir une phrase : ")
invert_cara(sentence)




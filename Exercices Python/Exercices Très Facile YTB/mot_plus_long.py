
def longest_word(sentence):
    long_mot = ""
    list_mots = sentence.split()
    for mot in list_mots:
        if len(mot) > len(long_mot):
            long_mot = mot
    print("Le mot le plus long de la phrase est :", long_mot)


phrase = input("Insérez une phrase : ")
longest_word(phrase)

def select_mot(message, longueur):
    Liste_mot_long = []
    List_message = message.split()

    for word in List_message:
        if len(word) >= longueur:
            Liste_mot_long.append(word)
    return Liste_mot_long


phrase = input("Insérer une phrase : ")
nombre = int(input("Insérer un chiffre : "))
print("Voici les mots de plus de ", nombre, "sont : ", select_mot(phrase, nombre))
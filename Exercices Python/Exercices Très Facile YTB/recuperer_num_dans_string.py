
def collect_num(texte):
    list_num = []
    for x in texte:
        if x.isnumeric():
            x = int(x)
            list_num.append(x)
    print("La liste des numeros issue du texte est : ", list_num)

mot = input("Insérez votre chaine de caractères : ")
collect_num(mot)
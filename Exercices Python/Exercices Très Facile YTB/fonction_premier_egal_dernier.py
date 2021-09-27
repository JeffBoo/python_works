
def first_is_last(texte):
    if texte[0] == texte[-1]:
        return True
    else:
        return False

mot = input("Entrez un mot : ")
print(first_is_last(mot))

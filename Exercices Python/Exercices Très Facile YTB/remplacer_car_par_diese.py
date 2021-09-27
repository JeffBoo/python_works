
def remplace_diese(texte):
    chain_diese = ""
    n = len(texte)
    for i in range(n):
        if i % 2 == 0:
            chain_diese += texte[i]
        else:
            chain_diese += "#"
    return chain_diese

mot = input("Insérez la chaine à trafiquer : ")
print("Après trafic, le mot : ", mot, "devient :", remplace_diese(mot))
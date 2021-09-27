
def maxx(x, y):
    if x < y:
        return y
    else:
        return x

n = int(input("Donnez un chiffre n : "))
m = int(input("Donnez un chiffre m : "))
maxx(n, m)
print(maxx(n, m), "est le plus grand nombre")


# TP : compteur de voyelles :

def nb_voyelles(mot):
    count = 0

    for letter in mot:
        if letter in ["a", "e", "i", "o", "u", "y"]:
            count += 1

    return count

word = input("Donner un mot : ")
print(word, "contient", nb_voyelles(word), "voyelles")
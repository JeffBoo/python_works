
vowels = ["a", "e", "i", "o", "u", "y"]

def get_vowels_numbers(mot):
    vowels_count = 0
    text = [char for char in mot]
    for char in text:
        if char in vowels:
            vowels_count += 1
    if vowels_count == 0:
        print("Il n'y a pas de voyelle dans le mot")
    return vowels_count

entrée = input("Ecrire un mot : ")
print("Nombre de voyelle(s) trouvée(s) :", get_vowels_numbers(entrée))


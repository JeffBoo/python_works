
mot = input("Entrez un mot : ")
envers = mot[::-1]

if mot == envers:
    print(mot, "est un palindrome")
else:
    print(mot, "n'est pas un palindrome")
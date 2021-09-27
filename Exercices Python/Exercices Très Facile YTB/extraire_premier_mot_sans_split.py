
text = input("Entrez du texte : ")
i=0
premier_mot = " "
while text[i] != " ":
    premier_mot += text[i]
    i += 1
print("Le premier mot du texte est :", premier_mot)
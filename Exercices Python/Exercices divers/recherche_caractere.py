s = input("s : ")
for i in range(len(s)):
    if s[i] == "c":
        print("La lettre 'c' se trouve à la position: ", i+1)
        break;
else:
    i = -1
    print("Il n'y a pas de 'c' dans le mot")




n = int(input("Entrez un nombre n : "))
liste_div = []

for num in range(1,n+1):
    if n % num == 0:
        liste_div.append(num)
print("La liste des diviseurs de", n, "sont", liste_div)
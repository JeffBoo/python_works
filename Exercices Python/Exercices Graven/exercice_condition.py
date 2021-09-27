age = int(input("Quel age avez-vous ? : "))
somme_a_payer = 0
prix_mineur = 7
prix_majeur = 12
prix_popcorn = 5

if age <= 18:
    somme_a_payer += prix_mineur
else:
    somme_a_payer += prix_majeur
popcorn = input("Souhaitez-vous du popcorn ? : ")
if popcorn == "oui":
    somme_a_payer += prix_popcorn
    print("Voilà l'addition :", somme_a_payer)
else:
    print("Vous devez payer :", somme_a_payer)

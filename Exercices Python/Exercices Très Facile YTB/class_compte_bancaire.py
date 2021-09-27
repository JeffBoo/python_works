
class Compte_bancaire:
    def __init__(self, nom_prenom, no_compte, solde):
        self.nom_prenom = nom_prenom
        self.no_compte = no_compte
        self.solde = solde

    def Versement(self, somme_à_verser):
        self.solde += somme_à_verser

    def Retrait(self, somme_à_retirer):
        if somme_à_retirer > self.solde:
            print("Solde Insuffisant !", self.solde, "sur le compte !")
        else:
            self.solde -= somme_à_retirer

    def Agios(self, pourcentage):
        self.solde -= (pourcentage/100)*self.solde

    def Afficher(self):
        print("Le compte appartient à : ", self.nom_prenom)
        print("Le numéro de compte est : ", self.no_compte)
        print("Solde du compte sauf erreur ou omission : ", self.solde)


new_conto = Compte_bancaire("Jarbour", 123456, 2800)
new_conto.Afficher()

new_conto.Versement(300)
print("Nouveau solde du compte sauf erreur ou omission : ", new_conto.solde)

new_conto.Retrait(5000)
print("Nouveau solde du compte sauf erreur ou omission : ", new_conto.solde)

new_conto.Retrait(500)
print("Nouveau solde du compte sauf erreur ou omission : ", new_conto.solde)

new_conto.Agios(5)
print("Nouveau solde du compte sauf erreur ou omission : ", new_conto.solde)

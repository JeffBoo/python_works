
#1)
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

#2)
    def Perimetre(self):
        return 2*(self.largeur + self.longueur)

    def Surface(self):
        return self.longueur*self.largeur

#3)
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def Volume(self):
        return self.longueur*self.largeur*self.hauteur

mon_rectangle = Rectangle(3,2)
print("La largeur du rectangle est : ", mon_rectangle.largeur)
print("La longueur du rectangle est : ", mon_rectangle.longueur)
print("La surface du rectangle est : ", mon_rectangle.Surface())
print("Le périmètre du rectangle est : ", mon_rectangle.Perimetre())

mon_parallelepipede = Parallelepipede(8, 7, 6)
print("Le volume du parallélépipède  est : ", mon_parallelepipede.Volume())
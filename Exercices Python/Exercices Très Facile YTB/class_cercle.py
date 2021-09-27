from math import pi

class Cercle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def Perimetre(self):
        return 2*pi*self.r

    def Surface(self):
        return pi*self.r**2

    def Appartenance_cercle(self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 == self.r

mon_cercle = Cercle(0, 0, 5)

print("Le rayon du cercle vaut : ", mon_cercle.r)
print("Le périmètre du cercle vaut : ", mon_cercle.Perimetre())
print("La surface du cercle vaut : ", mon_cercle.Surface())
print("Le point appartient au cercle ? ", mon_cercle.Appartenance_cercle(1, 2))
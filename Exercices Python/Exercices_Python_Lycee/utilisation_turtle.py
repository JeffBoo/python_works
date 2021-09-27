from turtle import *


def polygone(nbre_cote, demi_longueur, angle, epaisseur_trait, couleur1, couleur2):
    pas = 0
    while pas < nbre_cote:
        color(couleur1)
        width(epaisseur_trait)
        forward(demi_longueur) # On avance
        left(angle) # 90 degrés à gauche
        color(couleur2)
        width(epaisseur_trait) # Epaisseur du trait
        forward(demi_longueur)
        pas += 1
    exitonclick()
    return


def lettre_p():
    width(5)
    left(90)
    forward(30)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    up()
    return

def lettre_y():
    down()
    width(5)
    right(90)
    forward(20)
    left(30)
    forward(10)
    backward(10)
    right(60)
    forward(10)
    return

lettre_p()
goto(40, 0)
lettre_y()
polygone(6, 30, 60, 3, "blue", "green")


from random import*

class Domino ():
    def __init__(self, pointsA, pointsB):
        self.pointsA = pointsA
        self.pointsB = pointsB

    def affiche_points (self):
     print ("Face A :",self.pointsA," Face B :",self.pointsB)
    def valeur (self):
        return (self.pointsA + self.pointsB)


def cree_pioche():
    pioche = []
    for i in range(7):
        a= randint(1,6)
        b = randint(1,6)
        domino= Domino(a,b)
        pioche.append(domino)
    return pioche




liste_pioche= cree_pioche()
for domino in liste_pioche:
    domino.affiche_point()


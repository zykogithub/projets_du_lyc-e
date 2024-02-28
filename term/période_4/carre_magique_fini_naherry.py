from math import sqrt

class Carre:
    def __init__(self, nombres):
        self.ordre = int(sqrt(len(nombres)))
        self.tableau = [[nombres[j + i*self.ordre] for j in range(self.ordre)] for i in range(self.ordre)]

    def affiche(self):
        '''Affiche un carré'''
        for ligne in self.tableau:
            print(ligne)

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        sume=sum(self.tableau[i])
        print(sume)
        return sume

    def somme_colonne(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        liste=[]
        for elt in self.tableau:
            liste.append(elt[j])
        sume=sum(liste)
        return sume

    def est_semi_magique(self):
        somme_commune = self.somme_ligne(0)
        for i in range(1,self.ordre):
            if somme_commune!=self.somme_ligne(i):
                return False
        for i in range(1,self.ordre):
            if somme_commune!=self.somme_colonne(i):
                return False
        return True
         
# Tests

nombres_2 = (1, 7, 7, 1)
nombres_3 = (3, 4, 5, 4, 4, 4, 5, 4, 3)
nombres_3_bis = (2, 9, 4, 7, 0, 3, 6, 1, 8)
nombres_4 = (1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34)
carre_2 = Carre(nombres_2)
carre_3 = Carre(nombres_3)
carre_3_bis = Carre(nombres_3_bis)
carre_4 = Carre(nombres_4)

print("Carré 4")
carre_4.affiche()

assert carre_3.somme_ligne(0) == 12
assert carre_3_bis.somme_colonne(1) == 10
assert carre_2.est_semi_magique() is True
assert carre_3.est_semi_magique() is True
assert carre_3_bis.est_semi_magique() is False
assert carre_4.est_semi_magique() is False


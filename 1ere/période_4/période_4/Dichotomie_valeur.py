# Créé par souve, le 14/04/2022 en Python 3.7
from random import*


def milieu(i, j):
    return (i+j)//2


def dichotomie(valeur, tab):


    gauche, droite = 0, len(tab)-1

    while gauche <= droite:
        centre = milieu(gauche, droite)
        if tab[centre] == valeur: return True
        if tab[centre] < valeur:
            gauche, droite = centre+1, droite
        else:
            gauche, droite = gauche, centre-1


    return False


def point_fixe(tab):
   print(dichotomie(8,ie))
   for i in range(len(tab)):
        if tab[i] == i:
            return i
   return None
ie=[0,18,2,3,19]
ie.sort


print(point_fixe(ie))
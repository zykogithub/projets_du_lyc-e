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


# TESTS
from random import randint
L = [randint(-10, 10) for i in range(12, 29)]
L.sort()
print( dichotomie(8, L) )
# vérif avec in:
print( 8 in L )

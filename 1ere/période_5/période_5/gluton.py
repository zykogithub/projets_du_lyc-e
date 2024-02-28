# Créé par n.mohamed, le 12/04/2022 en Python 3.7

# Rendu de monnaie d'Alice
#  coding: utf-8

'''



def somme(liste):
    """ Fonction qui retourne la somme de tous les éléments de la liste"""
    resultat=0
    for element in liste:
        resultat=element+resultat
    return resultat

def monnaieAlice(rendre):
    """Fonction qui donne les différentes façons de donner rendre euros
       avec un nombre minimum de pièces de 3 valeurs différentes,
       4, 3 et 1"""

    minimum = rendre
    # minimum représente le nombre minimum de pieces à rendre
    listePieces = [] # liste des solutions possibles (optimales ou non)

    for i in range(rendre+1): # i est le nombre de pièces de 4 utilisées
        for j in range(rendre+1): # j est le nombre de pièces de 3 utilisées
            for k in range(rendre+1): # k est le nombre de pièces de 1 utilisées
                nombrePieces = i+j+k
                if i*4 + j*3 + k*1 ==    rendre  and nombrePieces <=  minimum :
                    minimum =nombrePieces
                    listePieces.append([i,j,k])

    solution = [] # liste des solutions optimales

    for possibilite in listePieces:
        if somme(possibilite)==minimum :
            solution.append(possibilite)

    return [solution,minimum]


#Programme principal
rendre=int(input("somme à rendre:"))
reponse=monnaieAlice(rendre)[0]
mini=monnaieAlice(rendre)[1]
print("On peut rendre ",rendre," avec",mini," pieces" )
for element in reponse:
    print( element[0],"pieces de 4, et ", element[1]    ,"pieces de 3, et ",  element[2]     ,"pieces de 1")

bob
def monnaieBob(somme):
    pieces=[4,3,1]
    arendre=somme
    liste=[]
    for piece in pieces:
        while arendre>=0 :
            arendre=arendre-piece
            liste.append(piece)
    return liste


#Programme principal


somme=int(input("somme à rendre: "))
print(monnaieBob(somme))
'''
# Comparaison du temps d'execution des algorithmes
# méthode brute et algorithme glouton
import time

def monnaie_brute(rendre):
    """Fonction qui donne les différentes façons de donner rendre euros
       avec un nombre minimum de pièces de 3 valeurs différentes,
       4, 3 et 1"""

    minimum = rendre
    # minimum représente le nombre minimum de pieces à rendre
    # Une des pieces vaut 1, on peut donc initialiser le nombre minimum
    # de pièces à rendre à sa plus grande valeur possible, c'est-à-dire somme

    listePieces = [] # liste des solutions possibles (optimales ou non)

    for i in range(rendre+1): # i est le nombre de pièces de 4 utilisées
        for j in range(rendre+1): # j est le nombre de pièces de 3 utilisées
            for k in range(rendre+1): # k est le nombre de pièces de 1 utilisées
                nombrePieces = i + j + k
                if i*4 + j*3 + k*1 == rendre and nombrePieces <= minimum:
                    minimum = nombrePieces
                    listePieces.append([i,j,k])

    solution = [] # liste des solutions optimales

    for possibilite in listePieces:
        if sum(possibilite)==minimum:
            solution.append(possibilite)

    return [solution,minimum]


def monnaieGlouton(somme):
    pieces=[4,3,1]
    arendre=somme
    liste=[]
    for piece in pieces:
        while arendre>=piece:
            liste.append(piece)
            arendre=arendre-piece
    return liste

#Programme principal

arendre=int(input("somme à rendre: "))
t0=time.time() # début du chrono
for i in range(10000):
    monnaie_brute(arendre)
t1=time.time() #
for i in range(10000):
    monnaieGlouton(arendre)
t2=time.time()


tempsBrut=t1-t0
tempsGlouton=t2-t1
print("temps par l algorithme brut : ",tempsBrut)
print("temps par l algorithme glouton : ",tempsGlouton)
print("temps brut/temps glouton",tempsBrut/tempsGlouton)

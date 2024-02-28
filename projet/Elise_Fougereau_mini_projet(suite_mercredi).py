# Créé par emoumdjian, le 17/10/2021 avec EduPython
from lycee import *
from random import *


#La fonction suivante simule le comportement d'un dé à 6 faces.
#Pour cela, on utilise la fonction randint() du module random.
def lancer_De():
    """ Création d'une liste de 10 lancers de dés """
    resultat = [randint(1, 6) for i in range(10)]
    return lancer_De


def points(liste):
    """ retourne le nombre de points de la liste """
    global nombre
    nombre = liste.count(6)

def regle(ptns) :
    ptns=0
    if nombre>=2:
        ptns=ptns+1
    else :
        ptns=ptns+0
    return ptns

######################
#si une de cesassertions est fausse, l'exécution du programme s'arrête
#et le message d'erreur (AssertionError) specifie s'affiche

# Programme principal
#####################

points_Alice=0 #Initialisation du nombre de points d'Alice
points_Bob=0  #Initialisation du nombre de points de Bob
alice=[]
bob=[]

# Simulation du jeu tant qu'Alice ou Bob n'ont pas dix points
while points_Alice<1 and points_Bob<1:
    lancer_De()
    points(alice)
    regle(points_Alice)
    lancer_De()
    points(bob)
    regle(points_Bob)
# Determination du gagnant



if points_Alice==1 and points_Bob!=10 :
    print("Alice a gagné !")
elif (points_Bob==10 and points_Alice!=10):
    print("Bob a gagné !")
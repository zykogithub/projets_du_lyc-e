# Créé par n.mohamed, le 07/04/2022 en Python 3.7

from math import*
import matplotlib.pyplot as plt

liste_x_1=[1,3,8,13]
liste_y_1=[28,27.2,37.6,40.7]

liste_x_2=[2,3,10,15]
liste_y_2=[30,26,39,35.5]

plt.axis([0,15,0,50])
plt.axis("equal")
plt.xlabel("caractéristique 1")
plt.ylabel("caractéristique 2")
plt.title("representation des deux types")
plt.grid()
plt.scatter(liste_x_1,liste_y_1, label="type 1")
plt.scatter(liste_x_2,liste_y_2, label="type 2")

plt.scatter(7,28.4, label='cible')
plt.legend()
plt.show()

table=[['t1',1,28],['t1',3,27.2],['t1',8,37.6],['t1',13,40.7],['t2',2,30],['t2',3,26],["t2",10,39],["t2",15,35.5]]
cibel=[7,28.4]
k=30

def k_plus_proche_voisin(table,cible,k):
    def distance_cible(donnee):
        distance=abs(donnee[1]-cible[0])+abs(donnee[2]-cible[1])
        print(distance)
        return distance
    table_tri=sorted(table,key=distance_cible)
    proche_voisin=[table_tri[i] for i in range(k)]
    return proche_voisin

print("la liste des",k,"plus proches voisins de la cible : ",k_plus_proche_voisin(table,cibel,k))



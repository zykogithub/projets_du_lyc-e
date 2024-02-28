##exercice 1
"""
from random import*

chiffre=[i for i in range(1,50)]
choix=[]
for k in range(6):
    choice=chiffre.pop(randint(1,49-k))
    choix.append(choice)
complementaire=chiffre.pop(randint(1,43))

print(choix)
print(complementaire)


##exercice 2

liste = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
maj=[]
for j in range(len(liste)):
    if liste[j]==liste[j+1]:
        del(liste[j+1])
        print(liste)
"""
##corection


liste = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
maj=[]
for nombre in maj:
    if nombre not in maj:
        maj.append(nombre)
    print(maj)
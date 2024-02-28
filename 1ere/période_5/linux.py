# Créé par souve, le 27/04/2022 en Python 3.7

from random import*

activite=["courir","basket","renforcement","kata"]
jour=[]
for i in range(3):
    a=randint(0,3)
    if i==a:
        print(i,a)
        jour.append(activite[i])
        activite.pop(activite[i])




print(activite[0])
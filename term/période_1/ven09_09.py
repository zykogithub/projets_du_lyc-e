# Créé par n.mohamed, le 12/09/2022 en Python 3.7
from random import*
'''
##exercice 1
def max(liste):
    k=0
    for i in liste:
        if i>k:
            k=i
    return liste.index(k),k

listeee=[randint(1,10) for i in range(5)]

print(listeee)
print(max(listeee))

##exercice 2

def multiple_3(liste):
    compteur=0
    for element in liste:
        if element%3==0:
            compteur+=1
            print(compteur)
    return compteur

listeee=[randint(1,10) for i in range(5)]
print(listeee,multiple_3(listeee))


def somme(liste):
    k=0
    for i in liste:
        k=k+i
    return k

def moy_pair(liste):
    pair=[]
    for i in liste:
        if i%2==0:
            pair.append(i)
    for k in pair:
        tu=somme(pair)/len(pair)
    return tu

listeee=[randint(1,10) for i in range(5)]
print(listeee,moy_pair(listeee))


chaine = "abcdefabcdef"


print(chaine[0],
chaine[2:4],
chaine[:3],
chaine[2:],
chaine[-1])

def reverse_str(chaine: str) -> str:
    """
    :params chaine:str:la chaine de départ
    :returns:str:la chaine écrite en ordre inversée
    la fonction crée un nouvelle chaine et renvoi le résultat
    """

    new_chaine = ""
    for caractere in chaine :
        new_chaine = caractere + new_chaine
    return new_chaine


reverse_str("truc")

'''


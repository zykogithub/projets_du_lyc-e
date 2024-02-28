# Créé par n.mohamed, le 20/01/2022 en Python 3.7
from turtle import*
from math import*

def polygone(x,y): #fonction pour tracer la figuer qui formera le polygone
    for i in range(x):
        forward(y)
        left(360/x)




def main():
    dico={"carre" : 4, "triangle" : 3, "pentagone" : 5, "hexagone" : 6, "heptagone" : 7, "octogone" : 8, "nonagone" : 9, "decagone" : 10} #dictionnaire contenat un ensemble de figure qui ont entre 3 et 10 côtés. La figure et le nombre de côté étant le couple clef valeur.
    element= input("Quel forme voulez-vous ? ") #rentrer le figure qu'aura la rosace

    if element not in   dico.keys():
        assert element=='Saisir un Carre , un Triangle, un Pentagone, un Heptagone, un Octogone, un Nonagone ou un Decagone'

    else:

        cote=int(input("pixel ")) #taille du crayon
        b=dico.get(element)

        for i in range(12):
            polygone(b,cote)
            left(360/12)

    done()


print(main())

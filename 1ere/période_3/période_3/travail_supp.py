# Créé par n.mohamed, le 11/01/2022 en Python 3.7

from turtle import*


demande= input("Quel forme voulez-vous ?")
dico={"carre" : 4, "triangle" : 3, "pentagone" : 5 }
cote=int(input("pixel"))

def polygone(x,y):
    for i in range(x):
        forward(cote)
        left(360/x)



if demande=="carre":
    b=dico.get("carre")
    for i in range(12):
        polygone(b,cote)
        goto(100,100)
        left(360/12)
elif demande=="triangle":
    b=dico.get("triangle")
    for i in range(12):
        polygone(b,cote)
        goto(100,100)
        left(360/12)
elif demande=="pentagone":
    b=dico.get("pentagone")
    for i in range(12):
        polygone(b,cote)
        goto(100,100)
        left(360/12)



done()
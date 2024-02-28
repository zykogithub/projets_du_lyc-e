# Créé par n.mohamed, le 19/09/2022 en Python 3.7

from random import*

class Personnage:
    def __init__(self,pv,a):
        self.vie = pv
        self.age = a

    def __str__(self):
        return "vie : " + str(self.vie)

    def perdVie(self,base):
        self.vie-=randint(1,base)
        if base<0:
            base=0
        return base

    def boirePotion(self,ajout):
        self.vie+=ajout


    def donneEtat(self):
        return self.vie

def simul(n):
    perso = Personnage(n,45)
    perso.boirePotion(38)
    return perso.vie


persona = Personnage(100,150)
gollum = Personnage(15,127)
gollum.perdVie(10)
gollum.perdVie(10)
gollum.perdVie(10)

print(gollum.donneEtat())
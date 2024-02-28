from random import*

class Pokemon:
    def __init__(self,a,v,d):
        self.posX = 0
        self.posY = 0
        self.attaque=a
        self.vie=v
        self.defense=d
    def pertespv(self,perso,pertes):
        self.vie-=pertes+self.defense
    def seDeplace(self,nouveauX,nouveauY) :
        self.posX = nouveauX
        self.posY = nouveauY


    def attak(self,perso,perdu):
        perso.pertespv(perso,perdu)

    def vivant(self):
        return self.vie>0
    def __str__(self):
        return 'posX = ' + str( self.posX) +' posY = ' + str( self.posY) +' pv = ' + str( self.vie) + ' attaque = ' + str( self.attaque) + ' défense = ' + str( self.defense)


Bulbizarre=Pokemon(randint(70,90),randint(20,60),randint(50,80))
Pikachu=Pokemon(randint(70,90),randint(20,60),randint(50,80))
Bulbizarre.attak(Pikachu,Bulbizarre.attaque)
print("les paramètres de Pikachu : ",Pikachu)
print("les paramètres de Bulbizarre: ", Bulbizarre)

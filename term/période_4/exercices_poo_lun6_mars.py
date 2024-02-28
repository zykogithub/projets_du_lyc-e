#exercice 1

class Eleve:
    def __init__(self,nom,classe,note):
        self.nom=nom
        self.classe=classe
        self.note=note
    
#code principal    
Elea = Eleve("Le Roux","T5",16.0)
Naherry = Eleve("Mohamed Darouèche","T3",18.75)
Benjamin = Eleve("Garault","T7",16.25)

def compare(eleve1,eleve2):
    if eleve1.note>eleve2.note:
        return eleve1.nom
    else:
        return eleve2.nom
print(compare(Elea,Benjamin))

#exercice 2

from math import*

class TriangleRect:
    def __init__(self,cote_a,cote_b):
        self.cote_a=cote_a
        self.cote_b=cote_b
        self.hypotenuse= sqrt(cote_a**2+cote_b**2)



print(TriangleRect(3, 4).hypotenuse)

#exercice 3 correction

class Chrono:
    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s

    def affiche(self):
        return "Il est {} heures, {} minutes \
et {} secondes".format(self.heures, self.minutes, self.secondes)
    def avance(self, s):
        self.secondes += s
        self.minutes += self.secondes // 60
        self.secondes = self.secondes % 60
        self.heures += self.minutes // 60
        self.minutes = self.minutes % 60
        
#exercice 4

class Player:
    def __init__(self):
        self.energie=3
        self.alive= self.energie>0
    def blessure(self):
        self.energie-=1
        return self.energie
    def soin(self):
        if self.energie>0:#correction
            self.energie+=1
            return self.energie
    
#exercice 5

class CompteBancaire:
    def __init__(self,titulaire,solde):
        self.nom=titulaire
        self.solde=solde
    def retrait(self,somme):
        comparaison=self.solde-somme
        if comparaison>=0:
            return "Vous avez retiré " + str(somme)+ "euros" + "/n"+ "Solde actuel du compte : "+ str(self.solde-=somme)
        else :
            return "Retrait impossible"
    def depot(self,somme):
        return "Vous avez déposé " + str(somme)+ "euros" + "/n"+ "Solde actuel du compte : "+ str(self.solde+=somme)

#correction       
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def retrait(self, somme):
        if somme > self.solde:
            print("Retrait impossible")
        else :
            self.solde -= somme
            print("Vous avez retiré {} euros".format(somme))
            print("Solde actuel du compte : {} euros".format(self.solde))
    def depot(self, somme):
        self.solde += somme
        print("Vous avez déposé {} euros".format(somme))
        print("Solde actuel du compte : {} euros".format(self.solde))


        




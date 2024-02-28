# Créé par n.mohamed, le 28/09/2022 en Python 3.7
proposition=5 ==7-3

if proposition:
    print("ok")
else:
    print("mal")


help(Vide)
help(Liste)
help(est_vide)
help(tete)
help(queue)

lst1 = Vide()
print(lst1)
print(est_vide(lst1))
lst2= Liste(2,lst1)
print(lst2)
print(est_vide(lst2))
lst2= Liste(3,lst2)
print(lst2)
lst2 = queue(lst2)
print(lst2)


lst1 = Vide()
lst1 = Liste("a", Liste("b", Liste("c",Vide())))
print(lst1)

def longueur(liste):
   cpt=0
   while not est_vide(liste):
      liste= queue(liste)
      cpt = cpt+1
   return cpt
vide= Vide()
lst= Liste(2,vide)
liset= Liste(1,lst)
print(longueur(liset))



def longueur(liste):
    if liste==Vide():
        return 0
    else:
        return 1+longueur(queue(liste))


vide= Vide()
lst= Liste(2,vide)
liset= Liste(1,lst)
print(longueur(liset))


def enleve_tete(liste):
   liste=queue(liste)
   return liste


vide= Vide()
lst= Liste(2,vide)
liset= Liste(1,lst)
print(enleve_tete(liset))


def appartient(x, liste):

   if est_vide(liste):
      return False
   elif tete(liste)==x:
      return True
   else:
      return appartient(x,queue(liste))

vide= Vide()
lst= Liste(2,vide)
liset= Liste(1,lst)
print(appartient(3,liset))




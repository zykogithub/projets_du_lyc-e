# Créé par n.mohamed, le 01/02/2022 en Python 3.7
# question 1
# téléchargement du fichier fichier.csv correspondants aux émissions de l'année 2017
# et enregistrement dans le répertoire jupyter

from csv import*

# question 2
'''' Définition de la fonction importation : fonction qui lit le fichier csv et le rentre dans une
liste de dictionnaire '''
def importation(doc):
    importer= open(doc)
    reader= DictReader(importer)
    air = [dict(ligne) for ligne in reader]
    importer.close()
    return air
# Test de la fonction importation sur 5 lignes
# renvoie une liste de dictionnaire contenant les attributs des 5 premières lignes
for i in range (5):
    print(importation("fichier.csv")[i])


compteur=0
for i in importation("fichier.csv"):
    ville=[]
    ville.append(i["pm10"])
    ville.




































''''
qualite_air=[]
for i in importation("fichier.csv") :
#for i in dammarie
    qualite_air.append(int(i["pm10"]))
def top_3_air(qualite):
    top_liste=[]
    for i in range(3):
        qualite_max=-1
        for i in qualite:
            if i>qualite_max:
                qualite_max=i
        qualite.remove(qualite_max)
        top_liste.append(qualite_max)
    return top_liste

print("polution max top 3 : ",
    top_3_air(qualite_air))

'''def reduction(prix,taux):
    prix_reduit=prix*(1-taux/100)
    economie=prix-prix_reduit
    assert taux<100, "Je vais pas te donner de l'argent, petit rat que tu es !"
    return prix_reduit,economie

prix_demande=float(input("Saisir un prix. Prix initale de :"))
reduction_demande=float(input("Saisir une réduction. Réduction de :"))
print("Après une réduction, vous devez payer :", reduction(prix_demande,reduction_demande)[0], "€", "Vous avez économisé : ", reduction(prix_demande,reduction_demande)[1], "€")
'''

def recherche(prénom,classe):
    fois_eleve=0
    for eleve in classe :
        if eleve[0]==prénom:
            fois_eleve=fois_eleve+1
    return fois_eleve,prénom




def nomre_de_fois(eleve,classe):
    occurence=[]##fallait créer une liste
    for eleve in classe :
        if occurence>=2:
            print(occurence)
    return occurence,eleve

eleve_1=("Naherry", "Mohamed Darouèche", 16 )
eleve_2=("Camille", "Echavidre",15)
eleve_3=("Camille", "Lacombe", 30)
classe_test=(eleve_1,eleve_2,eleve_3)

de=(recherche("Camille",classe_test))
print(de)




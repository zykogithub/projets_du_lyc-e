# Créé par souve, le 08/12/2021 en Python 3.7

classe={"candidat1": 8,
       "candidat2": 12,
       "candidat3": 17, #2
       "candidat4": 18, #1
       "candidat5": 15, #3
       "candidat6": 14}

def top_3_candidats(moyenne):
    note=None #moyenne d'un élève
    eleve=None #un élève lambda
    for i in range(3): #au lieu de faire une boucle pour le 1er,2eme,3eme, on répète le procédé 3fois
        for candidats,notation in moyenne.items():#fonction pokemon : placer un élève au plus haut possible
            if note is None or notation>note :
                eleve=candidats
                note=notation
        if i==0 : #lors du premier tour on place le 1er avec la variable eleve puis on met eleve et note à None pour recommencer le procédé
            premier=eleve
            eleve=None
            note=None
            moyenne.pop(premier) #pour retirer le premier du dictionnaire
        if i==1 : #lors du deuxième tour on place le 2e avec la variable eleve puis on met eleve et note à None pour recommencer le procédé
            deuxieme=eleve
            moyenne.pop(deuxieme) #pour retirer le second du dictionnaire
            eleve=None
            note=None
        if i==2 : #lors du troisieme tour on place le 3e avec la variable eleve puis on met eleve et note à None pour recommencer le procédé
            troisieme=eleve
            moyenne.pop(troisieme) #pour retirer le troisieme du dictionnaire
    top3=(premier,deuxieme,troisieme) #tuple classant en ordre décroissant les élèves
    return top3

print("Voici les prétendants au top 3 : ", classe)
print("Et le top3 est : ", top_3_candidats(classe), "Félicitations à vous !")
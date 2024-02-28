def scores_aimes(votes):
    """
    Renvoie le dictionnaire dont les clés sont les personnes,
    et les valeurs le nombre de personnes qui leur ont attribué des J'aime.
    """
    liste=[]
    for valeur in votes.values():
        liste+=valeur   
    dico_jaime={}
    for cle,valeur in votes.items():
        dico_jaime[cle]=liste.count(cle)
    return liste,dico_jaime

    

def gagnants(votes):
    """
    Renvoie la liste des personnes ayant le plus reçu de : J'aime
    """
    liste=[]
    gagnant=[]
    for valeur in votes.values():
        liste+=valeur
    for nom in range(len(liste)-1):
        if liste.count(liste[nom])<liste.count(liste[nom+1]):
            gagnant.append(liste[nom+1])
            del gagnant[0]
        elif liste.count(liste[nom])==liste.count(liste[nom+1]):
            gagnant.append(liste[nom+1])
    
    
    
    for parcours in range(len(gagnant)-1):
        if gagnant.count(gagnant[parcours])>1:
            del gagnant[parcours]
    return liste,gagnant




# Tests
# votes_soiree = {
#     "Alice": ["Bob", "Carole", "Dylan"],
#     "Bob": ["Carole", "Esma"],
#     "Esma": ["Bob", "Alice"],
#     "Fabien": ["Dylan"],
#     "Carole": [],
#     "Dylan":[],
# }


# assert scores_aimes(votes_soiree) == {
#     "Bob": 2,
#     "Alice": 1,
#     "Esma": 1,
#     "Fabien": 0,
#     "Carole": 2,
#     "Dylan": 2,
# }

# assert sorted(gagnants(votes_soiree)) == ["Bob", "Carole", "Dylan"]
votes_soiree = {
    "Alice": ["Bob", "Carole", "Dylan"],
    "Bob": ["Carole", "Esma"],
    "Esma": ["Bob", "Alice"],
    "Fabien": ["Dylan"],
    "Carole": [],
    "Dylan":[],
}

print("score : ",scores_aimes(votes_soiree))
print("gagnant : ",gagnants(votes_soiree))


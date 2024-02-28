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
    return dico_jaime
    
    
def gagnants(votes):
    """
    Renvoie la liste des personnes ayant le plus reçu de : J'aime
    """
    dico_jaime=scores_aimes(votes)
    stockage=[]
    for valeur in dico_jaime.values():
        stockage.append(valeur)
    stockage.sort()
    gagnant=[]
    for cle in dico_jaime.keys():
        if dico_jaime[cle]==stockage[-1]:
            gagnant.append(cle)
    return gagnant
        




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
'''votes_soiree_vide = {
    "Alice": [],
    "Bob": [],
    "Esma": [],
    "Fabien": [],
    "Carole": [],
    "Dylan":[],
}'''
print("score : ",scores_aimes(votes_soiree))
print("gagnant : ",gagnants(votes_soiree))


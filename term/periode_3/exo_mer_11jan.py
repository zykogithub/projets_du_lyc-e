def scores_aimes(votes):
    """
    Renvoie le dictionnaire dont les clés sont les personnes,
    et les valeurs le nombre de personnes qui leur ont attribué des J'aime.
    """
    liste=[]
    for valeur in votes.values():
        liste.append(valeur)
    dico_jaime={}
    for cle in votes.keys():
        dico_jaime[cle]=liste.count(cle)
    return dico_jaime
    

def gagnants(votes):
    """
    Renvoie la liste des personnes ayant le plus reçu de : J'aime
    """
    liste=[]
    for valeur in votes.values():
        liste.append(valeur)
    return liste









# Tests
votes_soiree = {
    "Alice": ["Bob", "Carole", "Dylan"],
    "Bob": ["Carole", "Esma"],
    "Esma": ["Bob", "Alice"],
    "Fabien": ["Dylan"],
    "Carole": [],
    "Dylan":[],}



print(scores_aimes(votes_soiree))
print(gagnants(votes_soiree))




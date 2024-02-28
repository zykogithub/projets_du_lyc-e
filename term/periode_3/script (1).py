votes_soiree_vide = {
    "Alice": [],
    "Bob": [],
    "Esma": [],
    "Fabien": [],
    "Carole": [],
    "Dylan":[],
}


'''code essaie'''
    if liste==[]:
        for cle in votes.keys():
            liste.append(cle)
    else:
votes_soiree = {
    "Alice": ["Bob", "Carole", "Dylan"],
    "Bob": ["Carole", "Esma"],
    "Esma": ["Bob", "Alice"],
    "Fabien": ["Dylan"],
    "Carole": [],
    "Dylan":[],
}

# print("score : ",scores_aimes(votes_soiree_vide))
# print("gagnant : ",gagnants(votes_soiree_vide))
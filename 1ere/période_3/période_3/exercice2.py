# Créé par n.mohamed, le 07/12/2021 en Python 3.7
Trois=0
Deux=0
Un=0
troisième=None
deuxième=None
premier=None
for (candidats,moyenne) in moyennes.items():
    if Un<moyenne:
            Un=moyenne
            premier=candidats
    elif Deux<moyenne:
            Deux=moyenne
            deuxième=candidats
    elif Trois<moyenne:
            Trois=moyenne
            troisième=candidats
    return troisième


classement={"candidats1" : 12,
           "candidats2" : 20,
           "candidats3" : 13,
           "candidats4" : 18,
           "candidats5" : 14}

print(top_3_candidats(classement))

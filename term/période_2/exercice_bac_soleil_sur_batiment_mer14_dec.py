def nb_batiments_eclaires(hauteurs):
    if hauteurs==[] or hauteurs==[0] :
        return 0
    else:
        intialisation=hauteurs[0]
        compteur=1
        for i in range (0,len(hauteurs)):
            if intialisation<hauteurs[i] and intialisation!=0:
                intialisation=hauteurs[i]
                compteur+=1
        return compteur




# tests
assert 4 == nb_batiments_eclaires([2, 1, 2, 4, 0, 4, 5, 3, 5, 6])
assert 1 == nb_batiments_eclaires([0, 3, 1, 2])



def nb_batiments_eclaires_correction(hauteurs):
    resultat = 0
    plafond = 0
    for h in hauteurs:
        if h > plafond:
            plafond = h
            resultat += 1
    return resultat


# tests

assert 4 == nb_batiments_eclaires_correction([2, 1, 2, 4, 0, 4, 5, 3, 5, 6])
assert 1 == nb_batiments_eclaires_correction([0, 3, 1, 2])



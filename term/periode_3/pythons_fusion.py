def fusion(gauche, droite):
    """
    Fusionne gauche et droite
    Les tableaux intiaux sont triés
    Le tableau résultat l'est aussi
    """
    taille_gauche = len(gauche)
    taille_droite = len(droite)
    nouveau = [None] * (taille_gauche + taille_droite)

    i_nouveau = 0
    i_gauche = 0
    i_droite = 0

    # Il reste des éléments à gauche ET à droite
    while i_gauche < taille_gauche and i_droite < taille_droite:
        if gauche[i_gauche] <= droite[i_droite]:
            nouveau[i_nouveau] = gauche[i_gauche]
            i_gauche += 1
        else:
            nouveau[i_nouveau] = droite[i_droite]
            i_droite+=1
        i_nouveau += 1

    # Il ne reste des éléments QUE à gauche
    while i_gauche < taille_gauche :
        nouveau[i_nouveau] = gauche[i_gauche]
        i_gauche += 1
        i_nouveau += 1

    # Il ne reste des éléments QUE à droite
    while i_droite < taille_droite :
        nouveau[i_nouveau] = droite[i_droite]
        i_droite += 1
        i_nouveau += 1


    return nouveau


# Même taille
gauche = [0, 2, 4]
droite = [1, 3, 5]
assert fusion(gauche, droite) == [0, 1, 2, 3, 4, 5]
# Un tableau plus court
gauche = [0, 2, 4]
droite = [1, 3]
assert fusion(gauche, droite) == [0, 1, 2, 3, 4]
# Un tableau vide
gauche = []
droite = [1, 3, 5]
assert fusion(gauche, droite) == [1, 3, 5]
# gauche est toujours plus petit
gauche = [0, 1]
droite = [2, 3]
assert fusion(gauche, droite) == [0, 1, 2, 3]


print("Bravo !")


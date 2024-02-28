def sous_tableau(tableau, debut, fin):
    """
    Renvoie une copie des éléments d'indices
    compris entre debut (inclus) et fin (exclu)
    de tableau
    """
    nouveau = [None] * (fin - debut)  # pas indispensable
    copie=[]
    for i in range(debut,fin):
        copie.append(tableau[i])
    return copie

# Tests
tableau = [0, 1, 2, 3, 4, 5]
assert sous_tableau(tableau, 0, 2) == [0, 1]
assert sous_tableau(tableau, 2, 6) == [2, 3, 4, 5]
assert sous_tableau(tableau, 0, 6) == [0, 1, 2, 3, 4, 5]
assert sous_tableau(tableau, 0, 0) == []
print("Bravo !")


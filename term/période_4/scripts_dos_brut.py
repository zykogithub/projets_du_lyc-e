def possibilités(objets, poids):
    prendre = []
    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                for i4 in range(2):
                    for i5 in range(2):
                        for i6 in range(2):
                            if i1*objets[1][2]+i2*objets[2][2]+i3*objets[3][2]+i4*objets[4][2]+i5*objets[5][2]+i6*objets[6][2]<=poids:
                                prendre.append([i1,i1,i1,i1,i1,i1])
    return prendre

def butin_brut(objets, poids):
    possibles = possibilités(objets, poids)
    maxi = 0
    resultat = []
    for possible in possibles:
        if 
        

    return (resultat, max)


objets = [["A", 13, 700], ["B", 12, 500], ["C", 8, 200],\
 ["D", 10, 300], ["E", 14, 600], ["F", 18, 800]]

# Tests
assert butin_brut(objets, 40) == ([1, 1, 0, 0, 1, 0], 1800)


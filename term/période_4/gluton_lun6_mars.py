PIECES = [4, 3, 1]

def monnaie_Glouton(montant):
    a_rendre = montant
    liste = []
    for piece in PIECES:
        while a_rendre>=piece:
                a_rendre-=piece
                liste.append(piece)
    return liste



def possibilites(montant):
    rendre = []
    for i in range(montant + 1): # au plus montant pièces (de 1 par exemple)
        for j in range(montant + 1):
            for k in range(montant + 1):
                if i * PIECES[0] + j * PIECES[1] + k * PIECES[2] == montant :
                    rendre.append([i,j, k])
    return rendre

def monnaie_brute(montant):
    possibles = possibilites(montant)
    mini = montant
    for liste in possibles:
        if sum(liste) < mini:
            resultat = liste # La liste renvoyée
            mini = sum(liste) # Le nombre de pièces
    return (resultat, mini)

liste=[6,10,22,100]
for i in liste:
    print("Algorithme Gluton pour ",i, ": ",monnaie_Glouton(i))
    print("Algorithme méthode brute : ",i, ": ",monnaie_brute(i))


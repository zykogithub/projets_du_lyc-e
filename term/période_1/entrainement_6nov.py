def filtre_par_longueur(liste_prenoms, longueur):
    resultat = []
    for prenom in liste_prenoms :
        if len(prenom) == longueur:
            resultat.append(prenom)
    return resultat


# Testsprenom
prenoms = ['Anne', 'Francky', 'Charles', 'Léa', 'Nicolas']
assert filtre_par_longueur(prenoms, 7) == ['Francky', 'Charles', 'Nicolas']
assert filtre_par_longueur(prenoms, 3) == ['Léa']
assert filtre_par_longueur(prenoms, 10) == []

